from api.domain.entities.category_entity import Category

def test_category_creation():
    product = Category(id=None, name="Smartphone")
    assert product.name == "Smartphone"
