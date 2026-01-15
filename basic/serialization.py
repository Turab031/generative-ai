from pydantic import BaseModel,ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street:str
    city:str
    zip_code:str
    
class User(BaseModel):
    id:int
    name:str
    is_active:bool=True
    createdAt:datetime
    address:Address
    tags:List[str]=[]
    
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )




from datetime import datetime

user = User(
    id=1,
    name="turab",
    
    createdAt=datetime(2025, 3, 15, 14, 30),
    address=Address(
        street="prayag",
        city="allahabad",
        zip_code="211011"  
    ),
    is_active=False,
    tags=["premium", "subscribe"]
)


python_dict=user.model_dump()
print(user)

print("="*30)
print(python_dict)

json_Str=user.model_dump_json()
print("="*30)
print(json_Str)