from dataclasses import dataclass
from typing import List
from datetime import datetime

# These are the dataclasses that we will use to represent the data in our application.

@dataclass
class Product:
    id: int
    name: str
    description: str
    price: float

@dataclass
class User:
    id: int
    name: str
    email: str
    
@dataclass
class Company:
    id: int
    slug: str
    name:str
    arr: str
    address: str
    contact: User

@dataclass
class OrderItem:
    product: Product
    quantity: int
    discount: float = 0.0
    item_price: float = 0.0

@dataclass
class Order:
    id: int
    company: Company
    items: List[OrderItem]
    total_price: float
    order_date: datetime
    validated: bool = False
