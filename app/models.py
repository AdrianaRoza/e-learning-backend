from sqlalchemy import Column, Integer, String, Float
from .database import Base


class Course(Base):
    __tablename__= "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    price = Column(Float, default=0.0)
    image = Column(String, nullable=True)