from sqlalchemy import create_engine,String,Float,Column,Integer
from sqlalchemy.orm import sessionmaker,relationship,Session,Mapped,mapped_column,declarative_base,DeclarativeBase
from dotenv import load_dotenv
import os 

load_dotenv()

URL=os.getenv("DATABASE_URL")

engine = create_engine(URL, echo=True)


class Base(DeclarativeBase):
    pass

class Client(Base):
    __tablename__='client'
    name:Mapped[str]=mapped_column(primary_key=True,nullable=False)
    


Base.metadata.create_all(engine) 
Session=sessionmaker(bind=engine)
session_local=Session()