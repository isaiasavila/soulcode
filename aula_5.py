from pymongo import MongoClient
import pymongo
client = pymongo.MongoClient("mongodb+srv://isaias:isaias@cluster0.h4ljz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('soulcode')
records = db.scItems #Coleção
# Aves
itens = [
{
    'id' : 'av1',
    'capacidadeVoar' : 'não',
    'especie' : 'Avestruz',
    'idade' : 12,
    'peso' : 90.1
},
{
    'id' : 'av2',
    'capacidadeVoar' : 'não',
    'especie' : 'Pinguim',
    'idade' : 2,
    'peso' : 4.1
},
{
    'id' : 'av3',
    'capacidadeVoar' : 'sim',
    'especie' : 'Urubu',
    'idade' : 7,
    'peso' : 11.2
},
{
    'id' : 'av4',
    'capacidadeVoar' : 'sim',
    'especie' : 'Corvo',
    'idade' : 4,
    'peso' : 3.6
},
{
    'id' : 'av5',
    'capacidadeVoar' : 'sim',
    'especie' : 'Chupim',
    'idade' : 3,
    'peso' : 2.2
},
{
    'id' : 'av6',
    'capacidadeVoar' : 'sim',
    'especie' : 'Calopsita',
    'idade' : 4,
    'peso' : 3.5
},
{
    'id' : 'av7',
    'capacidadeVoar' : 'sim',
    'especie' : 'Papagaio',
    'idade' : 3,
    'peso' : 4.2
},
{
    'id' : 'av8',
    'capacidadeVoar' : 'sim',
    'especie' : 'Periquito',
    'idade' : 3,
    'peso' : 3.2
},
{
    'id' : 'av9',
    'capacidadeVoar' : 'sim',
    'especie' : 'Saracura',
    'idade' : 10,
    'peso' : 4.0
},
{
    'id' : 'av10',
    'capacidadeVoar' : 'sim',
    'especie' : 'Quero-Quero',
    'idade' : 4,
    'peso' : 3.2
},
{
    'id' : 'av11',
    'capacidadeVoar' : 'sim',
    'especie' : 'Flamingo',
    'idade' : 5,
    'peso' : 6.2
},
{
    'id' : 'av12',
    'capacidadeVoar' : 'sim',
    'especie' : 'Marreco',
    'idade' : 3,
    'peso' : 3.9
},
{
    'id' : 'av13',
    'capacidadeVoar' : 'sim',
    'especie' : 'Pato',
    'idade' : 3,
    'peso' : 4.2
},
{
    'id' : 'av14',
    'capacidadeVoar' : 'sim',
    'especie' : 'Pavão',
    'idade' : 3,
    'peso' : 9.2
},
{
    'id' : 'av15',
    'capacidadeVoar' : 'sim',
    'especie' : 'Pelicano',
    'idade' : 3,
    'peso' : 10.2
},
{
    'id' : 'av16',
    'capacidadeVoar' : 'sim',
    'especie' : 'Canário',
    'idade' : 2,
    'peso' : 3.0
},
{
    'id' : 'av17',
    'capacidadeVoar' : 'sim',
    'especie' : 'Andorinha',
    'idade' : 3,
    'peso' : 2.2
},
{
    'id' : 'av18',
    'capacidadeVoar' : 'sim',
    'especie' : 'Pardal',
    'idade' : 6,
    'peso' : 4.2
},
{
    'id' : 'av19',
    'capacidadeVoar' : 'sim',
    'especie' : 'Falcão',
    'idade' : 5,
    'peso' : 6.2
},
{
    'id' : 'av20',
    'capacidadeVoar' : 'sim',
    'especie' : 'Águia',
    'idade' : 3,
    'peso' : 7.2
},
#Peixes
{
    'id' : 'pe21',
    'ViveCardume' : 'sim',
    'especie' : 'Peixe Rei',
    'habitat' : 'Água salgada',
    'peso' : 3.2
},
{
    'id' : 'pe22',
    'ViveCardume' : 'sim',
    'especie' : 'Peixe Sapo',
    'habitat' : 'Água salgada',
    'peso' : 4.2
},
{
    'id' : 'pe23',
    'ViveCardume' : 'sim',
    'especie' : 'Papa Terra',
    'habitat' : 'Água salgada',
    'peso' : 7.2
},
{
    'id' : 'pe24',
    'ViveCardume' : 'não',
    'especie' : 'Tubarão',
    'habitat' : 'Água salgada',
    'peso' : 7.2
},
{
    'id' : 'pe25',
    'ViveCardume' : 'sim',
    'especie' : 'Arraia',
    'habitat' : 'Água salgada',
    'peso' : 7.2
},
{
    'id' : 'pe26',
    'ViveCardume' : 'sim',
    'especie' : 'Cascudo',
    'habitat' : 'Água doce',
    'peso' : 3.2
},
{
    'id' : 'pe27',
    'ViveCardume' : 'sim',
    'especie' : 'Lambari',
    'habitat' : 'Água doce',
    'peso' : 1.2
},
{
    'id' : 'pe28',
    'ViveCardume' : 'sim',
    'especie' : 'Piranha',
    'habitat' : 'Água doce',
    'peso' : 4.2
},
{
    'id' : 'pe29',
    'ViveCardume' : 'sim',
    'especie' : 'Viola',
    'habitat' : 'Água salgada',
    'peso' : 7.2
},
{
    'id' : 'pe30',
    'ViveCardume' : 'sim',
    'especie' : 'Acará',
    'habitat' : 'Água doce',
    'peso' : 4.2
},
{
    'id' : 'pe31',
    'ViveCardume' : 'não',
    'especie' : 'Mussum',
    'habitat' : 'Água doce',
    'peso' : 7.2
},
{
    'id' : 'pe32',
    'ViveCardume' : 'sim',
    'especie' : 'Peixe Palhaço',
    'habitat' : 'Água salgada',
    'peso' : 1.2
},
{
    'id' : 'pe33',
    'ViveCardume' : 'sim',
    'especie' : 'Peixe Tubarão',
    'habitat' : 'Água salgada',
    'peso' : 7.2
},
{
    'id' : 'pe34',
    'ViveCardume' : 'sim',
    'especie' : 'Carpa',
    'habitat' : 'Água doce',
    'peso' : 2.2
},
{
    'id' : 'pe35',
    'ViveCardume' : 'sim',
    'especie' : 'Salmão',
    'habitat' : 'Água salgada',
    'peso' : 7.2
},
#Anfíbios
{
    'id' : 'pe36',
    'EmExtincao' : 'sim',
    'especie' : 'Sapo Rosa',
    'endemico' : 'sim',
    'peso' : 4.2
},
{
    'id' : 'pe37',
    'EmExtincao' : 'sim',
    'especie' : 'Sapo Preto',
    'endemico' : 'não',
    'peso' : 4.1
},
{
    'id' : 'pe38',
    'EmExtincao' : 'sim',
    'especie' : 'Sapo Touro',
    'endemico' : 'sim',
    'peso' : 3.9
},
{
    'id' : 'pe39',
    'EmExtincao' : 'sim',
    'especie' : 'Sapo Tatu',
    'endemico' : 'sim',
    'peso' : 4.2
},
{
    'id' : 'pe40',
    'EmExtincao' : 'sim',
    'especie' : 'Sapo Xiru',
    'endemico' : 'sim',
    'peso' : 4.1
},
{
    'id' : 'pe41',
    'EmExtincao' : 'sim',
    'especie' : 'Sapo Mamão',
    'endemico' : 'não',
    'peso' : 4.0
},
{
    'id' : 'pe42',
    'EmExtincao' : 'sim',
    'especie' : 'Perereca',
    'endemico' : 'sim',
    'peso' : 2.9
},
{
    'id' : 'pe43',
    'EmExtincao' : 'sim',
    'especie' : 'Rã',
    'endemico' : 'não',
    'peso' : 2.7
},
{
    'id' : 'pe44',
    'EmExtincao' : 'sim',
    'especie' : 'Sapo Cachorro',
    'endemico' : 'sim',
    'peso' : 2.2
},
{
    'id' : 'pe45',
    'EmExtincao' : 'sim',
    'especie' : 'Sapo Quindinho',
    'endemico' : 'não',
    'peso' : 4.2
},
{
    'id' : 'pe46',
    'EmExtincao' : 'sim',
    'especie' : 'Sapo Verde',
    'endemico' : 'sim',
    'peso' : 4.0
},
{
    'id' : 'pe47',
    'EmExtincao' : 'sim',
    'especie' : 'Sapo Girino',
    'endemico' : 'sim',
    'peso' : 4.2
},
{
    'id' : 'pe48',
    'EmExtincao' : 'sim',
    'especie' : 'Sapo Jirayia',
    'endemico' : 'não',
    'peso' : 4.2
},
{
    'id' : 'pe49',
    'EmExtincao' : 'não',
    'especie' : 'Sapo Anão',
    'endemico' : 'não',
    'peso' : 3.9
},
{
    'id' : 'pe50',
    'EmExtincao' : 'sim',
    'especie' : 'Sapo Cururu',
    'endemico' : 'não',
    'peso' : 3.8
},
#Mamíferos
{
    'id' : 'pe51',
    'origem' : 'Ex sito',
    'especie' : 'Cachorro',
    'idade' : 2,
    'peso' : 8.8
},
{
    'id' : 'pe52',
    'origem' : 'In sito',
    'especie' : 'Camelo',
    'idade' : 9,
    'peso' : 38.8
},
{
    'id' : 'pe53',
    'origem' : 'In sito',
    'especie' : 'Onça',
    'idade' : 2,
    'peso' : 32.8
},
{
    'id' : 'pe54',
    'origem' : 'Ex sito',
    'especie' : 'Tigre',
    'idade' : 3,
    'peso' : 32.6
},
{
    'id' : 'pe55',
    'origem' : 'In sito',
    'especie' : 'Jaguar',
    'idade' : 21,
    'peso' : 33.8
},
{
    'id' : 'pe56',
    'origem' : 'Ex sito',
    'especie' : 'Puma',
    'idade' : 22,
    'peso' : 31.8
},
{
    'id' : 'pe57',
    'origem' : 'In sito',
    'especie' : 'Lobo Guará',
    'idade' : 2,
    'peso' : 29.8
},
{
    'id' : 'pe58',
    'origem' : 'Ex sito',
    'especie' : 'Hiena',
    'idade' : 25,
    'peso' : 25.8
},
{
    'id' : 'pe59',
    'origem' : 'Ex sito',
    'especie' : 'Zebra',
    'idade' : 12,
    'peso' : 26.8
},
{
    'id' : 'pe60',
    'origem' : 'In sito',
    'especie' : 'Lontra',
    'idade' : 2,
    'peso' : 15.8
}
]
#records.insert_many(itens)
detalhes_itens = records.find() # Busca os dados
for item in detalhes_itens:
    print(item['id'], item['especie']) # Imprimi somente o que se deseja

records.update_one({'idade':12}, {'$set':{'idade':3}})
chave = "desconto_maximo"
valor = "11%"
records.delete_many({chave : valor})
#collection_name.update_many({"desconto_maximo":"35%"}, {"$set":{"desconto_maximo":"11%"}})
#collection_name.delete_one({"_id":"SC001"}) # Ou use many para vários