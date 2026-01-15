from pydantic import BaseModel,field_validator,model_validator

class User(BaseModel):
    username:str
    @field_validator('username')
    def username_length(cls,v):
        if len(v)<4:
            raise ValueError("username must be atleast 4 chars")
        return v
     
    
class SignupData(BaseModel):
    password:str
    confirm_password:str
    @model_validator(mode='after')
    def password(cls,values):
        if values.password!= values.confirm_password:
            raise ValueError("password dont match")
        return values
    
        
        