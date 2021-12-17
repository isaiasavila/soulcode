def conectarSpark():
    import findspark

    findspark.init()

    from pyspark.sql import SparkSession

    spark = SparkSession.builder \
        .master('local') \
        .appName('Aula1') \
        .config('spark.executor.memory','1gb') \
        .getOrCreate()

    return spark.sparkContext

sc = conectarSpark()

rdd = sc.textFile('C:\python\Salary_Data.csv')

rdd = rdd.map(lambda line: line.split(','))
#print(rdd.take(5)) # Mostra os cinco primeiros registros
#print(rdd.first()) # Mostra o primeiro registro

from pyspark.sql import Row
from pyspark.sql.types import *

df = rdd.map(lambda line: Row(AnosExperiencia=line[0],Salario=line[1])).toDF()
#df.show()
#df.printSchema()
def converterColuna(dataFrame, nomes, novoTipo):
    for nome in nomes:
        dataFrame = dataFrame.withColumn(nome,dataFrame[nome].cast(novoTipo))
    return dataFrame

colunas = ['AnosExperiencia','salario']
df = converterColuna(df,colunas,FloatType())
# df.show()
# df.printSchema()
# df.select('salario').show(5)
# df.groupby('salario').count().sort('salario',ascending=False).show()
# df.groupby('salario').count().show()
# df.describe().show()
# df.describe('salario').show()
# df.collect()
df.filter(df['salario']>50000).show()
df.select('salario').filter(df['salario']<50000).show()