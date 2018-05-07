# load topology and initial coordinates
  mol new CB8-G3-4/build/complex.prmtop type parm7
  mol addfile CB8-G3-4/build/complex.rst7
  set outfile [open CB8-G3-4/restraints/restraint_1.0.in w]

# selection
  set a1 [atomselect 0 "resname GST and name N2"]
  set a2 [atomselect 0 "resname GST and name C17"]
  set a3 [atomselect 0 "resname GST and name C18"]
  set a4 [atomselect 0 "resname HST and name N15"]
  set a5 [atomselect 0 "resname HST and name N14"]
  set a6 [atomselect 0 "resname HST and name N31"]

  set n1 [$a1 get index]
  set n2 [$a2 get index]
  set n3 [$a3 get index]
  set n4 [$a4 get index]
  set n5 [$a5 get index]
  set n6 [$a6 get index]

# distance, andles and dihedrals
#  lassign $n1 try1
#  lassign $n2 try2
#  lassign n1 [$a1 get index]
#  lassign n2 [$a2 get index]
#  set try {"$n1 $n2"}
#  set dist [measure bond {$m1 $m2}]
#  set dist [measure bond {[lindex $a3 get index] [lindex $a4 get index]}]
#  set ang1 [measure angle {$a2 get index} {$a3 get index} {$a4 get index}]
#  set ang2 [measure angle {$a3 get index} {$a4 get index} {$a5 get index}]
#  set dih1 [measure dihed {$a1 get index} {$a2 get index} {$a3 get index} {$a4 get index}]
#  set dih2 [measure dihed {$a2 get index} {$a3 get index} {$a4 get index} {$a5 get index}]
#  set dih3 [measure dihed {$a3 get index} {$a4 get index} {$a5 get index} {$a6 get index}]

  set dist [measure bond {161 51}]
  set ang1 [measure angle {160 161 51}]
  set ang2 [measure angle {161 51 47}]
  set dih1 [measure dihed {165 160 161 51}]
  set dih2 [measure dihed {160 161 51 47}]
  set dih3 [measure dihed {161 51 47 92}]

# output
  puts $outfile [format "bond %i %i 10 %.3f" $n3 $n4 $dist]
  puts $outfile [format "angle %i %i %i 500 %.3f" $n2 $n3 $n4 $ang1]
  puts $outfile [format "angle %i %i %i 500 %.3f" $n3 $n4 $n5 $ang2]
  puts $outfile [format "dihedral %i %i %i %i 500 %.3f" $n1 $n2 $n3 $n4 $dih1]
  puts $outfile [format "dihedral %i %i %i %i 500 %.3f" $n2 $n3 $n4 $n5 $dih2]
  puts $outfile [format "dihedral %i %i %i %i 500 %.3f" $n3 $n4 $n5 $n6 $dih3]

exit

