from typing import List,Optional
from pydantic import BaseModel

class Address(BaseModel):
    street:str
    city:str
    postal_code:str
    
    
class User(BaseModel):
    id:int
    name:str
    address:Address
    
    
address = Address(
    street="123 something ",
    city="allahabad",
    postal_code=21109
)

user = User(
    id=1,
    name="turab",
    address=address
)