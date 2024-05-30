#!/usr/bin/env python3 -m pytest

import os
import sys
import unittest

import pytest
from conftest import MOCK_OPEN_AI_API_KEY

from autogen import GroupChat, GroupChatManager
from autogen.agentchat.contrib.llamaindex_conversable_agent import LLamaIndexConversableAgent
from autogen.agentchat.conversable_agent import ConversableAgent

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from conftest import reason, skip_openai

skip_reasons = [reason]
try:
    from llama_index.core import Settings
    from llama_index.core.agent import ReActAgent
    from llama_index.core.agent.runner.base import AgentRunner
    from llama_index.core.chat_engine.types import AgentChatResponse
    from llama_index.embeddings.openai import OpenAIEmbedding
    from llama_index.llms.openai import OpenAI
except ImportError:
    skip_for_dependencies = True
    skip_reasons.append(f"dependency not installed: {ImportError.msg}")
else:
    skip_for_dependencies = False

openaiKey = os.environ.get("OPENAI_API_KEY", MOCK_OPEN_AI_API_KEY)

if openaiKey == MOCK_OPEN_AI_API_KEY:
    skip_reasons.append("openai key not found")
    skip_for_key = True
else:
    skip_for_key = False

skip = skip_openai or skip_for_dependencies or skip_for_key
skip_reason = ", ".join(skip_reasons)


@pytest.mark.skipif(skip, reason=skip_reason)
def test_group_chat_with_llama_index_conversable_agent() -> None:
    """
    Tests the group chat functionality with two MultimodalConversable Agents.
    Verifies that the chat is correctly limited by the max_round parameter.
    Each agent is set to describe an image in a unique style, but the chat should not exceed the specified max_rounds.
    """
    llm = OpenAI(
        model="gpt-4",
        temperature=0.0,
        api_key=openaiKey,
    )

    embed_model = OpenAIEmbedding(
        model="text-embedding-ada-002",
        temperature=0.0,
        api_key=openaiKey,
    )

    Settings.llm = llm
    Settings.embed_model = embed_model

    location_specialist = ReActAgent.from_tools(llm=llm, max_iterations=5)
    entertainent_specialist = ReActAgent.from_tools(llm=llm, max_iterations=5)

    # create an autogen agent using the react agent
    trip_assistant = LLamaIndexConversableAgent(
        "trip_specialist",
        llama_index_agent=location_specialist,
        system_message="You help customers finding more about places they would like to visit. You can use external resources to provide more details as you engage with the customer.",
        description="This agents helps customers discover locations to visit, things to do, and other details about a location. It can use external resources to provide more details. This agent helps in finding attractions, history and all that there si to know about a place",
    )

    # create an autogen agent using the react agent
    entertainent_assistant = LLamaIndexConversableAgent(
        "entertainent_specialist",
        llama_index_agent=entertainent_specialist,
        system_message="You help customer discovering entartainment opportunities.",
        description="This agents helps customers discovering entartainment opportunities like venues, musesms, and other places to visit. It can use external resources to provide more details. This agent helps in finding attractions, history and all that there si to know about a place",
    )

    llm_config = False
    max_round = 5

    user_proxy = ConversableAgent(
        "customer",
        description="This the customer trying to find information about Tokyo.",
        human_input_mode="NEVER",  # Options: 'ALWAYS' or 'NEVER'
    )

    group_chat = GroupChat(
        agents=[user_proxy, trip_assistant, entertainent_assistant],
        messages=[],
        max_round=100,
        send_introductions=False,
        speaker_selection_method="round_robin",
    )

    group_chat_manager = GroupChatManager(
        groupchat=group_chat,
        llm_config=llm_config,
    )

    # Initiating the group chat and observing the number of rounds
    user_proxy.initiate_chat(
        group_chat_manager,
        message="What can i find in Tokyo related to Hayao Miyazaki and its moveis like Spirited Away?.",
    )

    # Assertions to check if the number of rounds does not exceed max_round
    assert all(len(arr) <= max_round for arr in trip_assistant.values()), "Agent 1 exceeded max rounds"
    assert all(len(arr) <= max_round for arr in entertainent_assistant.values()), "Agent 2 exceeded max rounds"
    assert all(len(arr) <= max_round for arr in user_proxy._oai_messages.values()), "User proxy exceeded max rounds"


if __name__ == "__main__":
    """Runs this file's tests from the command line."""
    test_group_chat_with_llama_index_conversable_agent()
