from fasthtml.common import (
    Html,
    Head,
    Title,
    Body,
    Div,
    H1,
    H2,
    P,
    A,
    Form,
    Input,
    Textarea,
    Label,
    fast_app,
    Style,
    Header,
    Nav,
    Ul,
    Li,
    serve,
)
import core
from chaotic_shop.style import CSS
import time

app, rt = fast_app()


@rt("/")
def get():
    categories = core.ADJECTIVES
    category_list = Div(
        *[
            Div(
                H2(category),
                A("View Products", href=f"/category/{category}"),
                _class="category",
            )
            for category in categories
        ],
        _id="categories",
    )
    return Html(
        Head(Title("Chaotic Shop"), Style(CSS)),
        Body(
            Div(
                Header(
                    Div(H1("Chaotic Shop"), _id="branding"),
                    Nav(
                        Ul(
                            Li(A("Home", href="/")),
                            Li(A("Products", href="/")),
                        )
                    ),
                ),
                _class="container",
            ),
            Div(H1("Welcome to Chaotic Shop!"), category_list, _class="container"),
        ),
    )


@rt("/category/{category}")
def get(category: str):
    products = core.get_products_by_category(category)
    product_list = Div(
        *[
            Div(
                H2(product["name"]),
                P(product["description"]),
                P(product["price"]),
                P(product["category"]),
                A("View", href=f"/product/{product['id']}"),
                _class="product",
            )
            for product in products
        ],
        _id="products",
    )
    return Html(
        Head(Title(f"Products in {category}"), Style(CSS)),
        Body(
            Div(
                Header(
                    Div(H1("Chaotic Shop"), _id="branding"),
                    Nav(
                        Ul(
                            Li(A("Home", href="/")),
                            Li(A("Products", href="/")),
                        )
                    ),
                ),
                _class="container",
            ),
            Div(H1(f"Products in {category}"), product_list, _class="container"),
        ),
    )


@rt("/product/{product_id}")
def get(product_id: int):
    product = core.generate_product_by_id(product_id)

    if product:
        return Html(
            Head(Title(product["name"]), Style(CSS)),
            Body(
                Div(
                    Header(
                        Div(H1("Chaotic Shop"), _id="branding"),
                        Nav(
                            Ul(
                                Li(A("Home", href="/")),
                                Li(A("Products", href="/")),
                            )
                        ),
                    ),
                    _class="container",
                ),
                Div(
                    H1(product["name"]),
                    P(product["description"]),
                    P(product["price"]),
                    P(product["category"]),
                    A("Back to products", href="/"),
                    _class="container",
                ),
                Div(
                    H2("Leave a Review"),
                    Form(
                        Input(type="hidden", name="product_id", value=product_id),
                        Div(
                            Label("Name:"),
                            Input(type="text", name="name", required=True),
                        ),
                        Div(
                            Label("Review:"),
                            Textarea(name="review", required=True),
                        ),
                        Div(
                            Input(type="submit", value="Submit"),
                        ),
                        method="post",
                        action="/submit_review",
                    ),
                    _class="container",
                ),
            ),
        )
    else:
        return Html(
            Head(Title("Product not found"), Style(CSS)),
            Body(
                Div(
                    Header(
                        Div(H1("Chaotic Shop"), _id="branding"),
                        Nav(
                            Ul(
                                Li(A("Home", href="/")),
                                Li(A("Products", href="/")),
                            )
                        ),
                    ),
                    _class="container",
                ),
                Div(
                    H1("Product not found"),
                    A("Back to products", href="/"),
                    _class="container",
                ),
            ),
        )


@rt("/submit_review", methods=["POST"])
def post(request: dict):
    product_id = request.get("product_id")
    name = request.get("name")
    review = request.get("review")

    print(f"Received review for product {product_id} from {name}: {review}")

    time.sleep(4)

    return Html(
        Head(Title("Review Submitted"), Style(CSS)),
        Body(
            Div(
                Header(
                    Div(H1("Chaotic Shop"), _id="branding"),
                    Nav(
                        Ul(
                            Li(A("Home", href="/")),
                            Li(A("Products", href="/")),
                        )
                    ),
                ),
                _class="container",
            ),
            Div(
                H1("Thank you for your review!"),
                P(f"Review for product {product_id} from {name}: {review}"),
                A("Back to products", href="/"),
                _class="container",
            ),
        ),
    )


def main():
    serve()


if __name__ == "__main__":
    main()
