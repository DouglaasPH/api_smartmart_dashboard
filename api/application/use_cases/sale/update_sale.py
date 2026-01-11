from api.domain.entities.sale_entity import Sale
from api.domain.repositories.sale_repository import SaleRepository


class UpdateSaleUseCase:
    def __init__(self, repository: SaleRepository):
        self.repository = repository

    def execute(
        self,
        id: int,
        product_id: int | None = None,
        quantity: int | None = None,
        total_price: float | None = None,
        date: str | None = None,
    ) -> Sale:
        sale_exists = self.repository.get_by_id(id)
        if not sale_exists:
            raise ValueError(f"Sale with id '{id}' does not exist")

        sale = Sale(
            id=id,
            product_id=sale_exists.product_id,
            quantity=sale_exists.quantity,
            total_price=sale_exists.total_price,
            date=sale_exists.date,
        )

        if product_id:
            sale.product_id = product_id
        if quantity:
            sale.quantity = quantity
        if total_price:
            sale.total_price = total_price
        if date:
            sale.date = date

        return self.repository.save(sale)
