def criarStructField(nomeCampo):
    from pyspark.sql.types import (IntegerType, StringType, DateType, StructType, StructField, FloatType)

    # Definição do esquema para o tratamento de dados.
    #esquema = StructType()

    for i in range(len(nomeCampo)):
        esquema = StructType([StructField(nomeCampo[i], StringType())])

    return esquema