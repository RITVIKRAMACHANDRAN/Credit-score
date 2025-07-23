# Score Distribution Analysis

After computing credit scores for all wallets, we analyzed the behavior across various score bands to evaluate reliability, risk, and protocol interaction patterns.

---
## Credit Score Distribution Analysis

The following table shows the distribution of credit scores across wallets:

| Score Range | # Wallets | % of Total |
|-------------|-----------|------------|
| (0, 100]    | 2944      | 84.19%     |
| (100, 200]  | 545       | 15.58%     |
| (200, 300]  | 3         | 0.09%      |
| (300, 400]  | 2         | 0.06%      |
| (400, 500]  | 2         | 0.06%      |
| (500, 600]  | 1         | 0.03%      |
| (600, 700]  | 0         | 0.0%       |
| (700, 800]  | 0         | 0.0%       |
| (800, 900]  | 0         | 0.0%       |
| (900, 1000] | 0         | 0.0%       |

### Observations:

- The majority of wallets (84.19%) fall in the lowest credit score bucket (0–100), indicating either poor credit behavior or limited data availability.
- 15.58% of wallets are in the 100–200 range.
- Scores above 300 are extremely rare (less than 0.2%), and no wallets score above 600.
- This suggests the dataset may be skewed toward new, inactive, or risk-prone wallets.

---

This type of skewed distribution might indicate the need for:
- Further feature engineering to reward positive behaviors,
- Improved dataset balance or filtering,
- A review of the scoring model thresholds.

## Summary

These score distributions and behaviors help segment reliable vs. risky wallets. They offer insights for DeFi protocols aiming to:

* Whitelist responsible users
* Penalize or limit risky behavior
* Design dynamic interest/collateral policies

This scoring can be retrained or extended using ML models as more labeled data or behavior metrics become available.

Credit Score Distribution
[Credit Score Distribution](output/credit_score_distribution.png)
