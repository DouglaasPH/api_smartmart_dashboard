from api.domain.entities.sale_entity import Sale
from api.domain.repositories.sale_repository import SaleRepository
from api.infrastructure.database.models.sales_model import Sales


class DjangoSaleRepository(SaleRepository):
    def save(self, sale: Sale) -> Sale:
        model = Sales(
            id=sale.id,
            product_id=sale.product_id,
            quantity=sale.quantity,
            total_price=sale.total_price,
            date=sale.date,
        )
        model.save()
        return model

    def list(self) -> list[Sale]:
        return [
            Sale(
                id=s.id,
                product_id=s.product_id,
                quantity=s.quantity,
                total_price=s.total_price,
                date=s.date,
            )
            for s in Sales.objects.all()
        ]

    def get_by_id(self, sale_id: int) -> Sale | None:
        try:
            s = Sales.objects.get(id=sale_id)
            return Sale(
                id=s.id,
                product_id=s.product_id,
                quantity=s.quantity,
                total_price=s.total_price,
                date=s.date,
            )
        except Sales.DoesNotExist:
            return None
