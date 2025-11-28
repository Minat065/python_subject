"""
レッスン05: AIエージェント入門 - 練習問題

以下のクラスを実装してください。
"""

from dataclasses import dataclass


@dataclass
class Message:
    """
    チャットメッセージを表すデータクラス。

    Attributes:
        role: メッセージの役割（"system", "user", "assistant"のいずれか）
        content: メッセージの内容

    Example:
        >>> msg = Message(role="user", content="こんにちは")
        >>> msg.role
        'user'
        >>> msg.content
        'こんにちは'
    """

    role: str
    content: str


class ConversationMemory:
    """
    会話履歴を管理するクラス。

    Methods:
        add_message(message): メッセージを追加
        get_messages(): 全メッセージを取得
        clear(): 履歴をクリア

    Example:
        >>> memory = ConversationMemory()
        >>> memory.add_message(Message("user", "こんにちは"))
        >>> len(memory.get_messages())
        1
    """

    def __init__(self):
        # TODO: ここに実装を追加してください
        pass

    def add_message(self, message: Message) -> None:
        # TODO: ここに実装を追加してください
        pass

    def get_messages(self) -> list[Message]:
        # TODO: ここに実装を追加してください
        pass

    def clear(self) -> None:
        # TODO: ここに実装を追加してください
        pass


class SimpleAgent:
    """
    シンプルなAIエージェント。

    このクラスはLLMを使った会話エージェントの基本構造を表します。
    実際のLLM呼び出しはモック可能なメソッドとして実装します。

    Attributes:
        system_prompt: システムプロンプト
        memory: 会話履歴

    Methods:
        chat(user_message): ユーザーメッセージに応答

    Example:
        >>> agent = SimpleAgent("あなたは親切なアシスタントです。")
        >>> response = agent.chat("こんにちは")
    """

    def __init__(self, system_prompt: str):
        """
        SimpleAgentを初期化する。

        Args:
            system_prompt: エージェントの振る舞いを定義するシステムプロンプト
        """
        # TODO: ここに実装を追加してください
        pass

    def _call_llm(self, messages: list[Message]) -> str:
        """
        LLMを呼び出す（テスト時にモック可能）。

        Args:
            messages: 会話履歴

        Returns:
            LLMからの応答テキスト
        """
        # デフォルト実装: 簡単なエコー応答
        # 実際の実装では、OpenAI APIなどを呼び出す
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
        # TODO: ここに実装を追加してください
        # 1. ユーザーメッセージをメモリに追加
        # 2. _call_llmを呼び出して応答を取得
        # 3. アシスタントの応答をメモリに追加
        # 4. 応答を返す
        pass
