from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool=True
    
p_one= Product(id=1,name="laptop",price=99.99,in_stock=True)
p_two = Product(id=2,name="mouse",price=23.44)
print(p_one)
print(p_two)