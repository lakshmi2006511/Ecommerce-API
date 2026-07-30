 
from pydantic import BaseModel
from typing import Optional
 
 
# ---------- Product ----------
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    category: str
    price: float
    stock: int
 
class ProductResponse(ProductCreate):
    id: int
 
    model_config = {
        "from_attributes": True
    }
 
 
# ---------- Customer ----------
class CustomerCreate(BaseModel):
    name: str
    email: str
    address: Optional[str] = None
    phone: Optional[str] = None
 
class CustomerResponse(CustomerCreate):
    id: int
 
    model_config = {
        "from_attributes": True
    }
 
 
# ---------- Order ----------
class OrderCreate(BaseModel):
    customer_id: int
    product_id: int
    quantity: int
 
class OrderResponse(BaseModel):
    id: int
    customer_id: int
    product_id: int
    quantity: int
    total_price: float
    status: str
 
    model_config = {
        "from_attributes": True
    }
