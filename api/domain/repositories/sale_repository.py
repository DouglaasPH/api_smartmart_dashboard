from abc import ABC, abstractmethod
from typing import List, Optional

from api.domain.entities.sale_entity import Sale


class SaleRepository(ABC):
    @abstractmethod
    def save(self, sale: Sale) -> Sale:
        pass

    @abstractmethod
    def list(self) -> List[Sale]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Sale]:
        pass
