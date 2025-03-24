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
    assert product["name"] == "Efficient Hub #999"


def test_get_products_by_category():
    products = core.get_products_by_category("Compact")

    for product in products:
        assert product["category"] == "Compact"

    advanced = core.get_products_by_category("Advanced")

    for product in advanced:
        assert product["category"] == "Advanced"


def test_next_product_id_in_category():
    size_nouns = len(core.NOUNS)
    product_id = core.next_product_id_in_category("Advanced", 0)
    assert product_id == 1

    product_id = core.next_product_id_in_category("Basic", size_nouns)
    assert product_id == size_nouns + 1

    product_id = core.next_product_id_in_category("Basic", size_nouns + 1)
    assert product_id == size_nouns + 2

    last_element = core.NUMBER_OF_PRODUCTS - 1
    product_id = core.next_product_id_in_category("Versatile", last_element)
    assert product_id is None


def test_previous_product_id_in_category():
    product_id = core.previous_product_id_in_category("Advanced", 1)
    assert product_id == 0

    product_id = core.previous_product_id_in_category("Compact", 10)
    assert product_id is None

    product_id = core.previous_product_id_in_category("Basic", len(core.NOUNS) + 1)
    assert product_id == len(core.NOUNS)

    first_element = 0
    product_id = core.previous_product_id_in_category("Versatile", first_element)
    assert product_id is None
