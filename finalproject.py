# Final Project
# 23/09/21

def trabalho():
    '''
    Algoritmo do exercício
    '''
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    import pandas as pd

    data = pd.read_csv('c:\scripts\Libertadores_Matches.csv')

    label_names = data['stage']
    labels = data['season']
    feature_names = data['home_team']
    features = data['datetime']

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
    #print(preds)
    # Avaliação de precisão
    print(accuracy_score(test_labels, preds))

# trabalho()

def modelo_internet():
    '''
    https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html#sphx-glr-auto-examples-preprocessing-plot-scaling-importance-py
    '''
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.naive_bayes import GaussianNB
    from sklearn import metrics
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_wine
    from sklearn.pipeline import make_pipeline
    print(__doc__)

    # Code source: Tyler Lanigan <tylerlanigan@gmail.com>
    #              Sebastian Raschka <mail@sebastianraschka.com>

    # License: BSD 3 clause

    RANDOM_STATE = 42
    FIG_SIZE = (10, 7)


    features, target = load_wine(return_X_y=True)

    print(features, target,'...\n\n...')

    # Make a train/test split using 30% test size
    X_train, X_test, y_train, y_test = train_test_split(features, target,
                                                        test_size=0.30,
                                                        random_state=RANDOM_STATE)

    # Fit to data and predict using pipelined GNB and PCA.
    unscaled_clf = make_pipeline(PCA(n_components=2), GaussianNB())
    unscaled_clf.fit(X_train, y_train)
    pred_test = unscaled_clf.predict(X_test)

    # Fit to data and predict using pipelined scaling, GNB and PCA.
    std_clf = make_pipeline(StandardScaler(), PCA(n_components=2), GaussianNB())
    std_clf.fit(X_train, y_train)
    pred_test_std = std_clf.predict(X_test)

    # Show prediction accuracies in scaled and unscaled data.
    print('\nPrediction accuracy for the normal test dataset with PCA')
    print('{:.2%}\n'.format(metrics.accuracy_score(y_test, pred_test)))

    print('\nPrediction accuracy for the standardized test dataset with PCA')
    print('{:.2%}\n'.format(metrics.accuracy_score(y_test, pred_test_std)))

    # Extract PCA from pipeline
    pca = unscaled_clf.named_steps['pca']
    pca_std = std_clf.named_steps['pca']

    # Show first principal components
    print('\nPC 1 without scaling:\n', pca.components_[0])
    print('\nPC 1 with scaling:\n', pca_std.components_[0])

    # Use PCA without and with scale on X_train data for visualization.
    X_train_transformed = pca.transform(X_train)
    scaler = std_clf.named_steps['standardscaler']
    X_train_std_transformed = pca_std.transform(scaler.transform(X_train))

    # visualize standardized vs. untouched dataset with PCA performed
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=FIG_SIZE)


    for l, c, m in zip(range(0, 3), ('blue', 'red', 'green'), ('^', 's', 'o')):
        ax1.scatter(X_train_transformed[y_train == l, 0],
                    X_train_transformed[y_train == l, 1],
                    color=c,
                    label='class %s' % l,
                    alpha=0.5,
                    marker=m
                    )

    for l, c, m in zip(range(0, 3), ('blue', 'red', 'green'), ('^', 's', 'o')):
        ax2.scatter(X_train_std_transformed[y_train == l, 0],
                    X_train_std_transformed[y_train == l, 1],
                    color=c,
                    label='class %s' % l,
                    alpha=0.5,
                    marker=m
                    )

    ax1.set_title('Training dataset after PCA')
    ax2.set_title('Standardized training dataset after PCA')

    for ax in (ax1, ax2):
        ax.set_xlabel('1st principal component')
        ax.set_ylabel('2nd principal component')
        ax.legend(loc='upper right')
        ax.grid()

    plt.tight_layout()

    plt.show()

def exemploYoutube():
    '''
    https://github.com/franciscoicmc/ciencia-de-dados/blob/master/Aula4-Classificacao-Naive%20Bayes.ipynb
    '''
    import random
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score

    random.seed(42)

    data = pd.read_csv('c:/scripts/Iris.csv', header=(0))
    print(data)
    classes = np.array(pd.unique(data[data.columns[-1]]), dtype=str)  

    # Converte para matriz e vetor do numpy
    data = data.to_numpy()
    nrow,ncol = data.shape
    y = data[:,-1]
    X = data[:,0:ncol-1]

    # Transforma os dados para terem media igual a zero e variancia igual a 1
    #scaler = StandardScaler().fit(X)
    #X = scaler.transform(X)

    # Seleciona os conjuntos de treinamento e teste
    p = 0.8 # fraction of elements in the test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        train_size = p, random_state = 42)

    # ajusta o classificador Naive-Bayes de acordo com os dados
    model = GaussianNB()
    model.fit(X_train, y_train)
    # realiza a predicao
    y_pred = model.predict(X_test)
    # calcula a acuracia
    score = accuracy_score(y_pred, y_test)
    print('Acuracia:', score)

def trabalho2():
    '''
    '''
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score

    df = pd.read_csv(r'c:\scripts\fruits.csv', header=(0))
    # gols = df.loc[:,['home_goal','away_goal']]
    
    df = df.drop(['fruit_label','fruit_subtype'], axis=1)
    # Excluindo valores não numéricos
    df = df.dropna(axis='rows')
    # Converte para matriz e vetor do numpy
    
    data = df.to_numpy()
    nrow,ncol = data.shape
    y = data[:,-1]
    X = data[:,0:ncol-1]
    print(y,'\n',X)

    # Seleciona os conjuntos de treinamento e teste
    p = 0.3 # fraction of elements in the test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = p, random_state = 42)

    # ajusta o classificador Naive-Bayes de acordo com os dados
    model = GaussianNB()
    model.fit(X_train, y_train)
    # realiza a predicao
    y_pred = model.predict(X_test)
    # calcula a acuracia
    score = accuracy_score(y_pred, y_test)
    print('Acurácia:', score)

trabalho2()
# exemploYoutube()

