
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
 
 
class Product(Base):
    __tablename__ = "products"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    category = Column(String(100), nullable=False)   # e.g. "Electronics", "Clothing", "Books"
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
 
    orders = relationship("Order", back_populates="product")
 
 
class Customer(Base):
    __tablename__ = "customers"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    address = Column(String(255), nullable=True)
    phone = Column(String(20), nullable=True)
 
    orders = relationship("Order", back_populates="customer")
 
 
class Order(Base):
    __tablename__ = "orders"
 
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    total_price = Column(Float, nullable=False)
    status = Column(String(30), nullable=False, default="pending")  # pending, shipped, delivered, cancelled
 
    customer = relationship("Customer", back_populates="orders")
    product = relationship("Product", back_populates="orders")
