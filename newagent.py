# import os
# from dotenv import load_dotenv
# from groq import Groq
# import json
# import requests

# load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")
# client = Groq(api_key=api_key)



# def get_Weather(city:str):
#     url=f"https://wttr.in/{city.lower()}?format=%c+%t"
#     response = requests.get(url)
#     if response.status_code==200:
#         return f"the weather in {city} is {response.text}"
#     else:
#         return "something went wrong"
    
# available_tools ={
#     "get_weather":get_Weather
# }
   
# SYSTEM_PROMPT = """
#  You're an expert AI assisten in resolving user queries using chain of thought.
#  You work on START,PLAN and OUTPUT steps.
#  You need to first PLAN what needs to be done.The PLAN can be multiple steps.
#  Once you think enough PLAN has been done,finally you can give an OUTPUT.
#  You can also call a tool if required from the list of available tools.
#  For every tool call wait for the observer step which is the output from the called tool.
#  RULES:
#  -strictl Follow the given JSON format
#  -Only run one step at a time.
#  -The sequence of steps is START(where user gives an input),PLAN(That can 
#  be multiple times) and finally OUTPUT(which is going to be displayed to the 
#  user).
#  Output JSON Format:
#  {"step":"START"|"PLAN"|"OUTPUT"|"TOOL","content":"string","content":"string","tool":"string","input":"string"}
#  Available Tools:
#  -get_weather(city:str):takes city  name as an input string and returns the weather info about the city.
 
#  Example 1:
#  START:Hey,can you solve 2+3*5/10
#  PLAN:{"step":"PLAN":"content":"seems like user is interested in math problem"}
#  PLAN:{"steps":"PLAN":"content":"looking at the problem, we should solve using BODMAS method "}
#  PLAN:{"steps":"PLAN":"content":"Yes,The BODMAS is correct thing to be done here "}
#  PLAN:{"steps":"PLAN":"content":"First we multiply 3*5 which is 15"}
#  PLAN:{"steps":"PLAN":"content":"Now the new equation is 2+15/10 "}
#  PLAN:{"steps":"PLAN":"content":" We must perform divide that is 15/10=1.5 "}
#  PLAN:{"steps":"PLAN":"content":"Now the new equation is 2+1.5 "}
#  PLAN:{"steps":"PLAN":"content":"Now finally lets perform the addition  "}
#  PLAN:{"steps":"PLAN":"content":"Great,we have solved and left with 3.5 as ans "}
#  OUTPUT:{"steps":"OUTPUT":"content":"3.5 "}
 
#  Example 2:
#  START:What is weather of Delhi?
#  PLAN:{"step":"PLAN":"content":"seems like user is interested in getting weather in Delhi in India"}
#  PLAN:{"steps":"PLAN":"content":"Let's see if we have available tools from list of available tools. "}
#  PLAN:{"steps":"PLAN":"content":"Great,we have get_weather tool available for query "}
#  PLAN:{"steps":"PLAN":"content":"I need to call get_weather tool for Delhi as input for city"}
#  PLAN:{"steps":"TOOL": "TOOL":"get_weather" :"content":"Delhi  "}
#  PLAN:{"steps":"OBSERVER":"TOOL":"get_weather":"output":" The weather of Delhi is cloudy with 20 C"}
#  PLAN:{"steps":"PLAN":"content":"Great,I got weather info about Delhi"}
 
#  OUTPUT:{"steps":"OUTPUT":"content":"The current weather in Delhi is 20 C with cloudy sky "}
 
 
  
   
 
 
 

# """
# print("\n\n\n")

# message_history=[
#     {"role":"system","content":SYSTEM_PROMPT},
# ]
# user_query=input("👉🏻")
# message_history.append({"role":"user","content":user_query})
# while True:
#     response = client.chat.completions.create(
    
#         model="llama-3.1-8b-instant",
#         response_format={"type":"json_object"},
#         messages=message_history
#     )
    
#     raw_result = (response.choices[0].message.content)
#     message_history.append({"role":"assistant","content":raw_result}),
#     parsed_result = json.loads(raw_result)
#     if parsed_result.get("step")=="START":
#         print("🔥",parsed_result.get("content"))
#         continue
#     if parsed_result.get("step")=="TOOL":
#         tool_to_call = parsed_result.get("tool")
#         tool_input = parsed_result.get("input")
#         print(f"🔎:{tool_to_call}({tool_input})={tool_response}")
#         tool_response=available_tools[tool_to_call](tool_input)
#         message_history.append({"role":"developer","content":json.dumps(
#             {"step":"OBSERVE","tool":tool_to_call,"input":tool_input,"output":tool_response}
#         )})
#         continue
#     if parsed_result.get("step")=="PLAN":
        
#         print("🧠",parsed_result.get("content"))
        
#     if parsed_result.get("step")=="OUTPUT":
#         print("🤖",parsed_result.get("content"))
#         break
        
    
# print("\n\n\n")


import os
from dotenv import load_dotenv
from groq import Groq
import json
import requests

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)


def get_Weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%c+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"the weather in {city} is {response.text}"
    else:
        return "something went wrong"

available_tools = {
    "get_weather": get_Weather
}
   
SYSTEM_PROMPT = """
You're an expert AI assistant in resolving user queries using chain of thought.
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.
You can also call a tool if required from the list of available tools.
For every tool call wait for the OBSERVE step which is the output from the called tool.
RULES:
- strictly Follow the given JSON format
- Only run one step at a time.
- The sequence of steps is START (where user gives an input), PLAN (that can 
be multiple times), TOOL (when calling a tool), OBSERVE (tool output), and finally OUTPUT (which is going to be displayed to the user).
Output JSON Format:
{"step":"PLAN"|"TOOL"|"OUTPUT", "content":"string", "tool":"string", "input":"string"}
Available Tools:
- get_weather(city:str): takes city name as an input string and returns the weather info about the city.

Example 1:
START: Hey, can you solve 2+3*5/10
PLAN: {"step":"PLAN", "content":"seems like user is interested in math problem"}
PLAN: {"step":"PLAN", "content":"looking at the problem, we should solve using BODMAS method"}
PLAN: {"step":"PLAN", "content":"Yes, The BODMAS is correct thing to be done here"}
PLAN: {"step":"PLAN", "content":"First we multiply 3*5 which is 15"}
PLAN: {"step":"PLAN", "content":"Now the new equation is 2+15/10"}
PLAN: {"step":"PLAN", "content":"We must perform divide that is 15/10=1.5"}
PLAN: {"step":"PLAN", "content":"Now the new equation is 2+1.5"}
PLAN: {"step":"PLAN", "content":"Now finally lets perform the addition"}
PLAN: {"step":"PLAN", "content":"Great, we have solved and left with 3.5 as ans"}
OUTPUT: {"step":"OUTPUT", "content":"3.5"}

Example 2:
START: What is weather of Delhi?
PLAN: {"step":"PLAN", "content":"seems like user is interested in getting weather in Delhi in India"}
PLAN: {"step":"PLAN", "content":"Let's see if we have available tools from list of available tools"}
PLAN: {"step":"PLAN", "content":"Great, we have get_weather tool available for query"}
PLAN: {"step":"PLAN", "content":"I need to call get_weather tool for Delhi as input for city"}
TOOL: {"step":"TOOL", "tool":"get_weather", "input":"Delhi"}
(System will provide OBSERVE step with tool output)
PLAN: {"step":"PLAN", "content":"Great, I got weather info about Delhi"}
OUTPUT: {"step":"OUTPUT", "content":"The current weather in Delhi is 20 C with cloudy sky"}
"""

print("\n\n\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("👉🏻")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        response_format={"type": "json_object"},
        messages=message_history
    )
    
    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)
    
    step = parsed_result.get("step")
    
    if step == "START":
        print("🔥", parsed_result.get("content"))
        continue
    
    elif step == "TOOL":
        tool_to_call = parsed_result.get("tool")
        tool_input = parsed_result.get("input")
        tool_response = available_tools[tool_to_call](tool_input)
        print(f"🔎: {tool_to_call}({tool_input}) = {tool_response}")
        message_history.append({"role": "user", "content": json.dumps(
            {"step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response}
        )})
        continue
    
    elif step == "PLAN":
        print("🧠", parsed_result.get("content"))
        continue
    
    elif step == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break

print("\n\n\n")