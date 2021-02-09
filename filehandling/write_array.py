import math
import matplotlib.pyplot as plt
t = 0
X= []
Y= []
T =[]
n = range(1,21,2)
while t<=4:
    x = 0
    y = 0
    for N in [math.pi*i for i in n]:
        x += 4/N*math.cos(N*t)
        y += 4/N*math.sin(N*t)
    X.append(x)
    Y.append(y)
    T.append(t)
    t += 0.005

fig, axs = plt.subplots(1,2)
axs[0].plot(X,Y,'r-')
axs[1].plot(T,Y,'b-')
plt.show()

# T = [T1, T2, .....]
# X = [Xv1, Xv2 , .....]
# Y = [Yv1, Yv2 , .....]
fileobj = open('./write_array.dat','w')
for t,x,y in zip(T,X,Y):
    fileobj.write(f'{t:.4f} {x:.5f} {y:.5f}\n')
fileobj.close()
