from dataclasses import dataclass
from typing import Protocol, List
from pathlib import Path

from ..tools import Tool


@dataclass
class User:

    name: str
    bio: str
    preferences: str


@dataclass
class ChatMessage:

    id: int
    root_id: int
    role: str
    content: str
    timestamp: int


@dataclass
class ChatHistory:

    root_id: int
    messages: List[ChatMessage]


class DatabaseManager(Protocol):

    async def initialize(self) -> None:
        pass

    async def reset(self) -> None:
        pass

    async def get_chat_history(self) -> ChatHistory:
        pass

    async def get_chat_message(self, root_id: int, id: int) -> ChatMessage:
        pass

    async def set_chat_message(self, message: ChatMessage) -> None:
        pass

    async def clear_chat_history(self) -> None:
        pass

    async def get_user(self) -> User:
        pass

    async def set_user(self, user: User) -> None:
        pass

    async def get_tools(self) -> List[Tool]:
        pass

    async def get_tool_with_id(self, id: int) -> Tool:
        pass

    async def set_tool(self, tool: Tool) -> None:
        pass

    async def delete_tool(self, id: int) -> None:
        pass
