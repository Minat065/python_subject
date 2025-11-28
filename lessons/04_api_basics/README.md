# レッスン04: APIの基礎

## 学習目標
- HTTPリクエストの基本を理解する
- requestsライブラリを使ってAPIを呼び出す
- JSONデータの処理を学ぶ

## 内容

### 1. HTTPリクエストの基本

```python
import requests

# GETリクエスト
response = requests.get("https://api.example.com/users")
data = response.json()

# POSTリクエスト
payload = {"name": "太郎", "age": 25}
response = requests.post("https://api.example.com/users", json=payload)
```

### 2. レスポンスの処理

```python
response = requests.get("https://api.example.com/users/1")

# ステータスコードの確認
if response.status_code == 200:
    user = response.json()
    print(f"ユーザー名: {user['name']}")
else:
    print(f"エラー: {response.status_code}")
```

### 3. エラーハンドリング

```python
try:
    response = requests.get("https://api.example.com/users/1", timeout=5)
    response.raise_for_status()  # ステータスコードが4xx/5xxの場合に例外発生
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"リクエストエラー: {e}")
```

## 課題

`exercises/exercise_04.py` を編集して、以下の機能を実装してください：

1. `ApiClient`: APIクライアントクラス
   - GETリクエスト機能
   - POSTリクエスト機能
   - エラーハンドリング

## 提出方法

1. `lesson04-あなたの名前` というブランチを作成する
2. `exercises/exercise_04.py` を実装する
3. プルリクエストを作成する
