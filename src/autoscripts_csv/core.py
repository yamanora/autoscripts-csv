import pandas as pd


def filter_dataframe(df: pd.DataFrame, col: str, val: str) -> pd.DataFrame:
    if col not in df.columns:
        raise ValueError(f"列'{col}'が存在しません・")
    return df[df[col] == val]


def drop_column(df: pd.DataFrame, drop_cols: list):
    return df.drop(columns=drop_cols, errors="ignore")
