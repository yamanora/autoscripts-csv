# micro02_pdf

指定したPDFファイルから文字列を抽出し、標準出力に表示／Slackに通知するPoC用スクリプトです。

---

## 使い方（例）

```bash
# 標準出力に抽出結果を表示
poetry run python cli.py --pdf tests/fixtures/sample.pdf

# Slackにも通知する場合
poetry run python cli.py --pdf tests/fixtures/sample.pdf --notify
```

---

## 出力例

```
抽出内容は以下です
--- page 1 ---
Invoice
Total amount: 123,456 yen
```

Slackにも同じ内容を通知できます。

---

## 必要な環境変数（Slack通知）

プロジェクトルートに `.env` を作成し、以下を記述してください：

```
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
```

---

## 備考

- サンプルPDFは `tests/fixtures/sample.pdf` に含まれています。
- 英数字ベースのシンプルなPDFを対象に検証しています。
- PDFのレイアウトやフォントによっては抽出結果が変化する可能性があります。
