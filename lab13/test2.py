import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.api import qqplot
from matplotlib import pyplot as plt
import pylab
import random
from pandas import read_csv
from matplotlib import pyplot
from math import sqrt

t=[]
z=[]
a=[]
N=5000
Sg=0.9
Fi1=0.6
Fi2=0.2
Tt1=0.4
Tt2=0.3
k=random.gauss(0, Sg)
t.append(0)
z.append(0)
a.append(k)
t.append(1)
k=random.gauss(0, Sg)
v=Fi1*z[0]-Tt1*a[0]+k
z.append(v)
a.append(k)
for i in range(2,N):
    k=random.gauss(0, Sg)
    t.append(i)
    v=Fi1*z[i-1]+Fi2*z[i-2]-Tt1*a[i-1]-Tt2*a[i-2]+k
    z.append(v)
    a.append(k)
# to file
f=open('model2.csv','w')
s='i'+'   ' +'model'+'\n'
f.write(s)
for i in range(0,N):
    s=str(i)+','
    s=s+str(z[i])+'\n'
    f.write(s)
f.close()
series = read_csv('model2.csv', header=0, index_col=0)
series.plot()
pyplot.show()