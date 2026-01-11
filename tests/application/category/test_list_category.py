from api.domain.entities.category_entity import Category
from api.application.use_cases.category.list_category import ListCategoryUseCase

class FakeCategoryRepository:
    def __init__(self):
        self.saved = []

    def save(self, category: Category):
        self.saved.append(category)
        return category

    def get_by_name(self, category_name: str):
        return None

    def list(self):
        return []


def test_list_category_usecase():
    category_repo = FakeCategoryRepository()

    use_case = ListCategoryUseCase(category_repo)

    category = use_case.execute()

    assert category == []
