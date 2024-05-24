from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_wine
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# Загрузка данных
wine = load_wine()
X = wine.data
y = wine.target
feature_names = wine.feature_names

# Выбор признаков (4 7 8 9)
X_selected = X[:, [3, 6, 7, 8]]  # Индексы 2, 4, 7, 10 соответствуют признакам 3, 5, 8, 11

# Обучение модели линейного дискриминантного анализа
lda = LDA(n_components=2)
X_r2 = lda.fit(X_selected, y).transform(X_selected)

# Построение графика
colors = ['navy', 'turquoise', 'darkorange']
target_names = wine.target_names

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], alpha=0.8, color=color, label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA of Wine dataset')
plt.xlabel('LD1')
plt.ylabel('LD2')
plt.show()

# Предсказание класса для неизвестного вина
unknown_wine = np.array([[14.3, 2.5, 2.8, 1.9]])  # Пример параметров неизвестного вина
unknown_wine_transformed = lda.transform(unknown_wine)
predicted_class = lda.predict(unknown_wine)
print(f'Предсказанный класс: {wine.target_names[predicted_class][0]}')


iris = load_iris()
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
