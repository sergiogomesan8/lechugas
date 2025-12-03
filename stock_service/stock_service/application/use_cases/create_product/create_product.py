from stock_service.domain.entities.product import Product
from stock_service.domain.ports.product_repository import IProductRepository
from stock_service.domain.value_objects.expiration_date import ExpirationDate

from stock_service.application.use_cases.create_product.dtos import CreateProductDTO


class CreateProduct:

    def __init__(
        self,
        repository: IProductRepository
    ):
        self._repository = repository
    
    def create_product(self, create_product_dto: CreateProductDTO):
        product = Product.create(
            name=create_product_dto.name,
            expiration_date=ExpirationDate(create_product_dto.expiration_date), 
            stock=create_product_dto.initial_stock
        )
        return self._repository.create_product(product)