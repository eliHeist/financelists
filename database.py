from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()

class List(Base):
    __tablename__ = "lists"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    items = relationship("Item", back_populates="list", cascade="all, delete")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    list_id = Column(Integer, ForeignKey("lists.id"))
    name = Column(String, nullable=False)
    quantity = Column(Integer, default=1)
    amount = Column(Float, nullable=False)
    list = relationship("List", back_populates="items")

# Database Connection
engine = create_engine("sqlite:///lists.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
