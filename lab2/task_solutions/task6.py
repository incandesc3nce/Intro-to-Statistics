from collections import Counter
import math

# среднее
def calculate_mean(data):
    return sum(data) / len(data)

# мода
def calculate_mode(data):
    counts = Counter(data)
    return max(counts, key=counts.get)

# медиана
def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        return sorted_data[n//2]

# дисперсия
def calculate_variance(data):
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# стандартное отклонение
def calculate_std_dev(data):
    return math.sqrt(calculate_variance(data))

# асимметрия
def calculate_skew(data):
    mean = calculate_mean(data)
    std_dev = calculate_std_dev(data)
    n = len(data)
    skew = sum((x - mean) ** 3 for x in data) * n / ((n - 1) * (n - 2) * std_dev ** 3)
    return skew

# эксцесс
def calculate_kurtosis(data):
    mean = calculate_mean(data)
    std_dev = calculate_std_dev(data)
    n = len(data)
    kurt = sum((x - mean) ** 4 for x in data) * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * std_dev ** 4) - 3 * (n - 1) ** 2 / ((n - 2) * (n - 3))
    return kurt

# main

with open('input.txt', 'r') as file:
    data = [int(x) for x in file.readline().split()]


mean = calculate_mean(data)
mode = calculate_mode(data)
median = calculate_median(data)
variance = calculate_variance(data)
std_dev = calculate_std_dev(data)
skewness = calculate_skew(data)
kurtosis = calculate_kurtosis(data)


with open('output.txt', 'w') as file:
    file.write(f"Среднее: {mean}\n")
    file.write(f"Мода: {mode}\n")
    file.write(f"Медиана: {median}\n")
    file.write(f"Дисперсия: {variance}\n")
    file.write(f"Стандартное отклонение: {std_dev}\n")
    file.write(f"Асимметрия: {skewness}\n")
    file.write(f"Эксцесс: {kurtosis}\n")

print(f"Среднее: {mean}")
print(f"Мода: {mode}")
print(f"Медиана: {median}")
print(f"Дисперсия: {variance}")
print(f"Стандартное отклонение: {std_dev}")
print(f"Асимметрия: {skewness}")
print(f"Эксцесс: {kurtosis}")
