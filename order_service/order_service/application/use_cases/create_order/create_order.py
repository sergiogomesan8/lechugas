from order_service.domain.entities.order import Order
from order_service.application.use_cases.create_order.dtos import CreateOrderDTO

from order_service.domain.ports.order_repository import IOrderRepository
from order_service.domain.ports.event_publisher_interface import IEventPublisher
from order_service.application.events.order_created_event import OrderCreatedEvent


class CreateOrder:

    def __init__(
            self,
            repository: IOrderRepository,
            publisher: IEventPublisher,
    ):
        self._repository = repository
        self._publisher = publisher
    
    def create_order(self, create_order_dto: CreateOrderDTO):
        print(create_order_dto)
        order = Order.create(
            items=create_order_dto.items
        )
        self._repository.create_order(order)
        order_create_event = OrderCreatedEvent.create(order.items)
        self._publisher.publish(order_create_event)
        
        return order