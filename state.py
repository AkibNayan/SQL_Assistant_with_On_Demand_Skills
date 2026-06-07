from langchain.agents.middleware import AgentState
from typing import NotRequired


class CustomState(AgentState):
    skills_loaded: NotRequired[str]  # Track which skills have been loaded  #
