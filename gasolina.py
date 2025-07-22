import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lê o CSV (colunas do seu arquivo: dia, venda)
df = pd.read_csv("gasolina.csv")

# Renomeia para ficar semântico
df = df.rename(columns={"venda": "preco"})

sns.set(style="whitegrid")
ax = sns.lineplot(data=df, x="dia", y="preco", marker="o")
ax.set(title="Preço médio da gasolina - SP (01–10/jul/2021)",
       xlabel="Dia",
       ylabel="Preço (R$)")
plt.tight_layout()
plt.savefig("gasolina.png", dpi=300)
