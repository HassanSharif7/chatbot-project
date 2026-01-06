from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, AIMessage
from database import conversations
from graph import build_graph
import os

app = FastAPI(title="Chatbot API", version="1.0.0")

# Enable CORS for frontend deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chatbot = build_graph()

@app.get("/")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "Chatbot API is running"}

class ChatRequest(BaseModel):
    conversation_id: str
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    # 1. Load conversation from MongoDB
    doc = conversations.find_one({"conversation_id": req.conversation_id})

    messages = []
    if doc:
        for m in doc["messages"]:
            if m["role"] == "human":
                messages.append(HumanMessage(content=m["content"]))
            else:
                messages.append(AIMessage(content=m["content"]))

    # 2. Add new user message
    messages.append(HumanMessage(content=req.message))

    # 3. Run LangGraph
    result = chatbot.invoke({"messages": messages})
    ai_msg = result["messages"][-1]

    # 4. Save back to MongoDB
    stored_messages = []
    for m in result["messages"]:
        role = "human" if isinstance(m, HumanMessage) else "ai"
        stored_messages.append({
            "role": role,
            "content": m.content
        })

    conversations.update_one(
        {"conversation_id": req.conversation_id},
        {"$set": {"messages": stored_messages}},
        upsert=True
    )

    return {"response": ai_msg.content}
