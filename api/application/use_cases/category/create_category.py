from api.domain.entities.category_entity import Category
from api.domain.repositories.category_repository import CategoryRepository


class CreateCategoryUseCase:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def execute(self, name: str) -> Category:
        category_exists = self.repository.get_by_name(name)
        if category_exists:
            raise ValueError(f"Category '{name}' already exists")

        category = Category(id=None, name=name)
        return self.repository.save(category)
