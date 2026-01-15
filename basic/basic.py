from pydantic import BaseModel  


class User(BaseModel):
    id:int
    name:str
    is_active:bool
    


ip_data={'id':101,'name':"turab",'is_active':True  }

user = User(**ip_data)

print(user) 
  