# Exercício 09/09/21
# Classe usada para conexão
import utilidades as ut
# Importando os tipos necessários
from pyspark.sql.types import (IntegerType, StringType, DateType, StructType, StructField)

# Definição do esquema para o tratamento de dados.
esquema = StructType([StructField("sofifa_id", IntegerType()),
                   StructField("short_name", StringType()),
                   StructField("age", IntegerType()),
                   StructField("dob",DateType()),
                   StructField("height_cm", IntegerType()),
                   StructField("weight_kg", IntegerType()),
                   StructField("nationality", StringType()),
                   StructField("club", StringType()),
                   StructField("overall", IntegerType()),
                   StructField("potential", IntegerType()),
                   StructField("player_positions", StringType()),
                   StructField("preferred_foot", StringType()),
                   StructField("international_reputation", StringType()),
                   StructField("weak_foot", StringType()),
                   StructField("skill_moves", StringType()),
                   StructField("work_rate", StringType()),
                   StructField("body_type", StringType()),
                   StructField("player_tags", StringType()),
                   StructField("team_position", StringType()),
                   StructField("joined", StringType()),
                   StructField("contract_valid_until", StringType()),
                   StructField("nation_position", StringType()),
                   StructField("nation_jersey_number", StringType()),
                   StructField("pace", IntegerType()),
                   StructField("shooting", IntegerType()),
                   StructField("passing", IntegerType()),
                   StructField("dribbling", IntegerType()),
                   StructField("defending", IntegerType()),
                   StructField("physic", IntegerType())
                  ])
# Informando o caminho do arquivo que será aberto
caminho = "c:/scripts/players_15_alt.csv"
# Chamo o método para criar uma sessão spark
spark = ut.conectarSpark('Ex2','local','1gb',1)
# Informações para o dataFrame
df = spark.read.load(caminho,format="csv",sep=",", inferSchema="true",header="true")

print('Iniciando...\nParte1')
#df.printSchema()
# Impressão dos 50 primeiros jogadores da base
#df.show(50)
# Definição das colunas que sofrerão alteração
lista = ['joined', 'nation_jersey_number']
# Alteração dos campos joined e nation_jersey_number para o tipo inteiro
df = ut.converterColunaDF(df, lista, IntegerType())
#df.printSchema()
# Exibição dos jogadores com overall maior que 90
df.select('short_name','nationality','age').filter(df['overall']>90).show()
df = df.select('short_name','nationality','age','skill_moves')
df.show(10)
# print('Parte2')
# # Informando o caminho do novo arquivo que será aberto
# caminho = "c:/scripts/teams_and_leagues.csv"
# # Informações para o dataFrame
# df = spark.read.load(caminho,format="csv",sep=",", inferSchema="true",header="true")
# # Impressão das 50 primeiras ligas da base
# #df.show(50)
# # Inicia um novo DataFrame para fazer o join
# print('Parte extra!')
# dfextra = spark.read.load('c:/scripts/players_15_alt.csv',format="csv", sep=",", inferSchema="true", header="true")
# # Seleciona três campos para juntar no novo dataFrame
# dfextra = dfextra.select('short_name','nationality','age')
# ##dfextra.show(50)
# # Seleciona dois campos para juntar no novo dataFrame
# cases = df.select('url', 'league_name')
# #cases.show()
# print('..........JOIN...........')
# cases = cases.join(dfextra)#, ['short_name','age'], how='right')
# cases.show(500)

input('ok')