'''===================
Part 1: Setup
==================='''
from sqlalchemy import create_engine, ForeignKey, String, Float, select, text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, relationship
from typing import List, Optional

# create engine
engine = create_engine('sqlite:///shop.db')
Session = sessionmaker(bind=engine)
session = Session()


'''===================
Part 2: Define Tables
==================='''
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
    
    # one-to-many 
    orders: Mapped[List['Order']] = relationship(back_populates="user") 
    
# Product Table
class Product(Base):
    __tablename__= 'products'
    
    # columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Float)
    
    # one-to-many
    products: Mapped[List['Order']] = relationship(back_populates="product") 

# Order Table

class Order(Base):
    __tablename__ = "orders"
    
    # columns
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id")) 
    quantity: Mapped[int] = mapped_column(default=1)
    status: Mapped[bool] = mapped_column(default=False)
    
    user: Mapped['User'] = relationship(back_populates="orders")
    product: Mapped['Product'] = relationship(back_populates="products") 


'''===================
Part 3: Create Tables
==================='''
Base.metadata.create_all(engine)
session.commit()

# ALTER Order table to have status column
with engine.connect() as conn:
    columns = [row[1] for row in conn.execute(text("PRAGMA table_info(orders)"))]
    if 'status' not in columns:
        conn.execute(text("ALTER TABLE orders ADD COLUMN status BOOLEAN DEFAULT 0"))
        conn.commit()
    

'''===================
Part 4: Insert Data
==================='''
# ADD users ---
# new_user = User(name='Karson', email='kh@gmail.com')
# session.add(new_user)
# session.commit() 
# lilly = User(name='Lilly', email='lillars@gmail.com')
# robin = User(name='Robin', email='rbird@gmail.com')
# baily = User(name='Baily', email='bail@email.com') 
# session.add_all([lilly, robin, baily])
# session.commit()

# ADD products ---
# jacket = Product(name='North Face - jacket', price=20.00)
# session.add(jacket)
# session.commit() 
# pants = Product(name='Carharrt - pants', price=80.00) 
# backpack = Product(name='Topo Designs - backpack', price=125.00)
# headphones = Product(name='Base - Headphones', price='200.53')
# session.add_all([pants, backpack, headphones]) 
# session.commit() 

# ADD orders ---
# new_order = Order(user_id=1, product_id=1, quantity=2)
# session.add(new_order)
# session.commit() 

# DELETE order ---
# order = session.get(Order, 2)
# session.delete(order)
# session.commit()


'''===================
Part 5: Queries
==================='''
# query for all users and print their info ---
query = select(User)
users = session.execute(query).scalars().all()

for user in users:
    print(f'Username: {user.name} | emal: {user.email}')


# query for all products and print name and price ---
query = select(Product)
products = session.execute(query).scalars().all()

for product in products:
    print(f'Product name: {product.name} | price: {product.price}')
    

# query for all orders showing users.name, product.nae, and quantitity --- 
query = select(Order)
orders = session.execute(query).scalars().all()

for order in orders:
    print(f'Order information for User: {order.user.name} | Product: {order.product.name} | Quantity: {order.quantity}')

# UPDATE a product's price ---
# product = session.get(Product, 1)
# product.price = 120.40
# session.commit()

# DELETE a user by ID ---
# user = session.get(User, 2)
# session.delete(user)
# session.commit()
    
'''===================
Part 6: Bonus
==================='''
# query all orders that arn't shipped
query = select(Order).where(Order.status == False)
unshipped_orders = session.execute(query).scalars().all()

for order in unshipped_orders:
    print(f'Unshipped order: | User: {order.user.name} | Product: {order.product.name} | Quantity: {order.quantity}')


# count the total number of order per user ---
query = select(User.name, func.count(Order.id)).join(Order).group_by(User.id)
order_counts = session.execute(query).all()

for name, count in order_counts:
    print(f'User: {name} | Total Order: {count}') 

    





