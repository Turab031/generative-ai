import os
from dotenv import load_dotenv
from groq import Groq
import json

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

SYSTEM_PROMPT = """
 You're an expert AI assisten in resolving user queries using chain of thought.
 You work on START,PLAN and OUTPUT steps.
 You need to first PLAN what needs to be done.The PLAN can be multiple steps.
 Once you think enough PLAN has been done,finally you can give an OUTPUT.
 RULES:
 -strictl Follow the given JSON format
 -Only run one step at a time.
 -The sequence of steps is START(where user gives an input),PLAN(That can 
 be multiple times) nd finally OUTPUT(whic is going to be displayed to the 
 user).
 Output JSON Format:
 {"step":"START"|"PLAN"|"OUTPUT","content":"string"}
 Example:
 START:Hey,can you solve 2+3*5/10
 PLAN:{"step":"PLAN":"content":"seems like user is interested in math problem"}
 PLAN:{"steps":"PLAN":"content":"looking at the problem, we should solve using BODMAS method "}
 PLAN:{"steps":"PLAN":"content":"Yes,The BODMAS is correct thing to be done here "}
 PLAN:{"steps":"PLAN":"content":"First we multiply 3*5 which is 15"}
 PLAN:{"steps":"PLAN":"content":"Now the new equation is 2+15/10 "}
 PLAN:{"steps":"PLAN":"content":" We must perform divide that is 15/10=1.5 "}
 PLAN:{"steps":"PLAN":"content":"Now the new equation is 2+1.5 "}
 PLAN:{"steps":"PLAN":"content":"Now finally lets perform the addition  "}
 PLAN:{"steps":"PLAN":"content":"Great,we have solved and left with 3.5 as ans "}
 OUTPUT:{"steps":"OUTPUT":"content":"3.5 "}
 
 
  
   
 
 
 

"""

message_history=[
    {"role":"system","content":SYSTEM_PROMPT},
]
user_query=input("👉🏻")
message_history.append({"role":"user","content":user_query})
while True:
    response = client.chat.completions.create(
    
        model="llama-3.1-8b-instant",
        response_format={"type":"json_object"},
        messages=message_history
    )
    
    raw_result = (response.choices[0].message.content)
    message_history.append({"role":"assistant","content":raw_result}),
    parsed_result = json.loads(raw_result)
    if parsed_result.get("step")=="START":
        print("🔥",parsed_result.get("content"))
        continue
    
    if parsed_result.get("step")=="PLAN":
        print("🧠",parsed_result.get("content"))
        

response = client.chat.completions.create(
    
    model="llama-3.1-8b-instant",
    response_format={"type":"json_object"},
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role": "user", "content":"Hey,write a code to add n numbers in js" },
        {"role":"assistant","content":json.dumps({
            "step":"PLAN",
            "content":"We need to write a JavaScript function to add n numbers"
        })},
         {"role":"assistant","content":json.dumps({
            "step":"PLAN",
            "content": "The function will take an array of numbers as input, so the function declaration will be like addNumbers(arr) or simply add(arr)"
        })},
         
        {"role":"assistant","content":json.dumps({
            "step":"PLAN",
            "content": "We will use the reduce() method of the array to add all the numbers in it and return the result"
        })},
        
        {"role":"assistant","content":json.dumps({
            "step":"PLAN",
            "content": "Here's a sample JavaScript function: \nfunction add(arr) { \nreturn arr.reduce((total, number) => { return total + number; }); \n}"
        })},
         
         
         
        
    ] 
)

print(response.choices[0].message.content)