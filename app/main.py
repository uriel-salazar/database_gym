from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from sqlalchemy.orm import Session
from fastapi import HTTPException,Depends
from models import get_db,User
import crud
#from crud import create_user,get_users,update_user
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

@app.get("/users",response_model = list[User_Response]) 
async def read_users(skip: int= 0, limit :int = 10,
    db:Session = Depends(get_db)):
    return crud.get_users(db ,skip=skip,limit=limit)
    


@app.get("/user/{user_id}",response_model=User_Response)
async def read_user(user_id:int,db: Session = Depends(get_db)):
      user = db.query(User).filter(User.user_id==user_id).first()
      if not user:
          raise HTTPException(status_code=404,detail="User not found :( ")
      return user
  

@app.post("/users",response_model=User_Response,status_code=201)
async def create(user_create:User_Create,db:Session=Depends(get_db)):
    if user_create.age  <= 11:
        raise HTTPException(status_code=403,detail="You're too young")
    
    return crud.create_user(db,user_create)


@app.put("/users/{user_id}",response_model=User_Response)
async def update_user(user_id:int, user_update:User_Create,db: Session = Depends(get_db)):    
    update = crud.update_user(db,user_id,user_update)
    if update is None:
        raise HTTPException(status_code=404,detail='User not found')
    if  update.age <=11:
       raise HTTPException(status_code=403,detail="You're too young")
    return update


@app.delete("/users/{users_id}",response_model=User_Response,status_code=200)
async def delete_user(user_id :int, db:Session = Depends(get_db)):
    delete = crud.delete_user(db,user_id)
    if delete is None:
        raise HTTPException(status_code=404,detail='User not found')
    return delete
    
    
if __name__ == "__main__":
    uvicorn.run("main:app", 
            host="localhost", reload=True)