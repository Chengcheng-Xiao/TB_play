#!/usr/bin/env python

# Copyright under GNU General Public License 2010, 2012, 2016
# by Sinisa Coh and David Vanderbilt (see gpl-pythtb.txt)

from __future__ import print_function
from pythtb import * # import TB model class
import matplotlib.pyplot as plt

# read output from Wannier90 that should be in folder named "example_a"
# see instructions above for how to obtain the example output from Wannier90
# for testing purposes
Te=w90(r"Te_1l",r"wannier90.up")

# hard coded fermi level in eV
fermi_ev= -2.6959

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
my_model=Te.model(zero_energy=fermi_ev,min_hopping_norm=None,max_distance=25,ignorable_imaginary_part=0.01)
my_model.display()

# visualize infinite model
(fig,ax)=my_model.visualize(0,1)
ax.set_title("Te_2l, 2D_bulk")
ax.set_xlabel("x coordinate")
ax.set_ylabel("y coordinate")
fig.tight_layout()
fig.savefig("visualize_bulk.pdf")

# cutout finite model along direction 0
cut_one=my_model.cut_piece(8,0,glue_edgs=False)
#
(fig,ax)=cut_one.visualize(0,1)
ax.set_title("Te_2l, ribbon")
ax.set_xlabel("x coordinate")
ax.set_ylabel("y coordinate")
fig.tight_layout()
fig.savefig("visualize_ribbon.pdf")

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
fig.savefig("Te_up.pdf")
