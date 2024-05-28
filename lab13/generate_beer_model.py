import numpy as np
from matplotlib import pyplot as plt
import pylab
t=[]
z=[]
N=0
f = open('test.txt','r')
while True:
    s = f.readline()
    if len(s) == 0:
        break
    s1=s.split()
    for i in range(0, len(s1)):
        s2=s1[i]
        z.append(float(s1[i]))
        t.append(N)
        N=N+1
f.close()
print(z)
pylab.plot (t, z, "-b") # -b - синий цвет
pylab.show()
# запись в файл chemistry.csv
f=open('beer.csv','w')
s='N'+' ' +'Beer'+'\n'
f.write(s)
for i in range(0,48):
    s=str(i)+','
    s=s+str(z[i])+'\n'
    f.write(s)
f.close()