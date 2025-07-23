import pandas as pd
import json
from datetime import datetime
import os
import numpy as np

def load_data(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    df = pd.json_normalize(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df['amount'] = pd.to_numeric(df['actionData.amount'], errors='coerce')
    df['price_usd'] = pd.to_numeric(df['actionData.assetPriceUSD'], errors='coerce')
    df['amount_usd'] = df['amount'] * df['price_usd']
    return df[['userWallet', 'timestamp', 'action', 'amount_usd']]

def engineer_features(df):
    grouped = df.groupby('userWallet')
    features = pd.DataFrame()
    features['total_deposit'] = grouped.apply(lambda x: x[x.action == 'deposit'].amount_usd.sum())
    features['total_borrow'] = grouped.apply(lambda x: x[x.action == 'borrow'].amount_usd.sum())
    features['total_repay'] = grouped.apply(lambda x: x[x.action == 'repay'].amount_usd.sum())
    features['total_redeem'] = grouped.apply(lambda x: x[x.action == 'redeemunderlying'].amount_usd.sum())
    features['liquidations'] = grouped.apply(lambda x: (x.action == 'liquidationcall').sum())
    features['repay_ratio'] = features['total_repay'] / features['total_borrow'].replace(0,1)
    features['redeem_ratio'] = features['total_redeem'] / features['total_deposit'].replace(0,1)
    tx_count = df.groupby("userWallet").size()
    active_days = df.groupby("userWallet").timestamp.nunique()
    features['tx_count'] = tx_count
    features['active_days'] = active_days
    features = features.replace([float('inf'), -float('inf')], 0)
    features = features.fillna(0)
    features = features.reset_index()
    return features


def score_wallets(features):
    from sklearn.preprocessing import MinMaxScaler

    scoring_cols = ['total_deposit', 'total_borrow', 'repay_ratio', 'redeem_ratio', 'tx_count', 'active_days']
    X = features[scoring_cols].copy()
    X['liquidations'] = -features['liquidations']  # negative weight

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    scores = (X_scaled * [0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1]).sum(axis=1)
    features['credit_score'] = (scores * 1000).clip(0, 1000).round(0).astype(int)
    return features[['userWallet', 'credit_score']]

def main():
    input_file = 'user-wallet-transactions.json'
    output_file = 'output/wallet_scores.csv'

    os.makedirs('output', exist_ok=True)
    print("Loading data...")
    df = load_data(input_file)
    print("Engineering features...")
    features = engineer_features(df)
    print("Scoring wallets...")
    scores = score_wallets(features)
    features.reset_index(inplace=True)
    scores.to_csv(output_file, index=False)
    print(f"Done. Scores saved to {output_file}")

if __name__ == '__main__':
    main()
