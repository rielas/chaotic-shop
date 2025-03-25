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
    Header,
    Nav,
    Link,
    Ul,
    Li,
    serve,
    fast_app,
    Titled,
    Main,
)
import core
from chaotic_shop.product_page import product_page
import time

app, rt = fast_app(
    hdrs=(
        (),
        Link(
            rel="stylesheet",
            href="/assets/styles.css",
            type="text/css",
        ),
    ),
    pico=True,
    static_path="public",
)

CHAOS_DEGREE = 2


@app.get("/")
def home():
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
    return Titled(
        "Chaotic Shop",
        Main(
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


@app.get("/category/{category}")
def category(category: str):
    categories = core.ADJECTIVES
    products = core.get_products_by_category(category)
    category_list = Div(
        *[Li(A(category, href=f"/category/{category}")) for category in categories],
        _class="sidebar",
    )
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
    return Titled(
        f"Products in {category}",
        Main(
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
                Div(category_list, _class="sidebar-container"),
                Div(H1(f"Products in {category}"), product_list, _class="main-content"),
                _class="container",
            ),
        ),
    )


@rt("/product/{product_id}")
def get(product_id: int):
    return product_page(product_id)


@rt("/submit_review", methods=["POST"])
def post(request: dict):
    product_id = request.get("product_id")
    name = request.get("name")
    review = request.get("review")

    print(f"Received review for product {product_id} from {name}: {review}")

    time.sleep(4)

    return Titled(
        "Review Submitted",
        Main(
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


@rt("/checkout", methods=["POST"])
def post(request: dict):
    product_id = request.get("product_id")

    print(f"Processing checkout for product {product_id}")

    time.sleep(4)

    return Titled(
        "Checkout Complete",
        Main(
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
                H1("Checkout Complete"),
                P(f"Your checkout for product {product_id} is complete."),
                A("Back to products", href="/"),
                _class="container",
            ),
        ),
    )


def main():
    serve()


if __name__ == "__main__":
    main()
