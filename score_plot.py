import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("output/wallet_scores.csv")

df['score_bucket'] = pd.cut(df['credit_score'], bins=range(0, 1100, 100))

distribution = df['score_bucket'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
sns.barplot(x=distribution.index.astype(str), y=distribution.values, palette="Blues_d")

plt.title("Credit Score Distribution of Wallets")
plt.xlabel("Score Range")
plt.ylabel("Number of Wallets")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig("output/credit_score_distribution.png")
plt.show()
