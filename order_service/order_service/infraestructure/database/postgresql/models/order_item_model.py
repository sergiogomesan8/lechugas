from django.db import models
from order_service.infraestructure.database.postgresql.models.order_model import OrderModel

class OrderItemModel(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(OrderModel, related_name="items", on_delete=models.CASCADE)
    product_id = models.CharField(max_length=36)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = "order_items"