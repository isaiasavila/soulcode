from g3spark import SparkG3
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType

from pyspark.sql.functions import *

spark = SparkG3().iniciar_sessao()

rawDF = spark.read.json("c:/scripts/sample.json", multiLine = "true")
rawDF.printSchema()
# renomeando
sampleDF = rawDF.withColumnRenamed("id", "key")
# índice campo
batDF = sampleDF.select("key", "batters.batter")
batDF.printSchema()
# mostrar
batDF.show(1, False)
bat2DF = batDF.select("key", explode("batter").alias("new_batter"))
bat2DF.show()

# schema = StructType(
#     [
#         StructField('key1', StringType(), True),
#         StructField('key2', StringType(), True)
#     ]
# )
# conexao = SparkG3()
# path = "C:/scripts/paralympics_tokyo.json"


# data1 = conexao.read.parquet(path)
# json_schema = conexao.read.json(data1.rdd.map(lambda row: row.json_col)).schema
# data2 = data1.withColumn("event", from_json("json_col", json_schema))

# col1 = data2.columns
# col1.remove("event")
# col2 = data2.select("data.*").columns
# append_str ="data."
# col3 = [append_str + val for val in col2]
# col_list = col1 + col3
# data3 = data2.select(*col_list).drop("json_col")

# df.withColumn("data", from_json("data", schema))\
#     .select(col('id'), col('point'), col('data.*'))\
#     .show()

# import json

# texto = """
# {
#     "nome": "Fulano",
#     "idade": 90,
#     "filmes_preferidos": [ "Pulp Fiction", "Clube da Luta" ],
#     "contatos": {
#         "telefone": "(11) 91111-2222",
#         "emails": [ "fulano@gmail.com", "fulano@yahoo.com" ]
#     }
# }
# """

# obj = json.loads(texto)
# # obter o nome
# print('...',obj['nome'])
# # percorrer o array de filmes
# for filme in obj['filmes_preferidos']:
#     print(filme)
#     print('....................................')
# # percorrer as chaves e valores do objeto "contatos"
# for tipo, contato in obj['contatos'].items():
#     print('lululululu')
#     print('{}={}'.format(tipo, contato))

# # incluir um novo contato
# obj['contatos']['twitter'] = '@fulano'
# # imprimir o json (indentando com 2 espaços)
# print('nininini')
# print(json.dumps(obj, indent=2))
# import json
 
# # Creating a dictionary
# Dictionary ={1:'Welcome', 2:'to',
#             3:'Geeks', 4:'for',
#             5:'Geeks'}
  
# # Converts input dictionary into
# # string and stores it in json_string
# json_string = json.dumps(Dictionary)
# print('Equivalent json string of input dictionary:', json_string)
# print("   ")
# print(':::')
# json_string = json_string.split(':')
# #json_string = json_string.split(',')
# print(json_string)

# # print (lista)
# print ('|||')
# # Checking type of object
# # returned by json.dumps
# print(type(json_string))

# list_data = [1,2,3,4.....,50]

# df \
# .select(collect_list(struct(F.col("*"))).alias("data")) \
# .withColumn("list",F.array([F.lit(i) for i in list_data])) \
# .select(F.explode(F.arrays_zip(F.col("data"),F.col("list"))).alias("full_data")) \ 
# .select(F.col("full_data.data.*"),F.col("full_data.list").alias("col3")) \ 
# .show()

# from pyspark.sql.functions import from_json, col
# from pyspark.sql.types import StructType, StructField, StringType

# schema = StructType(
#     [
#         StructField('key1', StringType(), True),
#         StructField('key2', StringType(), True)
#     ]
# )

# df.withColumn("data", from_json("data", schema))\
#     .select(col('id'), col('point'), col('data.*'))\
#     .show()