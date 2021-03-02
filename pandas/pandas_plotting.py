import pandas as pd
import matplotlib.pyplot as plt
#file reading by using --> (pd.read_csv function)
#result = pd.read_csv('./test_result.dat',sep='\t',skiprows=1,names=['t','V','I','deg','torque','tmp'])
result = pd.read_csv('../cylinder_test/data/C-S5-W047/110.dat',sep='\t',skiprows=1,names=['t','V','I','deg','torque','tmp'])
result = result.drop(columns=['tmp'])
print(result.mean())
result.plot(x='t')
plt.show()
