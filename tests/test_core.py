import pytest
import core


def test_find_product_by_id():
    product = core.generate_product_by_id(1)
    assert product is not None
    assert product["name"] is not None


def test_find_product_by_id_not_found():
    product = core.generate_product_by_id(999)
    assert product is None


def test_get_products_by_category():
    products = core.get_products_by_category("Compact")

    for product in products:
        assert product["category"] == "Compact"

    advanced = core.get_products_by_category("Advanced")

    for product in advanced:
        assert product["category"] == "Advanced"
