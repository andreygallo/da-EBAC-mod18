import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv', sep=',')
gasolina_df 

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda", palette="pastel")
  grafico.set(title='Preço Gasolina', xlabel='Dia', ylabel='Preço');
  plt.savefig('gasolina.png', format='png')
  plt.show()