# Exercício Um
#Importando bibliotecas necessárias.
from pyspark.sql.session import SparkSession
#Importar tipos de dados a serem trabalhados
from pyspark.sql.types import (BooleanType, IntegerType, StringType, DateType,
                               TimestampType, StructType, MapType,
                               StructField, ArrayType,
                               TimestampType, FloatType)

#Trataremos funções como F
import pyspark.sql.functions as F
# Função que converte dipos de dados das colunas de um dataframe
def converterColuna(dataframe, nomes, novoTipo):
    for nome in nomes: 
        dataframe = dataframe.withColumn(nome, dataframe[nome].cast(novoTipo))
    return dataframe

#Cria sessão SPARK
spark = SparkSession.builder.appName('Adult')\
   .config('spark.master', 'local')\
   .config("spark.executor.memory", "1gb") \
   .config('spark.shuffle.sql.partitions', 1)\
   .getOrCreate()

#Definir esquema de tratamento dos dados.
esquema = StructType([StructField("id", IntegerType()),
                   StructField("age", IntegerType()),
                   StructField("workclass", StringType()),
                   StructField("fnlwgt", IntegerType()),
                   StructField("education", StringType()),
                   StructField("education_num",IntegerType()),
                   StructField("marital", StringType()),
                   StructField("occupation", StringType()),
                   StructField("relationship", StringType()),
                   StructField("race", StringType()),
                   StructField("sex", StringType()),
                   StructField("capital_gain", IntegerType()),
                   StructField("capital_loss", IntegerType()),
                   StructField("hours_week", StringType()),
                   StructField("native_country", StringType()),
                   StructField("label", StringType()),
                  ])

caminho = "c:/python/adult_data.csv"

df   = spark.read.format("csv")\
                  .schema(esquema)\
                  .load(caminho)
print('Esquema...')
# Imprima o Schema final desse DF.
# df.printSchema()
print('Primeira amostra...')
# Imprima os 5 primeiros itens do DF.
# df.show(5)
lista = ['age']
# Converta o campo idade do tipo inteiro para o tipo float
df = converterColuna(df, lista, FloatType())
print('Novo esquema...')
# df.printSchema()
# Exiba somente 5 itens com os campos ‘age’ e ‘education’.
print('Apenas os cinco primeiros age e education...')
#df.select('age','education').show(5)
#Agrupe a quantidade de itens em ‘education’ ordenados de maneira ascendente.
# df.groupBy("education","education_num").count().sort("education_num",ascending=True).show()
df.groupBy("education").count().sort("count",ascending=True).show() # ascending=True padrão
#Exiba um describe da tabela ‘capital_gain’
print('Exiba um describe da tabela ‘capital_gain’')
df.describe('capital_gain').show()