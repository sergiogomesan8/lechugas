from stock_service.domain.value_objects.product_id import ProductId
from stock_service.domain.ports.product_repository import IProductRepository

class AddStockForProduct:

    def __init__(
            self, 
            repository: IProductRepository
    ):
        self._repository = repository
    

    def add_stock_for_product(self, product_id: ProductId, quantity: int) -> int:
        return self._repository.add_stock_for_product_by_product_id(product_id, quantity)