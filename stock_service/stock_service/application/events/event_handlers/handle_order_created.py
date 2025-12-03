from stock_service.application.use_cases.reduce_stock_for_product.reduce_stock_for_product import ReduceProductStock
from stock_service.domain.value_objects.product_id import ProductId

class OrderCreatedEventHandler:
    def __init__(self, reduce_product_stock_use_case: ReduceProductStock):
        self.reduce_product_stock_use_case = reduce_product_stock_use_case

    def handle(self, event: dict):
        self.reduce_product_stock_use_case.reduce_product_stock(
            ProductId(event["product_id"]),
            event["quantity"]
        )