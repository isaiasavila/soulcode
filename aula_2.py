#Aula 2 - 25/08/21 - Exercícios
#0) Escreva uma função que leia um número e retorne True se o número for perfeito
def numeroPerfeito(numero):
    teste = 0
    for i in range(1, numero):
        if numero % i == 0:
            teste = teste + i
    if teste == numero:
        return True
    return False

#1) Implementar duas funções: Uma que converta temperatura em graus Celsius para Fahrenheit. Outra que converta temperatura em graus Fahrenheit para Celsius.
def celsiusParaFahrenheit(celsius):
    return(celsius * 9 / 5) + 32

def fahrenheitParaCelsius(fahrenheit):
    return(fahrenheit - 32) * 5 / 9

#2) Escreva uma função que: Receba uma frase como parâmetro. Retorne uma nova frase com cada palavra com as letras invertidas
def palindromo(frase):
    return frase[::-1]

#3)Fazer um programa com duas funções, uma para verificar se o número é primo e retornar verdadeiro ou falso, e outra para exibir os números primos até chegarem nele.
def Primo(v = 2):
    c = 0 #A variável está zerada para a lógica de números primos
    f = False
    if v > 1: #Como o um não é primo 
        for i in range(1, v):#divide o número de um até o penúltimo, pois todo número é divisível por ele mesmo
            resto = v % i # Tenta efetuar a divisão exata
            if resto == 0: # se for adiciona ao contador
                c +=1
        if c == 1:
            f = True
    return f

def primoAte(v = 2):
    if Primo(v) == True:
        print('o número é primo')
        print('Primo 1')
        for i in range(1, v):
            if Primo(i) == True:
                print(f'Primo {i}')
        print('Primo', v)

#4) Implementar uma função que receba uma lista de listas de comprimentos quaisquer e retorne uma lista de uma dimensão.
def listaUmaDimensao(lista):
    listaTemp = []
    for lista_ in lista:
        for e in lista_:
            listaTemp.append(e)
    return listaTemp

#Programação orientada a objeto
class Pessoa():
    def __init__(self, nome, sexo, cpf, ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ativo = ativo

    def desativar(self):
        self.ativo = False

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

#Classe Bola: Crie uma classe que modele uma bola:
#a. Atributos: Cor, circunferência, material
#b. Métodos: trocaCor e mostraCor
class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mostraCor(self):
        return self.cor

    def trocaCor(self, cor):
        self.cor = cor

#2. Classe Quadrado: Crie uma classe que modele um quadrado:
#a. Atributos: Tamanho do lado
#b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área
class Quadrado():
    def __init__(self, lado):
        self.lado = lado

    def mudarValorLado(self, lado):
        self.lado = lado

    def retornarValorLado(self):
        return self.lado

    def calcularArea(self):
        return self.lado * self.lado

#3. Classe Pessoa: Crie uma classe que modele uma pessoa:
#a. Atributos: nome, idade, peso e altura
#b. Métodos: Envelhercer, engordar, emagrecer, crescer. 
#Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.crescer()
        self.idade = int(self.idade + 1)

    def engordar(self, quanto):
        self.peso = (self.peso + float(quanto))

    def emagrecer(self, quanto):
        self.peso = (self.peso - float(quanto))

    def crescer(self):
        if self.idade < 21:
            self.altura += 0.05

#4. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
#A classe deve possuir os seguintes atributos: número da conta, nome do correntista 
#e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; 
#No construtor, saldo é opcional, com valor default zero e os demais 
#atributos são obrigatórios.
class ContaCorrente():#print(vars(objeto))
    def __init__(self, nConta, nProprietario, saldo = 0):
        self.nConta = nConta
        self.nProprietario = nProprietario
        self.saldo = saldo
    
    def alterarNome(self, nNome):
        self.nProprietario = nNome

    def deposito(self, valor):
        self.saldo = self.saldo + valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
        else:
            print(f'Impossível! Seu saldo é de apenas {self.saldo}')

'''
'''