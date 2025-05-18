# micro01_http

任意のURLにGETリクエストを送り、取得したJSONから `title` を抽出し、Slackに通知するPoC用スクリプトです。  

---

## 使い方（例）

```bash
poetry run python cli.py --url https://jsonplaceholder.typicode.com/todos/1
```

---

## 出力例

```
新しいタスク取得:
delectus aut autem
ID: 1
URL: https://jsonplaceholder.typicode.com/todos/1
```

Slackにも同様の内容で通知できます。

---

## 必要な環境変数（Slack通知）

プロジェクトルートに `.env` を作成し、以下を記述してください：

```
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
```

