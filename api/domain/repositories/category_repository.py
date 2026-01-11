from abc import ABC, abstractmethod
from typing import List, Optional

from api.domain.entities.category_entity import Category


class CategoryRepository(ABC):
    @abstractmethod
    def save(self, category: Category) -> Category:
        pass

    @abstractmethod
    def list(self) -> List[Category]:
        pass

    @abstractmethod
    def get_by_name(self, category_name: str) -> Optional[Category]:
        pass

    @abstractmethod
    def get_by_id(self, category_id: int) -> Optional[Category]:
        pass
