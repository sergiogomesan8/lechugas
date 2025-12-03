from stock_service.domain.value_objects.product_id import ProductId
from stock_service.domain.value_objects.expiration_date import ExpirationDate

class Product:
    def __init__(
            self,
            product_id: ProductId = None, 
            name: str = '',
            expiration_date: ExpirationDate = None,
            stock: int = 0
    ) -> None:
        self._id = product_id
        self.name = name
        self._expiration_date = expiration_date
        self.stock = stock

    @property
    def id(self) -> ProductId:
        return self._id
    
    @property
    def expiration_date(self) -> ExpirationDate:
        return self._expiration_date
    
    @classmethod
    def create(cls, name: str, expiration_date: ExpirationDate, stock: int):
        return cls(ProductId.new_one(), name, expiration_date, stock)
    