from api.domain.entities.category_entity import Category
from api.domain.repositories.category_repository import CategoryRepository


class ListCategoryUseCase:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def execute(self) -> Category:
        all_categories = self.repository.list()
        return all_categories
