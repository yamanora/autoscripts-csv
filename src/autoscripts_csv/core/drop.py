import pandas as pd


def drop_column(df: pd.DataFrame, drop_cols: list):
    return df.drop(columns=drop_cols, errors="ignore")
