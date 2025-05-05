import pandas as pd
import pytest

from autoscripts_csv import core


def test_filter_dataframe():
    df = pd.DataFrame(
        {
            "担当": ["佐藤", "田中", "佐藤"],
            "実施": ["◯", "☓", "◯"],
            "備考": [" ", " ", " "],
        }
    )
    filterd = core.filter_dataframe(df, "担当", "佐藤")
    assert len(filterd) == 2
    assert all(filterd["担当"] == "佐藤")


def test_filter_invalid_columns():
    df = pd.DataFrame({"担当": ["佐藤"]})

    with pytest.raises(ValueError):
        core.filter_dataframe(df, "操作", "佐藤")


def test_drop_column():
    df = pd.DataFrame(
        {"担当": ["佐藤", "佐藤"], "実施": ["◯", "☓"], "備考": [" ", " "]}
    )
    dropped = core.drop_column(df, "備考")
    assert "備考" not in dropped.columns
    assert list(dropped.columns) == ["担当", "実施"]


def test_drop_only_nonexistent_column():
    df = pd.DataFrame(
        {"担当": ["佐藤", "佐藤"], "実施": ["◯", "☓"], "備考": [" ", " "]}
    )
    dropped = core.drop_column(df, "メモ")
    assert list(dropped.columns) == ["担当", "実施", "備考"]


def test_drop_exist_column():
    df = pd.DataFrame(
        {"担当": ["佐藤", "佐藤"], "実施": ["◯", "☓"], "備考": [" ", " "]}
    )
    dropped = core.drop_column(df, ["備考", "メモ"])
    assert "備考" not in dropped.columns
    assert list(dropped.columns) == ["担当", "実施"]
