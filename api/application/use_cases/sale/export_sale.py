import csv

from django.http import HttpResponse

from api.domain.entities.sale_entity import Sale
from api.domain.repositories.sale_repository import SaleRepository


class ExportSalesUseCase:
    def __init__(self, repository: SaleRepository):
        self.repository = repository

    def execute(self) -> Sale:
        all_sales = self.repository.list()

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="sales.csv'

        writer = csv.writer(response)

        writer.writerow(["id", "product_id", "date", "quantity", "total_price"])

        for sale in all_sales:
            writer.writerow(
                [sale.id, sale.product_id, sale.date, sale.quantity, sale.total_price]
            )

        return response
