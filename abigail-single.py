from htbac import Protocol, Simulation, System, Runner, AbFile
from htbac.protocols import Esmacs

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
        systems.append(System(name, files=[pdb, top, coord, rest]))

esm = Protocol(clone_settings=False)

for step, numsteps in zip(Esmacs.steps, Esmacs.numsteps):
    sim = Simulation()
    sim.engine = 'namd_openmp_cuda'

    sim.cutoff = 12.0
    sim.pairlistdist = 13.5
    sim.switchingdist = 10.0
    sim.numsteps = step

    sim.add_ensemble('replica', range(25))
    sim.add_ensemble('system', [systems])
    sim.add_ensemble('lamdawindow', [1.0, 0.9, 0.8])

    sim.add_input_file(step, is_executable_argument=True)

    sim.add_variable(name='k1', value=property(lambda: sim.lamdawindow * 10), in_file='*restraint_1.0.in')
    sim.add_variable(name='k2', value=property(lambda: sim.lamdawindow * 500), in_file='*restraint_1.0.in')

    esm.append(sim)

runner = Runner(resource='titan_orte', comm_server=('csc190specfem.marble.ccs.ornl.gov', 30672))
runner.add_protocol(esm)
runner.run(walltime=720, dry_run=True)
