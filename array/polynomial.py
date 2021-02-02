import matplotlib.pyplot as plt
x = range(-100,101,1)
y = []

for i in x:
    y_value= (i-30)*i*(i+70)
    y.append(y_value)

plt.plot(x,y,'r-')
plt.show()
