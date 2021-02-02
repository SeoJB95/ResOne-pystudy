import matplotlib.pyplot as plt
import math
Re = range(10000,10000000,1000)
Cf = []

for re in Re:
    Cf_value = (0.075)/(math.log10(re)-2)**2
    Cf.append(Cf_value)

plt.plot(Re,Cf)
plt.xscale('log')
plt.grid()
plt.legend(['ITTC 78 Frcition line'])
plt.show()
