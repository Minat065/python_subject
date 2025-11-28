"""
レッスン01のテスト
"""

import sys
from pathlib import Path

# exercisesディレクトリをパスに追加
sys.path.insert(
    0, str(Path(__file__).parent.parent / "lessons" / "01_python_basics" / "exercises")
)

from exercise_01 import greet, is_even, sum_list


class TestGreet:
    def test_greet_basic(self):
        assert greet("太郎") == "こんにちは、太郎さん！"

    def test_greet_different_name(self):
        assert greet("花子") == "こんにちは、花子さん！"

    def test_greet_english_name(self):
        assert greet("John") == "こんにちは、Johnさん！"


class TestIsEven:
    def test_is_even_with_even_number(self):
        assert is_even(4) is True

    def test_is_even_with_odd_number(self):
        assert is_even(7) is False

    def test_is_even_with_zero(self):
        assert is_even(0) is True

    def test_is_even_with_negative_even(self):
        assert is_even(-2) is True

    def test_is_even_with_negative_odd(self):
        assert is_even(-3) is False


class TestSumList:
    def test_sum_list_basic(self):
        assert sum_list([1, 2, 3, 4, 5]) == 15

    def test_sum_list_empty(self):
        assert sum_list([]) == 0

    def test_sum_list_single_element(self):
        assert sum_list([10]) == 10

    def test_sum_list_negative_numbers(self):
        assert sum_list([-1, -2, -3]) == -6

    def test_sum_list_mixed_numbers(self):
        assert sum_list([1, -1, 2, -2]) == 0
