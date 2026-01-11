import csv
from io import StringIO

from django.http import HttpResponse

import pytest

from api.application.use_cases.product.export_product import ExportProductUseCase
from api.domain.entities.product_entity import Product


class FakeProductRepository:
    def list(self):
        return [
            Product(
                id=1,
                name="iPhone 14",
                description="Celular",
                price=299.99,
                brand="Apple",
                category_id=1,
            ),
            Product(
                id=2,
                name="Galaxy S22",
                description="Celular",
                price=199.99,
                brand="Samsung",
                category_id=1,
            ),
        ]


@pytest.mark.django_db
def test_export_product_usecase():
    repo = FakeProductRepository()
    use_case = ExportProductUseCase(repo)

    response = use_case.execute()

    assert isinstance(response, HttpResponse)
    assert response["Content-Type"] == "text/csv"
    assert response["Content-Disposition"] == 'attachment; filename="products.csv"'

    csv_content = response.content.decode("utf-8")
    csv_file = StringIO(csv_content)
    reader = list(csv.reader(csv_file))

    assert reader[0] == ["id", "name", "description", "price", "brand", "category_id"]

    assert reader[1] == ["1", "iPhone 14", "Celular", "299.99", "Apple", "1"]
    assert reader[2] == ["2", "Galaxy S22", "Celular", "199.99", "Samsung", "1"]
