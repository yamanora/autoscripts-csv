import pandas as pd

from autoscripts_csv.core import drop


def test_drop_column():
    df = pd.DataFrame(
        {"担当": ["佐藤", "佐藤"], "実施": ["◯", "☓"], "備考": [" ", " "]}
    )
    dropped = drop.drop_column(df, "備考")
    assert "備考" not in dropped.columns
    assert list(dropped.columns) == ["担当", "実施"]


def test_drop_only_nonexistent_column():
    df = pd.DataFrame(
        {"担当": ["佐藤", "佐藤"], "実施": ["◯", "☓"], "備考": [" ", " "]}
    )
    dropped = drop.drop_column(df, "メモ")
    assert list(dropped.columns) == ["担当", "実施", "備考"]


def test_drop_exist_column():
    df = pd.DataFrame(
        {"担当": ["佐藤", "佐藤"], "実施": ["◯", "☓"], "備考": [" ", " "]}
    )
    dropped = drop.drop_column(df, ["備考", "メモ"])
    assert "備考" not in dropped.columns
    assert list(dropped.columns) == ["担当", "実施"]
