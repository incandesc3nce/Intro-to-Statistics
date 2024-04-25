import tkinter as tk
from tkinter import messagebox
import math

class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Lab 6")
        self.window.geometry("500x500")

        self.create_widgets()

    def create_widgets(self):
        self.labelX = tk.Label(self.window, text="Введите x: ")
        self.labelX.place(x=50, y=30)

        self.labelInstruction = tk.Label(self.window, text="Результат функции: ")
        self.labelInstruction.place(x=30, y=300)

        self.labelResult = tk.Label(self.window, text="")
        self.labelResult.place(x=160, y=300)

        self.inputX = tk.Entry(self.window)
        self.inputX.place(x=130, y=30)

        self.formula1RadioVar = tk.IntVar()
        self.formula1Radio = tk.Radiobutton(self.window, text="sin(sin(x-1)+2.5)", variable=self.formula1RadioVar, command=lambda: self.calculate_radio(1))
        self.formula1Radio.place(x=60, y=80)

        self.formula2RadioVar = tk.IntVar()
        self.formula2Radio = tk.Radiobutton(self.window, text="cos(x+2)", variable=self.formula2RadioVar, command=lambda: self.calculate_radio(2))
        self.formula2Radio.place(x=60, y=120)

        self.formula3RadioVar = tk.IntVar()
        self.formula3Radio = tk.Radiobutton(self.window, text="3x^3", variable=self.formula3RadioVar, command=lambda: self.calculate_radio(3))
        self.formula3Radio.place(x=60, y=160)


        self.doubleResultVar = tk.BooleanVar()
        self.doubleResult = tk.Checkbutton(self.window, text="Удвоить результат", variable=self.doubleResultVar, command=self.calculate_checkbox)
        self.doubleResult.place(x=300, y=260)

        self.calculateButton = tk.Button(self.window, text="Посчитать", command=self.calculate)
        self.calculateButton.place(x=120, y=260)

        self.inputX.bind("<Key>", self.clear_radios)

    def calculate(self):
        self.clear_radios(None)

        try:
            x = float(self.inputX.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат ввода")
            return

        if x < -1:
            result = math.sin(math.sin(x - 1) + 2.5)
            self.formula1Radio.select()
        elif x < 3:
            result = math.cos(x + 2)
            self.formula2Radio.select()
        else:
            result = 3 * x ** 3
            self.formula3Radio.select()

        if self.doubleResultVar.get():
            result *= 2

        self.labelResult.config(text=str(result))

    def clear_radios(self, event):
        self.formula1Radio.deselect()
        self.formula2Radio.deselect()
        self.formula3Radio.deselect()

    def calculate_radio(self, radio_num):
        self.clear_radios(None)
        if radio_num == 1:
            self.formula2Radio.deselect()
            self.formula3Radio.deselect()
            try:
                x = float(self.inputX.get())
                result = math.sin(math.sin(x - 1) + 2.5)
                if self.doubleResultVar.get():
                    result *= 2
                self.labelResult.config(text=str(result))
            except ValueError:
                self.labelResult.config(text="Неверный формат ввода")
        elif radio_num == 2:
            self.formula1Radio.deselect()
            self.formula3Radio.deselect()
            try:
                x = float(self.inputX.get())
                result = math.cos(x + 2)
                if self.doubleResultVar.get():
                    result *= 2
                self.labelResult.config(text=str(result))
            except ValueError:
                self.labelResult.config(text="Неверный формат ввода")
        elif radio_num == 3:
            self.formula1Radio.deselect()
            self.formula2Radio.deselect()
            try:
                x = float(self.inputX.get())
                result = 3 * x ** 3
                if self.doubleResultVar.get():
                    result *= 2
                self.labelResult.config(text=str(result))
            except ValueError:
                self.labelResult.config(text="Неверный формат ввода")

    def calculate_checkbox(self):
        try:
            result = float(self.labelResult.cget("text"))
            if self.doubleResultVar.get():
                result *= 2
            else:
                result /= 2
            self.labelResult.config(text=str(result))
        except ValueError:
            self.labelResult.config(text="Неверный формат ввода")

if __name__ == "__main__":
    UI = UserInterface()
    UI.window.mainloop()
