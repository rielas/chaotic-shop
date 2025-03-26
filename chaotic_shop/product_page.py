from fasthtml.common import (
    Title,
    Main,
    Img,
    Div,
    H1,
    H2,
    P,
    A,
    Form,
    Input,
    Textarea,
    Label,
    Nav,
    Ul,
    Li,
    Aside,
    Section,
)
import core
from core.skeleton import Skeleton
import chaotic_shop


def product_page(product_id: int):
    categories = core.ADJECTIVES
    product = core.generate_product_by_id(product_id)
    category = product["category"]
    skeleton = Skeleton(chaos_degree=chaotic_shop.CHAOS_DEGREE, category=category)
    elements = skeleton.sections
    category_list = Nav(
        Ul(*[Li(A(category, href=f"/category/{category}")) for category in categories]),
        _class="sidebar",
    )

    if product:
        next_id = core.next_product_id_in_category(product["category"], product_id)
        previous_id = core.previous_product_id_in_category(
            product["category"], product_id
        )

        content = []
        for element in elements:
            if element == "description":
                content.append(
                    P(
                        product["description"],
                        _class="product-description",
                        id=skeleton.description_id if skeleton.description_id else None,
                    )
                )
            elif element == "back_to_products":
                content.append(
                    Div(
                        A("Back to products", href="/", _class="navigation-button"),
                        _class="navigation",
                        id=(
                            skeleton.back_to_products_id
                            if skeleton.back_to_products_id
                            else None
                        ),
                    )
                )
            elif element == "leave_review":
                content.append(
                    Div(
                        H2("Leave a Review"),
                        Form(
                            Input(type="hidden", name="product_id", value=product_id),
                            Div(
                                Label("Name:"),
                                Input(type="text", name="name", required=True),
                            ),
                            Div(
                                Label("Review:"), Textarea(name="review", required=True)
                            ),
                            Div(Input(type="submit", value="Submit")),
                            method="post",
                            action="/submit_review",
                        ),
                        _class="leave-review-id container",
                        id=(
                            skeleton.leave_review_id
                            if skeleton.leave_review_id
                            else None
                        ),
                    )
                )
            elif element == "checkout":
                content.append(
                    Div(
                        H2("Checkout"),
                        Form(
                            Input(type="hidden", name="product_id", value=product_id),
                            Div(Input(type="submit", value="Checkout")),
                            method="post",
                            action="/checkout",
                        ),
                        _class="container checkout",
                        id=skeleton.checkout_id if skeleton.checkout_id else None,
                    )
                )
            elif element == "navigation":
                content.append(
                    Div(
                        Div(
                            (
                                A("Previous Product", href=f"/product/{previous_id}")
                                if previous_id is not None
                                else ""
                            ),
                            _class="navigation-left",
                        ),
                        Div(
                            (
                                A("Next Product", href=f"/product/{next_id}")
                                if next_id is not None
                                else ""
                            ),
                            _class="navigation-right",
                        ),
                        _class="navigation",
                    )
                )

        return (
            Title(product["name"]),
            Main(
                Div(
                    chaotic_shop.navigation(),
                    _class="container",
                ),
                Div(
                    Aside(category_list),
                    Section(
                        H1(product["name"]),
                        Img(src="https://placehold.co/300"),
                        P(product["price"]),
                        P(product["category"]),
                        *content,
                        _class="main-content",
                    ),
                    _class="container content-wrapper",
                ),
            ),
        )
    else:
        return (
            Title("Product not found"),
            Main(
                Div(
                    chaotic_shop.navigation(),
                    _class="container",
                ),
                Div(
                    H1("Product not found"),
                    A("Back to products", href="/"),
                    _class="container",
                ),
            ),
        )
