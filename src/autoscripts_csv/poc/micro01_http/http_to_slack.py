import os

import requests
from dotenv import load_dotenv

load_dotenv()


def fetch_data(url: str) -> dict:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"[ERROR] リクエスト失敗: {e}")
        raise


def extract_info(data: dict) -> str:
    return data.get("title", "タイトル取得失敗")


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
