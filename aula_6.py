#Aula 6 31/08/21
# from pymongo import MongoClient
# import pymongo
# client = pymongo.MongoClient("mongodb+srv://isaias:isaias@cluster0.h4ljz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.get_database('soulcode')
# records = db.scItems #Coleção
# SCRIPT CRUD MONGO
# •	Crie uma função cadastrar documento, onde seja possível inserir quantos campos forem necessários. Todos os campos devem ser do tipo string. Informe mensagem ao usuário que o documento foi cadastrado.
# •	Crie uma função que exiba todos os documentos da coleção.
# •	Crie uma função que atualize apenas um item por id e que atualize todos os campos sendo esse campo dado pelo usuário.
# •	Crie uma função que delete o documento por id.
# •	Crie uma função que delete todos os documento
# *Não é necessário CRIAR MENU no main, basta apenas chamar as funções.
# *Nas funções, podem ser usados MENUs, caso seja necessário.

# def CadastrarDoc():
#     l1 = []
#     l2 = []
#     while True:
#         c = input('Digite a chave. xxxx-para finalizar: ')
#         if c != 'xxxx':
#             d = input('Digite o dado: ')
#             l1.append(c)
#             l2.append(d)
#         else:
#             item = {}
#             for i in range (len(l1)):
#                 item = {l1[i]:l2[i]}
#             return item
#         print('Cadastrado!')

# def mostrarTodos(_db, _records):
#     _records = _db.scItems
#     detalhes_itens = _records.find() # Busca os dados
#     for item in detalhes_itens: # Imprime os dados
#         print(item)

# def atualizaUm(_records, chaveVelha, dadoVelho, chaveNova, dadoNovo):
#     _records.update_one({chaveVelha:dadoVelho}, {'$set':{chaveNova:dadoNovo}})

# def atualizaUm_v2(_records, chave, dadoVelho, dadoNovo):
#     # Se as chaves forem diferentes, criará uma nova
#     _records.update_one({chave:dadoVelho}, {'$set':{chave:dadoNovo}})

# def deletaUm(_records, chave, dado):
#     _records.delete_one({chave:dado})

# def deletaTodos(_records, chave, dado):
#     _records.delete_many({chave:dado})
    
# def buscarUm(_records, dado):
#     lista(_records.find(dado))
#     #detalhes_itens = 
#     return True

# lista = {
#     'id' : 'av4',
#     'capacidadeVoar' : 'sim',
#     'especie' : 'Corvo',
#     'idade' : 4,
#     'peso' : 3.6
# }
#it = {}
#it = CadastrarDoc()
#records.insert_one(it)
#mostrarTodos(db, records)
#atualizaUm(records, input('Chave velha '), input('Dado velho '), input('Chave nova '), input('Dado novo '))
# mostrarTodos(db, records)
# deletaUm(records, input('Chave: '), input('Dado: '))
# mostrarTodos(db, records)
# records = db.scItems #Coleção
# mostrarTodos(db, records)
# while True:
#     try:
#         deletaTodos(records, input('Chave: '), input('Dado: '))
#         mostrarTodos(db, records)
#         input('Apagado...')
#     except:
#         print('Erro!')
#         break
    
# #Exibir ordenado.
# detalhes_itens = collection_name.find().sort("nome_item", -1)

# #Exibir com parâmetros.
# detalhes_itens = collection_name.find({"categoria" : "Online"})

# #Exibir por valores lógicos
# detalhes_itens = collection_name.find({"$or" : [{"categoria" : "Online"},{"categoria" : "Fisico"}]} )
# detalhes_itens = collection_name.find({"$and" : [{"categoria" : "Fisico"},{"nome_item" : "Camera"}]} )
# #Exibir por partes de string.
# detalhes_itens = collection_name.find({ "nome_item": { "$regex": "^mera" } })

# #Mostrar por valores distintos
# detalhes_itens = collection_name.distinct("desconto_maximo")
# #Exibir por limite.
# detalhes_itens = collection_name.find({"categoria" : "Fisico"}).limit(2)

# #Saltar registros
# detalhes_itens = collection_name.find({},{"nome_item","desconto_maximo"}).skip(2)
#import mysqlclient
from mysql.connector import connect
import MySQLdb

db = MySQLdb.connect(host="185.201.11.44", user="u781216269_rootx", passwd="h5S3J#oP1@", db="u781216269_library")
cursor = db.cursor()
cursor.execute("SELECT * FROM ´tblbooks´")
numrows = int(cursor.rowcount)
linhas = cursor.fetchall()
print(f'Linhas {cursor.rowcount}')
i = 0
for linha in linhas:
    print(f'ID: {linha[0]}')
    print(f'Nome: {linha[1]}')
    print(f'ISBN: {linha[4]}')
    print(f'R$: {linha[5]}')
input('...')

def mySQLToMongo(tabela):
    # Método criado pelo professor
    from mysql.connector import connect
    import MySQLdb

    db = MySQLdb.connect(host="185.201.11.44", user="u781216269_rootx", 
    passwd="h5S3J#oP1@", db="u781216269_library")

    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM `{tabela}`")
    numrows = int(cursor.rowcount)
    linhas = cursor.fetchall()

    print("Número total de registros encontrados: ", cursor.rowcount)
    print("\nMostrando resultados...")

    i=0
    for linha in linhas:
        print("ID: ", linha[0])
        print("Dado_1 : ", linha[1])
        print("Dado_2 : ", linha[2])    
        print("Dado_3 : ", linha[3])

    dbname = get_database()
    for linha in linhas:
        collection_name = dbname["scItems"]  
        item = {
            "id": linha[0], 
            "dado_1": linha[1],
            "dado_2": linha[2],
            "dado_3": linha[3]
        }
        collection_name.insert_one(item)
        print("Documento vindo do MySQL inserido em Mongo!")   