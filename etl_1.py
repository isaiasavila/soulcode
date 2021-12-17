#INICIO DE SESS�O
from pyspark.sql.session import SparkSession

from pyspark.sql.types import (BooleanType, IntegerType, StringType, 
                               StructType,StructField, ArrayType,
                               TimestampType,FloatType)

import pyspark.sql.functions as F

spark = SparkSession.builder.appName('meu_etl')\
   .config('spark.master', 'local')\
   .config("spark.executor.memory", "2gb") \
   .config('spark.shuffle.sql.partitions', 2)\
   .getOrCreate() 

schema = StructType([StructField("target", StringType()),
                   StructField("_id", IntegerType()),
                   StructField("date", StringType()),
                   StructField("flag", StringType()),
                   StructField("user", StringType()),
                   StructField("text", StringType()),
                  ]) 
#FIM DE SESS�O

#EXTRACT
path = "c:/scripts/training.1600000.processed.noemoticon.csv"

df = spark.read.format("csv")\
    .schema(schema)\
    .load(path)
#EXTRACT

#TRANSFORM
#Eliminar colunas target e flag.
df = df.drop("target", "flag")

#Pegar apenas partes das linhas de uma coluana.
df = df.withColumn("day_week", df.date.substr(1,3))\
       .withColumn("day", df.date.substr(9,2))\
       .withColumn("month", df.date.substr(5,3))\
       .withColumn("time", df.date.substr(12,8))\
       .withColumn("year", df.date.substr(25,4))\
       .drop("date")


def converterColuna(dataframe, nomes, novoTipo):
    for nome in nomes: 
        dataframe = dataframe.withColumn(nome, dataframe[nome].cast(novoTipo))
    return dataframe 

colunas_inteiro = ['day']

df = converterColuna(df,colunas_inteiro,IntegerType())

#df.printSchema()
#TRANSFORM

#LOAD
df = df.limit(20)
df.show()
df2 = df.limit(10)
# df2.write.format("json").mode("overwrite").save("teste.json")
# df.write.format('json').save('teste.json')#save('meudf')
# df2.write.format("json").saveAsTable("novoteste") 
pandas_df = df.toPandas()
#pandas_df.to_dict('Teste.json')
pandas_df.to_json("Test.json")
# método do professor
#df.write.format('json').save('meuDF2.json')
print("JSON gerado com sucesso!")