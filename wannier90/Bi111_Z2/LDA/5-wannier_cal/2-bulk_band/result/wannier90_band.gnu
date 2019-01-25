set style data dots
set nokey
set xrange [0: 2.35770]
set yrange [ -6.23426 :  3.01277]
set arrow from  0.86298,  -6.23426 to  0.86298,   3.01277 nohead
set arrow from  1.36122,  -6.23426 to  1.36122,   3.01277 nohead
set xtics ("G"  0.00000,"Y"  0.86298,"M"  1.36122,"G"  2.35770)
 plot "wannier90_band.dat"
