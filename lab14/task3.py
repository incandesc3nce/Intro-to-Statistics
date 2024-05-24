import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_wine
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# Загрузка данных
wine = load_wine()
X = wine.data
y = wine.target
feature_names = wine.feature_names

# Выбор признаков (4 7 8 9)
X_selected = X[:, [3, 6, 7, 8]]  # Индексы 2, 4, 7, 10 соответствуют признакам 3, 5, 8, 11

# Трехмерное изображение по признакам 3, 5, 8
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_selected[:, 0], X_selected[:, 1], X_selected[:, 2], c=y, cmap='viridis', edgecolor='k', s=40)
ax.set_xlabel(feature_names[3])
ax.set_ylabel(feature_names[6])
ax.set_zlabel(feature_names[7])
plt.title('3D Plot of Selected Wine Features')
plt.show()

# Двумерный график по признакам 3 и 5
plt.figure()
plt.scatter(X_selected[:, 0], X_selected[:, 1], c=y, cmap='viridis', edgecolor='k', s=40)
plt.xlabel(feature_names[3])
plt.ylabel(feature_names[6])
plt.title('2D Plot of Selected Wine Features')
plt.show()

# Дискриминантный анализ по признакам 3, 5, 8, 11
lda = LDA()
X_lda = X_selected[:, [0, 1, 2, 3]]
lda.fit(X_lda, y)

# Пример параметров нового вина для предсказания класса
new_wine = np.array([[14.3, 14.4, 17.0, 11.0]])  # Признаки 3, 5, 8, 11
predicted_class = lda.predict(new_wine)
print(f'Предсказанный класс: {wine.target_names[predicted_class][0]}')
