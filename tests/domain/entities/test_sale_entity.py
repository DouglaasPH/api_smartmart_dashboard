from api.domain.entities.sale_entity import Sale


def test_sale_creation():
    sale = Sale(
        id=None, product_id=1, quantity=20, total_price=402302.32, date="2025-01-20"
    )
    assert sale.product_id == 1
    assert sale.quantity == 20
    assert sale.total_price == 402302.32
    assert sale.date == "2025-01-20"
