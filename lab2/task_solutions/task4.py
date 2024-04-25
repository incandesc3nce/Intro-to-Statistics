def arrayInterval(array):
    try:
        firstZero = array.index(0)
        lastZero = len(array) - 1 - array[::-1].index(0)
    except ValueError:
        print("В вашем массиве не хватает нулей!")
        return

    array_B = array[firstZero + 1:lastZero]

    print(array_B)
    return len(array_B)

array = []
while True:
    n = 0
    try:
        n = input("Введите количество чисел в массиве: ")
        n = int(n)
        break
    except ValueError:
        print("Введите целое число!")
        continue

while True:
    for i in range(1, n+1):
        try:
            num = input("Введите число " + str(i) + " (ваш массив должен содержать 2 нуля!): ")
            num = int(num)
            array.append(num)
        except ValueError:
            print("Введите целое число!")

    break

print( arrayInterval(array) )