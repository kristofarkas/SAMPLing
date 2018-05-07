# load topology and initial coordinates
  mol new OA-G6-4/build/complex.prmtop type parm7
  mol addfile OA-G6-4/build/complex.rst7
  set outfile [open OA-G6-4/restraints/restraint_1.0.in w]

# selection
  set a1 [atomselect 0 "resname GST and name C2"]
  set a2 [atomselect 0 "resname GST and name C6"]
  set a3 [atomselect 0 "resname GST and name C5"]
  set a4 [atomselect 0 "resname HST and name C8"]
  set a5 [atomselect 0 "resname HST and name C7"]
  set a6 [atomselect 0 "resname HST and name C30"]

  set n1 [$a1 get index]
  set n2 [$a2 get index]
  set n3 [$a3 get index]
  set n4 [$a4 get index]
  set n5 [$a5 get index]
  set n6 [$a6 get index]

# distance, andles and dihedrals
  set dist [measure bond {188 8}]
  set ang1 [measure angle {189 188 8}]
  set ang2 [measure angle {188 8 7}]
  set dih1 [measure dihed {185 189 188 8}]
  set dih2 [measure dihed {189 188 8 7}]
  set dih3 [measure dihed {188 8 7 37}]

# output
  puts $outfile [format "bond %i %i 10 %.3f" $n3 $n4 $dist]
  puts $outfile [format "angle %i %i %i 500 %.3f" $n2 $n3 $n4 $ang1]
  puts $outfile [format "angle %i %i %i 500 %.3f" $n3 $n4 $n5 $ang2]
  puts $outfile [format "dihedral %i %i %i %i 500 %.3f" $n1 $n2 $n3 $n4 $dih1]
  puts $outfile [format "dihedral %i %i %i %i 500 %.3f" $n2 $n3 $n4 $n5 $dih2]
  puts $outfile [format "dihedral %i %i %i %i 500 %.3f" $n3 $n4 $n5 $n6 $dih3]

exit

