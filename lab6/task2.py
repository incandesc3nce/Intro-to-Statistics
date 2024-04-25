import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scipy.stats import t, f


class HypothesisTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hypothesis Testing App")
        self.root.geometry("500x500")

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.data_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Данные", menu=self.data_menu)
        self.data_menu.add_command(label="Загрузить", command=self.load_data)

        self.hypothesis_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Гипотезы", menu=self.hypothesis_menu)
        self.hypothesis_menu.add_command(label="Средних", command=self.select_means_hypothesis)
        self.hypothesis_menu.add_command(label="Дисперсий", command=self.select_variances_hypothesis)

        self.menu.add_command(label="Выход", command=self.root.quit)

        self.label = ttk.Label(root, text="Уровень доверия:")
        self.label.pack()

        self.confidence_entry = ttk.Entry(root)
        self.confidence_entry.pack()

        self.calculate_button = ttk.Button(root, text="Вычислить", command=self.calculate_hypothesis)
        self.calculate_button.pack()

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack()

        self.data_loaded = False
        self.selected_hypothesis = None

    def load_data(self):
        file1 = filedialog.askopenfilename(title="Select data file 1")
        file2 = filedialog.askopenfilename(title="Select data file 2")

        if file1 and file2:
            self.data_loaded = True
            self.data1 = np.loadtxt(file1)
            self.data2 = np.loadtxt(file2)

            self.plot_data()

    def plot_data(self):
        plt.figure(figsize=(8, 6))
        plt.hist(self.data1, alpha=0.5, label='Data 1')
        plt.hist(self.data2, alpha=0.5, label='Data 2')
        plt.legend()

        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def select_means_hypothesis(self):
        self.selected_hypothesis = "means"

    def select_variances_hypothesis(self):
        self.selected_hypothesis = "variances"

    def calculate_hypothesis(self):
        if not self.data_loaded:
            self.result_label.config(text="Данные не загружены")
            return

        confidence_level = float(self.confidence_entry.get())

        if self.selected_hypothesis == "means":
            stat, p_value = ttest_means(self.data1, self.data2)
            critical_value = t.ppf(1 - confidence_level / 2, len(self.data1) + len(self.data2) - 2)
            if stat < critical_value:
                result = "Гипотеза отвергается\n"
            else:
                result = "Гипотеза принимается\n"
            result += f"|t|: {stat:.4f}\n"
            result += f"T1-alfa = {critical_value:.4f}"
        elif self.selected_hypothesis == "variances":
            stat = np.var(self.data1, ddof=1) / np.var(self.data2, ddof=1)
            critical_value1 = f.ppf(confidence_level / 2, len(self.data1) - 1, len(self.data2) - 1)
            critical_value2 = f.ppf(1 - confidence_level / 2, len(self.data1) - 1, len(self.data2) - 1)
            if stat < critical_value1 or stat < critical_value2:
                result = "Гипотеза принимается\n"
            else:
                result = "Гипотеза отвергается\n"
            result += f"c1: {stat:.4f} < "
            result += f"V: {critical_value1:.4f} < c2: {critical_value2:.4f}"
        else:
            result = "Гипотеза не выбрана"

        self.result_label.config(text=result)


def ttest_means(data1, data2):
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)
    std1 = np.std(data1, ddof=1)
    std2 = np.std(data2, ddof=1)
    n1 = len(data1)
    n2 = len(data2)

    pooled_std = np.sqrt((std1 ** 2 / n1) + (std2 ** 2 / n2))
    t_statistic = (mean1 - mean2) / pooled_std

    dof = n1 + n2 - 2
    p_value = 2 * (1 - t.cdf(abs(t_statistic), dof))

    return t_statistic, p_value


root = tk.Tk()
app = HypothesisTestApp(root)
root.mainloop()
