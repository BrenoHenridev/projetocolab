import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lê os dados do CSV
df = pd.read_csv('gasolina.csv')

# Cria o gráfico
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df, marker='o')
plt.title('Preço da gasolina em São Paulo - Julho/2021')  # Título alterado
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)

# Salva o gráfico
plt.savefig('gasolina.png')
