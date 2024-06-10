import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
file_path = 'datasets/restaurants-with-menus-utf8-illinois.csv'
data = pd.read_csv(file_path)

# Remover a coluna Unnamed
data_cleaned = data.drop(columns=['Unnamed: 0'])

# Converter menu_price para um valor numérico
data_cleaned['menu_price'] = data_cleaned['menu_price'].str.replace(' USD', '').astype(float)

# Preencher valores ausentes na coluna 'price_range' com 'Unknown'
data_cleaned['price_range'].fillna('Unknown', inplace=True)


# Distribuição dos restaurantes por categoria
restaurant_categories = data_cleaned['restaurant_category'].value_counts()

# Faixa de preços dos itens do menu
menu_price_range = data_cleaned['menu_price'].describe()

# Distribuição geográfica dos restaurantes
restaurant_locations = data_cleaned[['lat', 'lng']].drop_duplicates()

# Pontuações e número de avaliações dos restaurantes
restaurant_scores = data_cleaned['score'].dropna()
restaurant_ratings_count = data_cleaned['ratings_count'].dropna()

# Plotting
plt.figure(figsize=(14, 10))


# Faixa de preços dos itens do menu
plt.subplot(2, 2, 2)
sns.boxplot(x=data_cleaned['menu_price'])
plt.title('Faixa de Preços dos Itens do Menu')
plt.xlabel('Preço (USD)')

# Pontuações dos restaurantes
plt.subplot(2, 2, 4)
sns.histplot(restaurant_scores, bins=20, kde=True)
plt.title('Distribuição das Pontuações dos Restaurantes')
plt.xlabel('Pontuação')
plt.ylabel('Contagem')

plt.tight_layout()
plt.show()

print("Distribuição dos Restaurantes por Categoria:")
print(restaurant_categories)

print("\nFaixa de Preços dos Itens do Menu:")
print(menu_price_range)

print("\nResumo das Pontuações dos Restaurantes:")
print(restaurant_scores.describe())

print("\nResumo do Número de Avaliações dos Restaurantes:")
print(restaurant_ratings_count.describe())
