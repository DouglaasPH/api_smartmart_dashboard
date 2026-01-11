from api.domain.entities.category_entity import Category
from api.domain.repositories.category_repository import CategoryRepository


class FakeCategoryRepository(CategoryRepository):
    def save(self, category: Category):
        return category

    def list(self):
        return []

    def get_by_name(self, category_name: str):
        return None

    def get_by_id(self, category_id: int):
        return None


def test_product_repository_interface_methods_exists():
    repo = FakeCategoryRepository()
    
    category_by_name = repo.get_by_name("Smartphone")
    assert category_by_name is None
    
    category_by_id = repo.get_by_id(1)
    assert category_by_id is None

    c = Category(id=None, name="Smartphone")
    saved_category = repo.save(c)
    assert saved_category.name == "Smartphone"

    categories = repo.list()
    assert isinstance(categories, list)
