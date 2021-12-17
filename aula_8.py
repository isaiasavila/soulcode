# Aula 8 - 02/09/21
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from scipy.stats import gaussian_kde

#Series
n = [10, 5, 7., 10]
notas = pd.Series(n)
print(notas)
print(notas.index)
print(notas.values)
notas2 = pd.Series(n, index = ['Tiago','Pedro','João','Mateus']) # n precisa ser uma lista, não uma série
print(notas2)
p = ['João','Mateus','Tiago','Pedro']
notas2 = pd.Series([10, 5, 7., 10], p)
print(notas2.describe())
print(notas2.mean())
print(np.log(notas2))

#DataFrame
df = pd.DataFrame({
    'Aluno' : ['João','Mateus','Tiago','Pedro'],
    'Faltas' : [4, 2, 3, 3],
    'Prova' : [10, 9., 8, 4],
    'Seminario' : [9.1, 4, 5, 6]})
print(df.describe())
print(df[df['Seminario'] > 6.9])
display(df) # Forma diferente de apresentar os dados
print(df.dtypes)
print(df.columns)
print(df['Prova'])
df_csv = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')
display(df_csv)
print('.......')
print(df_csv.head(2))
print('.......')
print(df_csv.tail(2))
print(df_csv['bairro'].unique())
print(df_csv['bairro'].value_counts())
print(df_csv.groupby('bairro').mean())
df2 = df_csv.head()
df3 = df2.replace({'pm2':{12031.25: np.nan}})
print(df2.replace({'pm2':{np.nan: 12031.25}}))
print(df3.fillna(99))
print(df2.isna()) # Retorna True or False se os dados são números ou não
print(df3.isna())

#Grafic
plt.style.use('ggplot')
nome = ['Isaias','Laisa','Vinicius','Ítalo']
vetores = [5, 8 ,6, 2]
plt.plot(nome, vetores)
plt.title('Gráfico gerado no Python:')
plt.show()
df_csv['preco'].plot.hist(bins=30, edgecolor='black')
df_csv['bairro'].value_counts().plot.bar()
df_csv.plot.scatter(x='preco', y='area')
df_csv['bairro'].value_counts().plot.barh()
df_csv['quartos'].value_counts().plot.pie()

#Exercícios
# 1- Crie uma série com dados meteorológicos de cinco cidades como índices.
# Fonte www.inmet.gov.br
temMaxima = [27, 28, 29, 29, 30]
temMinima = [22, 20, 21, 21, 21]
cidades = ['Aracajú','Maceió','João Pessoa','Recife','Natal']
dadosMeteorologicos1 = pd.Series(temMaxima, index = cidades)
print(f'Temperatura máxima\n{dadosMeteorologicos1}')
print('Mínima: ',dadosMeteorologicos1.min())
print('Máxima: ',dadosMeteorologicos1.max())
print('Média: ',dadosMeteorologicos1.mean())
dadosMeteorologicos2 = pd.Series(temMinima, index = cidades)
print(f'Temperatura mínima\n{dadosMeteorologicos2}')
print('Mínima: ',dadosMeteorologicos2.min()) #describe()
print('Máxima: ',dadosMeteorologicos2.max())
print('Média: ',dadosMeteorologicos2.mean())
print('...')
print('...')
print('...')
# 2- Crie um Data Frame contendo os dados abaixo:
df = pd.DataFrame({
    'Nome' : ['João','Pedro','Carla','Suzane'],
    'Depósitos' : [100, 500, 300, 250],
    'Saques' : [10, 11.5, 35.3, 200],
    'Estornos' : [0, 0, 250, 300]})
# Usando o seu DataFrame mostre:
print('Os tipos de itens...')
print(df.dtypes)
print(df.head(0))
print('A média dos itens...')
print(df.mean(numeric_only=True))
print(df['Depósitos'].mean())
print(df['Saques'].mean())
print(df['Estornos'].mean())
print('Imprima o último item...')
print(df.tail(1))
print('Exiba os estornos maiores que 0...')
print(df[df['Estornos'] > 0])
print('Exiba os saques menores que 15...')
print(df[df['Saques'] < 15])
plt.style.use('ggplot')
plt.title('Temperaturas nas cidades:')
plt.plot(cidades, temMaxima, temMinima)
dadosMeteorologicos1.plot.bar()
plt.show()
plt.title('Dados bancários - Depósitos & Saques:')
nom = df['Nome'].values
dep = df['Depósitos'].values
saq = df['Saques'].values
est = df['Estornos'].values
plt.plot(nom, dep, saq)
plt.show()
df.plot.scatter(x='Nome', y='Depósitos')
df.plot.scatter(x='Nome', y='Saques')
df.plot.scatter(x='Nome', y='Estornos')
df.plot.kde(x='Nome',bw_method=0.3)
df.plot.line(x='Nome')
df = pd.DataFrame({'Depósitos': [100, 500, 300, 250],'Saques': [10, 11.5, 35.30, 200],'Estornos': [0, 0, 250, 300]}, index = ["João", "Pedro", "Carla", "Suzane"],)
display(df)
input('...')