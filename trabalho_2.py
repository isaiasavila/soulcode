# Trabalho 2

class Utilidades:
    def proximo(self):
        import os
        
        # mude a flag para mudar o curso do programa
        flag = 1
        if flag == 1:
            input('<enter>')
        else:
            print('.....')
        os.system('cls')

    def ler_dados(self, cabecalho, texto):
        #flag = ut.lerDados('- Escolha de base de dados -','Digite 1 para conexão local!\n') # Mudar para alterar o curso 
        print(cabecalho)
        return input(texto)

    def ler_senha(self):
        import getpass
        return input('Digite seu usuário: '), getpass.getpass('Digite sua senha: ')

    def menu(self, texto1, texto2='', cabecalho=''):
        '''
        Método utilizado para gerar o menu
        '''
        print(cabecalho)
        print(f'╔═════════════════════════════════════════════════════════════════════════════════╗')
        print(texto1)
        if texto2 != '':
            print(texto2)
        print(f'╚═════════════════════════════════════════════════════════════════════════════════╝')
        
    def mostrar_baselocal(self):
        print('Em implementação...')

    def mostrar_documentos(self, _tabela, _bancodados):
        from pymongo import MongoClient
        import pymongo
        # Forneça o url do atlas mongodb para conectar python a mongodb usando pymongo
        try:
            usuario ,senha = self.ler_senha()
            # Depois de ler o arquivo joga a informação para uma string de conexão
            CONNECTION_STRING = f'mongodb+srv://{usuario}:{senha}@cluster0.h4ljz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
            # Crie uma conexão usando MongoClient. Você pode importar MongoClient ou usar pymongo.MongoClient
            _client = MongoClient(CONNECTION_STRING)
            # Cria o banco de dados.
            _dbname = _client[_bancodados]
            # o parâmetro do método, específica a coleção que será utilizada
            _collection_name = _dbname[_tabela]
            # o método retorna uma coleção inteira, muita atenção quando ela for muito grande
            return _collection_name.find()
        except:
            print('Falha na conexão! Tente novamente')    

# Indicadores ambientais globais
# Environmental indicators help us to understand and analyze the health of the planet.
# https://www.kaggle.com/ruchi798/global-environmental-indicators
# Terrestrial_Marine protected areas
# Áreas terrestres e marinhas protegidas
# Tecnologias usadas Python, PyMongo, Pandas, MatPloitLib, IPython
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
import matplotlib.ticker as mtick

try:
    ut = Utilidades()
    # Escolha do tipo de gráfico
    plt.style.use('ggplot')
    # Escolha entre base de dados local ou remota
    flag = ut.ler_dados('- Escolha de base de dados -','Digite 1 para conexão local!\n') # Mudar para alterar o curso 
    # 1=Dados local
    if flag == '1':
        # Conectando localmente
        detalhes_items = ut.mostrar_baselocal()#'TerrestrialMarine.csv')
        print('Conexão Local Ativada!')
    else:
        # Conectando remotamente
        try:
            while True:
                df = pd.DataFrame(list(ut.mostrar_documentos('trabalho2','soulcode')))
                print('Conexão Remota Ativada!')                    
                break
        except:
            print('Erro de conexão!')
    # Todos os dados são inseridos em um dataFrame
    
    # Apresentação
    # Método para apresentar o menu
    if flag != 1: # Somente se não estiver em modo local
        # Renomeando os cabeçalhos para melhorar a forma de tratar os dados
        df.columns = ['_ID', 'País','Ano','Porcentagem','Código']
        # Setando para impressão apenas os valores que interessam
        df = df[['País','Porcentagem']]
    # Mostrar porcentagem mundial geral
    ut.menu('║            Porcentagem mundial de área marinha e terrestre protegida            ║','║ Áreas marinhas e terrestres protegidas em porcentagem de área territorial total ║','1')    
    # Mostra a linha um, que na tabela usada encontra-se a informação global
    display(df.loc[0,'País'],' - ',df.loc[0,'Porcentagem'],'%')
    # Apagando a informação da quantidade mundial
    df = df.drop(0, axis=0)
    # método usado para controlar o fluxo do programa
    ut.proximo()
    # Ordenando os dados por maiores porcentagens
    if flag != 1:
        # Alterando o tipo de porcentagem para float, para ordenar corretamente
        df[["Porcentagem"]] = df[["Porcentagem"]].apply(pd.to_numeric)
        dfp = df.sort_values('Porcentagem')
        dfp['%'] = '%'
        # Ordenando a lista em ordem crescente
        
    else:
        # Se for local muda 
        dfp = df
    ut.menu('║              Países sem nenhuma área terrestre ou marinha protegida             ║','','2')
    # Mostra os países que não tem área protegida
    display(dfp.loc[dfp['Porcentagem'] == 0.0, ['País','Porcentagem','%']])
    # Mostra a quantia de países que entraram na consulta acima
    lista = (dfp.loc[dfp['Porcentagem'] == 0.0].count())
    # Mostra a quantidade na tela
    print(lista[1],' País(es)')
    # Remover os países com índice 0, pois eles não interessam na análise
    # Guarda nesse dataFrame os países que têm porcentagem zerada
    remover = dfp.loc[(dfp['Porcentagem'] == .0)]
    # Remove do dataFrame, passando os índices através do dataFrame setado acima
    dfp = dfp.drop(remover.index)
    ut.proximo()
    ut.menu('║         TOP 12-  Países com menor porcentagem de área territorial total         ║','║                             - Áreas Protegidas -                                ║','3')
    # Mostra os 10 maiores países com área territorial protegida
    display(dfp.head(12))
    # Cria uma lista com os 12 países com menor área protegida
    df_12menos = dfp.head(12)
    #print('12 menos',df_12menos)
    ut.proximo()
    ut.menu('║         TOP 12-  Países com maior porcentagem de área territorial total         ║','║                             - Áreas Protegidas -                                ║','4')
    # Mostra os 10 maiores países com área territorial protegida
    display(dfp.tail(12))
    # Cria uma lista com os 12 países com menor área protegida
    df_12mais = dfp.tail(12)
    #print('12 mais',df_12mais)
    ut.proximo()
    ut.menu('║                     Padrões das áreas terrestres e marinhas                     ║','','5')
    print(dfp.describe())
    estatistica = dfp.describe().values
    ut.proximo()
    # Brasil
    ut.menu('║                           Escolha um país - Brazil?                             ║','','6')
    while True:
        # Solicita um nome para a pesquisa
        pais = input('Digite um país? s=sair\n')
        # Seta em um dataFrame temporário a pesquisa
        dftemp = dfp.loc[dfp['País'] == pais, ['País','Porcentagem','%']]        
        # Apresenta a infromação, se tiver o que mostrar
        if dftemp.empty == False:
            display(dftemp)
            print('Média: ',estatistica[1],'%')
        else:
            # Se for digitado 's' o programa continuará!
            if pais == 's':
                break
        
    ut.proximo()
    ut.menu('║                                   GRÁFICOS                                      ║','','7')
    # Mostra o gráfico dos 12 Mais usando os campos selecionados do tipo barra
    df_12mais.plot(kind='bar',x='País',y='Porcentagem',figsize=(8,6))
    # Seta o campo Porcentagem para %
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
    # Muda o título
    plt.title('Top 12+ Países...')
    # Apresenta o gráfico na tela
    plt.show()
    # Mostra o gráfico dos 12 Menos
    df_12menos.plot(kind='bar',x='País',y='Porcentagem',figsize=(8,6))
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
    plt.title('Top 12- Países...')
    plt.show()
    # Busca o Dataframe principal com todos os países
    df.plot(kind='scatter',x='País',y='Porcentagem',figsize=(8,6))
    plt.title('Todos os países...')
    plt.xlabel('')
    plt.ylabel('')
    plt.show()
    ut.proximo()
    input('Obrigado e até a próxima!')
except:
    # Se acontecer algum imprevisto ele vai gerar uma mensagem de erro!
    print('Erro fatal!\n')