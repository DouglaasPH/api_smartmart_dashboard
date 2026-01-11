from api.domain.entities.product_entity import Product
from api.domain.repositories.product_repository import ProductRepository


class FakeProductRepository(ProductRepository):
    def save(self, product: Product):
        return product

    def list(self):
        return []

    def get_by_name(self, name: str):
        return None


def test_product_repository_interface_methods_exists():
    repo = FakeProductRepository()
    
    product = repo.get_by_name("Iphone")
    assert product is None

    p = Product(id=None, name="14", description="Celular", price=299.99, category_id=1, brand="Iphone")
    saved_product = repo.save(p)
    assert saved_product.brand == "Iphone"

    products = repo.list()
    assert isinstance(products, list)
