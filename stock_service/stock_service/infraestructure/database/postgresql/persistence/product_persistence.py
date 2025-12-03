from stock_service.domain.ports.product_repository import IProductRepository
from stock_service.domain.value_objects.product_id import ProductId
from stock_service.domain.entities.product import Product

from stock_service.infraestructure.database.postgresql.models.stock_model import StockModel
from stock_service.infraestructure.database.postgresql.models.product_model import ProductModel

class ProductPersistence(IProductRepository):

    def create_product(self, product: Product) -> None:
        print(f"ProductPersistence -> create_product - product: {product}")

        product_model = ProductModel.objects.create(
            id=str(product.id),
            name=product.name,
            expiration_date=product.expiration_date.value,
        )

        StockModel.objects.create(
            product=product_model,
            quantity=product.stock
        )
            

    def get_product_stock_by_product_id(self, product_id: ProductId) -> int:
        print(f"ProductPersistence -> get_product_stock_by_product_id - product_id: {product_id}")
        try:
            stock_model = StockModel.objects.get(
                product_id=str(product_id)
            )
            return stock_model.quantity
        except StockModel.DoesNotExist:
            return 0

        # try:
        #     stock = StockModel.objets.get(product_id=str(product_id))
        #     return stock.quantity
        # except StockModel.DoesNotExist:
        #     return 0

    def add_stock_for_product_by_product_id(self, product_id: ProductId, quantity: int) -> int:
        print(f"ProductPersistence -> add_stock_for_product_by_product_id - product_id: {product_id} | quantity: {quantity}")
        pass


    def reduce_stock_for_product_by_product_id(lf, product_id: ProductId, quantity: int) -> int:
        print(f"ProductPersistence -> reduce_stock_for_product_by_product_id - product_id: {product_id} | quantity: {quantity}")
        pass