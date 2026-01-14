from dataclasses import dataclass


@dataclass
class Product:
    id: int | None
    name: str
    description: str
    price: float
    category_id: int
    brand: str


@dataclass
class Category:
    id: int
    name: str


@dataclass
class ProductForResponse:
    id: int | None
    name: str
    description: str
    price: float
    category: Category
    brand: str
