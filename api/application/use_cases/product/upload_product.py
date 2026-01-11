from api.domain.entities.product_entity import Product
from api.domain.repositories.category_repository import CategoryRepository
from api.domain.repositories.product_repository import ProductRepository


class UploadProductUseCase:
    def __init__(
        self,
        product_repository: ProductRepository,
        category_repository: CategoryRepository,
    ):
        self.product_repository = product_repository
        self.category_repository = category_repository

    def execute(
        self, name: str, description: str, price: float, category_id: int, brand: str
    ) -> Product:
        category_exists = self.category_repository.get_by_id(category_id)
        if not category_exists:
            raise ValueError(f"Category with id '{category_id}' does not exist")

        product_exists = self.product_repository.get_by_name(name)
        if product_exists:
            raise ValueError(f"Product '{name}' already exists")

        product = Product(
            id=None,
            name=name,
            description=description,
            price=price,
            category_id=category_id,
            brand=brand,
        )

        return self.product_repository.save(product)
