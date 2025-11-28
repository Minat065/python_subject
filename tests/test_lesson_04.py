"""
レッスン04のテスト
"""

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(
    0, str(Path(__file__).parent.parent / "lessons" / "04_api_basics" / "exercises")
)

from exercise_04 import ApiClient


class TestApiClient:
    def test_api_client_init(self):
        client = ApiClient("https://api.example.com")
        assert client.base_url == "https://api.example.com"

    @patch("exercise_04.requests.get")
    def test_api_client_get(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"data": "test"}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        client = ApiClient("https://api.example.com")
        result = client.get("/users")

        mock_get.assert_called_once()
        assert result == {"data": "test"}

    @patch("exercise_04.requests.post")
    def test_api_client_post(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": 1, "name": "太郎"}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        client = ApiClient("https://api.example.com")
        result = client.post("/users", {"name": "太郎"})

        mock_post.assert_called_once()
        assert result == {"id": 1, "name": "太郎"}

    @patch("exercise_04.requests.get")
    def test_api_client_get_with_params(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = [{"id": 1}]
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        client = ApiClient("https://api.example.com")
        result = client.get("/users", params={"page": 1})

        mock_get.assert_called_once()
        assert result == [{"id": 1}]
