products = [
    {
        "id": 1,
        "name": "Product 1",
        "description": "Description of Product 1",
        "price": "$10",
    },
    {
        "id": 2,
        "name": "Product 2",
        "description": "Description of Product 2",
        "price": "$20",
    },
    {
        "id": 3,
        "name": "Product 3",
        "description": "Description of Product 3",
        "price": "$30",
    },
]


def find_product_by_id(product_id):
    return next((p for p in products if p["id"] == int(product_id)), None)
