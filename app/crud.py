from sqlalchemy.orm import Session
from models import User
from schemas import User_create,User_response

def get_user(db:Session,user_id=User.user_id):
    """ Gets an specific user by the user_id 

    Args:
        db (Session): Database's session
        user_id (User, int): User id of the table

    Returns:
        User: Searches for a row where user_id matches the user_id provided and 
        and we get the first result.
    """
    return db.query(User).filter(User.user_id == user_id).first()


def create_user(db: Session,User_create):
    """ Creates a new user in the database with a  CRUD function. 

    Args:
        db (Session): Database session.
        Create_user (Create_user): An squema for creating an user from pydantic. 

    Returns:
        User: created and committed ORM object
    """
    db_user = User(name=User_create.name, age=User_create.age)
    db.add(db_user) 
    db.commit() 
    db.refresh(db_user)
    return db_user 

def delete_user(db:Session,user_id=User.user_id):
    user=db.query(User_response).filter(User.user_id==user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
