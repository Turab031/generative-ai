import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

SYSTEM_PROMPT = """
 You're an expert AI assisten in resolving user queries using chain of thought.
 You work on START,PLAN and OUTPUT steps.
 You need to first PLAN what
 
 

"""
response = client.chat.completions.create(
    
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content":"" }
    ]
)