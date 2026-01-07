import pytest

from product.models import Category

@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(
        title="Games",
        slug = "Games",
        description="Descrição da categoria",
        active = True
    )

    assert category.title == "Games"
    assert category.slug == category.title
    assert category.description == "Descrição da categoria"
    assert category.active == True
    