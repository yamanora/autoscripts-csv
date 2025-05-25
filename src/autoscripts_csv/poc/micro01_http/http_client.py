import requests


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
