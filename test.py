from langchain_core.utils.uuid import uuid7
from agents import agent

# Configuration for this conversation thread
thread_id = str(uuid7())
config = {"configurable": {"thread_id": thread_id}}

# Ask for SQL query
result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": (
                    "Write a SQL query to find all customers "
                    "who made orders over $1000 in the last month."
                ),
            }
        ]
    },
    config=config,
)

# Print the conversation
"""for message in result["messages"]:
    if hasattr(message, "pretty_print"):
        message.pretty_print()
    else:
        print(f"{message.type}: {message.content}")"""

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(str(result))
