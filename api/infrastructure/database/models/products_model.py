from django.db import models

from api.infrastructure.database.models.categories_model import Categories


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, db_column="category_id"
    )

    class Meta:
        app_label = "api"
        db_table = "products"
