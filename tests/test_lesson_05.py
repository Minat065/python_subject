"""
レッスン05のテスト
"""

import sys
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).parent.parent / "lessons" / "05_ai_agent_intro" / "exercises")
)

from exercise_05 import ConversationMemory, Message, SimpleAgent


class TestMessage:
    def test_message_creation(self):
        msg = Message(role="user", content="こんにちは")
        assert msg.role == "user"
        assert msg.content == "こんにちは"

    def test_message_roles(self):
        system_msg = Message(role="system", content="あなたはアシスタントです")
        user_msg = Message(role="user", content="質問")
        assistant_msg = Message(role="assistant", content="回答")

        assert system_msg.role == "system"
        assert user_msg.role == "user"
        assert assistant_msg.role == "assistant"


class TestConversationMemory:
    def test_conversation_memory_init(self):
        memory = ConversationMemory()
        assert len(memory.get_messages()) == 0

    def test_conversation_memory_add_message(self):
        memory = ConversationMemory()
        memory.add_message(Message("user", "こんにちは"))
        assert len(memory.get_messages()) == 1

    def test_conversation_memory_get_messages(self):
        memory = ConversationMemory()
        msg1 = Message("user", "質問1")
        msg2 = Message("assistant", "回答1")
        memory.add_message(msg1)
        memory.add_message(msg2)

        messages = memory.get_messages()
        assert len(messages) == 2
        assert messages[0].content == "質問1"
        assert messages[1].content == "回答1"

    def test_conversation_memory_clear(self):
        memory = ConversationMemory()
        memory.add_message(Message("user", "テスト"))
        memory.clear()
        assert len(memory.get_messages()) == 0


class TestSimpleAgent:
    def test_simple_agent_init(self):
        agent = SimpleAgent("あなたは親切なアシスタントです。")
        assert agent.system_prompt == "あなたは親切なアシスタントです。"

    def test_simple_agent_chat(self):
        agent = SimpleAgent("あなたは親切なアシスタントです。")
        response = agent.chat("こんにちは")

        # 応答が返されることを確認
        assert response is not None
        assert isinstance(response, str)
        assert len(response) > 0

    def test_simple_agent_memory_updated(self):
        agent = SimpleAgent("テスト用プロンプト")
        agent.chat("最初のメッセージ")

        # メモリにメッセージが追加されていることを確認
        messages = agent.memory.get_messages()
        assert len(messages) >= 2  # システム + ユーザー + アシスタント
