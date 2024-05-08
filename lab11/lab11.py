import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats

class Regr: # Линейная регрессия
    X = []
    Y = []

    def __init__(self, x, y):        
        self.X = x
        self.Y = y
        self.N = len(self.X)

    def Scatter(self):
         self.xx=np.zeros(shape=(self.N,4)) # формирование матрицы левой части
         for i in range(0,self.N):
             self.xx[i,0]=1
         for i in range(0,self.N):
             self.xx[i,1]=self.X[i]
         for i in range(0,self.N):
             self.xx[i,2]=self.X[i]*self.X[i]
         for i in range(0,self.N):
             self.xx[i,3]=self.X[i]*self.X[i]*self.X[i]
         self.xx1=self.xx.transpose() # транспонирование xx
         self.x=self.xx1.dot(self.xx)      # умножение матриц x=xx1 * xx
         self.yy=np.zeros(self.N)
         for i in range(0,self.N):
             self.yy[i]=self.Y[i]
         self.y=self.xx1.dot(self.yy)

    def Solve(self):
        y=self.xx1.dot(self.yy)
        self.AA=np.linalg.solve(self.x,y)

    def Graphics(self): 
          plt.scatter(self.X, self.Y)
          X=sorted(self.X)
          ylist=[self.AA[0]+self.AA[1]*x+self.AA[2]*x*x+self.AA[3]*x*x*x for x in X]
          plt.plot (X, ylist,color='red')
          plt.show()

    def Kdet(self):   
        N=self.N
        self.m=len(self.AA)
        Ysr=0
        for i in range(0,self.N):
            Ysr=Ysr+self.Y[i]
        Ysr=Ysr/self.N
        SS=0
        for i in range(0,self.N):
            SS=SS+(self.Y[i]-Ysr)*(self.Y[i]-Ysr)
        SE=0
        for i in range(0,self.N):
            z=self.AA[0]+self.AA[1]*self.X[i]+self.AA[2]*self.X[i]*self.X[i]+self.AA[3]*self.X[i]*self.X[i]*self.X[i]
            SE=SE+(self.Y[i]-z)*(self.Y[i]-z)
        self.D=1-SE/SS
        self.A=np.linalg.solve(self.x,self.y) # после нахождения коэффициентов 
        self.Ysr=0
        for i in range(0,N):
            self.Ysr=self.Ysr+self.Y[i]
        self.Ysr=self.Ysr/self.N
        self.SR=0 # обусловлена регрессией
        for i in range(0,N):
            z=self.A[0]+self.A[1]*self.X[i]+self.A[2]*self.X[i]*self.X[i]+self.A[3]*self.X[i]*self.X[i]*self.X[i]
            self.SR=self.SR+(z-self.Ysr)*(z-self.Ysr)
        self.SS=0 # общая сумма квадратов
        for i in range(0,N):
            self.SS=self.SS+(self.Y[i]-self.Ysr)*(self.Y[i]-self.Ysr)
        self.SE=0  # остаточная сумма квадратов
        for i in range(0,N):
            z=self.A[0]+self.A[1]*self.X[i]+self.A[2]*self.X[i]*self.X[i]+self.A[3]*self.X[i]*self.X[i]*self.X[i]
            self.SE=self.SE+(self.Y[i]-z)*(self.Y[i]-z)
        z1=self.SR/(self.m-1)
        z2=self.SE/(N-self.m-1)
        self.TE=z1/z2
        self.V=np.linalg.inv(self.x)  # обратная матрица к x
        for i in range(0,self.m):
            self.V[i,i]=self.V[i,i]*self.SE/(N-self.m-1)

    def Graphics2(self):
        plt.scatter(self.X, self.Y)
        N=self.N
        m=len(self.AA)
        Up=[]
        Down=[]
        Up= Up + [0]*(N - len( Up))
        Down=Down+[0]*(N - len( Down))
        X0=np.zeros((self.m),dtype=float)  # вектор прогноза
        X0V=np.zeros((self.m),dtype=float) # произведение V * X0
        self.X1=self.X
        self.X=sorted(self.X)
        S=self.SE/(N-self.m-1)
        alfa=0.95
        alfa=(1-alfa)/2
        alfa=1-alfa              
        z=N-m-1 
        t=stats.t(z)
        tcr=t.ppf(alfa)
        for i in range (0,N):
            x=self.X[i]
            X0[0]=1   # столбец текущего значения
            X0[1]=x
            X0[2]=x*x
            X0[3]=x*x*x
            Y0=self.A[0]+self.AA[1]*x+self.AA[2]*x*x+self.AA[3]*x*x*x # аппроксимация
            for j in range(0,self.m):
                X0V[j]=0
                for k in range(0,self.m):
                    X0V[j]=X0V[j]+self.V[j,k]*X0[k]
            XC=0  # X' V X
            for j in range(0,self.m):
                XC=XC+X0[j]*X0V[j]
            XC=math.sqrt(math.fabs(XC))
            Up[i]=Y0+S*tcr*XC # верхняя граница
            Down[i]=Y0-S*tcr*XC # нижняя граница
        self.X=self.X1
        self.X1=self.X
        self.X=sorted(self.X)
        ylist=[self.AA[0]+self.AA[1]*x+self.AA[2]*x*x+self.AA[3]*x*x*x for x in self.X]
        plt.plot (self.X, ylist,color='green')
        plt.plot(self.X,Up,'brown')
        plt.plot(self.X,Down,'brown')
        self.X=self.X1
        plt.show()




x= np.loadtxt('input.txt', skiprows=0, max_rows=1)
y = np.loadtxt('input.txt', skiprows=1, max_rows=1)

Rg = Regr(x,y)
Rg.Scatter() # вызов функции
Rg.Solve() # решение системы
A=Rg.AA
for i in range(0,len(A)):
    A[i]=math.floor(A[i]*1000)/1000
print(A)
Rg. Graphics()
Rg.Kdet()
D=Rg.D
D=math.floor(D*1000)/1000
r=math.sqrt(D)
r=math.floor(r*1000)/1000
print("D=",D,"R=",r)
Tcr=stats.f.ppf(0.95, len(A)-1, len(x)-len(A)-1) # распределение Фишера
TE=math.floor(Rg.TE*1000)/1000
Tcr=math.floor(Tcr*1000)/1000
print("TE=",TE,"Tcr=",Tcr)
m=Rg.m
alfa=0.95 
alfa=(1-alfa)/2
alfa=1-alfa              
m=len(x)-m-1 
t=stats.t(m)
tcr=t.ppf(alfa)
Rg. Graphics2()
for i in range(0,Rg.m):    
    z2=Rg.AA[i]+Rg.V[i,i]*tcr
    z1=Rg.AA[i]-Rg.V[i,i]*tcr
    a=Rg.AA[i]
    z1=math.floor(z1*1000)/1000
    z2=math.floor(z2*1000)/1000
    a=math.floor(a*1000)/1000
    print(z1,a,z2)
    if(z1<0 and z2>0):
        print("не значим")
        Rg.AA[i]=0
    else:
        print("значим")
Rg. Graphics()
Rg.Kdet()
D=Rg.D
D=math.floor(D*1000)/1000
r=math.sqrt(D)
r=math.floor(r*1000)/1000
print("D=",D,"R=",r)
Rg. Graphics2()

