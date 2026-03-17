from pydantic import BaseModel,Field


class User_Create(BaseModel):
      """ Pydantic models for creating a new user

      Args:
          BaseModel (class): Generates a data model type with validation logic.
      """
      name:str 
      age:int =Field(..., gt=11,
      description="User must be older than 11")
      email:str
      
class User_Response(BaseModel):
      """ Returned information 

      Args:
          BaseModel (class): Generates a data model type with validation logic.
      """
      
      user_id:int 
      name:str
      age:int
      email:str
  
      class ConfigDict:
         from_attributes=True


      