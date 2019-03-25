set style data dots
set nokey
set xrange [0: 3.48261]
set yrange [-11.07349 :  9.73527]
set arrow from  0.73639, -11.07349 to  0.73639,   9.73527 nohead
set arrow from  2.01077, -11.07349 to  2.01077,   9.73527 nohead
set xtics ("G"  0.00000,"X"  0.73639,"M"  2.01077,"G"  3.48261)
 plot "wannier90_band.dat"
