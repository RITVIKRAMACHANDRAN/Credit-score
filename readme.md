# Aave V2 Wallet Credit Scoring

This project builds a robust credit scoring system for DeFi wallets using transaction-level data from the Aave V2 protocol.

## Objective

Assign a **credit score (0–1000)** to each wallet, based solely on historical actions like:

* `deposit`
* `borrow`
* `repay`
* `redeemunderlying`
* `liquidationcall`

Higher scores indicate responsible usage (e.g., repaying loans), while lower scores flag risky or exploitative behavior.

Feature Engineering

From the raw wallet transaction data, the following features were extracted:
- `total_deposit`: Total USD amount deposited
- `total_borrow`: Total USD borrowed
- `total_repay`: Total USD repaid
- `total_redeem`: Amount withdrawn (redeemed)
- `liquidations`: Number of times liquidated

## Architecture Overview
        +--------------------------+
        |  Aave Raw CSV Data File |
        +--------------------------+
                     |
                     v
        +--------------------------+
        |    Feature Engineering   |
        |  (deposit, borrow, etc.) |
        +--------------------------+
                     |
                     v
        +--------------------------+
        |     Credit Score Logic   |
        +--------------------------+
                     |
                     v
        +--------------------------+
        |  Output: wallet_scores.csv |
        +--------------------------+
                     |
                     v
        +--------------------------+
        |  Analysis + Visualization |
        +--------------------------+

 Processing Flow
Input: Load raw transaction data (wallet_data.csv)

Feature Engineering:

Group data by wallet

Calculate deposit, borrow, repay, redeem, and liquidation stats

Score Computation:

Apply scoring formula

Normalize and bound scores between 0 and 1000

Analysis:

Bucket scores in ranges (e.g., 0–100, 100–200, etc.)

Count wallets per range

Visualize score distribution using bar chart

Output:

Save results to output/wallet_scores.csv

Generate visual summary chart



## Features Used for Scoring

Each wallet is summarized into the following features:

| Feature         | Description                  |
| --------------- | ---------------------------- |
| `total_deposit` | Total deposited in USD       |
| `total_borrow`  | Total borrowed in USD        |
| `total_repay`   | Total repaid in USD          |
| `repay_ratio`   | repay / borrow ratio         |
| `redeem_ratio`  | redeem / deposit ratio       |
| `liquidations`  | Number of liquidation events |
| `tx_count`      | Number of total transactions |
| `active_days`   | Days active on the protocol  |

---

## Scoring Logic
A simple, interpretable scoring function was used:
```python
credit_score = base_score + repayment_score - liquidation_penalty

## How to Run

1. Place your `user-wallet-transactions.json` file in the root directory
2. Run the script:

```bash
python score_wallets.py
```

3. Results will be saved to `output/wallet_scores.csv`

---

## Requirements

* Python 3.7+
* pandas, numpy, scikit-learn

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Author

Built for robust and explainable credit scoring using open DeFi data.
