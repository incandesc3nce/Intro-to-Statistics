import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from matplotlib import pyplot as plt
import random

N = 5020
Sg = 0.6
Tt1 = 0.24

t = []
z = []
a = []
for i in range(1):
    k = random.gauss(0, Sg)
    t.append(i)
    z.append(k)
    a.append(k)

for i in range(1, N):
    k = random.gauss(0, Sg)
    t.append(i)
    v = k - Tt1 * a[i-1]
    z.append(v)
    a.append(k)

with open('model_ma1.csv', 'w') as f:
    f.write('i,model\n')
    for i in range(N):
        f.write(f'{i},{z[i]}\n')

series = pd.read_csv('model_ma1.csv', header=0, index_col=0)
series.plot()
plt.show()

model = ARIMA(series, order=(0, 0, 1))
results = model.fit()
print(results.summary())