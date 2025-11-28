"""
レッスン03のテスト
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "lessons" / "03_object_oriented" / "exercises"),
)

from exercise_03 import BankAccount, SavingsAccount


class TestBankAccount:
    def test_bank_account_creation(self):
        account = BankAccount("田中太郎")
        assert account.owner == "田中太郎"
        assert account.get_balance() == 0

    def test_bank_account_deposit(self):
        account = BankAccount("田中太郎")
        account.deposit(10000)
        assert account.get_balance() == 10000

    def test_bank_account_withdraw(self):
        account = BankAccount("田中太郎")
        account.deposit(10000)
        account.withdraw(3000)
        assert account.get_balance() == 7000

    def test_bank_account_withdraw_insufficient_funds(self):
        account = BankAccount("田中太郎")
        account.deposit(1000)
        with pytest.raises(ValueError):
            account.withdraw(2000)

    def test_bank_account_multiple_transactions(self):
        account = BankAccount("田中太郎")
        account.deposit(5000)
        account.deposit(3000)
        account.withdraw(2000)
        assert account.get_balance() == 6000


class TestSavingsAccount:
    def test_savings_account_creation(self):
        savings = SavingsAccount("田中太郎", 0.05)
        assert savings.owner == "田中太郎"
        assert savings.interest_rate == 0.05

    def test_savings_account_add_interest(self):
        savings = SavingsAccount("田中太郎", 0.05)
        savings.deposit(10000)
        savings.add_interest()
        assert savings.get_balance() == 10500

    def test_savings_account_inherits_deposit_withdraw(self):
        savings = SavingsAccount("田中太郎", 0.01)
        savings.deposit(5000)
        savings.withdraw(1000)
        assert savings.get_balance() == 4000
