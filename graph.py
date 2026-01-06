from typing_extensions import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# Assume llm already created elsewhere
from llm import llm  

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

from langchain_core.messages import AIMessage

def chat_node(state):
    try:
        response = llm.invoke(state["messages"])
        return {"messages": [response]}
    except Exception as e:
        # Graceful fallback
        return {
            "messages": [
                AIMessage(
                    content=(
                        "⚠️ The AI model is temporarily unavailable "
                        "(API quota exceeded). Please try again later."
                    )
                )
            ]
        }


def build_graph():
    graph = StateGraph(ChatState)
    graph.add_node("chat", chat_node)
    graph.add_edge(START, "chat")
    graph.add_edge("chat", END)
    return graph.compile()
