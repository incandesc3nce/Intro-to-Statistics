import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_wine
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# Загрузка данных
iris = load_iris()
X = iris.data
y = iris.target

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Обучение модели линейного дискриминантного анализа
lda = LDA(n_components=2)
X_r2 = lda.fit(X_train, y_train).transform(X_train)

# Построение графика
colors = ['navy', 'turquoise', 'darkorange']
target_names = iris.target_names

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r2[y_train == i, 0], X_r2[y_train == i, 1], alpha=0.8, color=color, label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA of IRIS dataset')
plt.xlabel('LD1')
plt.ylabel('LD2')
plt.show()

# Предсказание класса для неизвестного цветка
unknown_flower = np.array([[5, 3, 1, 0.2]])  # Пример параметров неизвестного цветка
predicted_class = lda.predict(unknown_flower)
print(f'Предсказанный класс: {iris.target_names[predicted_class][0]}')

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

print(model.predict(unknown_flower))
