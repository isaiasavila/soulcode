# 26/08/21 Arthur, Isaias, Leonardo, Ricardo
#Sistema de ZooZoul
from abc import ABC, abstractmethod
import os

class Utilidades(): #Classe abstrata - métodos para todo o sistema
    @abstractmethod
    def imprimirObjeto(self, objeto):
        print(vars(objeto))
        input('<enter>')
    @abstractmethod
    def erro(self):
        print('Erro fatal!')
    @abstractmethod
    def Efeitos(self, vInicial, vFinal, texto):
        i = 0
        while vFinal > vInicial:
            if i == 0:
                msg = '≤≤≤≤≤≤'
            elif i == 1:
                msg = '≡≡≡≡≡≡'
            else:
                msg = '≥≥≥≥≥≥'
                i = -1
            i += 1
            os.system('cls')
            print(f'{texto} o sistema. Por favor aguarde! ', msg)
            vInicial += 1

class Animais(Utilidades): #Classe nível mais alto do sistema, núcleo da primeira parte
    def __init__(self, id = '', idade = '', peso = '', genero = '', habitat = ''):
        self.__id = id
        self.__idade = idade
        self.__peso = peso
        self.__genero = genero
        self.__habitat = habitat
        self.__fome = True

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_idade(self):
        return self.__idade
    
    def set_idade(self, idade):
        self.__idade = idade

    def get_peso(self):
        return self.__peso
    
    def set_peso(self, peso):
        self.__peso = peso

    def get_genero(self):
        return self.__genero
    
    def set_genero(self, genero):
        self.__genero = genero

    def get_habitat(self):
        return self.__habitat
    
    def set_habitat(self, habitat):
        self.__habitat = habitat

    def get_fome(self):
        return self.__fome

    def set_fome(self):
        if self.__fome == False:
            self.__fome = True
        else:
            print('Animal já está com fome!')

    def inputAnimal(self, id):
        l = []#id, idade, peso, genero, habitat
        t = ('ID;Idade;Peso;Gênero;Habitat'.split(';'))

        for i in range (len(t)):
            if i == 0:
                l.append(id)
            else:
                l.append(input(f'Qual {t[i]}: '))
        #print(l)
        texto = (f'{l[0]};{l[1]};{l[2]};{l[3]};{l[4]}')
        return texto
        
        #m = Mamiferos(o[1],o[2],o[3],o[4],o[5],o[6],o[7],o[8],o[9])
        #__baseDados = {l[0]: m.get_id(), l[1]: m.get_idade()}

class Mamiferos(Animais, Utilidades):

    def __init__(self, id = '', idade = '', peso = '', genero = '', habitat = '', especie = '', nome = '', dataDeEntrada = '', origem = ''):
        super().__init__(id, idade, peso, genero, habitat)
        self.especie = especie
        self.nome = nome
        self.dataDeEntrada = dataDeEntrada
        self.origem = origem #Opções: In sito ou Ex sito
        self.__vacinado = False

    def get_nome(self):
        return self.nome
    
    def get_dataDeEntrada(self):
        return self.dataDeEntrada

    def get_origem(self):
        return self.origem

    def set_obs(self, obs):
        self.obs = obs

    def vacinar(self):
        if self.__vacinado == False:
            print('Animal vacinado!')
            self.__vacinado = True
        else:
            print('Animal já vacinado!')

    def precisaVacina(self):
        if self.__vacinado == True:
            print('Animal precisa de vacina!')
        else:
            print('Animal não foi vacinado ainda!')

    def inputAnimal(self, id): #Polimorfismo
        texto = super().inputAnimal(id)
        l = []#especie, nome, dataDeEntrada, origem
        t = ('Espécie;Nome;Data de Entrada;Origem'.split(';'))

        for i in range (len(t)):
            l.append(input(f'Qual {t[i]}: '))
        texto += (f';{l[0]};{l[1]};{l[2]};{l[3]}')
        return texto

class Aves(Animais, Utilidades):
  def __init__ (self, id = '', idade = '', peso = '', genero = '', habitat = '', capacidadeVoar = '', vacinado = ''):
    super(). __init__ (id, idade, peso, genero, habitat)
    self.capacidadeVoar = capacidadeVoar
    self.vacinado = vacinado
  
  def vacinar (self, vacinado):
    if self.vacinado  == True:  
      print("A ave já foi vacinada!!")
    else:
      print("A ave precisa ser vacinada")

  def inputAnimal(self, id):
        texto = super().inputAnimal(id)
        l = []#capacidadeVoar, vacinado
        t = ('Pode Voar?;Está Vacinado?'.split(';'))

        for i in range (len(t)):
            l.append(input(f'{t[i]}: '))
        texto += (f';{l[0]};{l[1]}')
        return texto

class Repteis(Animais, Utilidades):
  def __init__ (self, id = '', idade = '', peso = '', genero = '', habitat = '', controlTemp = '', porta = ''):
    super().__init__ (idade, peso, genero, habitat)
    self.controlTemp = controlTemp
    self.porta = porta

  def controlarTemperatura (self, controlTemp):
    if controlTemp != 28:
        print("Checar o recinto de cobras, temperatura anormal.\n")
  
  def verificarPorta (self, porta):
    if porta == True:
      print("Verificar porta possível reptil perigoso a solta!")
    else:
      print("Porta ok!")

  def inputAnimal(self, id):
        texto = super().inputAnimal(id)
        l = []#controlTemp, porta
        t = ('Qual é a temperatura de controle?'.split(';'))

        for i in range (len(t)):
            l.append(input(f'{t[i]}: '))
        texto += (f';{l[0]}')
        return texto

class Peixes(Animais, Utilidades):
  def __init__(self, id = '', idade = '', peso = '', genero = '', habitat = '', especie = '', viveCardume = '', localNativo = ''):
    super().__init__(id, idade, peso, genero, habitat)
    self.__especie = especie
    self.viveCardume = viveCardume
    self.localNativo = localNativo

    def get_especie(self):
        return self.__especie
    
    def get_viveCardume(self):
        return self.viveCardume

    def get_localNativo(self):
        return self.localNativo

    def inputAnimal(self, id):
        texto = super().inputAnimal(id)
        l = []
        t = ('Qual Espécie;Vive em Cardume?;Local Nativo'.split(';'))
        for i in range (len(t)):
            l.append(input(f'{t[i]}: '))
        texto += (f';{l[0]};{l[1]};{l[2]}')
        return texto

# class Anfibios(Animais):
#     def __init__(self, idade, peso, genero, habitat, dataChegada, especie, dieta, reproducao):
#         super().__init__(idade, peso, genero, habitat)
#         self.__dataChegada = dataChegada
#         self.__especie = especie
#         self.__dieta = dieta
#         self.__reproducao = reproducao
#         self.__endemico = False
#         self.__extincao = False

#     def get_dataChegada(self):
#         return self.__dataChegada

#     def set_dataChegada(self, dataChegada):
#         self.__dataChegada = dataChegada #caso alguém erre no input?

#     def get_especie(self):
#         return self.__especie

#     def set_especie(self, especie):
#         self.__especie = especie #caso alguém erre no input?

#     def get_dieta(self):
#         return self.__dieta

#     def set_dieta(self, dieta):
#         self.__dieta = dieta #caso alguém erre no input?

#     def get_reproducao(self):
#         return self.__reproducao

#     def set_reproducao(self, reproducao):
#         self.__reproducao = reproducao #caso alguém erre no input?

#     def extincao(self):
#         if not self.__extincao:
#             self.__extinção = True
#         else:
#             self.__extinção = False

#Código do Sistema
class InterfaceUsuario():
    def __init__(self):
        self.flag = 0

    def BancoDados(self, listDB_):#, dicDB_):#Esse método seria em outra classe referente aos acessos em Bancos
        #print(f'Teste {listDB_} de banco de dados')
        os.system('cls')
        for i in range (len(listDB_)):
            #dicDB_[i] = listDB_[i]
            print(f'Detalhes do animal: {listDB_[i]}')
        
        #print({dicDB_})
        # tBD = {}
        # tupla = lista
        # for i in range (1):
        #     tupla = lista[].split()
        #     tBD = {lista[0]: lista[1]}
        
        # t = ('Qual Espécie;Vive em Cardume?;Local Nativo'.split(';'))
        # for i in range (len(t)):
        #     l.append(input(f'{t[i]}: '))
        # return tBD

    def menu(self):
        os.system('cls')
        print('-----------------------------------------------------------')
        print('|                   Sistema de ZooZoul                    |')
        print('-----------------------------------------------------------')
        print('-----------------------------------------------------------')
        print('| 1- Adicionar um animal para o Zoológico                 |')
        print('| 2- Adicionar um mamífero para o Zoológico               |')
        print('| 3- Adicionar um peixe para o Zoológico                  |')
        print('| 4- Adicionar uma ave para o Zoológico                   |')
        print('| 5- Adicionar um réptil para o Zoológico                 |')
        print('| 8- Consultar animais do Zoológico                       |')
        print('| Se não escolher nenhuma das opções o sistema finalizará |')
        print('-----------------------------------------------------------')

    def main(self):
        c = Utilidades()
        c.Efeitos(0,9,'Iniciando')
        #Seria criado classe para o devido acesso ao banco de dados 
        listDB = []
        dicDB = {}

        while True:
            try:
                i = InterfaceUsuario()
                i.menu()
                opcao = int(input('Digite a opção desejada ... '))
                if 0 < opcao < 10:
                    if opcao == 1:
                        m = Animais()
                        registro = 'a' + (m.inputAnimal(len(listDB)))
                        listDB.append(registro)
                    elif opcao == 2:
                        m = Mamiferos()
                        registro = 'm' + m.inputAnimal(len(listDB))
                        listDB.append(registro)
                    elif opcao == 3:
                        p = Peixes()
                        registro = 'p' + p.inputAnimal(len(listDB))
                        listDB.append(registro)
                    elif opcao == 4:
                        v = Aves()
                        registro = 'v' + v.inputAnimal(len(listDB))
                        listDB.append(registro)
                    elif opcao == 5:
                        r = Repteis()
                        registro = 'r' + r.inputAnimal(len(listDB))
                        listDB.append(registro)
                    elif opcao == 8:
                        i.BancoDados(listDB)
                        input('Registro(s) do(s) anima(is)!')
                    else:
                        break
                else:
                    break
            except:
                break
        c.Efeitos(0,9,'Finalizando')

#Inicialização do sistema
input('↑ ↑ ↓ ↓ ← → ← → A B') #Brincadeira
i = InterfaceUsuario()
i.main()