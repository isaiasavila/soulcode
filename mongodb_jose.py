# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:34:34 2021

@author: isavi
"""

def get_database():
    from pymongo import MongoClient
    import pymongo

    # Forneça o url do atlas mongodb para conectar python a mongodb usando pymongo
    CONNECTION_STRING = "mongodb+srv://root:root@cluster0.qqxjf.mongodb.net/mytestdb"

    # Crie uma conexão usando MongoClient. Você pode importar MongoClient ou usar pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Cria o banco de dados.
    
    return client['soul_code_database']
    
# Função principal
if __name__ == "__main__":    
    
    # Obtém o banco de dados
   dbname = get_database()
    #Criamos a coleção
   collection_name = dbname["soulcode_itens"]

    #NOVAS QUERIES

   #Exibir ordenado.
   detalhes_itens = collection_name.find().sort("nome_item", -1)

   #Exibir com parâmetros.
   detalhes_itens = collection_name.find({"categoria" : "Online"})

   #Exibir por valores lógicos
   detalhes_itens = collection_name.find({"$or" : [{"categoria" : "Online"},{"categoria" : "Fisico"}]} )
   detalhes_itens = collection_name.find({"$and" : [{"categoria" : "Fisico"},{"nome_item" : "Camera"}]} )

   #Exibir por partes de string.
   detalhes_itens = collection_name.find({ "nome_item": { "$regex": "^mera" } })

   #Mostrar por valores distintos
   detalhes_itens = collection_name.distinct("desconto_maximo")

   #Exibir por limite.
   detalhes_itens = collection_name.find({"categoria" : "Fisico"}).limit(2)

   #Saltar registros
   detalhes_itens = collection_name.find({},{"nome_item","desconto_maximo"}).skip(2)
