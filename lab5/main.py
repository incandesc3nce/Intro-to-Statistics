import numpy as np
import matplotlib.pyplot as plt

# Выборка
data = [1.3, 5.59, 1.21, 2.88, 0.399, 0.395, 1.12, 1.37, 0.379, 0.725, 0.945,
        0.231, 3.81, 0.0839, 2.23, 0.569, 1.15, 1.35, 1.06, 1.75, 3.17,
        3.53, 0.589, 2.89, 2.6, 1.88, 1.49, 0.307, 2.08, 1.09, 1.3,
        2.32, 2.11, 0.178, 1.29, 0.533, 1.58, 3, 0.00397, 1.16, 2.23,
        0.811, 1.58, 0.0488, 2.2, 2.83, 0.345, 1.26, 2.25, 0.413, 2.45,
        1.14, 1.61, 4.23, 0.714, 2.81, 0.0455, 0.367, 0.417, 0.0773, 0.289,
        0.00971, 0.0186, 0.446, 0.983, 1.1, 0.289, 0.00281, 0.572, 1.51, 0.156,
        0.0731, 0.0902, 3.55, 2.31, 0.883, 1.6, 0.354, 0.228, 1.14, 4.2,
        2.68, 0.76, 0.614, 1.06, 2.13, 2.61, 1.18, 0.751, 1.82, 0.346,
        0.468, 0.563, 0.664, 0.929, 0.454, 0.186, 0.383, 0.119, 0.828, 0.974,
        0.155, 0.932, 0.158, 0.378, 1.44, 2.65, 0.106, 0.161, 1.32, 2.04,
        0.464, 1.39, 1.37, 0.534, 1.3, 0.348, 2.05, 2, 0.204, 1.58,
        1.29, 1.21, 0.403, 0.324, 0.471, 0.528, 0.425, 2.61, 0.432, 2.93,
        0.966, 2.08, 0.202, 0.0392, 0.29, 1.48, 0.272, 0.203, 2.69, 0.531,
        0.398, 1.28, 0.115]

# Статистический ряд
def statisticheskiy_ryad(data):
    sorted_data = sorted(data)
    unique_values = sorted(set(sorted_data), key=sorted_data.index)
    frequencies = [sorted_data.count(value) for value in unique_values]
    return unique_values, frequencies

unique_values, frequencies = statisticheskiy_ryad(data)
print("Статистический ряд:")
print("Значение: ", unique_values)
print("Частота: ", frequencies)

# Вариационный ряд
variation_series = sorted(data)
print("\nВариационный ряд:")
print(variation_series)

# Сгруппированная выборка
def group_data(data, intervals):
    min_val = min(data)
    max_val = max(data)
    interval_length = (max_val - min_val) / intervals
    groups = []

    for i in range(intervals):
        group = {
            "Interval": f"{round(min_val + i * interval_length, 2)} - {round(min_val + (i + 1) * interval_length, 2)}",
            "Frequency": 0,
            "Cumulative Frequency": 0,
            "Relative Frequency": 0,
            "Cumulative Relative Frequency": 0
        }
        groups.append(group)

    for value in data:
        for group in groups:
            interval_start, interval_end = map(float, group["Interval"].split(" - "))
            if interval_start <= value < interval_end:
                group["Frequency"] += 1

    cumulative_frequency = 0
    cumulative_relative_frequency = 0
    for group in groups:
        cumulative_frequency += group["Frequency"]
        cumulative_relative_frequency += group["Frequency"] / len(data)
        group["Cumulative Frequency"] = cumulative_frequency
        group["Relative Frequency"] = group["Frequency"] / len(data)
        group["Cumulative Relative Frequency"] = cumulative_relative_frequency

    return groups

grouped_data = group_data(data, 4)

# Выводим на консоль
print("\nТаблица частот:")
print("№\tГраницы\t\tСередина\tЧастота\tНакопл. частота\tОтн. частота\tНакопл. отн. частота")
for i, group in enumerate(grouped_data):
    print(f"{i+1}\t{group['Interval']}\t{round((float(group['Interval'].split('-')[0]) + float(group['Interval'].split('-')[1])) / 2, 2)}\t\t\t{group['Frequency']}\t\t\t{group['Cumulative Frequency']}\t\t\t{round(group['Relative Frequency'], 5)}\t\t\t{round(group['Cumulative Relative Frequency'], 5)}")

# Гистограмма частот
interval_labels = [group["Interval"] for group in grouped_data]
frequencies = [group["Frequency"] for group in grouped_data]
plt.bar(interval_labels, frequencies, width=0.5, color='skyblue', edgecolor='black')
plt.xlabel('Интервалы')
plt.ylabel('Частота')
plt.title('Гистограмма частот')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Полигон частот
midpoints = [(float(group["Interval"].split("-")[0]) + float(group["Interval"].split("-")[1])) / 2 for group in grouped_data]
plt.plot(midpoints, frequencies, marker='o', linestyle='-')
plt.xlabel('Середины интервалов')
plt.ylabel('Частота')
plt.title('Полигон частот')
plt.grid(True)
plt.show()

