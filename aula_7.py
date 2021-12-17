# Aula 7 01/09/21
import os
#mongodb+srv://<username>:<password>@cluster0.h4ljz.mongodb.net/test
def get_database(nomeDB, usuario, senha):
    from pymongo import MongoClient
    import pymongo
    # Forneça o url do atlas mongodb para conectar python a mongodb usando pymongo
    CONNECTION_STRING = f"mongodb+srv://{usuario}:{senha}@cluster0.h4ljz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    # Crie uma conexão usando MongoClient. Você pode importar MongoClient ou usar pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    # Cria o banco de dados.
    return client[nomeDB]

def mostrarDocumentos(tabela):#, query):
    dbname = get_database('soulcode','isaias','isaias')
    collection_name = dbname[tabela]
    detalhes_itens = collection_name.find()#{"pageCount" : 0})
    # Quantos livros possuem número de páginas 0?
    #print(detalhes_itens.collection.count_documents({'pageCount' : 0}))
    # Quantos livros foram publicados?
    #print(detalhes_itens.collection.count_documents({}))
    # Qual o título do livro, cujo ISBN é 1933988924?
    #detalhes_itens = collection_name.find_one({'isbn':'1933988924'})
    #print(detalhes_itens['title'])
    # Qual a descrição do livro Machine Learning in Action?
    #detalhes_itens = collection_name.find_one({'title':'Machine Learning in Action'})
    #print(detalhes_itens['shortDescription'])
    # O Livro ArcGIS Web Development foi publicado?
    #detalhes_itens = collection_name.find_one({'title':'ArcGIS Web Development'})
    #print(detalhes_itens['_id'])
    # Qual a descrição do livro Secrets of the JavaScript Ninja pBook upgrade?
    #detalhes_itens = collection_name.find_one({'title':'Secrets of the JavaScript Ninja pBook upgrade'})
    #print(detalhes_itens['shortDescription'])
    # Quantas páginas possui o livro Jess in Action?
    #detalhes_itens = collection_name.find_one({'title':'Jess in Action'})
    #print(detalhes_itens['pageCount'])
    # Quais são os primeiros três livros da coleção?
    #print('----------------------------------')
    # detalhes_itens = collection_name.find().limit(3)
    # for item in detalhes_itens:
    #     print(item)
    # Qual o ID do livro, cujo ISBN é 1930110987? Ele é declarado ou setado pelo MongoDB?
    # detalhes_itens = collection_name.find({'isbn':'1930110987'})
    # if detalhes_itens.collection.count_documents({}) > 0:
    #     print(detalhes_itens[0])
    # else:
    #     print('O Livro não está cadastrado!')
    print('...')
    ###2) Qual é o número de paginas de cada livro cujo titulo começa com a letra U ?
    detalhes_itens = collection_name.find({"title": {"$regex": "^U"}})
    for item in detalhes_itens:
        print(item['pageCount'])
    # Exercícios
    # 1
    # print('Quais são os livros que foram escritos por Jon Skeet?')
    # detalhes_itens = collection_name.find({'authors':'Jon Skeet'}).sort('title', 1)
    # for item in detalhes_itens:
    #     print(item['title'])
    #     print('...')
    # 2
    # print('Quais são os livros abordam o assunto Software?')
    # detalhes_itens = collection_name.find({ "categories": { "$regex": "^Software" } }).sort('title', 1)
    # for item in detalhes_itens:
    #     print(item['title'])
    # print('')
    # 3
    # print('Digite todas as quantidades de páginas de toda a base de dados?\n')
    # detalhes_itens = collection_name.distinct("pageCount")
    # print(detalhes_itens)
    # 4
    # print('Qual o nome do livro com o ISBN 1933988797?')
    # detalhes_itens  = collection_name.find_one({'isbn': '1933988797'})
    # print(detalhes_itens['title'])
    # print('...')
    # 5
    # print('Quais livros têm 200 páginas?')
    # detalhes_itens = collection_name.find({'pageCount':200})
    # for item in detalhes_itens:
    #     print(item['title'])
    # detalhes_itens = collection_name.find().limit(-5)
    # for item in detalhes_itens:
    #     print(item['title'])
try:
    mostrarDocumentos('teste')
    print('...Finalizado!...')
except:
    print('Erro fatal!\n')

# #Exibir ordenado.
#    detalhes_itens = collection_name.find().sort("nome_item", -1)

#    #Exibir com parâmetros.
#    detalhes_itens = collection_name.find({"categoria" : "Online"})

#    #Exibir por valores lógicos
#    detalhes_itens = collection_name.find({"$or" : [{"categoria" : "Online"},{"categoria" : "Fisico"}]} )
#    detalhes_itens = collection_name.find({"$and" : [{"categoria" : "Fisico"},{"nome_item" : "Camera"}]} )

#    #Exibir por partes de string.
#    detalhes_itens = collection_name.find({ "nome_item": { "$regex": "^mera" } })

#    #Mostrar por valores distintos
#    detalhes_itens = collection_name.distinct("desconto_maximo")

#    #Exibir por limite.
#    detalhes_itens = collection_name.find({"categoria" : "Fisico"}).limit(2)

#    #Saltar registros
#    detalhes_itens = collection_name.find({},{"nome_item","desconto_maximo"}).skip(2)