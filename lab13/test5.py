import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.api import qqplot
from matplotlib import pyplot as plt
import pylab
import random
from pandas import read_csv
from math import sqrt

# Load the dataset
series = read_csv('beer.csv', header=0, index_col=0)

# Fit the ARIMA model
mod = ARIMA(series, order=(1,0,1))
results = mod.fit()

# Plot the original series and ARIMA predictions
plt.plot(series[10:48], color='r')
plt.plot(results.predict(35, 50), color='g')
plt.show()

# Splitting data into train and test sets
X = series.values
size = int(len(X) - 10)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()

# ARIMA forecasting
for t in range(len(test)):
    model = ARIMA(history, order=(1,0,1))
    model_fit = model.fit()
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    obs = test[t]
    history.append(obs)
    print('predicted=%f, expected=%f' % (yhat, obs))

# Plotting test data vs predictions
plt.plot(test, color='red')
plt.plot(predictions, color='green')
plt.show()

# Predict with confidence intervals
predictions_int = results.get_forecast(steps=10)
print(predictions_int.conf_int())

# Create a DataFrame with the series, predictions, and confidence intervals
conf_df = pd.concat([series, predictions_int.predicted_mean, predictions_int.conf_int()], axis=1)
conf_df.columns = ['observed', 'predicted_mean', 'lower_bound', 'upper_bound']

# Plot observed, predicted, and confidence intervals
fig = plt.figure(figsize=(8,5))
x = conf_df.index.values
upper = conf_df['upper_bound']
lower = conf_df['lower_bound']
plt.plot(series[10:48], color='b')
conf_df['predicted_mean'].plot(color='orange')
conf_df['lower_bound'].plot(color='gray')
conf_df['upper_bound'].plot(color='gray')
plt.fill_between(x, lower, upper, color='grey', alpha=0.1)
plt.show()