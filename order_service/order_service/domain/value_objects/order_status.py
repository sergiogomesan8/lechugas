from enum import Enum, unique

@unique
class OrderStatus(Enum):
    PENDING = "pending"       # Order created, not confirmed
    PAID = "paid"             # Payment received
    SHIPPED = "shipped"       # Order sent to customer
    DELIVERED = "delivered"   # Customer received the order
    CANCELLED = "cancelled"   # Order cancelled before completion