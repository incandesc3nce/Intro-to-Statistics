import math

def row(x, condition):

    p = 1
    power = 1
    k1 = 1
    k2 = 2
    fact1 = 1
    fact2 = 1

    result = 1
    if condition == 0:
        n = int
        while True:
            try:
                n = int(input("Введите число слагаемых: "))
                x = float(x)
                break
            except ValueError:
                print("Повторите ввод")
                continue



        for i in range(1, n+1):
            p = p * x * x
            power = power * 2 * 2
            fact1 *= k1
            fact2 *= k2
            if i % 2 == 0:
                result += p / power * fact1 * fact2
            else:
                result -= p / power * fact1 * fact2
            k1 += 1
            k2 += 1

    elif condition == 1:
        e0 = float
        while True:
            try:
                e0 = float(input("Введите точность: "))
                x = float(x)
                break
            except ValueError:
                print("Повторите ввод")
                continue

        i = 0
        while math.fabs(result) > e0:
            p = p * x * x
            power = power * 2 * 2
            fact1 *= k1
            fact2 *= k2
            if i % 2 == 0:
                result += p / power * fact1 * fact2
            else:
                result -= p / power * fact1 * fact2
            k1 += 1
            k2 += 1
            i += 1

    return result


x = float
condition = int

while True:
    try:
        x = input("Введите аргумент: ")
        x = float(x)
        break
    except ValueError:
        print("Повторите ввод")
        continue

while True:
    try:
        condition=int(input("Введите 0 - число слагаемых или 1 - точность: "))
    except ValueError:
        print("Повторите ввод")
        continue
    else:
        if condition == 0 or condition == 1:
            break
        else:
            print("Вы ввели не 0 или 1 ")
            continue

endResult = row(x, condition)
print("%.5f " %endResult)
