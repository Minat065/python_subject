# レッスン02: 関数とモジュール

## 学習目標
- 関数の定義と呼び出しを理解する
- 引数とデフォルト引数を使いこなす
- モジュールのインポートと作成を学ぶ

## 内容

### 1. 関数の定義

```python
def calculate_area(width, height):
    """長方形の面積を計算する"""
    return width * height

# 関数の呼び出し
area = calculate_area(5, 3)
print(f"面積: {area}")  # 面積: 15
```

### 2. デフォルト引数

```python
def greet(name, greeting="こんにちは"):
    """挨拶をする関数"""
    return f"{greeting}、{name}さん！"

print(greet("太郎"))            # こんにちは、太郎さん！
print(greet("太郎", "おはよう"))  # おはよう、太郎さん！
```

### 3. 可変長引数

```python
def sum_all(*args):
    """全ての引数を合計する"""
    return sum(args)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
```

### 4. モジュールのインポート

```python
# 標準ライブラリのインポート
import math
print(math.sqrt(16))  # 4.0

# 特定の関数だけインポート
from math import pi, ceil
print(pi)       # 3.141592653589793
print(ceil(4.2))  # 5
```

## 課題

`exercises/exercise_02.py` を編集して、以下の機能を実装してください：

1. `calculate_statistics(numbers)`: リストの平均、最大値、最小値を辞書で返す関数
2. `format_message(template, **kwargs)`: テンプレート文字列をフォーマットする関数
3. `create_counter()`: カウンター関数を返すクロージャ

## 提出方法

1. `lesson02-あなたの名前` というブランチを作成する
2. `exercises/exercise_02.py` を実装する
3. プルリクエストを作成する
