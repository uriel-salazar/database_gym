from sqlalchemy.orm import Session
from models import User

def get_user(db:Session,user_id=User.user_id):
    return db.query(User).filter(User.user_id == user_id)


def create_user(db:Session):
    pass



