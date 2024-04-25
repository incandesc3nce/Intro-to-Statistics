import numpy as np

M = 0
N = 0
while True:
    try:
        M = int(input("Введите количество строк M: "))
        break
    except ValueError:
        print("Введите целое число!")
        continue

while True:
    try:
        N = int(input("Введите количество столбцов N: "))
        break
    except ValueError:
        print("Введите целое число!")
        continue


array = np.zeros((M, N), dtype=int)

for i in range(M):
    for j in range(N):
        array[i][j] = (j + i) % N + 1

print(array)