from api.domain.entities.sale_entity import Sale
from api.domain.repositories.sale_repository import SaleRepository


class GetSaleByIdUseCase:
    def __init__(self, repository: SaleRepository):
        self.repository = repository

    def execute(self, sale_id: int) -> Sale:
        sale = self.repository.get_by_id(sale_id)

        if not sale:
            return None

        return sale
