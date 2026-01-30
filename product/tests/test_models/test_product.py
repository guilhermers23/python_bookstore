import pytest

from product.models import Product

@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        title="Playstaion 5",
        description="Descrição do produto acima",
        price=3500
    )

    assert product.title == "Playstaion 5"
    assert product.description == "Descrição do produto acima"
    assert product.price == 3500
    assert product.id is not None
