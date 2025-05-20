import argparse
import sys
from pathlib import Path

from extractor import extract_text_from_pdf


def main():
    parser = argparse.ArgumentParser(
        prog="autoscripts-csv", description="PDFファイルからテキストを抽出するCLI"
    )

    parser.add_argument(
        "--pdf", type=Path, required=True, help="文字列を抽出したいPDFのパス"
    )

    args = parser.parse_args()

    if not args.pdf.exists():
        sys.exit(f"PDFファイルが見つかりません:{args.pdf}")

    data = extract_text_from_pdf(args.pdf)

    print("抽出内容は以下です")
    print(data)


if __name__ == "__main__":
    main()
