from dataclasses import dataclass, field
from typing import Any, Dict

from order_service.application.events.base_event import BaseEvent
from order_service.domain.value_objects.order_item import OrderItem

@dataclass(frozen=True)
class OrderCreatedEvent(BaseEvent):
    name: str = field(default="order.created", init=False)

    @classmethod
    def create_payload(cls, items: list[OrderItem]) -> Dict[str, Any]:
        payload = {"items": [{"product_id": i.product_id, "quantity": i.quantity} for i in items]}
        return payload