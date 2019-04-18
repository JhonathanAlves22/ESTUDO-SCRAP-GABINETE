# ESTUDO-SCRAP-GABINETE
Este trabalho visa analisar o Scrap de produção no setor de Montagem dos Refrigeradores no primeiro semestre de 2019 e encontrar a causa raiz dos defeitos. 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Leitura do arquivo
base=pd.read_csv('Base_Scrap_2018.csv', encoding='utf-8')
print('Este dataset possui %s linhas e %s colunas' % (base.shape[0], base.shape[1]))

Respoasta: Este dataset possui 63738 linhas e 23 colunas


#Verificar os tipos de dados
print(base.dtypes)

Resposta: 
ORG. INVENTARIO                 object
TIPO ORDEM                     float64
ORDEM PROD.                    float64
ITEM                            object
DESCRIÇÃO DO ITEM               object
DESCRIÇÃO DO ITEM RED AJUST     object
DATA TRANSAÇÃO                  object
MÊS                             object
TRANSAÇÃO                      float64
TIPO TRANSAÇÃO                  object
CONTA CONTÁBIL                 float64
CÓDIGO DEFEITO                  object
DESCRIÇÃO DEFEITO               object
CENTRO  CUSTO                   object
DESCRIÇÃO CENTRO CUSTOS         object
QTDE (UNID)                     object
UNID                            object
CUSTO UND (R$)                  object
CUSTO TOTAL (R$)                object
ÁREA                            object
ÁREA AGRUPADA                   object
CONTA                           object
OBSERVAÇÃO                      object
dtype: object
