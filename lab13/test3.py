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

series = read_csv('beer.csv', header=0, index_col=0)
series.plot()
pyplot.show()
plot_acf(series,lags=10)
pyplot.show()
plot_pacf(series,lags=10)
pyplot.show()