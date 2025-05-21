from unittest.mock import MagicMock, patch

from autoscripts_csv.poc.micro01_http.http_client import (
    extract_info,
    fetch_data,
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
        "autoscripts_csv.poc.micro01_http.http_client.requests.get",
        return_value=fake_response,
    ):
        result = fetch_data("https://dummy-url.com")

    assert result == {"title": "モックタスク", "id": 1}
