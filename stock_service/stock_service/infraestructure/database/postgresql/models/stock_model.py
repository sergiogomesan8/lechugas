from django.db import models

from stock_service.infraestructure.database.postgresql.models.product_model import ProductModel

class StockModel(models.Model):
    product = models.OneToOneField(
        ProductModel,
        on_delete=models.CASCADE,
        related_name="stock"
    )
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = "stock"