import pandas as pd
import matplotlib as plt
import seaborn as sns
from xgboost import XGBClassifier
from IPython.display import display, HTML

git_url = "https://github.com/plotly/datasets/blob/master/diabetes.csv?raw=true"
df_diabetes = pd.read_csv(git_url)

NUM_POPULACAO = df_diabetes.shape[0]
NUM_ATRIBUTOS = df_diabetes.shape[1]

display( HTML( '<style>.container { width:100% !important; }</style>') )

# maximiza o número de colunas e linhas para impressão 
# quando do uso da função head() do Pandas
pd.options.display.max_columns = 15
pd.options.display.max_rows = 50

# apresenta cabecalho
display(HTML('<h3><b>BASE DE DADOS DIABETES</b></h3><hr/>'))

# carregando 10 amostras aleatórias
display(df_diabetes.head(10))
display(HTML('<hr/><h3><b>População : </b>' + 
             str(NUM_POPULACAO) + 
             '  |  Número de atributos : ' + 
             str(NUM_ATRIBUTOS) +'</h3>'))