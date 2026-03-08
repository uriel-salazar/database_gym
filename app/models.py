from sqlalchemy import Column, Integer, String,Float
from sqlalchemy.orm import mapped_column,Mapped,sessionmaker
from typing_extensions import Annotated
from database import Base,engine

template_name=Annotated[int,mapped_column(String(60),primary_key=True)]

class Client(Base):
    """_summary_

    Args:
        Base (_type_): This class inherits from the Declarative Base.
    """
    __tablename__='client'
    id:Mapped[int]= mapped_column(primary_key=True,nullable=False)
    username:Mapped[str] = mapped_column(nullable=True)
    age:Mapped[int]= mapped_column(nullable=True)



Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session_local=Session()