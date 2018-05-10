from htbac import Simulation, System, Runner, AbFile
from htbac.protocols import Afe

prefix = "models/complex"
system_names = ['CB8-G3', 'OA-G3', 'OA-G6']
systems = list()

for s in system_names:
    for r in range(5):
        folder = "{}/{}-{}/build/".format(prefix, s, r)
        rest_folder = "{}/{}-{}/restraints/".format(prefix, s, r)
        name = "{}-{}".format(s, r)
        pdb = AbFile(folder+"solvent.pdb", tag='pdb').with_prefix(name)
        top = AbFile(folder+"solvent.prmtop", tag='topology').with_prefix(name)
        coord = AbFile(folder+"solvent.rst7", tag='coordinate').with_prefix(name)
        rest = AbFile(rest_folder+"restraint_1.0.in", tag='restraint', needs_copying=True).with_prefix(name)
        systems.append(System(name, files=[pdb, top, coord, rest]))

step = Afe.step1
numsteps = Afe.numsteps[0]

sim = Simulation()
sim.engine = 'namd_mpi'
sim.cores = 32

sim.cutoff = 12.0
sim.pairlistdist = 13.5
sim.switchdist = 10.0
sim.numsteps = numsteps

sim.add_ensemble('replica', values=range(2))
sim.add_ensemble('system', values=systems[:2])
sim.add_ensemble('lambdawindow', values=[1.0, 0.75, 0.5, 0.3, 0.2, 0.15, 0.1, 0.075, 0.05, 0.025, 0.01, 0.0][:2])

sim.add_input_file(step, is_executable_argument=True)

sim.add_variable(name='k1', value=property(lambda:  10*sim.lambdawindow), in_file='*restraint_1.0.in')
sim.add_variable(name='k2', value=property(lambda: 500*sim.lambdawindow), in_file='*restraint_1.0.in')

runner = Runner(resource='bw_aprun', comm_server=('two.radical-project.org', 33162))
runner.add_protocol(sim)
runner.run(walltime=1440, queue='high', access_schema='local')
