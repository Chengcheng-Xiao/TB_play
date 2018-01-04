#set data style dots
set nokey
set xrange [0: 3.59730]
set yrange [ -8.69529 :  1.00237]
set arrow from  0.57224,  -8.69529 to  0.57224,   1.00237 nohead
set arrow from  1.32562,  -8.69529 to  1.32562,   1.00237 nohead
set arrow from  1.89786,  -8.69529 to  1.89786,   1.00237 nohead
set arrow from  2.65124,  -8.69529 to  2.65124,   1.00237 nohead
set xtics (" G "  0.00000," Y "  0.57224," M "  1.32562," X "  1.89786," G "  2.65124," M "  3.59730)
 plot "wannier90.up_band.dat"
