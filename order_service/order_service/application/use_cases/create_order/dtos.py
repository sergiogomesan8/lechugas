from pydantic import BaseModel
from order_service.domain.value_objects.order_item import OrderItem

class CreateOrderDTO(BaseModel):
    items: list[OrderItem]