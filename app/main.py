from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from sqlalchemy.orm import Session
from fastapi import HTTPException,Depends
from models import get_db,User
from crud import create_user
from schemas import User_Create,User_Response
from database import Base,engine


app=FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/",response_class=HTMLResponse)
async def welcome():
    return """<html>
        <body>
            <h1> Welcomee ! </h1>
        </body>
    </html>"""

@app.get("/users",response_model=User_Response)
async def read_users():
    pass

@app.get("/user/{user_id}",response_model=User_Response)
async def get_user(user_id:int,db:Session=Depends(get_db)):
      user=db.query(User).filter(User.user_id==user_id).first()
      if not user:
          HTTPException(status_code=404,detail="User not found :( ")
      return user
  

@app.post("/users",response_model=User_Response)
async def create(user_create:User_Create,db:Session=Depends(get_db)):
    return create_user(db,user_create)

if __name__ == "__main__":
    uvicorn.run("main:app", 
            host="localhost", reload=True)