from scipy.special import comb

p_success = 0.01
p_failure = 1 - p_success
n_students = 800
n_excellent_students = 5

# Вычисляем число сочетаний C(800, 5)
combinations = comb(n_students, n_excellent_students)

# Вычисляем вероятность
probability = combinations * (p_success**n_excellent_students) * (p_failure**(n_students - n_excellent_students))

print(f"Вероятность, что среди 800 студентов будет 5 отличников, равна {probability:.9f}")