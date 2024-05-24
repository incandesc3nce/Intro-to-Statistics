from sklearn.datasets import load_iris, load_wine
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

# Загрузка данных
iris = load_iris()
wine = load_wine()

# Дискриминантный анализ данных по вину
X_wine = wine.data
y_wine = wine.target
lda_wine = LDA(n_components=2)
X_r2_wine = lda_wine.fit_transform(X_wine, y_wine)

# Печать информации по вину
print(f"Проектированные данные по вину:\n{X_r2_wine}")

# Дискриминантный анализ данных по ирисам
X_iris = iris.data
y_iris = iris.target
lda_iris = LDA(n_components=2)
X_r2_iris = lda_iris.fit_transform(X_iris, y_iris)

# Печать информации по ирисам
print(f"Проектированные данные по ирисам:\n{X_r2_iris}")

# Визуализация данных по ирисам
fig = plt.figure(figsize=(14, 6))

# 3D-график по признакам 1, 3 и 4 (соответствуют индексам 0, 2 и 3)
ax = fig.add_subplot(121, projection='3d')
ax.scatter(X_iris[:, 0], X_iris[:, 1], X_iris[:, 2], c=y_iris, cmap='viridis', edgecolor='k')
ax.set_xlabel(iris.feature_names[0])
ax.set_ylabel(iris.feature_names[1])
ax.set_zlabel(iris.feature_names[2])
ax.set_title('3D Visualization of Iris Data')

# 2D-график по признакам 1 и 3 (соответствуют индексам 0 и 2)
ax2 = fig.add_subplot(122)
ax2.scatter(X_iris[:, 0], X_iris[:, 1], c=y_iris, cmap='viridis', edgecolor='k')
ax2.set_xlabel(iris.feature_names[0])
ax2.set_ylabel(iris.feature_names[1])
ax2.set_title('2D Visualization of Iris Data')

plt.tight_layout()
plt.show()

X = iris.data[:, :4]  # 4 показателя
y = iris.target  # 3 класса
model = LinearDiscriminantAnalysis()
model.fit(X, y) # готово
# метод оценивания модели
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
# оценивание модели
scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1)
print(np.mean(scores))  # оценка качества в %
# прогноз
new = [5, 3, 1, .4] # новый цветок с параметрами
print(model.predict([new]))

