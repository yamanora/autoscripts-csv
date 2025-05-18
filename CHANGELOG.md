# CHANGELOG
## [0.2.2] - 2025-05-18

### Added
- `poc/micro01_http/http_to_clack_py` のテストを追加

### Changed
- Slackへの通知内容を変更

## [0.2.1] - 2025-05-17

### Added
- `poc/micro01_http/` を追加（GET→title抽出→Slack通知のPoCスクリプト）
  - 任意のURLにアクセスし、JSONから `title` を抽出してSlackに通知

## [0.2.0] - 2025-05-15
### Added
- `--output` オプションを実装（CLIの出力先指定が可能に）
- Slack通知機能を追加
- `main()` を含む CLI全体のテスト（正常系）を新規実装

### Changed
- coverage CIの対象パスを修正し、正しいレポートが出るように対応
- READMEの記述を整理し、構成を見直し

---

## [0.1.0] - 2025-05-06
### Added
- `--input`, `--filter`, `--drop` のCSV整形CLIを実装
- Poetry / pytest / pre-commit / GitHub Actions CI 導入
