from sqlalchemy import create_engine,String,Float,Column,Integer
from sqlalchemy.orm import sessionmaker,relationship,Session,Mapped,mapped_column,declarative_base
from dotenv import load_dotenv
import os 

load_dotenv()

URL=os.getenv("DATABASE_URL")


engine = create_engine(URL, echo=True)