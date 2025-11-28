"""
レッスン02: 関数とモジュール - 解答例

注意: この解答は課題完了後に参照してください。
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
    """
    return {
        "average": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers),
    }


def format_message(template: str, **kwargs) -> str:
    """
    テンプレート文字列をキーワード引数でフォーマットする。

    Args:
        template: フォーマットする文字列テンプレート
        **kwargs: テンプレートに埋め込む値

    Returns:
        フォーマットされた文字列
    """
    return template.format(**kwargs)


def create_counter(start: int = 0):
    """
    カウンター関数を返すクロージャ。

    Args:
        start: カウンターの初期値（デフォルト: 0）

    Returns:
        呼び出すたびにカウントを1増やして返す関数
    """
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter
