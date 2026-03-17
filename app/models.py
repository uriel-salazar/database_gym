from sqlalchemy import String,ForeignKey,DateTime
from sqlalchemy.orm import mapped_column,Mapped,sessionmaker,relationship
from typing_extensions import Annotated
from database import Base,engine
from datetime import datetime

name_blueprint = Annotated[str,mapped_column(String(60),nullable=False)]

class User(Base):
    """ User  table with basic information like name,age and an email.

    Args:
        Base (class): This class inherits from the Declarative Base.
    """
    __tablename__='user'
    
    user_id:Mapped[int]=mapped_column(primary_key=True) 
    name:Mapped[name_blueprint]
    age:Mapped[int]= mapped_column(nullable=False)
    email:Mapped[str] = mapped_column(unique=True,nullable=True)
    status:Mapped[bool]= mapped_column(nullable=True)
    
    memberships:Mapped[list['Membership']]=relationship('Membership',back_populates='user')
    """An user can have many memberships; therefore it's a list, it's a relationship between 
    the membership table and this table."""
    
class Membership(Base):
    """ Table Membership that has a relationship with User's table.
    It contains the date of the membership,type of membership and an users_id (FK)

    Args:
        Base (class): This class inherits from the Declarative Base.
    """
    __tablename__='membership'
    id:Mapped[int]=mapped_column(primary_key=True)
    
    name:Mapped[name_blueprint]
    start_date:Mapped[datetime]=mapped_column(DateTime,nullable=False)
    user_id:Mapped[int]=mapped_column(ForeignKey('user.user_id'))
    
    user:Mapped['User']=relationship('User', back_populates='memberships')
    

Session=sessionmaker(bind=engine)

def get_db():
    """ Creates a database's session. 

    Yields:
        db(_type_): _description_
    """
    db = Session()
    try:
        yield db
    finally:
        db.close()