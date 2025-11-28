# レッスン05: AIエージェント入門

## 学習目標
- AIエージェントの基本概念を理解する
- OpenAI APIを使った基本的な実装を学ぶ
- プロンプトエンジニアリングの基礎を身につける

## 内容

### 1. AIエージェントとは

AIエージェントとは、与えられた目標を達成するために自律的に行動するAIシステムです。
主な構成要素：
- **LLM（大規模言語モデル）**: 推論と意思決定の中核
- **ツール**: 外部システムとの連携機能
- **メモリ**: 会話履歴や学習内容の保持

### 2. OpenAI APIの基本

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "あなたは親切なアシスタントです。"},
        {"role": "user", "content": "こんにちは！"}
    ]
)

print(response.choices[0].message.content)
```

### 3. シンプルなエージェントの実装

```python
class SimpleAgent:
    def __init__(self, system_prompt: str):
        self.client = OpenAI()
        self.system_prompt = system_prompt
        self.messages = [{"role": "system", "content": system_prompt}]
    
    def chat(self, user_message: str) -> str:
        self.messages.append({"role": "user", "content": user_message})
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=self.messages
        )
        
        assistant_message = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
```

## 課題

`exercises/exercise_05.py` を編集して、以下のクラスを実装してください：

1. `Message`: メッセージを表すデータクラス
2. `ConversationMemory`: 会話履歴を管理するクラス
3. `SimpleAgent`: シンプルなAIエージェント（モック実装可）

注意: 実際のAPI呼び出しはテストではモックに置き換えられます。

## 提出方法

1. `lesson05-あなたの名前` というブランチを作成する
2. `exercises/exercise_05.py` を実装する
3. プルリクエストを作成する

## 次のステップ

このカリキュラムを完了したら、以下のトピックを学習することをお勧めします：
- Function Calling（ツール使用）
- RAG（検索拡張生成）
- マルチエージェントシステム
- LangChain/LlamaIndexなどのフレームワーク
