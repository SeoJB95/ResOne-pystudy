import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
#file reading by using --> (pd.read_csv function)

result = pd.read_csv('../cylinder_test/data/C-S5-W047/110.dat',sep='\t',skiprows=1,names=['t','V','I','deg','torque','tmp'])
data = result.drop(columns='tmp')

#names를 부여한 경우, column 단위로 접근할 수 있는 속성을 가진다.
'''
print(data.t)      # <-- 시간의 열을 출력함
print(data.V)      # <-- 전압의 열을 출력함
print(data.I)      # <-- 전류의 열을 출력함
print(data.deg)    # <-- 포텐쇼 미터의 출력값의 열을 출력함
print(data.torque) # <-- 토크 센서의 전압을 출력함
'''

'''
1. 값을 점검하기 위하여 plotting 하기
판다스는 테이블의 형태로 정리된 값을 쉽게
플롯할 수 있도록하는 다양한 라이브러리를 제공함


    1) dataframe 객체의 plot 함수사용
        해당하는 함수는 matplotlib 의 pyplot함수를 이용하여 제작된 함수
        이므로, 그 모습을 렌더링 하기위해서는 plt.show() 구문과 함께 사용

        아무런 옵션이 없을때는 인덱스를 x 로 하여 그래프를 그립니다. 만약
        시간 t 를 x 로 하여 그래프를 그리기 위해서는 option x를 삽입합니다.
'''
data.plot(x='t')
#data.plot()
plt.show()
