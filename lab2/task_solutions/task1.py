import math

def f(x):
    module = math.fabs(x + 5)

    if module <= 0.1 or module < 2:
        if module <= 0.1:
            return math.sin(pow(x, 2)) + x
        else:
            return math.cos(x)
    else:
        return 0


number = input("Введите число: ")
number = float(number)

y = f(number)
print("%.4f " %y)
