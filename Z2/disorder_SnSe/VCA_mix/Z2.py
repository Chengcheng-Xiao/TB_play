import z2pack
import tbmodels
import matplotlib.pyplot as plt
model = tbmodels.Model.from_wannier_files(hr_file='19_hr.dat')
system = z2pack.tb.System(model)
result = z2pack.surface.run(
    system=system,
    surface=lambda t1, t2: [t1, t2, 0],
     save_file='19test.msgpack'
)
print(z2pack.invariant.chern(result))
print(z2pack.invariant.z2(result))
z2pack.plot.wcc(result)
plt.show()
