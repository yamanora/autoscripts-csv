import pandas as pd
import pytest

from autoscripts_csv.core import filter


def test_filter_dataframe():
    df = pd.DataFrame(
        {
            "担当": ["佐藤", "田中", "佐藤"],
            "実施": ["◯", "☓", "◯"],
            "備考": [" ", " ", " "],
        }
    )
    filterd = filter.filter_dataframe(df, "担当", "佐藤")
    assert len(filterd) == 2
    assert all(filterd["担当"] == "佐藤")


def test_filter_invalid_columns():
    df = pd.DataFrame({"担当": ["佐藤"]})

    with pytest.raises(ValueError):
        filter.filter_dataframe(df, "操作", "佐藤")
