from fastapi import FastAPI
import uvicorn
from schemas import User_create

app=FastAPI()
 
@app.get("/")
async def welcome():
    return {"message":"Hello Word"}

@app.post("/create")
async def create_user(user:User_create):
    return user


if __name__ == "__main__":
    uvicorn.run("main:app", 
            host="localhost", reload=True)