import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ler o arquivo
df = pd.read_csv("ecommerce_estatistica.csv")

# Histograma - distribuição dos preços
plt.figure(figsize=(8,5))
sns.histplot(df['Preço'], bins=30, kde=False)
plt.title("Distribuição dos preços")
plt.xlabel("Preço")
plt.ylabel("Frequência")
plt.show()

# Dispersão - Nota vs Preço
plt.figure(figsize=(8,5))
sns.scatterplot(x='Nota', y='Preço', data=df)
plt.title("Relação entre Nota e Preço")
plt.xlabel("Nota")
plt.ylabel("Preço")
plt.show()

# Mapa de calor - correlação entre variáveis numéricas
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Mapa de calor das correlações")
plt.show()

# Barra - média de preço por marca
plt.figure(figsize=(10,6))
sns.barplot(x='Marca', y='Preço', data=df)
plt.title("Preço médio por marca")
plt.xlabel("Marca")
plt.ylabel("Preço médio")
plt.xticks(rotation=45)
plt.show()

# Pizza - distribuição por gênero
df['Gênero'].value_counts().plot.pie(autopct='%1.1f%%', figsize=(6,6))
plt.title("Distribuição por gênero")
plt.ylabel("")
plt.show()

# Densidade - preços
plt.figure(figsize=(8,5))
sns.kdeplot(df['Preço'], shade=True)
plt.title("Densidade dos preços")
plt.xlabel("Preço")
plt.show()

# Regressão - Nota vs Qtd_Vendidos
plt.figure(figsize=(8,5))
sns.regplot(x='Nota', y='Qtd_Vendidos', data=df, scatter_kws={'alpha':0.5})
plt.title("Regressão linear: Nota vs Quantidade Vendida")
plt.xlabel("Nota")
plt.ylabel("Qtd Vendidos")
plt.show()
