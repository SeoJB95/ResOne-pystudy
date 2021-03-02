import pandas as pd

#file reading by using --> (pd.read_csv function)
result = pd.read_csv('./test_result.dat',sep='\t',skiprows=1,names=['t','V','I','deg','torque','tmp'])
print(result)
#print(type(result))
result = result.drop(columns=['tmp'])
print(result)
