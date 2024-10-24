import pandas as pd 

# Criando um DataFrame simples
data = {
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Idade': [25, 30, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

df = pd.DataFrame(data)

# Exibindo o DataFrame
print(df)

# Acessando uma coluna
# print(df['Nome'])

# Resumo estatístico
# print(df.describe())
