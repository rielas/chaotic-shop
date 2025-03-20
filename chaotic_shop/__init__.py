from fasthtml.common import *
from core import products

app, rt = fast_app()


@rt("/")
def get():
    product_list = Div(
        *[
            Div(
                H2(product["name"]),
                P(product["description"]),
                P(product["price"]),
                A("View", href=f"/product/{product['id']}"),
            )
            for product in products
        ]
    )
    return Div(H1("Welcome to Chaotic Shop!"), product_list)


@rt("/product/{product_id}")
def get(product_id: int):
    product = next((p for p in products if p["id"] == int(product_id)), None)

    if product:
        return Div(
            H1(product["name"]),
            P(product["description"]),
            P(product["price"]),
            A("Back to products", href="/"),
        )
    else:
        return Div(H1("Product not found"), A("Back to products", href="/"))


def main():
    serve()


if __name__ == "__main__":
    main()
