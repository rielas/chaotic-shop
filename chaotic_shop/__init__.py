from fasthtml.common import (
    Title,
    Aside,
    Strong,
    Img,
    Button,
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

CHAOS_DEGREE = 5


def navigation():
    return Header(
        Nav(
            Ul(Li(Strong("Chaotic Shop 😵‍💫"))),
            Ul(
                Li(A("Home", href="/")),
                Li(A("Categories", href="/")),
            ),
        ),
    )


@app.get("/")
def home():
    categories = core.ADJECTIVES
    descriptions = core.CATEGORIES_DESCRIPTIONS
    category_list = Div(
        *[
            Article(
                Header(category),
                Img(src="https://placehold.co/200"),
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
                Img(src="https://placehold.co/200"),
                P(product["description"]),
                P(product["price"]),
                P(product["category"]),
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
                    H1(f"Products in {category}"),
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
