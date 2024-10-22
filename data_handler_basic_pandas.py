# 1. Importação de Bibliotecas
import pandas as pd

# 2. Leitura de Dados
# Lendo um arquivo CSV
df = pd.read_csv('./files/dados.csv')

# Lendo um arquivo Excel
df = pd.read_excel('./files/dados.xlsx')

# 3. Visualização dos Dados
# Exibir as primeiras linhas do DataFrame
print(df.head())

# Exibir informações sobre o DataFrame
print(df.info())

# 4. Seleção de Dados
# Selecionar uma coluna
coluna = df['Nome']

# Selecionar múltiplas colunas
sub_df = df[['Nome', 'Categoria']]

# Selecionar linhas específicas
linhas = df.iloc[0:5]  # Primeiras 5 linhas

# 5. Filtragem de Dados
# Filtrar linhas com base em uma condição
filtro = df[df['Preço'] > 10]

# 6. Agrupamento de Dados
# Agrupar por uma coluna e calcular a média
agrupado = df.groupby('Preço').mean()

# 7. Manipulação de Dados
# Adicionar uma nova coluna
df['preco_dobrado'] = df['Preço'] * 2

# Renomear colunas
df.rename(columns={'Preço': 'preco'}, inplace=True)

# Remover colunas
df.drop(columns=['Categoria'], inplace=True)

# 8. Tratamento de Valores Faltantes
# Remover linhas com valores faltantes
df.dropna(inplace=True)

# Preencher valores faltantes
df.fillna(0, inplace=True)

# 9. Exportação de Dados
# Exportar para CSV
df.to_csv('./files/arquivo_saida.csv', index=False)

# Exportar para Excel
df.to_excel('./files/arquivo_saida.xlsx', index=False)