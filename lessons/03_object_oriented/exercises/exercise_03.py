"""
レッスン03: オブジェクト指向プログラミング - 練習問題

以下のクラスを実装してください。
"""


class BankAccount:
    """
    銀行口座を表すクラス。

    Attributes:
        owner: 口座名義人
        balance: 残高（初期値: 0）

    Methods:
        deposit(amount): 入金する
        withdraw(amount): 出金する（残高不足の場合はValueError）
        get_balance(): 現在の残高を返す

    Example:
        >>> account = BankAccount("田中太郎")
        >>> account.deposit(10000)
        >>> account.get_balance()
        10000
        >>> account.withdraw(3000)
        >>> account.get_balance()
        7000
    """

    def __init__(self, owner: str):
        # TODO: ここに実装を追加してください
        pass

    def deposit(self, amount: int) -> None:
        # TODO: ここに実装を追加してください
        pass

    def withdraw(self, amount: int) -> None:
        # TODO: ここに実装を追加してください
        pass

    def get_balance(self) -> int:
        # TODO: ここに実装を追加してください
        pass


class SavingsAccount(BankAccount):
    """
    貯蓄口座を表すクラス（BankAccountを継承）。

    利息計算機能を持つ。

    Attributes:
        interest_rate: 年利（例: 0.01 = 1%）

    Methods:
        add_interest(): 利息を口座に追加する

    Example:
        >>> savings = SavingsAccount("田中太郎", 0.05)
        >>> savings.deposit(10000)
        >>> savings.add_interest()
        >>> savings.get_balance()
        10500
    """

    def __init__(self, owner: str, interest_rate: float):
        # TODO: ここに実装を追加してください
        pass

    def add_interest(self) -> None:
        # TODO: ここに実装を追加してください
        pass
