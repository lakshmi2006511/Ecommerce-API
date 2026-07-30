
from sqlalchemy.orm import Session
import models
import schemas
 
 
# ---------- Product CRUD ----------
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
 
def get_products(db: Session):
    return db.query(models.Product).all()
 
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()
 
def get_by_category(db: Session, category_name: str):
    return db.query(models.Product).filter(models.Product.category == category_name).all()
 
def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    db_product.name = product.name
    db_product.description = product.description
    db_product.category = product.category
    db_product.price = product.price
    db_product.stock = product.stock
    db.commit()
    db.refresh(db_product)
    return db_product
 
def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product
 
 
# ---------- Customer CRUD ----------
def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer
 
def get_customers(db: Session):
    return db.query(models.Customer).all()
 
def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()
 
def delete_customer(db: Session, customer_id: int):
    db_customer = get_customer(db, customer_id)
    if not db_customer:
        return None
    db.delete(db_customer)
    db.commit()
    return db_customer
 
 
# ---------- Order CRUD ----------
def create_order(db: Session, order: schemas.OrderCreate):
    product = get_product(db, order.product_id)
    if not product:
        return None
    if product.stock < order.quantity:
        return "insufficient_stock"
 
    total_price = product.price * order.quantity
    db_order = models.Order(
        customer_id=order.customer_id,
        product_id=order.product_id,
        quantity=order.quantity,
        total_price=total_price,
        status="pending"
    )
    product.stock -= order.quantity  # reduce stock on order placement
 
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
 
def get_orders(db: Session):
    return db.query(models.Order).all()
 
def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()
 
def get_orders_by_customer(db: Session, customer_id: int):
    return db.query(models.Order).filter(models.Order.customer_id == customer_id).all()
 
def update_order_status(db: Session, order_id: int, status: str):
    db_order = get_order(db, order_id)
    if not db_order:
        return None
    db_order.status = status
    db.commit()
    db.refresh(db_order)
    return db_order
 
def delete_order(db: Session, order_id: int):
    db_order = get_order(db, order_id)
    if not db_order:
        return None
    db.delete(db_order)
    db.commit()
    return db_order