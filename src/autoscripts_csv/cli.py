# autoscripts-csv/cli.py

import argparse

import pandas as pd

from autoscripts_csv import core


def main():
    parser = argparse.ArgumentParser(
        prog="autoscripts-csv", description="Auto Scripts CLI Tool"
    )

    parser.add_argument("-i", "--input", required=True, help="入力ファイル名 (CSV)")
    parser.add_argument(
        "--f", "--filter", required=False, help="フィルターをかける項目名 例:担当=佐藤"
    )
    parser.add_argument("--d", "--drop", required=False, help="消去する列名 例:備考")
    parser.add_argument("--n", "--notify", required=False, help="Slackに送る通知文")

    args = parser.parse_args()
    df = pd.read_csv(args.input)

    if args.f:
        if "=" not in args.f:
            raise ValueError("形式は'列=値にしてください'")
        else:
            parts = args.f.split("=", 1)
            col, val = parts
            df = core.filter_dataframe(df, col, val)

    if args.d:
        drop_cols = args.d.split(",")
        df = core.drop_column(df, drop_cols)

    if args.n:
        core.notify_slack(args.n)

    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
