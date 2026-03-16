from sqlalchemy.orm import Session
from models import User
from schemas import User_Create,User_Response

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

def get_users(db:Session,skip:int = 0, limit: int =10):
    """ We make a query to return a subset of user.
        The user can decide how many items are returned and 
        the returning results with "skip" """
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session,User_Create):
    """ Creates a new user in the database with a  CRUD function. 

    Args:
        db (Session): Database session.
        Create_user (Create_user): An squema for creating an user from pydantic. 

    Returns:
        User: created and committed ORM object
    """
    db_user = User(name=User_Create.name, age=User_Create.age)
    if db_user.age <=11:
        return None
    db.add(db_user) 
    db.commit() 
    db.refresh(db_user)
    return db_user 

def delete_user(db:Session,user_id=User.user_id):
    user=db.query(User_Response).filter(User.user_id==user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

def update_user(db: Session, user_id:int, user:User_Create):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user is None:
        return None
    
    db_user.name = user.name
    db_user.age = user.age
    db.commit()
    db.refresh(db_user)
        
    return db_user

        