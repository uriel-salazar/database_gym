from pydantic import BaseModel,Field


class User_Create(BaseModel):
      name:str 
      age:int =Field(..., gt=11,
      description="User must be older than 11")
      
class User_Response(BaseModel):
      # I forgot to write the exact name of the column from the user's table. 
    user_id:int 
    name:str
    age:int
  
    class ConfigDict:
         from_attributes=True


      