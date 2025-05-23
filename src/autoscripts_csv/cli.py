import argparse

import pandas as pd

from autoscripts_csv.core import drop, filter, notify


def main():
    parser = argparse.ArgumentParser(
        prog="autoscripts-csv", description="Auto Scripts CLI Tool"
    )

    parser.add_argument("-i", "--input", required=True, help="入力ファイル名 (CSV)")
    parser.add_argument("-o", "--output", required=False, help="出力ファイル名 (CSV)")
    parser.add_argument(
        "-f", "--filter", required=False, help="フィルターをかける項目名 例:担当=佐藤"
    )
    parser.add_argument("-d", "--drop", required=False, help="消去する列名 例:備考")
    parser.add_argument("-n", "--notify", required=False, help="Slackに送る通知文")

    args = parser.parse_args()
    df = pd.read_csv(args.input)

    if args.filter:
        if "=" not in args.filter:
            raise ValueError("形式は'列=値にしてください'")
        else:
            parts = args.filter.split("=", 1)
            col, val = parts
            df = filter.filter_dataframe(df, col, val)

    if args.drop:
        drop_cols = args.drop.split(",")
        df = drop.drop_column(df, drop_cols)

    if args.notify:
        notify.notify_slack(args.notify)

    if args.output:
        df.to_csv(args.output, index=False)
    else:
        print(df.to_string(index=False))


if __name__ == "__main__":
    main()
