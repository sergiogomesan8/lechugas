from django.db import models
from order_service.domain.value_objects.order_status import OrderStatus

class OrderModel(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    order_date = models.DateField()

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]
    status = models.CharField(max_length=36, choices=STATUS_CHOICES, default="pending")

    class Meta:
        db_table = "orders"