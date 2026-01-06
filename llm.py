from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Set your API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY", "AIzaSyDw_gWd3Fs2OMlYwDieY1nb5cTUSzHv9OY")
os.environ["GOOGLE_API_KEY"] = api_key

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0.3,
    max_retries=3  # Retry up to 3 times on quota exceeded errors
)
