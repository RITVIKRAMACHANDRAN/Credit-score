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

---

## Architecture Overview

```
user-wallet-transactions.json
           |
           v
  [ score_wallets.py ]
           |
           v
engineer features  ---> score wallets  ---> output/wallet_scores.csv
```

---

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

The final score is derived by scaling features between 0–1, then applying the following weight formula:

```
score = (
  0.2 * total_deposit +
  0.2 * total_borrow +
  0.2 * repay_ratio +
  0.1 * redeem_ratio +
  0.1 * tx_count +
  0.1 * active_days +
  0.1 * (-liquidations)
) * 1000
```

Scores are clipped to the range 0–1000 and rounded to the nearest integer.

---

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
