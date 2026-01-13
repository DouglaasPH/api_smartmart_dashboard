import csv

from django.http import HttpResponse

from api.domain.entities.product_entity import Product
from api.domain.repositories.product_repository import ProductRepository


class ExportProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self) -> Product:
        all_products = self.repository.list()

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="products.csv"'

        writer = csv.writer(response)

        writer.writerow(["id", "name", "description", "price", "brand", "category_id"])

        for product in all_products:
            writer.writerow(
                [
                    product.id,
                    product.name,
                    product.description,
                    product.price,
                    product.brand,
                    product.category["id"],
                ]
            )

        return response
