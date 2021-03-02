import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
test = pd.DataFrame([[1,-2,3],[-6,2,7],[7,3,-2]])
result = pd.read_csv('../cylinder_test/data/C-S5-W047/080.dat',sep='\t',skiprows=1,names=['t','V','I','deg','torque','tmp'])


def Varience(series):
    M = series.mean()
    tmp = 0
    for i in series:
        tmp += (i-M)**2
    V = tmp/len(series)
    return V
def test_filtering(series):
    tmp = []
    for i in series:
        if i >= 0:
            tmp.append(i)
        else:
            tmp.append(-i)
    return pd.Series(tmp)
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
def Outlier_filtering(series):
    std = math.sqrt(Varience(series))
    if std < 10E-5:
        return series
    else:
        tmp = []
        for i in series:
            if abs(i/std)>3:
                tmp.append(0)
            else:
                tmp.append(i)
        return pd.Series(tmp)

def Covariance(series1,series2):
    X = series1
    Y = series2
    meanX = X.mean()
    meanY = Y.mean()
    tmp = []
    for x,y in zip(series1,series2):
        tmp.append((x-meanX)*(y-meanY))
    covariance = sum(tmp)/len(tmp)
    return covariance
def Correlation(series1,series2):
    X = series1
    Y = series2
    cov = Covariance(X,Y)
    corr = cov/(math.sqrt(Varience(X)*Varience(Y)))
    return corr

result = result.apply(Outlier_filtering)
result = result.apply(Moving_averaging,window=30)

Correlation(result.I,result.V)
result.corr(method='pearson')
result.plot(x='torque')
plt.show()
