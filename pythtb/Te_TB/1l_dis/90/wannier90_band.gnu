#set data style dots
set nokey
set xrange [0: 3.43577]
set yrange [ -8.15412 :  1.23544]
set arrow from  0.54547,  -8.15412 to  0.54547,   1.23544 nohead
set arrow from  1.26602,  -8.15412 to  1.26602,   1.23544 nohead
set arrow from  1.81149,  -8.15412 to  1.81149,   1.23544 nohead
set arrow from  2.53204,  -8.15412 to  2.53204,   1.23544 nohead
set xtics (" G "  0.00000," Y "  0.54547," M "  1.26602," X "  1.81149," G "  2.53204," M "  3.43577)
 plot "wannier90_band.dat"
