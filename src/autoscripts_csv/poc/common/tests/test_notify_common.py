import os
from unittest.mock import patch

from autoscripts_csv.poc.common.notify import post_to_slack


def test_post_to_slack():
    with patch("autoscripts_csv.core.notify.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.raise_for_status.return_value = None

        with patch.dict(os.environ, {"SLACK_WEBHOOK_URL": "http://dummy-url"}):
            post_to_slack("テストメッセージ")

        mock_post.assert_called_once_with(
            "http://dummy-url", json={"text": "テストメッセージ"}
        )
