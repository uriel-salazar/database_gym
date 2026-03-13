from pydantic import BaseModel


class User_create(BaseModel):
      name:str
      age:int

class User_response(BaseModel):
    id:int
    name:str
    age:int
    
    class Config:
        from_attributes=True


