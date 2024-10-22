import pandas as pd

# 1. Pivot Tables

# Criando um DataFrame
data = {
    'Vendedor': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie'],
    'Produto': ['A', 'A', 'B', 'B', 'A'],
    'Vendas': [100, 200, 150, 250, 300]
}
df = pd.DataFrame(data)

# Criando uma pivot table para somar vendas por vendedor e produto
pivot = df.pivot_table(values='Vendas', index='Vendedor', columns='Produto', aggfunc='sum', fill_value=0)
print(pivot)

# 2. Aplicando Funções Personalizadas com apply()
# Função para categorizar vendas
def categorizar_vendas(venda):
    if venda < 150:
        return 'Baixa'
    elif venda < 250:
        return 'Média'
    else:
        return 'Alta'

# Aplicando a função
df['Categoria'] = df['Vendas'].apply(categorizar_vendas)
print(df)

# 3. Uso de groupby() com Múltiplas Agregações
# Agrupando por vendedor e calculando múltiplas estatísticas
agg_df = df.groupby('Vendedor').agg({
    'Vendas': ['sum', 'mean', 'count'],
})
print(agg_df)

# 4. Transformações com transform()
# Normalizando as vendas
df['Vendas_normalizadas'] = df.groupby('Vendedor')['Vendas'].transform(lambda x: (x - x.mean()) / x.std())
print(df)

# 5. Análise de Séries Temporais
# Criando um DataFrame de séries temporais
data_dates = pd.date_range(start='2023-01-01', periods=5, freq='D')
sales_data = {
    'Data': data_dates,
    'Vendas': [200, 220, 180, 260, 240]
}
df_time = pd.DataFrame(sales_data)

# Definindo a coluna de Data como índice
df_time.set_index('Data', inplace=True)

# Calculando a média móvel
df_time['Média_móvel'] = df_time['Vendas'].rolling(window=2).mean()
print(df_time)

# 6. Usando stack() e unstack()
# Criando um DataFrame para demonstrar stack e unstack
data2 = {
    'Ano': [2020, 2020, 2021, 2021],
    'Produto': ['A', 'B', 'A', 'B'],
    'Vendas': [300, 400, 350, 450]
}
df2 = pd.DataFrame(data2)

# Definindo o índice
df2.set_index(['Ano', 'Produto'], inplace=True)

# Usando unstack
unstacked = df2.unstack()
print(unstacked)

# Usando stack
stacked = unstacked.stack()
print(stacked)

# 7. Manipulação Avançada de Strings
# Criando um DataFrame com dados de texto
data3 = {
    'Nome_Completo': ['Alice Silva', 'Bob Oliveira', 'Charlie Souza']
}
df3 = pd.DataFrame(data3)

# Separando o nome e sobrenome
df3[['Nome', 'Sobrenome']] = df3['Nome_Completo'].str.split(' ', expand=True)
print(df3)