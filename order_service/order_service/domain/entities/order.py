from order_service.domain.value_objects.order_id import OrderId
from order_service.domain.value_objects.order_item import OrderItem
from order_service.domain.value_objects.order_date import OrderDate
from order_service.domain.value_objects.order_status import OrderStatus

class Order:
    def __init__(
        self,
        order_id: OrderId = None,
        items: list[OrderItem] = None,
        order_date: OrderDate = None,
        status: OrderStatus = None,
    ) -> None:
        self._id = order_id
        self._items = items
        self._order_date = order_date
        self.status = status
    

    @property
    def id(self) -> OrderId:
        return self._id

    @property
    def order_date(self) -> OrderDate:
        return self._order_date

    @property
    def items(self) -> list[OrderItem]:
        return self._items

    @classmethod 
    def create(cls, items: list[OrderItem]) -> Order:
        return cls(OrderId.new_one(), items, OrderDate.create(), OrderStatus.PAID)