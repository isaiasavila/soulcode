from utilidades import *
import random
#Aula 1 - 24/08/21 - Exercícios
#01) Faça um Programa que leia uma lista de 5 números inteiros e mostre-os.
'''
lista = [0,0,0,0,0]
i = 0
while i < 5:
    lista[i] = int(input('Digite um número inteiro\n'))
    i += 1
print(lista)
'''
#02) Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.
'''
lista = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.1]
for i in range(1,10):
    lista[i] = float(input('Digite um número real\n'))
#lista.reverse()
for i in range(-1,len(lista)):
    print(float(lista[i]))
'''
#03) Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''
lista = [0,0,0,0]
for i in range(0,4):
    lista[i] = float(input(f'Digite a {i+1}ª nota\n'))
for i in range(4):
    print(f'{i+1}ª Nota: {lista[i]:.2f}')
media = (lista[0]+lista[1]+lista[2]+lista[3]) / 4
print(f'Média das notas: {media:.2f}')
'''
#04) Faça um Programa que leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na listar PAR e os números IMPARES na lista ímpar. Imprima os três vetores.
'''
lista = []
for c in range(20):
    lista.append(int(input('Digite um valor inteiro\n')))

par = []
impar = []
i = 0
while i < 20:    
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
    i += 1

print('Lista digitada', lista)
print('Números pares:', par)
print('Números ímpares:', impar)
'''
#05) Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
tupla = ('adao','eva','alfredo','dodo','getulio','joao')
for i in range(0, len(tupla)):
    print(tupla[i])
    texto = 'Vogais da palavra: '
    for c in range(0, len(tupla[i])):
        palavra = tupla[i].lower()
        if palavra[c] == 'a' or palavra[c] == 'e' or palavra[c] == 'i' or palavra[c] == 'o' or palavra[c] == 'u':
            texto += palavra[c]
    print(texto)
'''
#06) Faça um programa que leia nome e média de um aluno, guardando também a situção em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
dados = {}
dados = {'nome':input('Digite o nome do aluno\n').title(), 'media': float(input('Digite a média do aluno\n'))}
if dados['media'] > 5.0:
    dados['situacao'] = 'Aprovado'
else:
    dados['situacao'] = 'Reprovado'
print(dados)
'''
#07) Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.
'''
medias=[]
for i in range(2):#número de alunos
    n = 0.0
    print(f'Aluno {i+1}')
    for c in range(4):#número de notas
        n += (float(input(f'Digite a nota {c+1}:\n')))
    medias.append(n / 4)
n = 0
for i in range(len(medias)):
    if medias[i] >= 7:
        n += 1
print(f'{n} aluno(s) com média igual ou maior que 7.0')
'''
#08) Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das 
# temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 
# 2 – Fevereiro, #. . . ).
'''
temperaturas = []
meses = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
mAnual = 0
for i in range(12):
    temperaturas.append(float(input(f'Digite a temperatura de {meses[i]}\n')))
    mAnual += temperaturas[i]
mAnual /= 12
print(f'A média anual de temperatura foi de {mAnual:.2f}°')#Não pedia no enunciado
for i in range(12):
    if temperaturas[i] > mAnual:
        print(f'{i+1} - {meses[i]} a temperatura foi de {temperaturas[i]:.2f}°')
'''
#09) Exercício Maior e menor valores em Tupla. Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
#  mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
aleatorios = []
for i in range(5):
    aleatorios.append(random.randint(-20, 20))
tupla = aleatorios
tupla.sort()
print(f'Números gerados {tupla}')
print(f'Maior {tupla[4]}')
print(f'Menor {tupla[0]}')
'''
#10) Faça um programa que verifique se um inteiro digitado pelo usuário está presente
#dentro de um dicionário. Crie o dicionário no próprio programa.
d = {1:10, 2:20, 3:30, 4:40}
x = int(input('Digite um número'))

if x in d:
    print('O número digitado está no dicionário')
else:
	print('O número digitado não está no dicionário')
'''
'''
'''
lerInteiro()

for i in range (10):
    num = aleatorio(1,0,10)
    print(num)
nome = 'cArol'
print (nome[0].upper())
print (nome[1].lower())
#del dicionario[indice] apagar um
#len(dicionario)
#dicionario.keys()
'''