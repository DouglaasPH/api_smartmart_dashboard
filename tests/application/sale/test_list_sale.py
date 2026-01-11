from api.application.use_cases.sale.list_sales import ListSalesUseCase
from api.domain.entities.sale_entity import Sale


class FakeSaleRepository:
    def __init__(self):
        self.saved = []

    def save(self, sale: Sale):
        self.saved.append(sale)
        return sale

    def get_by_id(self, sale_id: int):
        return None

    def list(self):
        return []


def test_list_sale_usecase():
    sale_repo = FakeSaleRepository()

    use_case = ListSalesUseCase(sale_repo)

    sale = use_case.execute()

    assert sale == None
