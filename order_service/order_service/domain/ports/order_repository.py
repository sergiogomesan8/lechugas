from abc import ABC, abstractmethod

from order_service.domain.entities.order import Order


class IOrderRepository(ABC):
    
    @abstractmethod
    def create_order(self, order: Order) -> None:
        pass