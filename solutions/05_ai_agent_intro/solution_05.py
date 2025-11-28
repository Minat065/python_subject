"""
レッスン05: AIエージェント入門 - 解答例

注意: この解答は課題完了後に参照してください。
"""

from dataclasses import dataclass


@dataclass
class Message:
    """
    チャットメッセージを表すデータクラス。

    Attributes:
        role: メッセージの役割（"system", "user", "assistant"のいずれか）
        content: メッセージの内容
    """

    role: str
    content: str


class ConversationMemory:
    """
    会話履歴を管理するクラス。
    """

    def __init__(self):
        self._messages: list[Message] = []

    def add_message(self, message: Message) -> None:
        """メッセージを追加"""
        self._messages.append(message)

    def get_messages(self) -> list[Message]:
        """全メッセージを取得"""
        return self._messages.copy()

    def clear(self) -> None:
        """履歴をクリア"""
        self._messages = []


class SimpleAgent:
    """
    シンプルなAIエージェント。

    このクラスはLLMを使った会話エージェントの基本構造を表します。
    """

    def __init__(self, system_prompt: str):
        """
        SimpleAgentを初期化する。

        Args:
            system_prompt: エージェントの振る舞いを定義するシステムプロンプト
        """
        self.system_prompt = system_prompt
        self.memory = ConversationMemory()
        # システムプロンプトをメモリに追加
        self.memory.add_message(Message(role="system", content=system_prompt))

    def _call_llm(self, messages: list[Message]) -> str:
        """
        LLMを呼び出す（テスト時にモック可能）。

        Args:
            messages: 会話履歴

        Returns:
            LLMからの応答テキスト
        """
        # デフォルト実装: 簡単なエコー応答
        if messages:
            last_message = messages[-1]
            return f"「{last_message.content}」についてお答えします。"
        return "こんにちは！何かお手伝いできることはありますか？"

    def chat(self, user_message: str) -> str:
        """
        ユーザーメッセージに応答する。

        Args:
            user_message: ユーザーからのメッセージ

        Returns:
            エージェントからの応答
        """
        # 1. ユーザーメッセージをメモリに追加
        self.memory.add_message(Message(role="user", content=user_message))

        # 2. _call_llmを呼び出して応答を取得
        response = self._call_llm(self.memory.get_messages())

        # 3. アシスタントの応答をメモリに追加
        self.memory.add_message(Message(role="assistant", content=response))

        # 4. 応答を返す
        return response
