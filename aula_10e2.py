# Aula 10 - exercício 2
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
   .config('spark.master', 'local')\
   .config("spark.executor.memory", "1gb") \
   .config('spark.shuffle.sql.partitions', 1)\
   .getOrCreate()   

#============================================================
# df = spark.read.load("E:/python/covid_cases_no_header.csv", format="csv",\
#                     sep=",", inferSchema="true", header="true")

#============================================================
#--------------------------EXTRAIR-----------------------------
#Definir esquema de tratamento dos dados.
esquema = StructType([StructField("case_id", IntegerType()),
                   StructField("province", StringType()),
                   StructField("city", StringType()),
                   StructField("group", BooleanType()),
                   StructField("infection_case", StringType()),
                   StructField("confirmed",IntegerType()),
                   StructField("latitude", StringType()),
                   StructField("longitude", StringType()),
                  ])

caminho = "c:/python/covid_cases_no_header.csv"

# df = spark.read.format('csv').schema(esquema).load(caminho)
# #df.show(5)
# novodf = df.withColumn('NewConfirm',100 + F.col('confirmed'))
# novodf.show(5)
# novodf2 = df.withColumn('ExpConfirm', F.exp('confirmed'))
# novodf2.show(5)

