#!/usr/bin/env python

# Copyright under GNU General Public License 2010, 2012, 2016
# by Sinisa Coh and David Vanderbilt (see gpl-pythtb.txt)

from __future__ import print_function
from pythtb import * # import TB model class
import matplotlib.pyplot as plt

# read output from Wannier90 that should be in folder named "example_a"
# see instructions above for how to obtain the example output from Wannier90
# for testing purposes
Te=w90(r"90",r"wannier90")

# hard coded fermi level in eV
fermi_ev= -2.6041

# all pair distances berween the orbitals
print("Shells:\n",Te.shells())


Te.dist_hop()
# plot hopping terms as a function of distance on a log scale
#(dist,ham)=Te.dist_hop()
#fig, ax = plt.subplots()
#ax.scatter(dist,np.log(np.abs(ham)))
#ax.set_xlabel("Distance (A)")
#ax.set_ylabel(r"$\log H$ (eV)")
#fig.tight_layout()
#fig.savefig("Te_dist_ham.pdf")

# get tb model in which some small terms are ignored
my_model=Te.model(zero_energy=fermi_ev,min_hopping_norm=0.1,max_distance=50,ignorable_imaginary_part=0.01)
my_model.display()

# visualize infinite model
(fig,ax)=my_model.visualize(0,1)
ax.set_title("Te_2l, 2D_bulk")
ax.set_xlabel("x coordinate")
ax.set_ylabel("y coordinate")
fig.tight_layout()
fig.savefig("visualize_bulk.pdf")

# cutout finite model along direction 0
cut_one=my_model.cut_piece(7,0,glue_edgs=False)
#
(fig,ax)=cut_one.visualize(0,1)
ax.set_title("Te_2l, ribbon")
ax.set_xlabel("x coordinate")
ax.set_ylabel("y coordinate")
fig.tight_layout()
fig.savefig("visualize_ribbon.pdf")

# compute the band structure in the entire band
#cut_one.reduce_dim(1,0)
#cut_one.reduce_dim(1,0)
#cut_one.display()
cut_one.ignore_position_operator_offdiagonal()
path = [[-0.5, 0.0], [0.0, 0.0], [0.5, 0.0]]
(k_vec,k_dist,k_node)=cut_one.k_path(path,100)
#print(k_vec)
(evals,evecs)=cut_one.solve_all(k_vec,eig_vectors=True)
#print(evals.shape[0])


# plotting of band structure
print('Plotting bandstructure...')

# First make a figure object
fig, ax = plt.subplots()
# plot all bands
# the following line is to plot each band with all kpoints.
for i in range(evals.shape[0]):
    ax.plot(k_dist,evals[i,:],"k-", zorder=-50)

# color bands according to expectation value of y operator (red=top, blue=bottom)
for i in range(evecs.shape[1]):
  # get expectation value of the position operator for states at i-th kpoint
  pos_exp=cut_one.position_expectation(evecs[:,i],dir=0)

  # because kpoint is 2D, we have to change its dimension. or we can simply use the distance between kpoints (k_dis)
  # plot states according to the expectation value
  # the following line is to plot each kpoints with all bands, so len([k_dist[i]]*evals.shape[0])=len(evals[:,i]=126 which is the number of bands.
  s=ax.scatter([k_dist[i]]*evals.shape[0], evals[:,i], c=pos_exp, s=40,
                marker='o', cmap="coolwarm", edgecolors='none', vmin=0.0, vmax=float(7), zorder=-100)

# color scale
fig.colorbar(s,None,ax,ticks=[float(1),float(2),float(3),float(4),float(5),float(6),float(7)])

# plot Fermi energy
ax.axhline(0.0,c='m',zorder=-200)

# zoom in close to the zero energy
ax.set_xlim(k_dist[0],k_dist[-1])
ax.set_ylim(-1.0,2.0)
# put title on top
ax.set_title("Te surface band structure")
ax.set_xlabel("k parallel to edge")
ax.set_ylabel("Band energy")
ax.xaxis.set_ticks(k_node)
ax.set_xticklabels((r'$-X$',r'$\Gamma$',r'$-X$'))
# make an PDF figure of a plot
fig.tight_layout()
fig.savefig("supercell_band.pdf")


# in the case that all steps up to now take a lot of computer time
# it is advised to save tb model to disk with cPickle module:
#   import cPickle
#   cPickle.dump(my_model,open("store.pkl","wb"))
# Later one can load in the model from disk in a separate script with
#   my_model=cPickle.load(open("store.pkl","rb"))

# solve and plot on the same path as used in wannier90
# small discrepancy in the plot is there because of the terms that
# were ignore in the Te.model function call above
#
fig, ax = plt.subplots()
(w90_kpt,w90_evals)=Te.w90_bands_consistency()
for i in range(w90_evals.shape[0]):
    ax.plot(list(range(w90_evals.shape[1])),w90_evals[i]-fermi_ev,"k-",zorder=-100)
# now interpolate from the model on the same path in k-space
int_evals=my_model.solve_all(w90_kpt)
for i in range(int_evals.shape[0]):
    ax.plot(list(range(int_evals.shape[1])),int_evals[i],"r-",zorder=-50)
ax.set_xlim(0,int_evals.shape[1]-1)
ax.set_xlabel("K-path from Wannier90")
ax.set_ylabel("Band energy (eV)")
fig.tight_layout()
fig.savefig("Te_1l_bulk.pdf")
