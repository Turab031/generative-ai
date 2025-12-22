import os
from dotenv import load_dotenv
from sambanova import SambaNova

load_dotenv()

client = SambaNova(
    api_key=os.getenv("SAMBANOVA_API_KEY"),
    base_url="https://api.sambanova.ai/v1",
)

response = client.chat.completions.create(
    model="ALLaM-7B-Instruct-preview",
    messages=[
        {"role": "user", "content": "i am turab manzoor"},
        
    ],
    temperature=0.1,
    top_p=0.1
)

print(response.choices[0].message.content)
