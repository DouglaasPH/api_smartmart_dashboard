from api.domain.entities.product_entity import Product

def test_product_creation():
    product = Product(id=None, name="14", description="Celular", price=299.99, category_id=1, brand="Iphone")
    assert product.name == "14"
    assert product.brand == "Iphone"
    assert product.description == "Celular"
    assert product.price == 299.99
    assert product.category_id == 1
