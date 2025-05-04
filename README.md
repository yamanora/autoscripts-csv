# autoscripts-csv

![CI](https://github.com/yamanora/autoscripts-csv/actions/workflows/ci.yml/badge.svg)  
[![codecov](https://codecov.io/gh/yamanora/autoscripts-csv/branch/main/graph/badge.svg)](https://codecov.io/gh/yamanora/autoscripts_csv)

開発用Pythonテンプレート  
Poetry/pre-commit/pytest(+coverage) /CI

---

## セットアップ手順

```bash
poetry install --with dev
pre-commit install
```

---

## 使い方（例）

CLI モジュールが定義されている場合：

```bash
poetry run autoscripts-csv --help
```

---

## ファイル構成

```
autoscripts-csv/
├── src/
│   └── autoscripts_csv/          # パッケージ本体
│       ├── __init__.py
│       └── cli.py          # CLIのエントリーポイント
├── tests/                  # 単体テスト
│   └── test_dummy.py
├── .github/
│   └── workflows/
│       └── ci.yml          # CI設定
├── pyproject.toml
├── README.md
└── ...
```

---

処理構成のイメージ（Mermaid）：

```mermaid
flowchart TD
    A[cli.py] --> B[argparseで引数解析]
    B --> C[handler関数に分岐]
    C --> D1[format_csv]
    C --> D2[summarize_csv]
    D1 --> E1[出力ファイル保存]
    D2 --> E2[出力ファイル保存]
```
