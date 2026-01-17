import os
from dotenv import load_dotenv
from groq import Groq
import requests

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return "Something went wrong while fetching weather."

# User input
user_query = input("> ")

# AI response
response = client.chat.completions.create(
    
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": user_query}
    ]
)

print("AI:", response.choices[0].message.content)

# Weather output
print(get_weather("Delhi"))
