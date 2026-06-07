from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from models import model
from middleware import SkillMiddleware


# Create the agent with skill support
agent = create_agent(
   model=model,
   system_prompt=(
       "You are a SQL query assistant that helps users "
       "write SQL queries against business databases."
   ),
   middleware=[SkillMiddleware()],
   checkpointer=InMemorySaver()
)
