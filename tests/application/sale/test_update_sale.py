from api.domain.entities.sale_entity import Sale
from api.application.use_cases.sale.update_sale import UpdateSaleUseCase

class FakeSaleRepository:
    def __init__(self):
        self.saved = []

    def save(self, sale: Sale):
        self.saved.append(sale)
        return sale

    def get_by_id(self, sale_id: int):
        return Sale(id=sale_id, product_id=2, quantity=4, total_price=40.99, date="2026-01-11")

    def list(self):
        return []


def test_update_sale_usecase():
    sale_repo = FakeSaleRepository()

    use_case = UpdateSaleUseCase(sale_repo)

    sale = use_case.execute(id=4, product_id=3, date="2026-01-01")

    assert sale.id == 4
    assert sale.product_id == 3
    assert sale.quantity == 4
    assert sale.total_price == 40.99
    assert sale.date == "2026-01-01"