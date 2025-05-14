import sys
from unittest.mock import patch

import pandas as pd

from autoscripts_csv.cli import main


def test_input_csv_loads_correctly(monkeypatch, tmp_path):
    input_path = tmp_path / "input.csv"
    input_path.write_text("担当,実施,備考\n佐藤,◯\n鈴木,☓\n佐藤,☓", encoding="utf-8")

    output_path = tmp_path / "output.csv"

    # 引数の差し替え
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "autoscripts-csv",
            "-i",
            str(input_path),
            "-o",
            str(output_path),
            "-f",
            "担当=佐藤",
            "-d",
            "備考",
        ],
    )

    main()

    df = pd.read_csv(output_path)
    assert list(df.columns) == ["担当", "実施"]
    assert len(df) == 2
    assert df.iloc[0]["担当"] == "佐藤"
    assert df.iloc[1]["実施"] == "☓"


def test_notify_called(monkeypatch, tmp_path):
    input_path = tmp_path / "input.csv"
    input_path.write_text("担当,実施\n佐藤,◯\n鈴木,☓", encoding="utf-8")

    output_path = tmp_path / "output.csv"

    # 引数の差し替え
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "autoscripts-csv",
            "-i",
            str(input_path),
            "-o",
            str(output_path),
            "-n",
            "呼び出し確認",
        ],
    )

    with patch("autoscripts_csv.core.notify.notify_slack") as mock_notify:
        main()
        mock_notify.assert_called_once_with("呼び出し確認")
