from sqlalchemy.orm import Session
from models import User
from schemas import Create_user,Response_user

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


def create_user(db: Session,Create_user):
    """ Creates a new user in the database with a  CRUD function. 

    Args:
        db (Session): Database session.
        Create_user (Create_user): An squema for creating an user from pydantic. 

    Returns:
        User: created and committed ORM object
    """
    db_user = User(name=Create_user.name, age=Create_user.age, status=Create_user.status)
    db.add(db_user) 
    db.commit() 
    db.refresh(db_user)
    return db_user 

def delete_user(db:Session,user_id=User.user_id):
    user=db.query(Response_user).filter(User.user_id==user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
