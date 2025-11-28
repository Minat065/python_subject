# レッスン03: オブジェクト指向プログラミング

## 学習目標
- クラスとオブジェクトの概念を理解する
- 継承とポリモーフィズムを学ぶ
- 特殊メソッドを活用する

## 内容

### 1. クラスの定義

```python
class Person:
    """人を表すクラス"""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def greet(self) -> str:
        return f"こんにちは、{self.name}です。{self.age}歳です。"

# インスタンスの作成
person = Person("太郎", 25)
print(person.greet())
```

### 2. 継承

```python
class Student(Person):
    """学生を表すクラス（Personを継承）"""
    
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id
    
    def greet(self) -> str:
        base_greeting = super().greet()
        return f"{base_greeting} 学生番号は{self.student_id}です。"
```

### 3. 特殊メソッド

```python
class Vector:
    """2次元ベクトルを表すクラス"""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

## 課題

`exercises/exercise_03.py` を編集して、以下のクラスを実装してください：

1. `BankAccount`: 銀行口座を表すクラス
2. `SavingsAccount`: 貯蓄口座（BankAccountを継承、利息計算機能付き）

## 提出方法

1. `lesson03-あなたの名前` というブランチを作成する
2. `exercises/exercise_03.py` を実装する
3. プルリクエストを作成する
