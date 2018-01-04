#!/usr/bin/env python

# Copyright under GNU General Public License 2010, 2012, 2016
# by Sinisa Coh and David Vanderbilt (see gpl-pythtb.txt)

from pythtb import * # import TB model class
import matplotlib.pyplot as plt

# read output from Wannier90 that should be in folder named "example_a"
#   see instructions above for how to obtain the example output from
#   Wannier90 for testing purposes
Te=w90(r"Te_2l",r"wannier90")

# get tight-binding model without hopping terms above 0.01 eV
my_model=Te.model(min_hopping_norm=0.5)

# print model detail
my_model.display()

# solve model on a path and plot it
path=[[0,0,0],[0.0,0.5,0.0],[0.5,0.5,0.0],[0.5,0.0,0.0], [0.0,0.0,0.0],[0.5,0.5,0.0]]
# labels of the nodes
k_label=(r'$\Gamma$', r'$Y$', r'$M$', r'$X$', r'$\Gamma$', r'$M$')
# call function k_path to construct the actual path
(k_vec,k_dist,k_node)=my_model.k_path(path,101)
#
evals=my_model.solve_all(k_vec)
fig, ax = plt.subplots()
for i in range(evals.shape[0]):
    ax.plot(k_dist,evals[i],"k-")
for n in range(len(k_node)):
    ax.axvline(x=k_node[n],linewidth=0.5, color='k')
ax.set_xlabel("Path in k-space")
ax.set_ylabel("Band energy (eV)")
ax.set_xlim(k_dist[0],k_dist[-1])
ax.set_xticks(k_node)
ax.set_xticklabels(k_label)
fig.tight_layout()
fig.savefig("Te_quick.pdf")
