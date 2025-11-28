# レッスン01: Python基礎

## 学習目標
- Pythonの基本的な構文を理解する
- 変数、データ型、演算子を使えるようになる
- 条件分岐とループを理解する

## 内容

### 1. 変数とデータ型

```python
# 変数の宣言
name = "太郎"       # 文字列 (str)
age = 20            # 整数 (int)
height = 170.5      # 小数 (float)
is_student = True   # 真偽値 (bool)
```

### 2. 演算子

```python
# 算術演算子
a = 10
b = 3
print(a + b)   # 加算: 13
print(a - b)   # 減算: 7
print(a * b)   # 乗算: 30
print(a / b)   # 除算: 3.333...
print(a // b)  # 整数除算: 3
print(a % b)   # 剰余: 1
print(a ** b)  # 累乗: 1000
```

### 3. 条件分岐

```python
score = 75

if score >= 80:
    print("優秀です！")
elif score >= 60:
    print("合格です")
else:
    print("もう少し頑張りましょう")
```

### 4. ループ

```python
# for ループ
for i in range(5):
    print(i)

# while ループ
count = 0
while count < 5:
    print(count)
    count += 1
```

## 課題

`exercises/exercise_01.py` を編集して、以下の機能を実装してください：

1. `greet(name)`: 名前を受け取り、挨拶メッセージを返す関数
2. `is_even(number)`: 数値が偶数かどうかを判定する関数
3. `sum_list(numbers)`: リストの合計値を計算する関数

## 提出方法

1. このリポジトリをフォークまたはクローンする
2. `lesson01-あなたの名前` というブランチを作成する
3. `exercises/exercise_01.py` を実装する
4. プルリクエストを作成する

自動テストに合格すれば課題完了です！
