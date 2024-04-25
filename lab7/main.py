import scipy.stats as scipy

repeats = 20

with open('data.txt', 'r') as file:
    data1 = [next(file).strip() for _ in range(3)]
    data1 = [float(num) for line in data1 for num in line.split()]
with open('data2.txt', 'r') as file:
    data2 = [next(file).strip() for _ in range(3)]
    data2 = [float(num) for line in data2 for num in line.split()]
with open('data3.txt', 'r') as file:
    data3 = [next(file).strip() for _ in range(3)]
    data3 = [float(num) for line in data3 for num in line.split()]
with open('data4.txt', 'r') as file:
    data4 = [next(file).strip() for _ in range(3)]
    data4 = [float(num) for line in data4 for num in line.split()]

combined_data = data1 + data2 + data3 + data4
x = 0
a = 4
b = 3
r = 3

n = a*b*r

for i in range(a):
    for j in range(b):
        for k in range(r):
            x += combined_data[i * b * r + j * r + k]
x /= n

# Сумма квадратов
def sumOfSquares():
    ss = 0

    for i in range(a):
        for j in range(b):
            for k in range(r):
                ss += (combined_data[i * b * r + j * r + k] - x) ** 2

    return ss

# Средние по фактору A
def meanA():
    ma = []
    for i in range(a):
        sum = 0
        for j in range(b):
            for k in range(r):
                sum += combined_data[i * b * r + j * r + k]
        ma.append(sum / (b * r))
    return ma 

# Средние по фактору B
def meanB():
    mb = []
    for i in range(b):
        sum = 0
        for j in range(a):
            for k in range(r):
                sum += combined_data[j * b * r + i * r + k]
        mb.append(sum / (a * r))
    return mb

def sumOfSquaresA(): 
    ssa = 0
    ma = meanA()
    for i in range(a):
        ssa += (ma[i] - x) ** 2
    ssa *= b * r
    return ssa

def sumOfSquaresB():
    ssb = 0
    mb = meanB()
    for i in range(b):
        ssb += (mb[i] - x) ** 2
    ssb *= a * r
    return ssb

# средние по взаимодействиям A, B 
def meanAB():
    mab = []
    for i in range(a):
        for j in range(b):
            sum = 0
            for k in range(r):
                sum += combined_data[i * b * r + j * r + k]
            mab.append(sum / r)
    return mab

def sumOfSquaresAB():
    ssab = 0
    mab = meanAB()
    ma = meanA()
    mb = meanB()
    for i in range(a):
        for j in range(b):
            ssab += (mab[i * b + j] - ma[i] - mb[j] + x) ** 2
    ssab *= r
    return ssab

def sumOfSquaresError():
    sse = 0
    mab = meanAB()
    for i in range(a):
        for j in range(b):
            for k in range(r):
                sse += (combined_data[i * b * r + j * r + k] - mab[i * b + j]) ** 2
    return sse


# дисперсии A, B, AB, E
def varianceA():
    return sumOfSquaresA() / (a - 1)

def varianceB():
    return sumOfSquaresB() / (b - 1)

def varianceAB():
    return sumOfSquaresAB() / ((a - 1) * (b - 1))

def varianceError():
    return sumOfSquaresError() / (a * b) * (r - 1)



def F_AB():
    return varianceAB() / varianceError()

def F_A():
    return varianceA() / varianceError()

def F_B():
    return varianceB() / varianceError()

# fisher crit value
def F_crit():
    alpha = 0.05
    n1 = a - 1
    n2 = a * b * (r - 1)
    return scipy.f.ppf(alpha, n1, n2)


def main():
    mean_A = meanA()
    mean_B = meanB()
    mean_AB = meanAB()
    crit_f = F_crit()
    print("Общая сумма квадратов: ", round(sumOfSquares(), 3))
    print("Средние по фактору A: ")
    print(round(mean_A[0], 3), round(mean_A[1], 3), round(mean_A[2], 3), round(mean_A[3], 3))
    print("Сумма квадратов, обусловленная фактором A: ", round(sumOfSquaresA(), 3))
    print("Средние по фактору B: ")
    print(round(mean_B[0], 3), round(mean_B[1], 3), round(mean_B[2], 3))
    print("Сумма квадратов, обусловленная фактором B: ", round(sumOfSquaresB(), 3))
    print("Средние по взаимодействиям A, B: ")
    print("1-1 ", round(mean_AB[0], 3), "1-2 ", round(mean_AB[1], 3), "1-3 ", round(mean_AB[2], 3))
    print("2-1 ", round(mean_AB[3], 3), "2-2 ", round(mean_AB[4], 3), "2-3 ", round(mean_AB[5], 3))
    print("3-1 ", round(mean_AB[6], 3), "3-2 ", round(mean_AB[7], 3), "3-3 ", round(mean_AB[8], 3))
    print("4-1 ", round(mean_AB[9], 3), "4-2 ", round(mean_AB[10], 3), "4-3 ", round(mean_AB[11], 3))
    print("Сумма квадратов, обусловленная взаимодействием A и B: ", round(sumOfSquaresAB(), 3))
    print("Необъясненная сумма квадратов: ", round(sumOfSquaresError(), 3))
    print("Дисперсия A: ", round(varianceA(), 3))
    print("Дисперсия B: ", round(varianceB(), 3))
    print("Дисперсия AxB: ", round(varianceAB(), 3))
    print("Дисперсия E: ", round(varianceError(), 3))
    print("F_AB: ", round(F_AB(), 3), "Fкр: ", round(crit_f, 3))
    if F_AB() > crit_f:
        print("взаимодействие факторов значимо")
    else:
        print("взаимодействие факторов не значимо")
    print("F_A: ", round(F_A(), 3), "Fкр: ", round(crit_f, 3))
    if F_A() > crit_f:
        print("фактор A значим")
    else:
        print("фактор A не значим")
    print("F_B: ", round(F_B(), 3), "Fкр: ", round(crit_f, 3))
    if F_B() > crit_f:
        print("фактор B значим")
    else:
        print("фактор B не значим")



main()