"""
レッスン02のテスト
"""

import sys
from pathlib import Path

exercises_path = Path(__file__).parent.parent / "lessons"
exercises_path = exercises_path / "02_functions_modules" / "exercises"
sys.path.insert(0, str(exercises_path))

from exercise_02 import (  # noqa: E402
    calculate_statistics,
    create_counter,
    format_message,
)


class TestCalculateStatistics:
    def test_calculate_statistics_basic(self):
        result = calculate_statistics([1, 2, 3, 4, 5])
        assert result["average"] == 3.0
        assert result["max"] == 5
        assert result["min"] == 1

    def test_calculate_statistics_single_element(self):
        result = calculate_statistics([10])
        assert result["average"] == 10.0
        assert result["max"] == 10
        assert result["min"] == 10

    def test_calculate_statistics_negative_numbers(self):
        result = calculate_statistics([-5, -3, -1])
        assert result["average"] == -3.0
        assert result["max"] == -1
        assert result["min"] == -5


class TestFormatMessage:
    def test_format_message_single_placeholder(self):
        result = format_message("Hello, {name}!", name="World")
        assert result == "Hello, World!"

    def test_format_message_multiple_placeholders(self):
        result = format_message("{greeting}, {name}!", greeting="Hi", name="Alice")
        assert result == "Hi, Alice!"

    def test_format_message_no_placeholders(self):
        result = format_message("No placeholders here")
        assert result == "No placeholders here"


class TestCreateCounter:
    def test_create_counter_default_start(self):
        counter = create_counter()
        assert counter() == 1
        assert counter() == 2
        assert counter() == 3

    def test_create_counter_custom_start(self):
        counter = create_counter(10)
        assert counter() == 11
        assert counter() == 12

    def test_create_counter_independent(self):
        counter1 = create_counter(0)
        counter2 = create_counter(100)
        assert counter1() == 1
        assert counter2() == 101
        assert counter1() == 2
        assert counter2() == 102
