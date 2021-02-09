f = open('./write_array.dat','r')
result = f.readlines()
f.close()
t = []
x = []
y = []
for line in result:
    splited = line.split()
    c1 = float(splited[0])
    c2 = float(splited[1])
    c3 = float(splited[2])
    t.append(c1)
    x.append(c2)
    y.append(c3)

    
