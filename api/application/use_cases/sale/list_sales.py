from collections import defaultdict

from api.domain.entities.sale_entity import Sale
from api.domain.repositories.sale_repository import SaleRepository


class ListSalesUseCase:
    def __init__(self, repository: SaleRepository):
        self.repository = repository

    def execute(self) -> Sale:
        all_sales = self.repository.list()

        result = defaultdict(lambda: {"quantity": 0, "profit": 0})

        if not all_sales:
            return None

        for sale in all_sales:
            month = sale.date.strftime("%Y-%m")

            result[month]["quantity"] += sale.quantity
            result[month]["profit"] += float(sale.total_price)

        response = []

        for month, data in result.items():
            response.append(
                {
                    "month": month,
                    "quantity": data["quantity"],
                    "profit": round(data["profit"], 2),
                }
            )

        return response
