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
series = read_csv('beer.csv', header=0, index_col=0)
mod = ARIMA(series, order=(1,0,0)) # p=1 d=0(нет разности стационарна) q=0
results = mod.fit()
print(results.summary())

mod = ARIMA(series, order=(1,0,1))
results = mod.fit()

plt.plot(series[10:45],color='r')
plt.plot(results.predict(40,60),color='g')
pyplot.show()



series = read_csv('beer.csv', header=0, index_col=0)
mod = ARIMA(series, order=(1,0,1))
results = mod.fit()
X= series.values
size = int(len(X)-10)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
for t in range(len(test)):
    model = ARIMA(history, order=(1,0,1))
    model_fit = model.fit()
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    obs = test[t]
    history.append(obs)
    print('predicted=%f, expected=%f' % (yhat, obs))
pyplot.plot(test,color='red')
pyplot.plot(predictions, color='green')
pyplot.show()