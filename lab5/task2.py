import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2, norm, pareto, kstest

# Define samples
sample1 = np.loadtxt("test1")
sample2 = np.loadtxt("test2")

# Define functions for parameter estimation
def estimate_exponential_parameters(sample):
    lambda_estimate = 1 / np.mean(sample)
    return lambda_estimate

def estimate_normal_parameters(sample):
    mean_estimate = np.mean(sample)
    std_estimate = np.std(sample)
    return mean_estimate, std_estimate

def estimate_pareto_parameters(sample):
    Xm_estimate = np.min(sample)
    k_estimate = len(sample) / np.sum(np.log(sample / Xm_estimate))
    return Xm_estimate, k_estimate

# Chi-squared test
def chi_square_test(sample, distribution, params, plot_number):
    hist, bins = np.histogram(sample, bins=10, density=True)
    bin_centers = (bins[:-1] + bins[1:]) / 2

    if distribution == 'exponential':
        theoretical_pdf = np.exp(-params[0] * bin_centers) * params[0]
    elif distribution == 'normal':
        theoretical_pdf = norm.pdf(bin_centers, *params)
    elif distribution == 'pareto':
        theoretical_pdf = pareto.pdf(bin_centers, params[1], scale=params[0])

    valid_indices = theoretical_pdf != 0
    chi_statistic = np.sum(((hist[valid_indices] - theoretical_pdf[valid_indices]) ** 2) / theoretical_pdf[valid_indices])

    degrees_of_freedom = np.count_nonzero(valid_indices) - len(params) - 1

    plt.subplot(2, 3, plot_number)
    plt.hist(sample, bins=10, density=True, alpha=0.6, label='Гистограмма выборки')
    plt.plot(bin_centers[valid_indices], theoretical_pdf[valid_indices], label='Теоретическая PDF')
    plt.legend()
    plt.title(f'Тест Хи-квадрат ({distribution.capitalize()} распределение)')
    plt.xlabel('Значения')
    plt.ylabel('Вероятность')

    return chi_statistic

# Kolmogorov-Smirnov test
def ks_test(sample, distribution, params, plot_number):
    if distribution == 'exponential':
        ks_statistic, p_value = kstest(sample, 'expon', args=params)
    elif distribution == 'normal':
        ks_statistic, p_value = kstest(sample, 'norm', args=params)
    elif distribution == 'pareto':
        ks_statistic, p_value = kstest(sample, 'pareto', args=params)

    plt.subplot(2, 3, plot_number)
    plt.hist(sample, bins=10, density=True, cumulative=True, alpha=0.6, label='Эмпирическая CDF')
    if distribution == 'exponential':
        plt.plot(np.sort(sample), 1 - np.exp(-params[0] * np.sort(sample)), label='Теоретическая CDF')
    elif distribution == 'normal':
        plt.plot(np.sort(sample), norm.cdf(np.sort(sample), *params), label='Теоретическая CDF')
    elif distribution == 'pareto':
        plt.plot(np.sort(sample), pareto.cdf(np.sort(sample), *params), label='Теоретическая CDF')
    plt.legend()
    plt.title(f'Тест Колмогорова-Смирнова ({distribution.capitalize()} распределение)')
    plt.xlabel('Значения')
    plt.ylabel('Кумулятивная вероятность')

    return ks_statistic

# Confidence interval for normal distribution
def confidence_interval_normal(sample, alpha):
    n = len(sample)
    mean_estimate, std_estimate = estimate_normal_parameters(sample)
    z_critical = norm.ppf(1 - alpha / 2)
    lower_bound = mean_estimate - z_critical * (std_estimate / np.sqrt(n))
    upper_bound = mean_estimate + z_critical * (std_estimate / np.sqrt(n))
    return lower_bound, upper_bound

def confidence_interval_variance(sample, alpha):
    n = len(sample)
    _, std_estimate = estimate_normal_parameters(sample)
    chi_lower = chi2.ppf(alpha / 2, n - 1)
    chi_upper = chi2.ppf(1 - alpha / 2, n - 1)
    lower_bound = (n - 1) * std_estimate ** 2 / chi_upper
    upper_bound = (n - 1) * std_estimate ** 2 / chi_lower
    return lower_bound, upper_bound

alpha = 0.05
confidence_interval_mean_95 = confidence_interval_normal(sample2, alpha)
confidence_interval_mean_99 = confidence_interval_normal(sample2, 0.01)
confidence_interval_variance_95 = confidence_interval_variance(sample2, alpha)
confidence_interval_variance_99 = confidence_interval_variance(sample2, 0.01)

print("95% доверительный интервал для среднего (выборка 2):", confidence_interval_mean_95)
print("99% доверительный интвервал для среднего (выборка 2):", confidence_interval_mean_99)
print("95% доверительный интервал для дисперсии (выборка 2):", confidence_interval_variance_95)
print("99% доверительный интервал для дисперсии (выборка 2):", confidence_interval_variance_99)

# Hypothesis testing


# Пример использования:
lambda_estimate_sample1 = estimate_exponential_parameters(sample1)
mean_estimate_sample1, std_estimate_sample1 = estimate_normal_parameters(sample1)
Xm_estimate_sample1, k_estimate_sample1 = estimate_pareto_parameters(sample1)

plt.figure(figsize=(12, 8))

# Chi-square test for sample 1
chi_statistic_exp_sample1 = chi_square_test(sample1, 'exponential', (lambda_estimate_sample1,), 1)
chi_statistic_norm_sample1 = chi_square_test(sample1, 'normal', (mean_estimate_sample1, std_estimate_sample1), 2)
chi_statistic_pareto_sample1 = chi_square_test(sample1, 'pareto', (Xm_estimate_sample1, k_estimate_sample1), 3)

# Chi-square test for sample 2
lambda_estimate_sample2 = estimate_exponential_parameters(sample2)
mean_estimate_sample2, std_estimate_sample2 = estimate_normal_parameters(sample2)
Xm_estimate_sample2, k_estimate_sample2 = estimate_pareto_parameters(sample2)

chi_statistic_exp_sample2 = chi_square_test(sample2, 'exponential', (lambda_estimate_sample2,), 4)
chi_statistic_norm_sample2 = chi_square_test(sample2, 'normal', (mean_estimate_sample2, std_estimate_sample2), 5)
chi_statistic_pareto_sample2 = chi_square_test(sample2, 'pareto', (Xm_estimate_sample2, k_estimate_sample2), 6)

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))

# KS test for sample 1
ks_statistic_exp_sample1 = ks_test(sample1, 'exponential', (lambda_estimate_sample1,), 1)
ks_statistic_norm_sample1 = ks_test(sample1, 'normal', (mean_estimate_sample1, std_estimate_sample1), 2)
ks_statistic_pareto_sample1 = ks_test(sample1, 'pareto', (Xm_estimate_sample1, k_estimate_sample1), 3)

# KS test for sample 2
ks_statistic_exp_sample2 = ks_test(sample2, 'exponential', (lambda_estimate_sample2,), 4)
ks_statistic_norm_sample2 = ks_test(sample2, 'normal', (mean_estimate_sample2, std_estimate_sample2), 5)
ks_statistic_pareto_sample2 = ks_test(sample2, 'pareto', (Xm_estimate_sample2, k_estimate_sample2), 6)

plt.tight_layout()
plt.show()

print("Тест Хи-квадрат (Экспоненциальное распределение, выборка 1):", chi_statistic_exp_sample1)
print("Тест Хи-квадрат (Нормальное распределение, выборка 1):", chi_statistic_norm_sample1)
print("Тест Хи-квадрат (Распределение Парето, выборка 1):", chi_statistic_pareto_sample1)

print("Тест Хи-квадрат (Экспоненциальное распределение, выборка 2):", chi_statistic_exp_sample2)
print("Тест Хи-квадрат (Нормальное распределение, выборка 2):", chi_statistic_norm_sample2)
print("Тест Хи-квадрат (Распределение Парето, выборка 2):", chi_statistic_pareto_sample2)

print("Тест Колмогорова-Смирнова (Экспоненциальное распределение, выборка 1):", ks_statistic_exp_sample1)
print("Тест Колмогорова-Смирнова (Нормальное распределение, выборка 1):", ks_statistic_norm_sample1)
print("Тест Колмогорова-Смирнова (Распределение Парето, выборка 1):", ks_statistic_pareto_sample1)

print("Тест Колмогорова-Смирнова (Экспоненциальное распределение, выборка 2):", ks_statistic_exp_sample2)
print("Тест Колмогорова-Смирнова (Нормальное распределение, выборка 2):", ks_statistic_norm_sample2)
print("Тест Колмогорова-Смирнова (Распределение Парето, выборка 2):", ks_statistic_pareto_sample2)