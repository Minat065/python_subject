"""
レッスン02: 関数とモジュール - 練習問題

以下の関数を実装してください。
"""


def calculate_statistics(numbers: list[int | float]) -> dict:
    """
    リストの統計情報を計算する。

    Args:
        numbers: 数値のリスト（空でないこと）

    Returns:
        以下のキーを持つ辞書:
        - "average": 平均値
        - "max": 最大値
        - "min": 最小値

    Example:
        >>> calculate_statistics([1, 2, 3, 4, 5])
        {'average': 3.0, 'max': 5, 'min': 1}
    """
    # TODO: ここに実装を追加してください
    pass


def format_message(template: str, **kwargs) -> str:
    """
    テンプレート文字列をキーワード引数でフォーマットする。

    Args:
        template: フォーマットする文字列テンプレート
        **kwargs: テンプレートに埋め込む値

    Returns:
        フォーマットされた文字列

    Example:
        >>> format_message("Hello, {name}!", name="World")
        'Hello, World!'
    """
    # TODO: ここに実装を追加してください
    pass


def create_counter(start: int = 0):
    """
    カウンター関数を返すクロージャ。

    Args:
        start: カウンターの初期値（デフォルト: 0）

    Returns:
        呼び出すたびにカウントを1増やして返す関数

    Example:
        >>> counter = create_counter(10)
        >>> counter()
        11
        >>> counter()
        12
    """
    # TODO: ここに実装を追加してください
    pass
