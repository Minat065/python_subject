"""
レッスン01: Python基礎 - 解答例

注意: この解答は課題完了後に参照してください。
"""


def greet(name: str) -> str:
    """
    名前を受け取り、挨拶メッセージを返す。

    Args:
        name: 挨拶する相手の名前

    Returns:
        「こんにちは、{name}さん！」という形式の文字列
    """
    return f"こんにちは、{name}さん！"


def is_even(number: int) -> bool:
    """
    数値が偶数かどうかを判定する。

    Args:
        number: 判定する整数

    Returns:
        偶数ならTrue、奇数ならFalse
    """
    return number % 2 == 0


def sum_list(numbers: list[int]) -> int:
    """
    リストの合計値を計算する。

    Args:
        numbers: 整数のリスト

    Returns:
        リスト内の全ての整数の合計
    """
    return sum(numbers)
