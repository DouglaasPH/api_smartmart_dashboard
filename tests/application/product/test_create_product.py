from api.application.use_cases.product.create_product import CreateProductUseCase
from api.domain.entities.category_entity import Category
from api.domain.entities.product_entity import Product


class FakeProductRepository:
    def __init__(self):
        self.saved = []

    def save(self, product: Product):
        self.saved.append(product)
        return product

    def list(self):
        return []

    def get_by_name(self, name: str):
        return None


class FakeCategoryRepository:
    def get_by_id(self, category_id: int):
        return Category(id=category_id, name=f"Categoria {category_id}")


def test_create_product_usecase():
    product_repo = FakeProductRepository()
    category_repo = FakeCategoryRepository()

    use_case = CreateProductUseCase(product_repo, category_repo)

    product = use_case.execute(
        name="iPhone 14",
        description="Celular topo de linha",
        price=299.99,
        category_id=1,
        brand="Apple",
    )

    assert product.name == "iPhone 14"
    assert product.price == 299.99
    assert product.category_id == 1
    assert product.brand == "Apple"

    assert len(product_repo.saved) == 1
    saved_product = product_repo.saved[0]
    assert saved_product.name == "iPhone 14"
