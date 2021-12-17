import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display



#Exemplo de Série
#------------------------------------------------------

notas= pd.Series([10, 5, 7.5, 9, 10])
print(notas)

print(notas.values)#Imprimir valores
print(notas.index)#Imprimir index

notas2 = pd.Series(notas,index=['José', 'Carlos','André','Pedro', 'Maria'])#Atribuir Indices
print(notas2)

print(notas.describe())#Exibe informações estatísticas
print(notas.mean())#Exibe Média

print(notas**2)#Imprimiir Quadrado
print(np.log(notas))


#Exemplos de DataFrame
#------------------------------------------------------
df = pd.DataFrame({'Aluno' : ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                   'Faltas' : [3,4,2,1,4],
                   'Prova' : [2,7,5,10,6],
                   'Seminário': [8.5,7.5,9.0,7.5,8.0]})

print(df)#Imprimir    
display(df)#Imprimir com Display
print(df.dtypes)#Imprimir os tipos   
print(df.columns)#Imprimir colunas  
print(df["Aluno"])#Imprimir por nomes de colunas
print(df.describe())#Métodos estatísticos
print(df.sort_values(by="Seminário"))#Ordnar por parâmetro             
print(df.loc[3])#Acessar por index ou rótulo
print(df[df["Seminário"] > 8.0])#Filtrar por valor lógico
print(df[(df["Seminário"] > 8.0) & (df["Prova"] > 3)])#Filtrar por combinação Lógica