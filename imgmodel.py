import os
from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model='openai/gpt-oss-120b',
    messages=[
        # {"role":"user",
        #   "content":[
        #     {"type":"text","text":"generate a caption for this image in about 50 words"},
        #     {"type":"image_url","image_url":{"url":"https://images.pexels.com/photos/4164418/pexels-photo-4164418.jpeg"}}
        #   ]
        # }
        
        {
            "role": "user",
            "content": "Generate a caption for an image of a woman using a laptop"
        }
    ]
)
print("response",response.choices[0].message.content)
