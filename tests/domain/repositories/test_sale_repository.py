from api.domain.entities.sale_entity import Sale
from api.domain.repositories.sale_repository import SaleRepository


class FakeSaleRepository(SaleRepository):
    def save(self, sale: Sale):
        return sale

    def list(self):
        return []

    def get_by_id(self, id: int):
        return None


def test_sale_repository_interface_methods_exists():
    repo = FakeSaleRepository()
    
    sale = repo.get_by_id(1)
    assert sale is None

    s = Sale(id=None, product_id=1, quantity=32, total_price=30943299.99, date="2025-05-24")
    saved_sale = repo.save(s)
    assert saved_sale.date == "2025-05-24"

    sales = repo.list()
    assert isinstance(sales, list)
