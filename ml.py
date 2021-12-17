#Machine Learning
from operator import mod
import pandas as pd
from pandas.core.algorithms import mode
from sklearn import model_selection

arquivo = pd.read_csv('https://raw.githubusercontent.com/isaiasavila/datasets/main/wine_dataset.csv')
# arquivo.head(10)

arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)

y = arquivo['style']
x = arquivo.drop('style', axis=1)

from sklearn.model_selection import train_test_split

# Ao invés de utilizar o termo teste, alguns cientistas usam o termo avaliação
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=.3)
# print(arquivo.shape)
# print(x_treino.shape, x_teste.shape, y_treino.shape, y_teste.shape)

from sklearn.ensemble import ExtraTreesClassifier

modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)
resultado = modelo.score(x_teste, y_teste)
print('Acurácia: ', resultado)
print(y_teste[400:405]) # Mostrar cinco resultados?

previsao = modelo.predict(x_teste[400:405])
print(previsao)