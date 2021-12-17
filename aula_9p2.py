# Exercício aula 9 - 08/09/21
#Importando bibliotecas necessárias.
from pyspark.sql.session import SparkSession

#Importar tipos de dados a serem trabalhados
from pyspark.sql.types import (BooleanType, IntegerType, StringType, 
                               TimestampType, StructType,
                               StructField, ArrayType,
                               TimestampType,FloatType)

#Trataremos funções como F
import pyspark.sql.functions as F

#Cria sessão SPARK
spark = SparkSession.builder.appName('firstSeesion')\
   .config('spark.master', 'local[4]')\
   .config("spark.executor.memory", "1gb") \
   .config('spark.shuffle.sql.partitions', 1)\
   .getOrCreate()   

#============================================================
# df = spark.read.load("E:/scripts/covid_cases.csv",format="csv", 
#sep=",", inferSchema="true", header="true")

#============================================================
#--------------------------EXTRAIR-----------------------------
#Definir esquema de tratamento dos dados.
schema = StructType([StructField("case_id", IntegerType()),
                   StructField("province", StringType()),
                   StructField("city", StringType()),
                   StructField("group", BooleanType()),
                   StructField("infection_case", StringType()),
                   StructField("confirmed",IntegerType()),
                   StructField("latitude", StringType()),
                   StructField("longitude", StringType()),

                  ])

path = "E:/scripts/covid_cases_no_header.csv"

df   = spark.read.format("csv")\
                  .schema(schema)\
                  .load(path)

#=======================================================

#Imprima o Schema final desse DF.
df.printSchema()

#Imprima os 5 primeiros itens do DF.
df.show(5)

#Alterar o nome de uma tabela
cases = df.withColumnRenamed("infection_case","Casos de Infecção")

#Alterar todas as colunas
cases = cases.toDF(*['ID', 'Província', 'Cidade', 'Grupo', 'Casos de Infecção', 'Confirmados','Latitude', 'Longitude'])






















#Retorna apenas alguns dados
cases = cases.select('province','city','confirmed')
#Consultas lógicas
cases.filter((cases.confirmed>10) & (cases.province=='Daegu')).show()
#Ordenar em ordem decrescente
cases.sort(F.desc("confirmed")).show(5)
#Inicia novoDF
regions = spark.read.load("E:/scripts/Region.csv",format="csv", sep=",", inferSchema="true", header="true")
regions.limit(10).show()
#Juntar dois data sets modelo 1
cases = cases.join(regions, ['province','city'],how='left')
cases.limit(10).show()
#Juntar dois data sets modelo 2 - Melhor esse
regions = regions.withColumnRenamed("province", "Província")
regions = regions.withColumnRenamed("city","Cidade")
#Imprima o Schema final desse DF.
df.printSchema()
#Imprima os 5 primeiros itens do DF.
df.show(5)
#Alterar o nome de uma tabela
cases = df.withColumnRenamed("infection_case","Casos de Infecção")
#Alterar todas as colunas
cases = cases.toDF(*['ID', 'Província', 'Cidade', 'Grupo',
 'Casos de Infecção', 'Confirmados','Latitude', 'Longitude'])
# Join
cases = cases.join(regions, ['Província', 'Cidade'], how='left')
cases.show(40)