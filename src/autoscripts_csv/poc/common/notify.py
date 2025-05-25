import os

import requests
from dotenv import load_dotenv

load_dotenv()


def post_to_slack(message: str) -> None:
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")

    if not webhook_url:
        raise RuntimeError(
            "[ERROR] Slack通知のWebhook URLが未設定です。"
            "'.env'にSLACK_WEBHOOK_URLを設定してください。"
        )

    payload = {"text": message}

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[Slack通知失敗]{e}")
