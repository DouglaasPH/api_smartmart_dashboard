from api.application.use_cases.product.list_product import ListProductUseCase
from api.domain.entities.product_entity import Product


class FakeProductRepository:
    def __init__(self):
        self.saved = []

    def save(self, product: Product):
        self.saved.append(product)
        return product

    def get_by_name(self, product_name: str):
        return None

    def list(
        self,
        name: str | None = None,
        price: float | None = None,
        category_id: int | None = None,
        brand: str | None = None,
    ):
        return []


def test_list_product_usecase():
    product_repo = FakeProductRepository()

    use_case = ListProductUseCase(product_repo)

    product = use_case.execute(name=None, price=None, category_id=None, brand=None)

    assert product == []
