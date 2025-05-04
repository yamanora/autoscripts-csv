# tests/test_dummy.py
# NOTE: coverage/CI動作確認用のダミーテスト。
from temp_repo.cli import main


def test_dummy():
    main()
    assert True
