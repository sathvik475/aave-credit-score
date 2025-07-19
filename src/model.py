import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def score_wallets(df):
    df.fillna(0, inplace=True)

    # Feature weights (tweak as needed)
    df['score_raw'] = (
        (df['repay_ratio'] * 0.4) +
        ((df['total_deposit'] / (df['total_borrow'] + 1)) * 0.2) +
        ((1 / (1 + df['liquidation_count'])) * 0.2) +
        ((df['unique_assets'] / 10) * 0.1) +
        ((df['total_txs'] / 1000) * 0.1)
    )

    scaler = MinMaxScaler(feature_range=(0, 1000))
    df['credit_score'] = scaler.fit_transform(df[['score_raw']])
    df['credit_score'] = df['credit_score'].round(2)
    return df[['wallet', 'credit_score']]
