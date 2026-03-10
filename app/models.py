from sqlalchemy import Column, Integer, String,Float,ForeignKey,Date
from sqlalchemy.orm import mapped_column,Mapped,sessionmaker,relationship
from typing_extensions import Annotated
from database import Base,engine
from datetime import datetime

template_name=Annotated[int,mapped_column(String(60),nullable=True)]

class User(Base):
    """_summary_

    Args:
        Base (_type_): This class inherits from the Declarative Base.
    """
    __tablename__='user'
    user_id:Mapped[list['Membership']]=relationship('membership')
    name:Mapped[template_name]
    age:Mapped[int]= mapped_column(nullable=True)
    status:Mapped[bool]= mapped_column(nullable=True)


class Membership(Base):
    __tablename__='membership'
    id:Mapped[int]=mapped_column(primary_key=True)
    user_id:Mapped[int]=mapped_column(ForeignKey('user.user_id'))
    name:Mapped[template_name]
    start_date:Mapped[Date]=mapped_column(nullable=True)
    
    
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session_local=Session()