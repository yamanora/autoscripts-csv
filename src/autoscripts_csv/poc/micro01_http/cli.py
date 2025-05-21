import argparse

from autoscripts_csv.poc.common.notify import post_to_slack
from autoscripts_csv.poc.micro01_http.http_client import extract_info, fetch_data


def main():
    parser = argparse.ArgumentParser(
        prog="autoscripts-csv", description="Auto Scripts CLI Tool"
    )

    parser.add_argument("--url", required=True, help="情報を取得したいURL")

    args = parser.parse_args()

    data = fetch_data(args.url)

    title = extract_info(data)

    message = (
        f"新しいタスク取得:\n{title}\nID: {data.get('id', '不明')}\nURL: {args.url}"
    )

    print(message)
    post_to_slack(message)


if __name__ == "__main__":
    main()
