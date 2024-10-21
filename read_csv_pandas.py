import pandas as pd

# Lendo um arquivo CSV
df = pd.read_csv('./files/dados.csv')

# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Exibindo informações sobre o DataFrame
print(df.info())

# Resumo estatístico
print(df.describe())
