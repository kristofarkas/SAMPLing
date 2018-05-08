import parmed as pmd

prefix = "models/complex"
system_names = ['CB8-G3', 'OA-G3', 'OA-G6']

for s in system_names:
    for r in range(5):
        folder = "{}/{}-{}/build/".format(prefix, s, r)

        a = pmd.load_file(folder+"complex.pdb")

        for res in a.residues:
            if res.name == 'GST':
                for atom in res.atoms:
                    atom.bfactor = 1.0

        a.save(folder+"tags.pdb")

print('Done!')
