from api.application.use_cases.sale.get_sale import GetSaleByIdUseCase
from api.domain.entities.sale_entity import Sale


class FakeSaleRepository:
    def __init__(self):
        self.saved = []

    def save(self, sale: Sale):
        self.saved.append(sale)
        return sale

    def get_by_id(self, sale_id: int):
        return Sale(
            id=sale_id, product_id=2, quantity=4, total_price=40.99, date="2026-01-11"
        )

    def list(self):
        return []


def test_get_sale_usecase():
    sale_repo = FakeSaleRepository()

    use_case = GetSaleByIdUseCase(sale_repo)

    sale = use_case.execute(1)

    assert sale.id == 1
    assert sale.product_id == 2
    assert sale.quantity == 4
    assert sale.total_price == 40.99
    assert sale.date == "2026-01-11"
