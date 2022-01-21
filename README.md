# read_efg
Simple script to read Vzz and eta components of the electric field gradient from the gipaw output file

Usage: python get_efg --inp=input_file_name --loc=atom_location

atom_location is the atom number in the ATOMIC_POSITIONS section of the Quantum ESPRESSO input file.

For example, loc= 2 correspondes to the first Mn2 atom in for MnO2 with the following atomic positions section in the QE input file:

ATOMIC_POSITIONS crystal

 Mn1 -0.000000000 -0.000000000 0.001510848
 
 Mn2  0.500000000  0.500000000 0.248488348
 
 Mn2 -0.000000000 -0.000000000 0.501511652
 
 Mn1  0.500000000  0.500000000 0.748489152
 
   O  0.305588268  0.305588268 0.000454583
   
   O  0.694411732  0.694411732 0.000454583
   
   O  0.805588284  0.194411716 0.249545718
   
   O  0.194411716  0.805588284 0.249545718
   
   O  0.305588284  0.305588284 0.500454282
   
   O  0.694411716  0.694411716 0.500454282
   
   O  0.805588268  0.194411732 0.749545417
   
   O  0.194411732  0.805588268 0.749545417
   
