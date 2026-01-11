from dataclasses import dataclass


@dataclass
class Product:
    id: int | None
    name: str
    description: str
    price: float
    category_id: int
    brand: str
