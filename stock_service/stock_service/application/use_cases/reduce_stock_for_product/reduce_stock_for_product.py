from stock_service.domain.value_objects.product_id import ProductId
from stock_service.domain.ports.product_repository import IProductRepository

class ReduceProductStock:

    def __init__(
            self, 
            repository: IProductRepository
    ):
        self._repository = repository
    
    
    def reduce_product_stock(self, product_id: ProductId, quantity: int) -> int:
        return self._repository.reduce_stock_for_product_by_product_id(product_id, quantity)