# Aula 13 - 10/09/21
# Importação da biblioteca de conexão 
from pymongo import collection
import json
from pyspark.sql.types import IntegralType, TimestampType
import utilidades as ut
from pyspark.sql import SparkSession
# Importação da biblioteca de SQL
import pyspark.sql.functions as F

def parte_um():
    # Objeto principal da classe sendo criado
    spark = SparkSession \
        .builder \
        .appName("reading csv") \
        .getOrCreate()
    # Caminho do arquivo a ser aberto
    arquivo1 = 'c:\scripts\data.csv'
    # 
    df1 = spark.read.csv(arquivo1, header=True, sep=",").cache()
    # 
    df1.show()

    arquivo2 = 'c:\scripts\supermarket_sales.csv'
    df2 = spark.read.csv(arquivo2, header=True, sep=",").cache()
    gender = df2.groupby('Gender').count()
    gender.show()

    df2.registerTempTable('sales')
    print('Tudo')
    output = spark.sql('SELECT * FROM sales')
    print('Duas opções de filtro')
    output = spark.sql('SELECT * FROM sales WHERE `Unit Price` < 15 AND Quantity < 10')
    output.show()
    # Update
    output = output.withColumn('Customer type', F.when(F.col('Customer type') == 'Member', 'Membro').otherwise(F.col('Customer type')))

    output.show()
    # Delete
    print('Oculta coluna...')
    output = output.filter(output['Gender'] != 'Male')
    output.show()

#parte_um()

def parte_dois():
    from pyspark.sql.types import (IntegerType, StringType, DateType, StructType, StructField)

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
    # Extract
    path = 'c:/scripts/training.1600000.processed.noemoticon.csv'
    df = spark.read.format('csv')\
        .schema(schema)\
        .load(path)

    #df.printSchema()
    print('Primeiros 5')
    #df.show(5)
    # Transform
    df = df.drop('target','flag')
    #df.show(5)
    # Pegando apenas partes das linhas de uma coluna )
    df = df.withColumn('day_week',df.date.substr(1,3))\
        .withColumn('day',df.date.substr(9,2).cast(IntegerType()))\
        .withColumn('month',df.date.substr(5,3))\
        .withColumn('time',df.date.substr(12,8))\
        .withColumn('year',df.date.substr(25,4).cast(IntegerType()))\
        .drop('date')

    #df.printSchema()
    #df.show(10)
    # inteiro = ['day']
    # tempo = ['time']
    # ut.converterColunaDF(df,inteiro,IntegerType())
    # ut.converterColunaDF(df,tempo,TimestampType())
    #df.printSchema()
    # Load
    # Busca só 20 linhas
    df = df.limit(20)
    #df.show()
    input('...Criar json...')
    # Esse método não funciona
    #df.write.format("json").mode("overwrite").save("teste.json")
    # Gera um arquivo json, porém dentro de um array
    # Converte o df em df do pandas
    pandas_df = df.toPandas()
    # Gera um arquivo json salvando na raiz
    pandas_df.to_json('arquivo.json', orient='records')
    # Converte para um dicionário
    dictionary = pandas_df.to_dict('records')
    # Cria um arquivo json
    with open("isaias.json", "w") as saida:
        json.dump(dictionary, saida)
     
    # print('Arquivo json criado!')
    # Método para fazer upload no MongoDB
    # dbname = ut.get_database('trabalho2','root','root')
    # colecao = dbname['tabelajson']
    # df = df.toPandas()
    # data_dict = df.to_dict('records')
    # colecao.insert_many(data_dict)
    print('Upload success')

parte_dois()


    


#parte_tres()