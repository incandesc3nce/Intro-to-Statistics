import matplotlib.pyplot as plt
import numpy as np
import math

AllFormulas = []

class Regr: # Линейная регрессия
    X = []
    Y = []

    def __init__(self, x, y):        
        self.X = x
        self.Y = y
        self.N = len(self.X)

    def Koef(self): 
        C = D = E = F = 0
        for i in range(self.N):
            C += self.X[i]**2
            D += self.X[i]
            E += self.X[i] * self.Y[i]
            F += self.Y[i]

        Det = self.N*C - D**2
        self.a = (E*self.N - F*D)/Det
        self.b = (C*F - D*E)/Det        

    def Formula(self):
        self.Ytrue = [self.a*x + self.b for x in self.X]

    def Graphics(self, name):  
        plt.plot (self.X, self.Ytrue, "r")
        plt.scatter(self.X, self.Y)
        plt.title(name)
        plt.show()

    def Kdet(self):
        global AllFormulas
        Ysr = 0        
        for i in range(self.N):
            Ysr += self.Y[i]            
        Ysr /= self.N

        SS = 0
        SE = 0
        for i in range(self.N):
            SS += (self.Y[i] - Ysr)**2
            SE += (self.Ytrue[i] - self.Y[i])**2

        self.D = 1 - SE/SS
        self.R = math.sqrt(self.D)

        AllFormulas.append(self.Ytrue)

    def Display(self):
        print("a = " + str(round(self.a, 3)))
        print("b = " + str(round(self.b, 3)))
        print("Коэффициент детерминации = " + str(round(self.D, 3)))
        print("Коэффициент множественной корреляции = " + str(round(self.R, 3)))

class Exponential(Regr): # Экспоненциальная аппроксимация
    def Koef(self):
        for i in range(self.N):
            self.Y[i] = math.log(self.Y[i])
        Regr.Koef(self)        
        for i in range(self.N):           
            self.Y[i] = math.exp(self.Y[i])      

    def Formula(self):  
        self.Ytrue = [math.exp(self.b+self.a*x)  for x in self.X]
        self.b=math.exp(self.b)

class stepen(Regr): 
    def Koef(self):
        for i in range(self.N):
            self.Y[i] = math.log(self.Y[i])
        for i in range(self.N):
            self.X[i] = math.log(abs(self.X[i]))
        Regr.Koef(self)        
        for i in range(self.N):           
            self.Y[i] = math.exp(self.Y[i])  
        for i in range(self.N):           
            self.X[i] = math.exp(self.X[i])
        

    def Formula(self):  
        self.Ytrue = [math.exp(self.b)*(x**self.a)  for x in self.X]
        self.b=math.exp(self.b)

class logarithm(Regr): 
    def Koef(self):
        for i in range(self.N):
            self.X[i] = math.log(abs(self.X[i]))
        Regr.Koef(self)        
        for i in range(self.N):           
            self.X[i] = math.exp(self.X[i])  

    def Formula(self):  
        self.Ytrue = [self.b+(self.a*math.log(x))  for x in self.X]

class geperbola(Regr): 
    def Koef(self):
        for i in range(self.N):
            self.X[i]=1/self.X[i]
        Regr.Koef(self)        
        for i in range(self.N):           
            self.X[i]=1/self.X[i]  

    def Formula(self):  
        self.Ytrue = [self.b+self.a/x for x in self.X] 

x = np.loadtxt('input.txt', skiprows=0, max_rows=1)
y = np.loadtxt('input.txt', skiprows=1, max_rows=1)

print("Аппроксимация прямой:")
Rg = Regr(x, y)
Rg.Koef()
Rg.Formula()
Rg.Kdet()
Rg.Graphics("Аппроксимация прямой")
Rg.Display()
print("\nЭкспоненциальная аппроксимация:")
Ex = Exponential(x,y)
Ex.Koef()
Ex.Formula()
Ex.Kdet()
Ex.Graphics("Экспоненциальная аппроксимация")
Ex.Display()
print("\nСтепеная аппроксимация:")
Ex1 =  stepen(x,y)
Ex1.Koef()
Ex1.Formula()
Ex1.Kdet()
Ex1.Graphics("Степеная аппроксимация")
Ex1.Display()
print("\nЛогарифмическая аппроксимация:")
Ex2 =  logarithm(x,y)
Ex2.Koef()
Ex2.Formula()
Ex2.Kdet()
Ex2.Graphics("Логарифмическая аппроксимация")
Ex2.Display()
print("\nГиперболическая аппроксимация:")
Ex2 = geperbola (x,y)
Ex2.Koef()
Ex2.Formula()
Ex2.Kdet()
Ex2.Graphics("Гиперболическая аппроксимация")
Ex2.Display()

