# tests/test_dummy.py
# NOTE: coverage/CI動作確認用のダミーテスト。
from autoscripts_csv.cli import main


def test_dummy():
    main()
    assert True
