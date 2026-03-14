from fastapi import FastAPI
import uvicorn
from sqlalchemy.orm import Session
from fastapi import HTTPException,Depends
from models import get_db
from crud import create_user
from schemas import User_Create,User_Response
from database import Base,engine

app=FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/")
async def welcome():
    return {"message":"Hello Word"}

@app.post("/create",response_model=User_Response)
async def create(user_create:User_Create,db:Session=Depends(get_db)):
    return create_user(db,user_create)


if __name__ == "__main__":
    uvicorn.run("main:app", 
            host="localhost", reload=True)