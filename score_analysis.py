import pandas as pd

df = pd.read_csv("output/wallet_scores.csv")

df['score_bucket'] = pd.cut(df['credit_score'], bins=range(0, 1100, 100))

distribution = df['score_bucket'].value_counts().sort_index()

total_wallets = len(df)

print("| Score Range | # Wallets | % of Total |")
print("|-------------|-----------|------------|")
for bucket, count in distribution.items():
    pct = round((count / total_wallets) * 100, 2)
    print(f"| {bucket} | {count} | {pct}% |")
