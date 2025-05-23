from fasthtml.common import (
    Title,
    Aside,
    Strong,
    Img,
    Section,
    Div,
    H1,
    P,
    Article,
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
from typing import List, Tuple
import os

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

CATEGORY_CHAOS = int(os.getenv("CATEGORY_CHAOS", 0))
PRODUCT_CHAOS = int(os.getenv("PRODUCT_CHAOS", 0))


def navigation():
    return Header(
        Nav(
            Ul(Li(Strong("Chaotic Shop 😵‍💫"))),
            Ul(
                Li(
                    Strong("Chaos Levels: "),
                    f"category {CATEGORY_CHAOS}, "
                    f"product {PRODUCT_CHAOS}, "
                    f"Number of products {core.NUMBER_OF_PRODUCTS}",
                    _class="chaos-levels",
                ),
            ),
            Ul(Li(A("Home", href="/")), Li(A("Categories", href="/"))),
        ),
    )


def breadcrumbs(crumbs: List[Tuple | str]) -> Nav:
    """
    Generate a breadcrumb navigation.
    :param crumbs: Tuples of (label, href) or a single string for the current page.
    """
    return Nav(
        Ul(
            *[
                (
                    Li(A(crumb[0], href=crumb[1]))
                    if isinstance(crumb, tuple)
                    else Li(crumb)
                )
                for crumb in crumbs
            ],
        ),
        **{"aria-label": "breadcrumb"},
    )


@app.get("/")
def home():
    categories = core.ADJECTIVES
    descriptions = core.CATEGORIES_DESCRIPTIONS
    category_list = Div(
        *[
            Article(
                Header(category),
                A(
                    Img(
                        src=f"https://picsum.photos/id/{i}/300/200",
                        _class="center-image",
                    ),
                    href=f"/category/{category}",
                ),
                P(descriptions[i]),
                P(A(f"View {category}", href=f"/category/{category}")),
            )
            for i, category in enumerate(categories)
        ],
        _class="grid limited-grid",
    )
    return (
        Title("Chaotic Shop"),
        Main(navigation(), Main(category_list), _class="container"),
    )


@app.get("/category/{category}")
def category(category: str):
    categories = core.ADJECTIVES
    products = core.get_products_by_category(category)
    category_list = Nav(
        Ul(*[Li(A(category, href=f"/category/{category}")) for category in categories]),
        _class="sidebar",
    )
    product_list = Div(
        *[
            Article(
                Header(product["name"]),
                A(
                    Img(
                        src=f"https://picsum.photos/id/{product['id'] % 1000}/300/200",
                        _class="center-image",
                    ),
                    href=f"/product/{product['id']}",
                ),
                P(product["description"]),
                P(product["price"]),
                A("View", href=f"/product/{product['id']}"),
            )
            for product in products
        ],
        _id="products",
        _class="grid limited-grid",
    )
    return (
        Title(f"Products in {category}"),
        Main(
            navigation(),
            Main(
                Aside(category_list),
                Section(
                    breadcrumbs(
                        [
                            ("Categories", "/"),
                            (category, f"/category/{category}"),
                            f"Products in {category}",
                        ]
                    ),
                    P(f"Explore our wide range of {category} products."),
                    product_list,
                    _class="container",
                    _id="content",
                    role="document",
                ),
                _class="content-wrapper",
            ),
            _class="container",
        ),
    )


@rt("/product/{product_id}")
def get(product_id: int):
    return product_page(product_id)


@rt("/submit_review", methods=["POST", "GET"])
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
                navigation(),
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
def checkout(request: dict):
    product_id = request.get("product_id")

    print(f"Processing checkout for product {product_id}")

    time.sleep(4)

    return Titled(
        "Checkout Complete",
        Main(
            Div(
                navigation(),
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
