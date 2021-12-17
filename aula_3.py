#Aula 3 - 26/08/21 - Exercícios
class Funcionario():
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def get_bonificacao(self):
        return self.salario * 0.15

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self.qtd_funcionarios = qtd_funcionarios

    def get_bonificacao(self):#Polimorfismo
        return super().get_bonificacao() * 2

#joao = Funcionario('João','15975365411',2500)
#andre = Gerente('André','78945612355',3500,'admin', 25)
#print(andre.get_bonificacao())

from abc import ABC, abstractmethod

class Letras():
    @abstractmethod
    def mostrarTipo(self):
        print('Eu sou uma classe abstrata!')

class A(Letras):
    def __init__(self, descricao):
        self.descricao = descricao

    def imprimir(self):
        print('Aqui é um método da classe A')
'''
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
e. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
'''
class Carro():
    def __init__(self, consumoCombustivel):
        self.consumoCombustivel = consumoCombustivel
        self.quantidadeCombustivel = 0

    def obterGasolina(self):
        print(f'Tanque = {self.quantidadeCombustivel:.2f} lt')
        return self.quantidadeCombustivel

    def adicionarGasolina(self, quantidade):#Poderia jogar o obterGasolina() para mostrar nível atual
        if self.quantidadeCombustivel <= 60.00:
            self.quantidadeCombustivel = float(quantidade)
            print(f'Adicionado {quantidade:.2f} lt! Tanque = {self.quantidadeCombustivel:.2f} lt')
        else:
            print(f'Capacidade máximo de 60 lt! Tanque = {self.quantidadeCombustivel:.2f} lt')

    def andar(self, quantidade):
        tComb = quantidade / self.quantidadeCombustivel
        capacidade = self.quantidadeCombustivel * self.consumoCombustivel
        if quantidade <= capacidade:
            self.quantidadeCombustivel = self.quantidadeCombustivel - tComb
            print(f'O carro andou {quantidade:.2f} km. Tanque = {self.quantidadeCombustivel:.2f} lt')
        else:
            print(f'O carro não possui combustível suficiente! Tanque = {self.quantidadeCombustivel:.2f} lt')