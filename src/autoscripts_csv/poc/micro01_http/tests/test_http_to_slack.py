import os
from unittest.mock import MagicMock, patch

from autoscripts_csv.poc.micro01_http.http_to_slack import (
    extract_info,
    fetch_data,
    post_to_slack,
)


def test_extract_info():
    input_data = {
        "userId": "1",
        "id": "1",
        "title": "delectus aut autem",
        "completed": "false",
    }

    result = extract_info(input_data)

    assert result == "delectus aut autem"


def test_fetch_data_success():
    fake_response = MagicMock()
    fake_response.raise_for_status.return_value = None
    fake_response.json.return_value = {"title": "モックタスク", "id": 1}

    with patch(
        "autoscripts_csv.poc.micro01_http.http_to_slack.requests.get",
        return_value=fake_response,
    ):
        result = fetch_data("https://dummy-url.com")

    assert result == {"title": "モックタスク", "id": 1}


def test_post_to_slack():
    with patch("autoscripts_csv.core.notify.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.raise_for_status.return_value = None

        with patch.dict(os.environ, {"SLACK_WEBHOOK_URL": "http://dummy-url"}):
            post_to_slack("テストメッセージ")

        mock_post.assert_called_once_with(
            "http://dummy-url", json={"text": "テストメッセージ"}
        )
