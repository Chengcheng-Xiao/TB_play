set style data dots
set nokey
set xrange [0: 4.02198]
set yrange [-10.27562 : 10.23754]
set arrow from  1.47216, -10.27562 to  1.47216,  10.23754 nohead
set arrow from  2.32210, -10.27562 to  2.32210,  10.23754 nohead
set xtics ("G"  0.00000,"X"  1.47216,"M"  2.32210,"G"  4.02198)
 plot "wannier90_band.dat" w l
