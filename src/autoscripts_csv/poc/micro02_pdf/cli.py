import argparse
import sys
from pathlib import Path

from autoscripts_csv.poc.common.notify import post_to_slack
from autoscripts_csv.poc.micro02_pdf.extractor import extract_text_from_pdf


class CLIError(Exception):
    """CLIエラーを表すカスタム例外"""

    pass


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="autoscripts-csv", description="PDFファイルからテキストを抽出するCLI"
    )
    parser.add_argument(
        "--pdf", type=Path, required=True, help="文字列を抽出したいPDFのパス"
    )
    parser.add_argument("--output", type=Path, required=False, help="出力ファイル名")
    parser.add_argument(
        "--notify", action="store_true", help="Slackに通知を送るかどうか"
    )
    return parser


def run(args: argparse.Namespace) -> None:
    if not args.pdf.exists():
        raise CLIError(f"PDFファイルが見つかりません: {args.pdf}")

    data = extract_text_from_pdf(args.pdf)

    if args.notify:
        post_to_slack(data)

    if args.output:
        args.output.write_text(data, encoding="utf-8")
    else:
        print("抽出内容は以下です")
        print(data)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
        run(args)
        return 0
    except CLIError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
