import argparse

from src.score_wallets import run_credit_scoring

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='data/user_transactions.json', help='Path to input JSON')
    parser.add_argument('--output', type=str, default='outputs/wallet_scores.csv', help='Output CSV path')

    args = parser.parse_args()
    run_credit_scoring(args.input, args.output)
