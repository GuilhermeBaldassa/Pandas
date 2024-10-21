import pandas as pd

# Lendo o arquivo JSON
df = pd.read_json('./files/dados.json')

# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Exibindo informações sobre o DataFrame
print(df.info())
