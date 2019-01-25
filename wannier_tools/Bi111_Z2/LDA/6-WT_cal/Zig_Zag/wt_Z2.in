&TB_FILE
Hrfile = 'wannier90_hr.dat'
Package = 'VASP'
/

&CONTROL
BulkBand_calc         = F
SlabSS_calc           = F
Z2_3D_calc            = T
/

&SYSTEM
SOC = 1                 ! soc on
E_FERMI = -1.1651       ! e-fermi from VASP SCF calculation
Numoccupied = 6		! each Bi atom have 3 electrons, 2 Bi atoms means 6 occupied band
/

&PARAMETERS
Nk1 = 101               ! number k points  odd number would be better
Nk2 = 101               ! number k points  odd number would be better
/

SURFACE                 ! original cell
 1  0  0
 0  1  0
 0  0  1

KPATH_BULK              ! k point path
3                       ! number of k line only for bulk band
G 0.00000  0.00000 0.0000 Y 0.50000  0.00000 0.0000
Y 0.50000  0.00000 0.0000 M 0.33333  0.33333 0.0000
M 0.33333  0.33333 0.0000 G 0.00000  0.00000 0.0000

KPATH_SLAB
2                       ! numker of k line for 2D case
X  0.5  0.0 G  0.0  0.0 ! k path for 2D case
G  0.0  0.0 X  0.5  0.0

LATTICE
Angstrom
     2.1017795    -3.6403930     0.0000000
     2.1017795     3.6403930     0.0000000
     0.0000000     0.0000000    15.0000000

ATOM_POSITIONS
2                               ! number of atoms for projectors
Cartisen                          ! Direct or Cartisen coordinate
Bi       2.1017795     1.2134643    10.7681236
Bi       2.1017795    -1.2134643     9.0367958

PROJECTORS
3 3                     ! number of projectors
Bi pz px py
Bi pz px py

!WANNIER_CENTRES        ! copy from wannier90.wout
!Cartesian
