from django.db import models

class ProductModel(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=36, unique=True, default='')
    expiration_date = models.DateField()

    class Meta:
        db_table = "products"
