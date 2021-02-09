import pandas as pd
import matplotlib.pyplot as plt
#data = pd.read_csv('./write_array.dat',sep=' ',header=None)
data = pd.read_excel('./write_array.xlsx')

'''
#파일읽고 변경하기
#xy_col = data[1]*data[2]
#data['xy'] = xy_col

'''

'''
#엑셀로 원하는 데이터프레임 저장하기
#data.to_excel('./write_array_wPandas.xlsx',\
#index=False,float_format='%.5f',header=['t','x','y','xy'])
'''

'''
#확인용 플롯
fig,axe = plt.subplots(1,3)
axe[0].plot(data[0],data[1])
#axe[0].plot(data[0],data[1])
axe[1].plot(data[0],data[2])
#axe[1].plot(data[0],data[2])
axe[2].plot(data[1],data[2])
#axe[2].plot(data[1],data[2])
plt.show()
'''

fig,axe = plt.subplots(1,3)
axe[0].plot(data.t,data.x)
axe[1].plot(data.t,data.y)
axe[2].plot(data.x,data.y)
plt.show()
