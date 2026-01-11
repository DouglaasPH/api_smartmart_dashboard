import pytest

from api.domain.entities.product_entity import Product
from api.application.use_cases.product.upload_product import UploadProductUseCase


class FakeCategoryRepository:
    def __init__(self):
        self.categories = {1: "Smartphones"}

    def get_by_id(self, category_id: int):
        if category_id in self.categories:
            return {"id": category_id, "name": self.categories[category_id]}
        return None


class FakeProductRepository:
    def __init__(self):
        self.saved = []

    def save(self, product: Product):
        self.saved.append(product)
        return product

    def get_by_name(self, name: str):
        for p in self.saved:
            if p.name == name:
                return p
        return None


def test_upload_product_success():
    product_repo = FakeProductRepository()
    category_repo = FakeCategoryRepository()

    use_case = UploadProductUseCase(product_repo, category_repo)

    product = use_case.execute(
        name="iPhone 14",
        description="Novo iPhone 14",
        price=999.99,
        category_id=1,
        brand="Apple"
    )

    assert product.name == "iPhone 14"
    assert product.brand == "Apple"
    assert len(product_repo.saved) == 1


def test_upload_product_category_not_exists():
    product_repo = FakeProductRepository()
    category_repo = FakeCategoryRepository()

    use_case = UploadProductUseCase(product_repo, category_repo)

    with pytest.raises(ValueError) as exc:
        use_case.execute(
            name="Galaxy S23",
            description="Novo Galaxy",
            price=899.99,
            category_id=999,
            brand="Samsung"
        )

    assert "does not exist" in str(exc.value)


def test_upload_product_duplicate_name():
    product_repo = FakeProductRepository()
    category_repo = FakeCategoryRepository()

    use_case = UploadProductUseCase(product_repo, category_repo)

    use_case.execute(
        name="Pixel 7",
        description="Google Pixel",
        price=599.99,
        category_id=1,
        brand="Google"
    )

    with pytest.raises(ValueError) as exc:
        use_case.execute(
            name="Pixel 7",
            description="Google Pixel",
            price=599.99,
            category_id=1,
            brand="Google"
        )

    assert "already exists" in str(exc.value)
