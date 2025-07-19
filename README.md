# Aave V2 Credit Scoring System

This project calculates credit scores (0–1000) for wallets using raw transaction-level DeFi data from Aave V2 protocol.

## Features Used
- Total deposit/borrow amounts
- Repayment ratio
- Liquidation count
- Asset diversity
- Transaction frequency

## How to Run
```bash
pip install -r requirements.txt
python main.py --input data/user_transactions.json --output outputs/wallet_scores.csv
