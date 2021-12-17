# Aula 21/09/21
def teste_numerico(um, dois, tres, p1, p2, p3):
    from random import randint
    limite_treino = 1000
    contador_treino = 100

    entrada_treino = list()
    saida_treino = list()

    for i in range(contador_treino):
        _a = randint(0,limite_treino)
        _b = randint(0,limite_treino)
        _c = randint(0,limite_treino)
        op = (um*_a) + (dois*_b) + (tres*_c)
        entrada_treino.append([_a,_b,_c])
        saida_treino.append(op)

    from sklearn.linear_model import LinearRegression
    predictor = LinearRegression()
    predictor.fit(X=entrada_treino, y=saida_treino)

    X_TEST = [[p1, p2, p3]]#Teste

    outcome = predictor.predict(X_TEST) #Resultado de Y
    coefficients = predictor.coef_ #Custo de memória

    # print('Resultado: {}\nCoeficientes: {}'.format(outcome,coefficients)) # Format antigo
    print(f'Resultado: {outcome}\nCoeficientes: {coefficients}') # Format novo

# teste_numerico(1, 2, 3, 10, 20, 30)
# teste_numerico(3, 2, 1, 9, 18, 21)

def juliossolution():
    from numpy import array, transpose, linalg
    entrada_treino = array([[3,3,3],[2,7,15],[3,5,5],[1,1,1],[9,10,2]]) ### Matriz 5x3 (pedria ser 1000x3)
    saida_treino = transpose(array([18,35,24,6,49])) ### Vetor de ordem 5
    saida_treino = transpose(entrada_treino).dot(saida_treino) # novo vetor de ordem 3 com influencia de todos os dados
    entrada_treino = transpose(entrada_treino).dot(entrada_treino) #Nova matriz de ordem 3x3 com influencia de todos os dados
    coefficients = linalg.inv(entrada_treino).dot(saida_treino) # Solução do sistema linear
    X_TEST = array([30,30,30])
    outcome = X_TEST.dot(coefficients)
    print(f"Resultado: {outcome}\nCoeficientes: {coefficients}")

def regressao(um, dois, tres, r1, r2, r3):
    
    from random import randint
    limite_treino = 1000
    contador_treino = 100

    entrada_treino = list()
    saida_treino = list()

    for i in range(contador_treino):
        _a = randint(0,limite_treino)
        _b = randint(0,limite_treino)
        _c = randint(0,limite_treino)
        op = (um*um) + (dois*dois) - (tres*tres)
        entrada_treino.append([_a,_b,_c])
        saida_treino.append(op)

    from sklearn.linear_model import LinearRegression
    predictor = LinearRegression()
    predictor.fit(X=entrada_treino, y=saida_treino)

    X_TEST = [[r1, r2, r3]]#Teste

    outcome = predictor.predict(X_TEST) #Resultado de Y
    coefficients = predictor.coef_ #Custo de memória

    # print('Resultado: {}\nCoeficientes: {}'.format(outcome,coefficients)) # Format antigo
    print(f'Resultado: {outcome}\nCoeficientes: {coefficients}') # Format novo

# regressao(4,5,2,27,3377,279)

def rotina_ze():
    from random import randint
    limite_treino = 1000
    contador_treino = 100

    entrada_treino = list()
    saida_treino = list()

    for i in range(contador_treino):
        a = randint(0,limite_treino)
        b = randint(0,limite_treino)
        c = randint(0,limite_treino)
        op = a + (2*b) + (3*c)
        entrada_treino.append([a,b,c])
        saida_treino.append(op)

        from sklearn.linear_model import LinearRegression
        predictor = LinearRegression()
        predictor.fit(X=entrada_treino, y=saida_treino)

        X_TEST = [[10,20,30]]#Teste

        outcome = predictor.predict(X_TEST) #Resultado de Y
        coefficients = predictor.coef_ #Custo de memória

    print('Resultado: {}\nCoeficientes: {}'.format(outcome,coefficients))

# rotina_ze()

def aula_17_algoritmo1():
    '''
    '''
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier ##KNN Nearest Neighbor
    import numpy as np

    iris = load_iris()
    # print(iris.keys())
    # print(iris['target_names'])
    # print(iris['feature_names'])
    # print(iris['data'].shape)
    # print(iris['data'][:10])
    # print(iris['target'])

    X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'])

    # print(X_train.shape)
    # print(X_test.shape)
    # Criando o modelo
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)
    # Testando o modelo
    x_new = np.array([[5,2.9,1,0.2]])
    print(x_new)
    prediction = knn.predict(x_new)
    print(prediction)
    print(iris['target_names'][prediction])
    print('Acuracidade: ', knn.score(X_test, y_test))

# aula_17_algoritmo1()

def aula_17_algoritmo2():
    '''
    '''
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score

    data = load_breast_cancer()

    print(data)

    label_names = data['target_names']
    labels = data['target']
    feature_names = data['feature_names']
    features = data['data']

    print('Nome dos rótulos\n',label_names)
    print('Conteúdo do rótulo\n', labels[0])
    print('Nome da Característica\n', feature_names)
    print('Característica\n', features)

    train, test, train_labels, test_labels = train_test_split(features, labels, test_size=0.33)

    gnb = GaussianNB()

    # Treinar
    model = gnb.fit(train, train_labels)
    # Previsões
    preds = gnb.predict(test)
    print(preds)
    # Avaliação de precisão
    print(accuracy_score(test_labels, preds))

#aula_17_algoritmo2()
x = 1/3 * 2/3 * 1/3 * 2/3
y = 1/3 * 2/3
z = y * 1/3
w = z * 2/3
q = 4/81
print(x,'...',q)