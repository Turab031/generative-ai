import os
from dotenv import load_dotenv
from groq import Groq
import json
import requests

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def get_Weather(city:str):
    url=f"https://wttr.in/{city.lower()}?format=%c+%t"
    response = requests.get(url)
    if response.status_code==200:
        return f"the weather in {city} is {response.text}"
    else:
        return "something went wrong"
        
    
def main():
    user_query = input(">")
    response = client.chat.completions.create(
    
        model="llama-3.1-8b-instant",
        messages=[
            {"role":"user","content":user_query}
        ]
        
    )
    print(f"🤖:{response.choices[0].message.content}")
    
# main()
print(get_Weather("delhi"))