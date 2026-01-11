from dataclasses import dataclass, field
from datetime import date


@dataclass
class Sale:
    id: int | None
    product_id: int
    quantity: int
    total_price: float
    date: date = field(default_factory=date.today)
