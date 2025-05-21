import argparse
import sys
from pathlib import Path

from extractor import extract_text_from_pdf

from autoscripts_csv.poc.common.notify import post_to_slack


def main():
    parser = argparse.ArgumentParser(
        prog="autoscripts-csv", description="PDFファイルからテキストを抽出するCLI"
    )

    parser.add_argument(
        "--pdf", type=Path, required=True, help="文字列を抽出したいPDFのパス"
    )
    parser.add_argument(
        "--notify", action="store_true", help="Slackに通知を送るかどうか"
    )

    args = parser.parse_args()

    if not args.pdf.exists():
        sys.exit(f"PDFファイルが見つかりません:{args.pdf}")

    data = extract_text_from_pdf(args.pdf)

    if args.notify:
        post_to_slack(data)

    print("抽出内容は以下です")
    print(data)


if __name__ == "__main__":
    main()
