from abc import ABC, abstractmethod

from stock_service.domain.value_objects.product_id import ProductId
from stock_service.domain.entities.product import Product


class IProductRepository(ABC):

    @abstractmethod
    def create_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def get_product_stock_by_product_id(self, product_id: ProductId) -> int:
        pass


    @abstractmethod
    def add_stock_for_product_by_product_id(self, product_id: ProductId, quantity: int) -> int:
        pass


    @abstractmethod
    def reduce_stock_for_product_by_product_id(self, product_id: ProductId, quantity: int) -> int:
        pass