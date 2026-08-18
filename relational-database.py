from sqlalchemy import create_engine, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, relationship
from typing import List, Optional

# create engine
engine = create_engine('sqlite:///shop.db')
Session = sessionmaker(bind=engine)
session = Session()

# Base class for models
class Base(DeclarativeBase):
    pass

# User Table
class User(Base):
    __tablename__ = 'users'
    
    # columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False) 
    email: Mapped[str] = mapped_column(String(100), unique=True) 
    
# Product Table
class Product(Base):
    __tablename__= 'products'
    
    # columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[int] = mapped_column(String(10))

# Order Table

class Order(Base):
    __tablename__ = "orders"
    
    # columns
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = relationship(foreign_keys="users.id")
    product_id: Mapped[int] = relationship(foreign_keys="products.id")
    quantity: Mapped[int] = mapped_column(default=-0)
    
Base.metadata.create_all(engine)
# session.commit()
    
    





