#importar bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Leitura do arquivo
base=pd.read_csv('Base_Scrap_2018.csv', encoding='utf-8')
print('Este dataset possui %s linhas e %s colunas' % (base.shape[0], base.shape[1]))
#base['ABSENTEÍSMO'].fillna(0, inplace = True)
#base['REPROCESSO META'].fillna(0, inplace = True)
#base['REPROCESSO REAL'].fillna(0, inplace = True)
#base['SALDO PROD'].fillna(0, inplace = True)
#base['SALDO QUALID'].fillna(0, inplace = True)
#base['DATA'].fillna('NO_DATE', inplace = True)
#base.head()

#Verificar os tipos de dados
print(base.dtypes)

#Gerar estatísticas básicas
#print(base.describe())

#Criando gráfico deitado
#horas_perda = base[['HORÁRIO','SALDO PROD']].head(10).set_index('HORÁRIO').sort_values('SALDO PROD', ascending=True)
#horas_perda.plot(kind='barh',figsize=(11,7), grid=False, color='darkred', legend=True)

#Gráfico de perda de produção por hora
#horas_perda = base.groupby('HORÁRIO')['SALDO PROD'].sum().plot(kind='barh', color='green', figsize=(11,5),legend=True)
#plt.xlabel('HORA')
#plt.ylabel('PERDA DE PRODUÇÃO')
#plt.title('PERDA TOTAL DE PRODUÇÃO / HORA: ' + str(base['SALDO PROD'].sum())+ ' produtos perdidos')
#plt.xticks(rotation=0)
#plt.figure()
#plt.show()


#Gráfico de perda de produção por linha
#linha_perda = base.groupby('LINHA')['SALDO PROD'].sum().plot(kind='barh', color='green', figsize=(11,5),legend=True)
#plt.xlabel('LINHA')
#plt.ylabel('PERDA DE PRODUÇÃO')
#plt.title('PERDA TOTAL DE PRODUÇÃO / LINHA: ' + str(base['SALDO PROD'].sum())+ ' produtos perdidos')
#plt.xticks(rotation=0)
#plt.figure()
#plt.show()

#Gráfico de perda de produção por dia
#data_perda1 = base.groupby('DATA')['SALDO PROD'].sum().plot(kind='bar', color='green', figsize=(11,5),legend=True)
#plt.xlabel('DIA')
#plt.ylabel('ABSENTEÍSMO')
#plt.title('PERDA TOTAL DE PRODUÇÃO / DIA: ' + str(base['SALDO PROD'].sum())+ ' produtos perdidos')
#plt.xticks()
#plt.figure()
#plt.show()

#Gráfico de dispersão de produção por dia
#data_perda2 = plt.scatter(base['DATA'], base['SALDO PROD'], alpha=0.5, c=base['SALDO PROD'])
#plt.xticks(rotation=90)
#plt.figure()
#plt.show()

#Gráfico de perda de qualidade por hora
#qualidade_perda = base.groupby('HORÁRIO')['SALDO QUALID'].sum().plot(kind='barh', color='green', figsize=(11,5),legend=True)
#plt.xlabel('HORA')
#plt.ylabel('PERDA DE QUALIDADE')
#plt.title('PERDA TOTAL DE QUALIDADE / HORA: ' + str(base['SALDO QUALID'].sum())+ ' produtos perdidos')
#plt.xticks(rotation=0)
#plt.figure()
#plt.show()


