from api.domain.entities.product_entity import Product
from api.domain.repositories.product_repository import ProductRepository
from api.infrastructure.database.models.products_model import Products


class DjangoProductRepository(ProductRepository):
    def save(self, product: Product) -> Product:
        model = Products(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            category_id=product.category_id,
            brand=product.brand,
        )
        model.save()
        return model

    def list(
        self,
        name: str | None = None,
        price: float | None = None,
        category_id: int | None = None,
        brand: str | None = None,
    ) -> list[Product]:
        queryset = Products.objects.all()

        if name is not None:
            queryset = queryset.filter(name=name)

        if price is not None:
            queryset = queryset.filter(price=price)

        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)

        if brand is not None:
            queryset = queryset.filter(brand=brand)

        return [
            Product(
                id=p.id,
                name=p.name,
                description=p.description,
                price=float(p.price),
                category_id=p.category_id,
                brand=p.brand,
            )
            for p in queryset
        ]

    def get_by_name(self, product_name: int) -> Product | None:
        try:
            p = Products.objects.get(name=product_name)
            return Product(
                id=p.id,
                name=p.name,
                description=p.description,
                price=float(p.price),
                category_id=p.category_id,
                brand=p.brand,
            )
        except Products.DoesNotExist:
            return None
