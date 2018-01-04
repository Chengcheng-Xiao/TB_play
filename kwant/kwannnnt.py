import kwant
def make_system(a):
    ham = ("alpha * (k_x * sigma_x - k_y * sigma_y)"
           "+ (m + beta * kk) * sigma_z"
           "+ (gamma * kk + U) * sigma_0")
    subs = {"kk": "k_x**2 + k_y**2"}
    return kwant.continuum.discretize(ham, locals=subs, grid_spacing=a)

syst = make_system().finalized()
psi = kwant.wave_function(syst)(0)[0]
# create the operators
Q = kwant.physics.LocalOperator(syst)
J = kwant.physics.Current(syst)
# evaluate the expectation value with the wavefunction
q = Q(psi)
j = J(psi)

J = kwant.operator.Current(syst).bind(params=params)
current = sum(J(p) for p in psi)
kwant.plotter.current(syst, current)
