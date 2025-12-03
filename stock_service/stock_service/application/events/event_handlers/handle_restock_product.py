from stock_service.application.use_cases.add_stock_for_product.add_stock_for_product import AddStockForProduct
from stock_service.domain.value_objects.product_id import ProductId

class ProductStockedBySupplier:
    def __init__(self, add_stock_for_product_use_case: AddStockForProduct):
        self.add_stock_for_product_use_case = add_stock_for_product_use_case
    
    def handle(self, event:dict):
        self.add_stock_for_product_use_case.add_stock_for_product(
            ProductId(event["product_id"]),
            event["quantity"]
        )