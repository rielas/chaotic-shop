import pytest
from core import find_product_by_id


def test_find_product_by_id():
    product = find_product_by_id(1)
    assert product is not None
    assert product["name"] == "Product 1"


def test_find_product_by_id_not_found():
    product = find_product_by_id(999)
    assert product is None
