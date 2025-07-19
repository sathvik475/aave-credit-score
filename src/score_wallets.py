import json

from src.features import extract_wallet_features
from src.model import score_wallets


def run_credit_scoring(input_json, output_csv):
    with open(input_json, 'r') as f:
        data = json.load(f)

    feature_df = extract_wallet_features(data)
    score_df = score_wallets(feature_df)
    score_df.to_csv(output_csv, index=False)
    print(f"Scores saved to: {output_csv}")
