"""
レッスン03: オブジェクト指向プログラミング - 解答例

注意: この解答は課題完了後に参照してください。
"""


class BankAccount:
    """
    銀行口座を表すクラス。

    Attributes:
        owner: 口座名義人
        balance: 残高（初期値: 0）
    """

    def __init__(self, owner: str):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount: int) -> None:
        """入金する"""
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        """出金する（残高不足の場合はValueError）"""
        if amount > self.balance:
            raise ValueError("残高不足です")
        self.balance -= amount

    def get_balance(self) -> int:
        """現在の残高を返す"""
        return self.balance


class SavingsAccount(BankAccount):
    """
    貯蓄口座を表すクラス（BankAccountを継承）。

    利息計算機能を持つ。

    Attributes:
        interest_rate: 年利（例: 0.01 = 1%）
    """

    def __init__(self, owner: str, interest_rate: float):
        super().__init__(owner)
        self.interest_rate = interest_rate

    def add_interest(self) -> None:
        """利息を口座に追加する"""
        interest = int(self.balance * self.interest_rate)
        self.balance += interest
