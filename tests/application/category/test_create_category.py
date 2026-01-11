from api.domain.entities.category_entity import Category
from api.application.use_cases.category.create_category import CreateCategoryUseCase

class FakeCategoryRepository:
    def __init__(self):
        self.saved = []

    def save(self, category: Category):
        self.saved.append(category)
        return category

    def get_by_name(self, category_name: str):
        return None


def test_create_category_usecase():
    category_repo = FakeCategoryRepository()

    use_case = CreateCategoryUseCase(category_repo)

    category = use_case.execute(
        name="Smartphone",
    )

    assert category.name == "Smartphone"
