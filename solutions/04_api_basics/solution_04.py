"""
レッスン04: APIの基礎 - 解答例

注意: この解答は課題完了後に参照してください。
"""

import requests


class ApiClient:
    """
    シンプルなAPIクライアントクラス。

    Attributes:
        base_url: APIのベースURL
    """

    def __init__(self, base_url: str):
        """
        ApiClientを初期化する。

        Args:
            base_url: APIのベースURL（末尾のスラッシュなし）
        """
        self.base_url = base_url

    def get(self, endpoint: str, params: dict | None = None) -> dict:
        """
        GETリクエストを送信する。

        Args:
            endpoint: APIエンドポイント（例: "/users"）
            params: クエリパラメータ（オプション）

        Returns:
            レスポンスのJSONデータ

        Raises:
            Exception: リクエストが失敗した場合
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: dict) -> dict:
        """
        POSTリクエストを送信する。

        Args:
            endpoint: APIエンドポイント（例: "/users"）
            data: 送信するデータ

        Returns:
            レスポンスのJSONデータ

        Raises:
            Exception: リクエストが失敗した場合
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
