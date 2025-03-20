from .names import ADJECTIVES, NOUNS, DESCRIPTIONS

def generate_product_name(id: int) -> str:
    """
    Generate a product name by combining an adjective and a noun.
    """
    import random
    random.seed(id)
    adjective = random.choice(ADJECTIVES)
    noun = random.choice(NOUNS)
    return f"{adjective} {noun} #{id}"

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

def generate_product_by_id(id: int) -> dict:
    """
    Generate a product dictionary by ID.
    """
    return {
        "id": id,
        "name": generate_product_name(id),
        "price": generate_price(id),
        "description": generate_description(id),
    }

PRODUCTS = [
    generate_product_by_id(i) for i in range(1, 101)
]
