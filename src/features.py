from datetime import datetime

import pandas as pd


def extract_wallet_features(data):
    df = pd.DataFrame(data)

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s', errors='coerce')
    df = df[df['timestamp'].notna()]  # remove rows with invalid timestamp

    grouped = df.groupby('user')

    features = []

    for wallet, group in grouped:
        group = group.sort_values(by='timestamp')

        deposit_amt = group[group['type'] == 'deposit']['amount'].sum()
        borrow_amt = group[group['type'] == 'borrow']['amount'].sum()
        repay_amt = group[group['type'] == 'repay']['amount'].sum()
        liquidation_count = (group['type'] == 'liquidationcall').sum()
        tx_gap = group['timestamp'].diff().dt.total_seconds().mean()
        asset_count = group['reserve'].nunique()

        repay_ratio = repay_amt / borrow_amt if borrow_amt > 0 else 0

        features.append({
            'wallet': wallet,
            'total_deposit': deposit_amt,
            'total_borrow': borrow_amt,
            'total_repay': repay_amt,
            'repay_ratio': repay_ratio,
            'liquidation_count': liquidation_count,
            'avg_tx_gap': tx_gap or 0,
            'unique_assets': asset_count,
            'total_txs': len(group)
        })

    return pd.DataFrame(features)
