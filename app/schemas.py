from pydantic import BaseModel


class Create_user(BaseModel):
      name:str
      age:int
      status:bool

class Response_user(BaseModel):
    user_id:int
    class Config:
        from_attributes=True


