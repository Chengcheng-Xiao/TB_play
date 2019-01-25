set encoding iso_8859_1
#set terminal  postscript enhanced color
#set output 'surfdos_bulk.eps'
#set terminal  pngcairo truecolor enhanced  font ", 60" size 1920, 1680
set terminal  png truecolor enhanced font ", 60" size 1920, 1680
set output 'surfdos_bulk.png'
set palette defined (-10 "#194eff", 0 "white", 10 "red" )
#set palette rgbformulae 33,13,10
set style data linespoints
set size 0.8, 1
set origin 0.1, 0
unset ztics
unset key
set pointsize 0.8
set pm3d
#set view equal xyz
set view map
set border lw 3
#set cbtics font ",48"
#set xtics font ",48"
#set ytics font ",48"
#set ylabel font ",48"
unset cbtics
set ylabel "Energy (eV)"
#set xtics offset 0, -1
#set ylabel offset -6, 0 
set xrange [0:            1.49473]
set yrange [          -1.30000:           1.29352]
set xtics ("X"  0.00000,"G"  0.74736,"X"  1.49473)
set arrow from  0.74736,  -1.30000 to  0.74736,   1.29352 nohead front lw 3
set pm3d interpolate 2,2
splot 'dos.dat_bulk' u 1:2:(exp($3)) w pm3d
