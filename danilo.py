def get_database():
    from pymongo import MongoClient
    import pymongo
    #URL de conexão
    CONNECTION_STRING = "mongodb+srv://danilo:dan3top3@cluster0.smdnd.mongodb.net/myFirstDatabase"
    client = MongoClient(CONNECTION_STRING)#Conexão com o cliente
    return client['SoulCode']#Base de dados

#def mostrarDocumentos():
dbname = get_database()
collection_name = dbname["books"]

#Quantos livros possuem número de páginas 0?
# detalhes_itens  = collection_name.count_documents({'pageCount': 0})
#166
# print(detalhes_itens)
#Maneira Professor
# detalhes_itens = collection_name.find({"pageCount":0})
# i=0
# for item in detalhes_itens:
#     i+=1
# print(i)


#Quantos livros foram publicados?
# detalhes_itens  = collection_name.distinct('status')
# print(detalhes_itens)

#detalhes_itens  = collection_name.count_documents({'status': 'PUBLISH'})
#363
#detalhes_itens  = collection_name.count_documents({'status': 'MEAP'})
#print(detalhes_itens)

#Qual o título do livro, cujo ISBN é 1933988924? 
# detalhes_itens  = collection_name.find_one({'isbn': '1933988924'}, {'title': 1, '_id': 0})
# print(detalhes_itens)

#Outros jeitos
# detalhes_itens = collection_name.find_one({'isbn': '1933988924'})
# print(detalhes_itens['title'])

# detalhes_itens = collection_name.find_one({'isbn': '1933988924'})
# print(detalhes_itens['title'])


#Qual a descrição do livro Machine Learning in Action?
#detalhes_itens  = collection_name.find_one({'title': 'Machine Learning in Action'})
# detalhes_itens  = collection_name.find_one({'title': 'Machine Learning in Action'}, {'shortDescription': 1, '_id': 0})
# print(detalhes_itens)

#O Livro ArcGIS Web Development foi publicado?
#detalhes_itens  = collection_name.find_one({'title': 'ArcGIS Web Development'})
# detalhes_itens  = collection_name.find_one({'title': 'ArcGIS Web Development'}, {'status': 1, '_id': 0})
# print(detalhes_itens)
# if {'status': 'PUBLISH'} == True:
#     print('O livro ArcGIS Web Development foi publicado.')
# else:
#     print('O livro ArcGIS Web Development não foi publicado.')

#Qual a descrição do livro Secrets of the JavaScript Ninja pBook upgrade?
#detalhes_itens  = collection_name.find_one({'title': 'Secrets of the JavaScript Ninja pBook upgrade'})
# detalhes_itens  = collection_name.find_one({'title': 'Secrets of the JavaScript Ninja pBook upgrade'}, {'shortDescription': 1, '_id': 0})
# print(detalhes_itens)
#Maneira do Raffa
# doc = collection_name.find_one({'title': 'Secrets of the JavaScript Ninja pBook upgrade'})
# try:
#     print(doc['shortDescription'])
# except KeyError:
#     print('Chave não encontrada!')
# if {'shortDescription': 0} != True:
#     print('O livro Secrets of the JavaScript Ninja pBook upgrade não possui descrição.')
# else:
#     print('O livro ArcGIS Web Development não foi publicado.')
#Falta melhorar a maneira de informar, já que não existe o campo descrição.
# detalhes_itens  = collection_name.find({'title': 'Secrets of the JavaScript Ninja pBook upgrade'})
# for item in detalhes_itens:
#     print(item['shortDescription'])



#Quantas páginas possui o livro Jess in Action?
#detalhes_itens  = collection_name.find_one({'title': 'Jess in Action'})
# detalhes_itens  = collection_name.find_one({'title': 'Jess in Action'}, {'pageCount': 1, '_id': 0})
# 480
# print(detalhes_itens)
# detalhes_itens  = collection_name.find({'title': 'Jess in Action'})
# for item in detalhes_itens:
#     print(item['pageCount'])


#Quais são os primeiros três livros da coleção?
# detalhes_itens  = collection_name.find().limit(3)
# for item in detalhes_itens:
#     print(item['title'])


#Qual o ID do livro, cujo ISBN é 1930110987? Ele é declarado ou setado pelo 
# MongoDB?
# detalhes_itens  = collection_name.find_one({'isbn': '1930110987'}, {'_id': 1})
# print(detalhes_itens)
# detalhes_itens  = collection_name.find({'isbn': "1930110987"})
# for item in detalhes_itens:
#     print(item['_id'])

#Maneira da Heloísa
# detalhes_itens = collection_name.find({"isbn" : "1930110987"})
# for item in detalhes_itens:
#     print(f"\n{item['_id']}")
# if type(item['_id']) is int:
#     print('É declarado')
# else:
#     print('É setado pelo MongoDB\n')


#mostrarDocumentos()