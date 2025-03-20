from fasthtml.common import *
import core

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
            for product in core.PRODUCTS
        ]
    )
    return Div(H1("Welcome to Chaotic Shop!"), product_list)


@rt("/product/{product_id}")
def get(product_id: int):
    product = core.generate_product_by_id(product_id)

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
