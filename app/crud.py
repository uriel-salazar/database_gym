from sqlalchemy.orm import Session
from models import User
from schemas import Create_user

def get_user(db:Session,user_id=User.user_id):
    return db.query(User).filter(User.user_id == user_id)


def create_user(db: Session,Create_user):
    db_user = User(name=Create_user.name, age=Create_user.age, status=Create_user.status)
    db.add(db_user) # adds the user to the table. 
    db.commit() # commits the database operations 
    db.refresh(db_user)
    return db_user # returns the created user. 