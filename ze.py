import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

#Exemplo de Série
#------------------------------------------------------

# notas= pd.Series([10, 5, 7.5, 9, 10])
# print(notas)

# print(notas.values)#Imprimir valores
# print(notas.index)#Imprimir index

# notas2 = pd.Series(notas,index=['José', 'Carlos','André','Pedro', 'Maria'])#Atribuir Indices
# print(notas2)

# print(notas.describe())#Exibe informações estatísticas
# print(notas.mean())#Exibe Média

# print(notas**2)#Imprimiir Quadrado
# print(np.log(notas))


# #Exemplos de DataFrame
# #------------------------------------------------------
# df = pd.DataFrame({'Aluno' : ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
#                    'Faltas' : [3,4,2,1,4],
#                    'Prova' : [2,7,5,10,6],
#                    'Seminário': [8.5,7.5,9.0,7.5,8.0]})

# print(df)#Imprimir    
# display(df)#Imprimir com Display
# print(df.dtypes)#Imprimir os tipos   
# print(df.columns)#Imprimir colunas  
# print(df["Aluno"])#Imprimir por nomes de colunas
# print(df.describe())#Métodos estatísticos
# print(df.sort_values(by="Seminário"))#Ordnar por parâmetro             
# print(df.loc[3])#Acessar por index ou rótulo
# print(df[df["Seminário"] > 8.0])#Filtrar por valor lógico
# print(df[(df["Seminário"] > 8.0) & (df["Prova"] > 3)])#Filtrar por combinação Lógica

#Leitura de dados
df_csv = pd.read_csv("https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv")
print(df_csv)
print(df_csv.head(3))#Imprime os 3 primeiros registros
print(df_csv.tail(3))#Imprime os 3 últimos registros

#Manipulação
print(df_csv['bairro'].unique())#Exibir únicos
print(df_csv['bairro'].value_counts())#Contar dados
print(df_csv.groupby("bairro").mean())#Agrupar por média de bairros

df2 = df_csv.head()#Cria um dataframe com 5 itens usando o anterior.
df2 = df2.replace({"pm2": {12031.25: np.nan}})#Substitui o 12031 por NaN
print(df2)

# df2.dropna()#Remove linhas que possuam erros NaN
# print(df2)
# df2.fillna(99)#Trocar valores que possuem NaN por outro específico
# print(df2)
# df2.isna()#Verificar quem é NaN ou não.
# print(df2)


#Gráficos
# nome = ['carlos','jose','andre', 'pedro']
# valores = [5,8,6, 2]

# plt.plot(nome,valores)
try:
    df_csv['preco'].plot.hist()
except:
    print("Erro fatal!")
#df_csv['preco'].plot.hist(bins=30, edgecolor='black')
#df_csv['bairro'].value_counts().plot.bar()
#df_csv['bairro'].value_counts().plot.barh()
#df_csv['bairro'].value_counts().plot.barh(title = 'Números de bairros')
#df_csv.plot.scatter(x='preco', y='area')
#df_csv['quartos'].value_counts().plot.pie()