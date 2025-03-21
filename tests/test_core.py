import pytest
import core


def test_find_product_by_id():
    product = core.generate_product_by_id(0)
    assert product["name"] == "Advanced Adapter #0"
    product = core.generate_product_by_id(1)
    assert product["name"] == "Advanced Analyzer #1"
    last_element = len(core.ADJECTIVES) * len(core.NOUNS) - 1
    product = core.generate_product_by_id(last_element)
    assert product["name"] == f"Versatile Hub #{last_element}"


def test_find_product_by_id_not_found():
    product = core.generate_product_by_id(999)
    assert product["name"] == "Lightweight Tool #999"


def test_get_products_by_category():
    products = core.get_products_by_category("Compact")

    for product in products:
        assert product["category"] == "Compact"

    advanced = core.get_products_by_category("Advanced")

    for product in advanced:
        assert product["category"] == "Advanced"
