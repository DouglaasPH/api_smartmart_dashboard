from api.domain.entities.category_entity import Category
from api.domain.repositories.category_repository import CategoryRepository
from api.infrastructure.database.models.categories_model import Categories


class DjangoCategoryRepository(CategoryRepository):
    def save(self, category: Category) -> Category:
        model = Categories(name=category.name)
        model.save()
        return model

    def list(self) -> list[Category]:
        return [Category(id=c.id, name=c.name) for c in Categories.objects.all()]

    def get_by_name(self, category_name: str) -> Category | None:
        try:
            p = Categories.objects.get(name=category_name)
            return Category(id=p.id, name=p.name)
        except Categories.DoesNotExist:
            return None

    def get_by_id(self, category_id: int) -> Category | None:
        try:
            p = Categories.objects.get(id=category_id)
            return Category(id=p.id, name=p.name)
        except Categories.DoesNotExist:
            return None
