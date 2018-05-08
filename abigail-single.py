from htbac import Protocol, Simulation, System, Runner, AbFile
from htbac.protocols import Afe

prefix = "models/complex"
system_names = ['CB8-G3', 'OA-G3', 'OA-G6']
systems = list()

for s in system_names:
    for r in range(5):
        folder = "{}/{}-{}/build/".format(prefix, s, r)
        rest_folder = "{}/{}-{}/restraints/".format(prefix, s, r)
        name = "{}-{}".format(s, r)
        pdb = AbFile(folder+"complex.pdb", tag='pdb').with_prefix(name)
        top = AbFile(folder+"complex.prmtop", tag='topology').with_prefix(name)
        coord = AbFile(folder+"complex.rst7", tag='coordinate').with_prefix(name)
        rest = AbFile(rest_folder+"restraint_1.0.in", tag='restraint', needs_copying=True).with_prefix(name)
        tags = AbFile(folder+"tags.pdb", tag='alchemicaltags').with_prefix(name).with_prefix(name)
        systems.append(System(name, files=[pdb, top, coord, rest, tags]))

# afe = Protocol(clone_settings=False)
step = Afe.step0
numsteps = Afe.numsteps[0]

sim = Simulation()
sim.engine = 'namd_mpi'
sim.cores = 32

sim.cutoff = 12.0
sim.pairlistdist = 13.5
sim.switchingdist = 10.0
sim.numsteps = step

sim.add_ensemble('replica', values=range(5))
sim.add_ensemble('system', systems)
sim.add_ensemble('lamdawindow', [0.0, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

sim.add_input_file(step, is_executable_argument=True)

sim.add_variable(name='k1', value=10, in_file='*restraint_1.0.in')
sim.add_variable(name='k2', value=500, in_file='*restraint_1.0.in')

# afe.append(sim)

runner = Runner(resource='bw_aprun', comm_server=('two.radical-project.org', 33166), access_schema='local')
runner.add_protocol(sim)
runner.run(walltime=1440, queue='high')
