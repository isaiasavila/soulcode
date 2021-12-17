# Importar findspark 
import findspark

# Inicializa e pega o caminho da variável Ambiente. (C:\spark-3.1.2-bin-hadoop2.7)
findspark.init()

# Importa SparkSession
from pyspark.sql import SparkSession

# Constroi SparkSession
spark = SparkSession.builder \
   .master("local") \
   .appName("Linear Regression Model") \
   .config("spark.executor.memory", "1gb") \
   .getOrCreate()
   
sc = spark.sparkContext
#------------------------------------ 1º PARTE--------------------------------
#Cria um RDD.Conjuntos de dados distribuídos resilientes 
rdd = sc.textFile('E:\scripts\Salary_Data.csv')


rdd.take(2)

# Separar linhas por delimitador.
rdd = rdd.map(lambda line: line.split(","))

# Retornas as primeiras linhas.
rdd.take(2)

# Retorna o primeiro elemento.
rdd.first()

#------------------------------------ 2º PARTE--------------------------------
# Importa módulos de linhas SQL
from pyspark.sql import Row

# Mapear o RDD por delimitadores.
df = rdd.map(lambda line: Row(AnosExperincia=line[0], Salario=line[1])).toDF()

# Mostra as primeiras 20 linhas
df.show()

#Impressão de tipos de dados
df.printSchema()

#------------------------------------ 2º PARTE--------------------------------
# Importa todos os tipos em  `sql.types`
from pyspark.sql.types import *

# Função que converte dipos de dados das colunas de um dataframe
def converterColuna(dataframe, nomes, novoTipo):
    for nome in nomes: 
        dataframe = dataframe.withColumn(nome, dataframe[nome].cast(novoTipo))
    return dataframe 

# Adiciona nomes às colunas
colunas = ['AnosExperincia', 'Salario']

# Converter colunas do dataframe em tipo Float
df = converterColuna(df, colunas, FloatType())
#df.show()

#----------------------- 3º PARTE OPERAÇÕES DE AÇÃO -------------------
#Mostrar dados
df.select('Salario').show(10)#Separado por virgula pode escoher mais de uma.

#Agrupa salários por contagem e ordena.
df.groupBy("Salario").count().sort("Salario",ascending=False)#.show()

#Seleciona número de linhas salário.
df.select('Salario').count()

#Mostrar dados analíticos.
df.describe().show()
df.describe('Salario').show()

#Retorna todos os elemtnos como uma Matriz
df.collect()

#Filtra por condições específicas
df.filter(df['Salario'] > 50000).show()
df.select('Salario').filter(df['Salario'] > 50000).show()

