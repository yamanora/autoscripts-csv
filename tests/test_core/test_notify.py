import os
from unittest.mock import patch

import pytest
import requests

from autoscripts_csv.core.notify import notify_slack


def test_notify_slack_success():
    with patch("autoscripts_csv.core.notify.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.raise_for_status.return_value = None

        with patch.dict(os.environ, {"SLACK_WEBHOOK_URL": "http://dummy-url"}):
            notify_slack("テストメッセージ")

        mock_post.assert_called_once_with(
            "http://dummy-url", json={"text": "テストメッセージ"}
        )


def test_notify_slack_missing_env():
    with (
        patch.dict(os.environ, {}, clear=True),
        pytest.raises(RuntimeError, match="SLACK_WEBHOOK_URL"),
    ):
        notify_slack("テストメッセージ")


def test_notify_slack_post_failure():
    with patch("autoscripts_csv.core.notify.requests.post") as mock_post:
        mock_post.side_effect = requests.RequestException("接続エラー")

        with patch.dict(os.environ, {"SLACK_WEBHOOK_URL": "http://dummy-url"}):
            notify_slack("失敗ケース")

        mock_post.assert_called_once()
