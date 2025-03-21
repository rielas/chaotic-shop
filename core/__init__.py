from .names import ADJECTIVES, NOUNS, DESCRIPTIONS
from typing import Generator

NUMBER_OF_PRODUCTS = 10000


def get_category(id: int) -> str:
    return ADJECTIVES[id // len(NOUNS) % len(ADJECTIVES)]


def generate_product_name(id: int) -> str:
    """
    Generate a product name by combining an adjective and a noun.
    """
    import random

    random.seed(id)
    category = get_category(id)
    noun_size = len(NOUNS)
    noun = NOUNS[id % noun_size]
    return f"{category} {noun} #{id}"


def generate_price(id: int) -> str:
    """
    Generate a price for a product.
    """
    import random

    random.seed(id)
    price = random.randint(10, 100)
    return f"${price}"


def generate_description(id: int) -> str:
    """
    Generate a description for a product.
    """
    import random

    random.seed(id)

    return random.choice(DESCRIPTIONS)


def generate_product_by_id(id: int) -> dict | None:
    """
    Generate a product dictionary by ID.
    """

    if id < 0 or id > NUMBER_OF_PRODUCTS:
        return None

    return {
        "id": id,
        "name": generate_product_name(id),
        "price": generate_price(id),
        "description": generate_description(id),
        "category": get_category(id),
    }


def product_generator() -> Generator[dict]:
    """
    Generator function to yield products one by one.
    """

    for i in range(NUMBER_OF_PRODUCTS):
        yield generate_product_by_id(i)


def get_products_by_category(category: str) -> Generator[dict]:
    index = ADJECTIVES.index(category)

    for i in range(0, NUMBER_OF_PRODUCTS):
        if i // len(NOUNS) % len(ADJECTIVES) == index:
            yield generate_product_by_id(i)


def next_product_id_in_category(category: str, id: int) -> int | None:
    """
    Get the next product ID in the specified category.
    """
    if id < 0 or id >= NUMBER_OF_PRODUCTS - 1:
        return None

    index = ADJECTIVES.index(category)

    for i in range(id + 1, NUMBER_OF_PRODUCTS):
        if i // len(NOUNS) % len(ADJECTIVES) == index:
            return i

    return None


def previous_product_id_in_category(category: str, id: int) -> int | None:
    """
    Get the previous product ID in the specified category.
    """
    if id < 0 or id > NUMBER_OF_PRODUCTS:
        return None

    index = ADJECTIVES.index(category)

    for i in range(id - 1, -1, -1):
        if i // len(NOUNS) % len(ADJECTIVES) == index:
            return i

    return None
