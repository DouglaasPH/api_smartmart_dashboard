from api.domain.entities.product_entity import Product
from api.domain.repositories.product_repository import ProductRepository


class ListProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, name: str, price: float, category_id: int, brand: str) -> Product:
        all_products = self.repository.list(name, price, category_id, brand)
        return all_products
