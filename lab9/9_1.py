import math
import numpy as np
import matplotlib.pyplot as mpl
import scipy
import statistics
from tkinter import *

class Corr:
    dV1V3 = 0.0
    dV2V3 = 0.0
    dV1V2 = 0.0    
    def __init__(self,v1,v2,v3,v4,v5,v6,v7):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4
        self.V5 = v5
        self.V6 = v6
        self.V7 = v7
        self.sv1 = statistics.mean(self.V1)
        self.sv2 = statistics.mean(self.V2)
        self.sv3 = statistics.mean(self.V3)
        self.sv4 = statistics.mean(self.V4)
        self.sv5 = statistics.mean(self.V5)
        self.sgv1 = statistics.stdev(self.V1)
        self.sgv2 = statistics.stdev(self.V2)
        self.sgv3 = statistics.stdev(self.V3)
        self.sgv4 = statistics.stdev(self.V4)
        self.sgv5 = statistics.stdev(self.V5)
    
    
    def Scatter(self, var1, var2):
        n = len(self.V1)
        a = 0
        if var1 == 1:
            if var2 == 2:
                for i, _ in enumerate(self.V1):
                    a += (self.V1[i] - self.sv1) * (self.V2[i] - self.sv2)
                a = a / n
                a = a / (self.sgv1 * self.sgv2)
                self.dV1V2 = a
                mpl.scatter(self.V1, self.V2)
            elif var2 == 3:
                for i, _ in enumerate(self.V1):
                    a += (self.V1[i] - self.sv1) * (self.V3[i] - self.sv3)
                a = a / n
                a = a / (self.sgv1 * self.sgv3)
                self.dV1V3 = a
                mpl.scatter(self.V1, self.V3)
        elif var1 == 2:
            if var2 == 1:
                for i, _ in enumerate(self.V1):
                    a += (self.V1[i] - self.sv1) * (self.V2[i] - self.sv2)
                a = a / n
                a = a / (self.sgv1 * self.sgv2)
                self.dV1V2 = a
                mpl.scatter(self.V2, self.V1)
            elif var2 == 3:
                for i, _ in enumerate(self.V1):
                    a += (self.V2[i] - self.sv2) * (self.V3[i] - self.sv3)
                a = a / n
                a = a / (self.sgv2 * self.sgv3)
                self.dV2V3 = a
                mpl.scatter(self.V2, self.V3)
        elif var1 == 3:
            if var2 == 1:
                for i, _ in enumerate(self.V1):
                    a += (self.V1[i] - self.sv1) * (self.V3[i] - self.sv3)
                a = a / n
                a = a / (self.sgv1 * self.sgv3)
                self.dV1V3 = a
                mpl.scatter(self.V3, self.V1)
            elif var2 == 2:
                for i, _ in enumerate(self.V1):
                    a += (self.V2[i] - self.sv2) * (self.V3[i] - self.sv3)
                a = a / n
                a = a / (self.sgv2 * self.sgv3)
                self.dV2V3 = a
                mpl.scatter(self.V3, self.V2)
        if var1 == 5:
            if var2 == 4:
                
                for i, _ in enumerate(self.V5):
                        a += (self.V5[i] - self.sv5) * (self.V4[i] - self.sv4)
                    
                a = a / n
                a = a / (self.sgv5 * self.sgv4)
                mpl.scatter(self.V4, self.V5)
        mpl.show()
        return a
    
    def Indevedual(self, var1, var2, var3):
        res = (var1 - var2 * var3) / (math.sqrt((1 - var2 **2) * (1 - var3 **2)))
        res = math.floor(res * 100) / 100
        return res

    
    def importance(self, var1, var2, alfa):
        N = len(self.V1)
        if var1 == 1:
            if var2 == 2:
                te = self.dV1V2 * math.sqrt((N - 2) / (1 - self.dV1V2 * self.dV1V2))
            elif var2 == 3:
                te = self.dV1V3 * math.sqrt((N - 2) / (1 - self.dV1V3 * self.dV1V3))
        if var1 == 2:
            if var2 == 3:
                te = self.dV2V3 * math.sqrt((N - 2) / (1 - self.dV2V3 * self.dV2V3))
        alfa = (1 - alfa) / 2
        alfa = 1 - alfa
        m = N - 2
        t = scipy.stats.t(m)
        tcr = t.ppf(alfa)
        tcr = math.floor(tcr * 1000) / 1000
        te = math.floor(te * 1000) / 1000
        return te, tcr
    
    def many(self, var1, var2, var3):
        res = math.sqrt((var1 * var1 + var2 * var2 - (2 * var1 * var2 * var3)) / (1 - var3 * var3))
        res = math.floor(res * 1000) / 1000
        return res
    
    
    def Relation(self, var1, var2):
        mpl.scatter(var1, var2)
        N = len(self.V4)
        K = math.ceil(math.sqrt(N))
        Ni = np.zeros((K))
        Sum = np.zeros((K))
        Max = max(var1, key=lambda i: float(i))
        Min = min(var1, key=lambda i: float(i))
        for i in range (0, K):
            Ni[i] = 0
            Sum[i] = 0
        h = (Max - Min) / K
        for i in range(0, N):
            v = Min
            for j in range (0, K):
                if var1[i] >= v and var1[i] < v + h:
                    Ni[j] = Ni[j] + 1
                    Sum[j] = Sum[j] + var2[i]
                v = v + h
            v = Min
        for j in range(0, K):
            try:
                if (Sum[j]==0.0 and Ni[j]==0.0) : 
                    Sum[j]=0
                    continue
                Sum[j] = Sum[j] / Ni[j]
            except:
                Sum[j]=0
        S = 0
        sr = statistics.mean(var2)
        for j in range(0, K):
            S = S + (Sum[j] - sr) * (Sum[j] - sr) * Ni[j]
        S = S / N
        Sg1 = statistics.stdev(var2)
        Sg1 = math.pow(Sg1, 2)
        Et = math.sqrt(S / Sg1)
        res = math.floor(Et * 1000) / 1000
        return res
    
    
    def Rang(self):
        N = len(self.V6)
        mass1 = []
        for i in range (0, N):
            mass1.append(self.V6[i])
        mass1.sort()
        mass2 = []
        for i in range (0, N):
            mass2.append(self.V7[i])
        mass2.sort()
        R1 = []
        R2 = []
        for i in range(0, N):
            for j in range (0, N):
                if self.V6[i] == mass1[j]:
                    break
            R1.append(j)
        for i in range(0, N):
            for j in range (0, N):
                if self.V7[i] == mass2[j]:
                    break
            R2.append(j)
        D = 0
        for i in range (0, N):
            D = D + (R1[i] - R2[i]) * (R1[i] - R2[i])
        res = 1 - 6 * D / (N * (N * N - 1))
        res = math.floor(res * 1000) / 1000
        return res


def Doubles():
    var1 = int(En1.get())
    var2 = int(En2.get())
    res = obj.Scatter(var1, var2)
    res = math.floor(res * 100) / 100
    lb4.config(text = "Коэффициент парной корреляции: " + str(res))


def Indevedual():
    a = Radio.get()
    if a == 1:
        res = obj.Indevedual(obj.dV1V2, obj.dV1V3, obj.dV2V3)
    elif a == 2:
        res = obj.Indevedual(obj.dV1V3, obj.dV1V2, obj.dV2V3)
    else:
        res = obj.Indevedual(obj.dV2V3, obj.dV1V2, obj.dV1V3)
    lb4.config(text = "Коэффициент частной корреляции: " + str(res))

def importance():
    var1 = int(En1.get())
    var2 = int(En2.get())
    alfa = float(En3.get())
    res , rescr = obj.importance(var1, var2, alfa)
    if math.fabs(res) > math.fabs(rescr):
        lb4.config(text = "Нулевая гипотеза отвергается, потому что |te| = " + str(res) + " > tcr  = " + str(rescr))
    else:
        lb4.config(text = "Нулевая гипотеза потверждается, потому что |te| = " + str(res) + " < tcr  = " + str(rescr))


def many():
    a = Radio.get()
    if a == 1:
        res = obj.many(obj.dV1V2, obj.dV1V3, obj.dV2V3)
    elif a == 2:
        res = obj.many(obj.dV1V2, obj.dV2V3, obj.dV1V3)
    else:
        res = obj.many(obj.dV1V3, obj.dV2V3, obj.dV1V2)
    lb4.config(text = "Коэффициент множественной корреляции: " + str(res))


def Relation():
    a = Check.get()
    if a == 0:
        res = obj.Relation(obj.V4, obj.V5)
    if a == 1:
        res = obj.Relation(obj.V5, obj.V4)
    lb4.config(text = "Корреляционное отношение: " + str(res))


def Rang():
    res = obj.Rang()
    lb4.config(text = "Ранговый коэффициент корреляции : " + str(res))

v1 = np.loadtxt('input.txt', skiprows=0, max_rows=1)
v2 = np.loadtxt('input.txt', skiprows=1, max_rows=1)
v3 = np.loadtxt('input.txt', skiprows=2, max_rows=1)
v4 = np.loadtxt('input.txt', skiprows=3, max_rows=1)
v5 = np.loadtxt('input.txt', skiprows=4, max_rows=1)
v6 = np.loadtxt('input.txt', skiprows=5, max_rows=1)
v7 = np.loadtxt('input.txt', skiprows=6, max_rows=1)

print(v1, v2, v3, v4, v5, v6, v7, sep='\n')

obj = Corr(v1, v2, v3, v4, v5, v6, v7)
root = Tk()
root.title("Корреляционный анализ")
root.geometry("650x400")

lb1 = Label(root, text = "Введите номер выборки:")
lb1.place(x = 10, y = 10, width = 150, height = 25)
lb2 = Label(root, text = "Введите номер выборки:")
lb2.place(x = 10, y = 40, width = 150, height = 25)
lb3 = Label(root, text = "Введите уровень доверия:")
lb3.place(x = 210, y = 10, width = 150, height = 25)
lb4 = Label(root, text = "Результат")
lb4.place(x = 10, y = 260, width = 400, height = 25)

En1 = Entry(root)
En1.place(x = 160, y = 10, width = 25, height = 25)
En2 = Entry(root)
En2.place(x = 160, y = 40, width = 25, height = 25)
En3 = Entry(root)
En3.place(x = 370, y = 10, width = 25, height = 25)

bt1 = Button(root, text = "Коэф. парной корреляции", command = Doubles)
bt1.place(x = 50, y = 120, width = 200)
bt2 = Button(root, text = "Коэф. частной корреляции", command = Indevedual)
bt2.place(x = 50, y = 170, width = 200)
bt3 = Button(root, text = "Значимость коэф. корреляции", command = importance)
bt3.place(x= 50, y = 220, width = 200)
bt4 = Button(root, text = "Коэф. множеcтвенной корреляции", command = many)
bt4.place(x = 300,y = 120, width = 200)
bt5 = Button(root, text = "Корреляционное отношение", command = Relation)
bt5.place(x = 300, y = 170, width = 200)
bt6 = Button(root, text = "Ранговые корреляции", command = Rang)
bt6.place(x = 300, y = 220, width = 200)

Radio = IntVar()
Check = IntVar()
R1 = Radiobutton(root, text = "12/3 или 1(23)", variable = Radio, value = 1)
R1.place(x = 50, y = 90, width = 140, height = 25)
R2 = Radiobutton(root, text = "13/2 или 2(13)", variable = Radio, value = 2)
R2.place(x = 200, y = 90, width = 140, height = 25)
R3 = Radiobutton(root, text = "23/1 или 3(12)", variable = Radio, value = 3)
R3.place(x = 350, y = 90, width = 140, height = 25)
C1 = Checkbutton(root, text = "Обратное отношение XY", variable = Check, onvalue = 1, offvalue = 0)
C1.place(x = 210, y = 50, width = 200, height = 25)
R1.select()

root.mainloop()

