import pandas as pd

# 1. Filtragem de Dados

# Criando um DataFrame
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Idade': [24, 30, 22, 29],
    'Salário': [50000, 60000, 45000, 70000]
}
df = pd.DataFrame(data)

# Filtrando para encontrar pessoas com idade maior que 25
filtro_idade = df[df['Idade'] > 25]

# 2. Agrupamento e Agregação
# Agrupando por idade e calculando a média de salário
media_salario = df.groupby('Idade')['Salário'].mean()
print(media_salario)

# 3. Criação de Colunas Derivadas
# Criando uma coluna que representa o salário em mil
df['Salário em mil'] = df['Salário'] / 1000
print(df)

# 4. Mesclagem de DataFrames
# Criando outro DataFrame
data2 = {
    'Nome': ['Alice', 'Bob', 'Eve'],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}
df2 = pd.DataFrame(data2)

# Mesclando os DataFrames
merged_df = pd.merge(df, df2, on='Nome', how='left')
print(merged_df)

# 5. Ordenação de Dados
# Ordenando o DataFrame pelo salário
df_sorted = df.sort_values(by='Salário', ascending=False)
print(df_sorted)

# 6. Tratamento de Valores Faltantes
# Criando um DataFrame com valores faltantes
data3 = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Salário': [50000, None, 45000, 70000]
}
df3 = pd.DataFrame(data3)

# Preenchendo valores faltantes com a média
df3['Salário'].fillna(df3['Salário'].mean(), inplace=True)
print(df3)