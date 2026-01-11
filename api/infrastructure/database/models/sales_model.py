from django.db import models

from api.infrastructure.database.models.products_model import Products


class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, db_column="product_id"
    )

    class Meta:
        app_label = "api"
        db_table = "sales"
