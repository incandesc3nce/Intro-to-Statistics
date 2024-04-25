import matplotlib.pyplot as plt
import numpy as np
import math
import tkinter as tk
# реализация класса для корреляционного анализа. всего будет 7 выборок:
# парная корреляция, частичная корреляция, множественная корреляция - из файла main_corr.txt
# корреляционное отношение - из файла corr_relation.txt
# коэффициент Спирмена - из файла spirman.txt
class Corr:
  def __init__(self):
      self.data = []
      self.data1 = []
      self.data2 = []

  def read_data(self, filename):
      with open(filename, 'r') as file:
          for line in file:
              self.data.append([float(x) for x in line.split()])
      self.data1 = self.data[0]
      self.data2 = self.data[1]

  def read_data2(self, filename):
      with open(filename, 'r') as file:
          for line in file:
              self.data.append([float(x) for x in line.split()])
      self.data1 = self.data[2]
      self.data2 = self.data[3]

  def pair_corr(self):
      return np.corrcoef(self.data1, self.data2)[0][1]
  
  def partial_corr(self):
      return np.corrcoef(self.data1, self.data2)[0][1]
  
  def multiple_corr(self):
      return np.corrcoef(self.data1, self.data2)[0][1]
  
  def corr_relation(self):
      return np.corrcoef(self.data1, self.data2)[0][1]
  
  def spirman(self):
      return np.corrcoef(self.data1, self.data2)[0][1]
  
  def plot(self):
      plt.scatter(self.data1, self.data2)
      plt.show()

class GUI:
  def __init__(self):
      self.root = tk.Tk()
      self.root.title('Lab 9')
      self.root.geometry('500x600')
      self.corr = Corr()
      self.corr.read_data('main_corr.txt')
      self.corr.read_data2('main_corr.txt')
      
      
      self.label1 = tk.Label(self.root, text='Введите номер выборки:')
      self.label1.pack()
      self.entry1 = tk.Entry(self.root)
      self.entry1.pack()

      self.label2 = tk.Label(self.root, text='Введите номер выборки:')
      self.label2.pack()
      self.entry2 = tk.Entry(self.root)
      self.entry2.pack()

      self.trust_label = tk.Label(self.root, text='Введите уровень доверия:')
      self.trust_label.pack()
      self.trust_entry = tk.Entry(self.root)
      self.trust_entry.pack()

      self.var = tk.IntVar()
      self.checkbutton = tk.Checkbutton(self.root, text='Обратное отношение yx', variable=self.var)
      self.checkbutton.pack()

      #radiobuttons 12-3 или 1-23, 13-2 или 2-13, 23-1 или 3-12
      self.var1 = tk.IntVar()
      self.var2 = tk.IntVar()
      self.var3 = tk.IntVar()
      
      self.radiobutton1 = tk.Radiobutton(self.root, text='12-3 или 1-23', variable=self.var1, value=1)
      self.radiobutton1.pack()
      self.radiobutton2 = tk.Radiobutton(self.root, text='13-2 или 2-13', variable=self.var2, value=2)
      self.radiobutton2.pack()
      self.radiobutton3 = tk.Radiobutton(self.root, text='23-1 или 3-12', variable=self.var3, value=3)
      self.radiobutton3.pack()



      self.pair_corr = tk.Button(self.root, text='Коэф. парной корреляции', command=self.pair_corr)
      self.pair_corr.pack()
      self.partial_corr = tk.Button(self.root, text='Коэф. частной корреляции', command=self.partial_corr)
      self.partial_corr.pack()
      self.corr_relation = tk.Button(self.root, text='Корреляционное отношение', command=self.corr_relation)
      self.corr_relation.pack()
      # значимость коэф. корреляции
      self.significance = tk.Button(self.root, text='Значимость коэф. корреляции', command=self.significance)
      self.significance.pack()
      # коэф множественной корреляции
      self.multiple_corr = tk.Button(self.root, text='Коэф. множественной корреляции', command=self.multiple_corr)
      self.multiple_corr.pack()
      # ранговые корреляции
      self.spirman = tk.Button(self.root, text='Ранговые корреляции', command=self.spirman)
      self.spirman.pack()

      # label коэффициент парной корреляции
      self.label_pair_corr = tk.Label(self.root, text='Коэффициент парной корреляции:')
      self.label_pair_corr.pack()

      self.root.mainloop()
      

  def pair_corr(self):
      self.button = tk.Button(self.root, text='Коэф. парной корреляции', command=self.pair_corr)
      self.button.pack()

  
  def partial_corr(self):
      self.button = tk.Button(self.root, text='Коэф. частной корреляции', command=self.partial_corr)
      self.button.pack()

  
  def multiple_corr(self):
      self.button = tk.Button(self.root, text='Множественная корреляция', command=self.multiple_corr)
      self.button.pack()

  
  def corr_relation(self):
      self.button = tk.Button(self.root, text='Корреляционное отношение', command=self.corr_relation)
      self.button.pack()

  
  def spirman(self):
      self.button = tk.Button(self.root, text='Ранговые корреляции', command=self.spirman)
      self.button.pack()

  
  def significance(self):
      self.button = tk.Button(self.root, text='Значимость коэф. корреляции', command=self.significance)
      self.button.pack()

  def pair_corr_label(self):
      self.label_pair_corr = tk.Label(self.root, text='Коэффициент парной корреляции: ' + str(self.corr.pair_corr()))
      self.label_pair_corr.pack()

  
  
      