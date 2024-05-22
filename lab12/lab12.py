import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats
from numpy import eye, asarray, dot, sum, diag
from numpy.linalg import svd


def varimax(Phi, gamma = 1, q = 20, tol = 1e-6):
    p,k = Phi.shape
    R = eye(k)
    d=0
    for i in range(q):
        d_old = d
        Lambda = dot(Phi, R)
        u,s,vh = svd(dot(Phi.T,asarray(Lambda)**3 - (gamma/p) * dot(Lambda, diag(diag(dot(Lambda.T,Lambda))))))
        R = dot(u,vh)
        d = sum(s)
        if d/d_old < tol: break
    return dot(Phi, R)


N=10
M=9
x= np.loadtxt('inputs/input2.txt', skiprows=0, max_rows=1)
xx=np.zeros(shape=(N,M))
k=0
for i in range(0,N):
    for j in range(0,M):
        xx[i,j]=x[k]
        k+=1

sr=0
s=0
print("Номер переменной        ","Средние","    Ст. отклонения")
for i in range(0,M):
    for j in range(0,N):
        sr+= xx[j,i]
    sr=sr/N
    for jj in range(0,N):
        s+= (xx[jj,i]-sr)**2
    s=s/(N-1)
    print(i+1,"                      ", round(sr,10),"        ", round(math.sqrt(s),10))
    sr=0
    s=0
print()
sr1=0
s1=0
sr2=0
s2=0
rk=0
cor=np.zeros(shape=(M,M))
for i in range(0,M):
    for jj in range(0,N):
            sr1+= xx[jj,i]
    sr1=sr1/N
    for jjj in range(0,N):
            s1+= (xx[jjj,i]-sr1)**2
    s1=math.sqrt(s1/(N-1))
    for j in range(0,M):
        for r in range(0,N):
            sr2+= xx[r,j]
        sr2=sr2/N
        for rr in range(0,N):
            s2+= (xx[rr,j]-sr2)**2
        s2=math.sqrt(s2/(N-1))
        for v in range(0,N):
            rk+=(xx[v,i]-sr1)*(xx[v,j]-sr2)
        rk=(rk/(N-1))/(s1*s2)
        cor[i,j]=rk;
        print(i+1,":",j+1,round(rk,3)," ",end="" )
        sr2=0
        s2=0
        rk=0
    sr1=0
    s1=0
    print()
print()
R=np.zeros((M),dtype=float)
A=np.zeros((M,M),dtype=float)
D=np.zeros((M),dtype=float)

R,A=np.linalg.eig(cor)

for i in range(0,M-1):
    for j in range(i+1,M):
        if(R[i]<R[j]):
            z=R[i]
            R[i]=R[j]
            R[j]=z
            for n in range(0,M):
                z=A[n,i]
                A[n,i]=A[n,j]
                A[n,j]=z

D=R
D=D/M*100
for i in range(1,M):
    D[i]=D[i]+D[i-1]


print("Собственные числа","  Накопленные отношения %")
for i in range(0,M):
    print(round(R[i],3), "        ",round(D[i],3))
S=int(input("Введите количество  факторов: "))
print()
B=np.zeros((M,M),dtype=float)
B=A.transpose()
for i in range(0,M):
    print("вектор ",i+1, B[i])

Ng=np.zeros((M,S),dtype=float)

for m in range(0,M):
    for s in range(0,S):
        Ng[m,s]=math.sqrt(R[s])*A[m,s]
print()
for m in range(0,M):
        print("Переменная ",m+1,Ng[m])

for m in range(0,M):
        Ng[m,1]= Ng[m,1]
        Ng[m,0]= Ng[m,0]
print()
Ng=varimax(Ng, gamma = 1.0, q = 20, tol = 1e-6)
print("переменные факторы","\t","ф1","\t","ф2")
for m in range(0,M):
    spred=["Иностранный язык","Физика             ","Дискретная математика","Физкультура      ", "Математика          ", "Программирование  ", "Операционные системы ","Базы данных       ", "Электротехника     "]
    print(spred[m],"\t",round(Ng[m,0],2),"  ",round(Ng[m,1],2))
print()
L1=np.zeros((S,S),dtype=float)
for i in range(0,S):
    for j in range(0,S):
        L1[i,j]=0
        for k in range(0,M):
            L1[i,j]=L1[i,j]+Ng[k,i]*Ng[k,j]

L2=np.linalg.inv(L1)
L3=np.zeros((S,M),dtype=float)
F=np.zeros((N,S),dtype=float)
for i in range(0,S):
    for j in range(0,M):
        L3[i,j]=0
        for k in range(0,S):
            L3[i,j]=L3[i,j]+L2[i,k]*Ng[j,k]

for i in range(0,N):
    for j in range(0,S):
        F[i,j]=0
        for k in range(0,M):
           F[i,j]= F[i,j]+L3[j,k]*xx[i,k]

print()
for m in range(0,N):
        print(f"Ученик номер {m+1}", abs(F[m]))

