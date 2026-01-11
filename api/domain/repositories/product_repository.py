# domain/repositories/sale_repository.py
from abc import ABC, abstractmethod
from typing import List, Optional

from api.domain.entities.product_entity import Product


class ProductRepository(ABC):
    @abstractmethod
    def save(self, sale: Product) -> Product:
        pass

    @abstractmethod
    def list(
        self,
        name: str | None = None,
        price: float | None = None,
        category_id: int | None = None,
        brand: str | None = None,
    ) -> List[Product]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Product]:
        pass
