from stock_service.domain.value_objects.product_id import ProductId
from stock_service.domain.ports.product_repository import IProductRepository

class CheckProductStock:

    def __init__(
            self, 
            repository: IProductRepository
    ):
        self._repository = repository
    
    def check_product_stock(self, product_id: ProductId) -> int:
        return self._repository.get_product_stock_by_product_id(product_id)