import sys
import math
import numpy
from scipy.stats import chi2
from scipy import stats
import matplotlib.pyplot as pyplot


def funcExp(x, L):
    return 1 - math.exp(-L * x)


def funcPareto(x, Xm, k):
    return 1 - (Xm / x) ** k


def funcNorm(x, Xsr, Sg):
    return 0.5 * (1 + math.erf((x - Xsr) / math.sqrt(2 * Sg * Sg)))


file = 'test1'
file = 'test2'
v = int(input("\n Выберите выборку 1 или 2: "))
A = list()
if v == 1:
    A = numpy.loadtxt(file)
elif v == 2:
    A = numpy.loadtxt(file)

B = list()
for i, item in enumerate(A):
    A[i] = (float(item))
    B.append(abs(item))

print("\n Выборка из экспоненциального закона.")
k = int(math.sqrt(len(A)) * 2)  # Increased number of intervals
h = round((max(A) - min(A)) / k, 1)  # шаг по оси оХ
Hist = numpy.zeros((k - 1), dtype=numpy.int32)
nak_min = min(A)
nak_max = min(A) + h
counter = 0
for i in range(0, k - 1):
    for item in enumerate(A):
        if item[1] >= nak_min and item[1] <= nak_max:
            counter += 1
    Hist[i] = counter
    counter = 0
    nak_min += h
    nak_max += h
x = []
z = 0
i = 0
while i < k - 1:
    x.append(z)
    z = z + h
    i = i + 1
width = 1
for i in range(0, k - 1):
    x[i] = math.floor(x[i] * 10) / 10
pyplot.bar(x, Hist, width)
pyplot.xticks(x)
L = 1 / (sum(A) / len(A))
fyE = []
z = min(A)
for i in range(0, k - 1):
    f = funcExp(z + h, L) - funcExp(z, L)
    fyE.append(f * len(A))  # теоретическое число попаданий в интервал
    z = z + h
pyplot.plot(x, fyE, -k, color='r')
pyplot.show()
print("\n Гистограмма распределения выборки и график теоретических вероятностей распределений для эксп. закона.")
Vexp = 0
for i in range(0, k - 1):
    t = Hist[i] - fyE[i]
    Vexp = Vexp + t * t / fyE[i]
p = numpy.array([0.99, 0.95, 0.75, 0.5, 0.25, 0.05, 0.01])
df = numpy.array(range(k - 1, k)).reshape(-1, 1)
t = chi2.isf(p, df)
for i in range(0, 1):
    for j in range(0, 7):
        t[i, j] = math.floor(t[i, j] * 100) / 100
print(" p = ", p)
print(" t = ", t)
print(" хи-квадрат: Vexp =  %.2f" % Vexp)

print("\n Выборка из закона Парето.")
pyplot.bar(x, Hist, width)
pyplot.xticks(x)
fyP = []

z = min(B)
Xm = min(B)
sumLn = 0
for i in range(0, len(B)):
    sumLn += math.log((B[i]) / Xm)
k1 = len(B) / sumLn
for i in range(0, k - 1):
    f = funcPareto(z + h, Xm, k1) - funcPareto(z, Xm, k1)
    fyP.append(f * len(B))
    z = z + h
pyplot.plot(x, fyP, -k, color='r')
pyplot.show()
print("\n Гистограмма распределения выборки и график теоретических вероятностей распределений для закона Парето.")
Vpar = 0
for i in range(0, k - 1):
    t = Hist[i] - fyP[i]
    Vpar = Vpar + t * t / fyP[i]
df = numpy.array(range(k - 1, k)).reshape(-1, 1)
t = chi2.isf(p, df)
for i in range(0, 1):
    for j in range(0, 7):
        t[i, j] = math.floor(t[i, j] * 100) / 100
print(" p = ", p)
print(" t = ", t)
print(" хи-квадрат: Vpar =  %.2f" % Vpar)

print("\n Выборка из нормального закона.")
pyplot.bar(x, Hist, width)
pyplot.xticks(x)
fyN = []
z = min(A)
Xsr = sum(A) / len(A)
Sg = numpy.std(A)
for i in range(0, k - 1):
    f = funcNorm(z + h, Xsr, Sg) - funcNorm(z, Xsr, Sg)
    fyN.append(f * len(A))
    z = z + h
pyplot.plot(x, fyN, -k, color='r')
pyplot.show()
print("\n Гистограмма распределения выборки и график теоретических вероятностей распределений для нормального закона.")
Vnorm = 0
for i in range(0, k - 1):
    t = Hist[i] - fyN[i]
    Vnorm = Vnorm + t * t / fyN[i]
df = numpy.array(range(k - 1, k)).reshape(-1, 1)
t = chi2.isf(p, df)
for i in range(0, 1):
    for j in range(0, 7):
        t[i, j] = math.floor(t[i, j] * 100) / 100
print(" p = ", p)
print(" t = ", t)
print(" хи-квадрат: Vnorm =  %.2f" % Vnorm)

print("\n" + 6 * " " + "Выполним тест Колмогорова-Смирнова для рассмотренных распределений.")
yp1 = numpy.zeros((7), dtype=numpy.float64)
df = numpy.zeros((7), dtype=numpy.float64)
for i in range(0, 7):
    yp1[i] = 0.5 * math.log(1 / (1 - p[i]))
    yp1[i] = math.sqrt(yp1[i])
for i in range(0, 7):
    df[i] = yp1[i] - 100 ** (-0.5) / 6.0
for i in range(0, 7):
    df[i] = math.floor(df[i] * 100) / 100
print(" p =  %s" % p)
print(" df = %s" % df)

x = A

x.sort()
y = []  # Значения эмпирической функции распределения
for i in range(0, len(A)):
    y.append(i / len(A))
pyplot.plot(x, y, color='r')
# Значения теоретической функции распределения
fyET = []
for i in range(0, len(A)):
    z = funcExp(x[i], L)
    fyET.append(z)
pyplot.plot(x, fyET, color='b')
pyplot.show()
print("\n Графики эмпирической и теоретической функций распределения при предположении об эксп. законе.")
V1exp = -sys.maxsize - 1
V2exp = -sys.maxsize - 1
for i in range(0, len(A)):
    if math.sqrt(k) * (y[i] - fyET[i]) >= V1exp:
        V1exp = math.sqrt(k) * (y[i] - fyET[i])
for i in range(0, len(A)):
    if math.sqrt(k) * (fyET[i] - y[i]) >= V2exp:
        V2exp = math.sqrt(k) * (fyET[i] - y[i])
print(" V1exp = %.2f" % V1exp)
print(" V2exp = %.2f" % V2exp)
pyplot.plot(x, y, color='r')

fyPT = []
for i in range(0, len(A)):
    z = funcPareto(abs(x[i]), Xm, k1)
    fyPT.append(z)
pyplot.plot(x, fyPT, color='b')
pyplot.show()
print("\n Графики эмпирической и теоретической функций распределения при предположении о законе Парето.")
V1par = -sys.maxsize - 1
V2par = -sys.maxsize - 1
for i in range(0, len(A)):
    if math.sqrt(k) * (y[i] - fyPT[i]) >= V1par:
        V1par = math.sqrt(k) * (y[i] - fyPT[i])
for i in range(0, len(A)):
    if math.sqrt(k) * (fyPT[i] - y[i]) >= V2par:
        V2par = math.sqrt(k) * (fyPT[i] - y[i])
print(" V1par = %.2f" % V1par)
print(" V2par = %.2f" % V2par)
pyplot.plot(x, y, color='r')

fyNT = []
for i in range(0, len(A)):
    z = funcNorm(x[i], Xsr, Sg)
    fyNT.append(z)
pyplot.plot(x, fyNT, color='b')
pyplot.show()
print("\n Графики эмпирической и теоретической функций распределения при предположении о нормальном законе.")
V1norm = -sys.maxsize - 1
V2norm = -sys.maxsize - 1
for i in range(0, len(A)):
    if math.sqrt(k) * (y[i] - fyNT[i]) >= V1norm:
        V1norm = math.sqrt(k) * (y[i] - fyNT[i])
for i in range(0, len(A)):
    if math.sqrt(k) * (fyNT[i] - y[i]) >= V2norm:
        V2norm = math.sqrt(k) * (fyNT[i] - y[i])
print(" V1norm = %.2f" % V1norm)
print(" V2norm = %.2f" % V2norm)

if v == 2:
    print("\n" + 6 * " " + "Доверительные интервалы для истинных среднего и дисперсии при уровне доверия 0,95 и 0,99.")
    alfa = 0.05
    m = len(A) - 1
    t = stats.t(m)
    tcr = t.ppf(1 - alfa / 2)
    x1 = Xsr - Sg / math.sqrt(len(A)) * tcr
    x2 = Xsr + Sg / math.sqrt(len(A)) * tcr
    x1 = math.floor(x1 * 1000) / 1000
    x2 = math.floor(x2 * 1000) / 1000
    print("  Интервал для истинного значения среднего при уровне доверия 0.95:")
    print(" ", x1, x2)
    alfa = 0.01
    m = len(A) - 1
    t = stats.t(m)
    tcr = t.ppf(1 - alfa / 2)
    x1 = Xsr - Sg / math.sqrt(len(A)) * tcr
    x2 = Xsr + Sg / math.sqrt(len(A)) * tcr
    x1 = math.floor(x1 * 1000) / 1000
    x2 = math.floor(x2 * 1000) / 1000
    print("  Интервал для истинного значения среднего при уровне доверия 0.99:")
    print(" ", x1, x2)
    a = 0.95
    p1 = (1 + a) / 2
    p2 = (1 - a) / 2
    p = numpy.array([p1, p2])
    df = numpy.array(range(len(A) - 1, len(A))).reshape(-1, 1)
    t = chi2.isf(p, df)
    for i in range(0, 2):
        t[0, i] = math.floor(t[0, i] * 1000) / 1000
    x1 = (len(A) - 1) * Sg / t[0, 1]
    x2 = (len(A) - 1) * Sg / t[0, 0]
    x1 = math.floor(x1 * 1000) / 1000
    x2 = math.floor(x2 * 1000) / 1000
    print("  Интервал для истинного значения дисперсии при уровне доверия 0.95:")
    print(" ", p)
    print(" ", t)
    print(" ", x1, x2)
    a = 0.99
    p1 = (1 + a) / 2
    p2 = (1 - a) / 2
    p = numpy.array([p1, p2])
    df = numpy.array(range(len(A) - 1, len(A))).reshape(-1, 1)
    t = chi2.isf(p, df)
    for i in range(0, 2):
        t[0, i] = math.floor(t[0, i] * 1000) / 1000
    x1 = (len(A) - 1) * Sg / t[0, 1]
    x2 = (len(A) - 1) * Sg / t[0, 0]
    x1 = math.floor(x1 * 1000) / 1000
    x2 = math.floor(x2 * 1000) / 1000
    print("  Интервал для истинного значения дисперсии при уровне доверия 0.99:")
    print(" ", p)
    print(" ", t)
    print(" ", x1, x2)
