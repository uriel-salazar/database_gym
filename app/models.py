from sqlalchemy import Integer, String,ForeignKey,DateTime
from sqlalchemy.orm import mapped_column,Mapped,sessionmaker,relationship
from typing_extensions import Annotated
from database import Base,engine
from datetime import datetime

name_blueprint = Annotated[str,mapped_column(String(60),nullable=False)]

class User(Base):
    """_summary_

    Args:
        Base (_type_): This class inherits from the Declarative Base.
    """
    __tablename__='user'
    
    user_id:Mapped[int]=mapped_column(primary_key=True) 
    name:Mapped[name_blueprint]
    age:Mapped[int]= mapped_column(nullable=False)
    status:Mapped[bool]= mapped_column(nullable=True)
    
    memberships:Mapped[list['Membership']]=relationship('Membership',back_populates='user')
    """An user can have many memberships; therefore it's a list, it's a relationship between 
    the membership table and this table."""
    
class Membership(Base):
    __tablename__='membership'
    id:Mapped[int]=mapped_column(primary_key=True)
    
    name:Mapped[name_blueprint]
    start_date:Mapped[datetime]=mapped_column(DateTime,nullable=False)
    user_id:Mapped[int]=mapped_column(ForeignKey('user.user_id'))
    
    user:Mapped['User']=relationship('User', back_populates='memberships')
    

Session=sessionmaker(bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()