import pandas as pd
import matplotlib.pyplot as plt
#file reading by using --> (pd.read_csv function)
#result = pd.read_csv('./test_result.dat',sep='\t',skiprows=1,names=['t','V','I','deg','torque','tmp'])
result = pd.read_csv('../cylinder_test/data/C-S5-W047/110.dat',sep='\t',skiprows=1,names=['t','V','I','deg','torque','tmp'])
result = result.drop(columns=['tmp'])

def test_apply_func(series):
    mean = series.mean()
    return mean
def G_filter(series):
    mean = series.mean()
    std = series.std()
    tmp =[]
    for i in series:
        if i>mean-3*std and i<mean+3*std:
            tmp.append(i)
        else:
            tmp.append(0)
    tmp_series = pd.Series(tmp)
    return tmp_series
def Moving_averaging(series,window):
    tmp = []
    window_value_list= []
    if series.name=='t':
        return series
    else:
        for i in series:
            window_value_list.append(i)
            if len(window_value_list)<window:
                tmp.append(i)
            elif len(window_value_list)==window:
                mean = sum(window_value_list)/len(window_value_list)
                tmp.append(mean)
            else:
                #longer than 'window'
                window_value_list.pop(0) # eliminate first value in list
                mean = sum(window_value_list)/len(window_value_list)
                tmp.append(mean)
        return tmp

result_G_f  = result.apply(G_filter)
result_MA = result_G_f.apply(Moving_averaging,window=50)
result_MA.plot(x='t')
plt.show()
#print(result.mean())
#result.plot(x='t')
#plt.show()
