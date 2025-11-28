"""
レッスン04: APIの基礎 - 練習問題

以下のクラスを実装してください。
"""

import requests  # noqa: F401


class ApiClient:
    """
    シンプルなAPIクライアントクラス。

    Attributes:
        base_url: APIのベースURL

    Methods:
        get(endpoint): GETリクエストを送信
        post(endpoint, data): POSTリクエストを送信

    Example:
        >>> client = ApiClient("https://api.example.com")
        >>> response = client.get("/users")
        >>> response = client.post("/users", {"name": "太郎"})
    """

    def __init__(self, base_url: str):
        """
        ApiClientを初期化する。

        Args:
            base_url: APIのベースURL（末尾のスラッシュなし）
        """
        # TODO: ここに実装を追加してください
        pass

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
        # TODO: ここに実装を追加してください
        pass

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
        # TODO: ここに実装を追加してください
        pass
