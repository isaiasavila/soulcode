import pandas as pd
import numpy as np
np.random.seed(5)
df = pd.DataFrame(np.random.randint(100, size=(100, 6)), 
                  columns=list('ABCDEF'), 
                  index=['R{}'.format(i) for i in range(100)])
df.head()
#Para obter as colunas de C a E (observe que, diferentemente da fatia inteira, 'E' está incluído nas colunas):
df.loc[:, 'C':'E']