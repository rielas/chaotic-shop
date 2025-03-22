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
    Header,
    Nav,
    Ul,
    Li,
    Style,
)
import core
from core.skeleton import Skeleton
from chaotic_shop.style import CSS


def product_page(product_id: int):
    categories = core.ADJECTIVES
    product = core.generate_product_by_id(product_id)
    category = product["category"]
    skeleton = Skeleton(chaos_degree=1, category=category)
    elements = skeleton.get_elements()
    category_list = Div(
        *[Li(A(category, href=f"/category/{category}")) for category in categories],
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
                content.append(P(product["description"]))
            elif element == "back_to_products":
                content.append(
                    Div(
                        A("Back to products", href="/", _class="navigation-button"),
                        _class="navigation",
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
                        _class="container",
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
                        _class="container",
                    )
                )
            elif element == "navigation":
                content.append(
                    Div(
                        Div(
                            A("Previous Product", href=f"/product/{previous_id}")
                            if previous_id is not None
                            else "",
                            _class="navigation-left",
                        ),
                        Div(
                            A("Next Product", href=f"/product/{next_id}")
                            if next_id is not None
                            else "",
                            _class="navigation-right",
                        ),
                        _class="navigation",
                    )
                )

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
                    Div(category_list, _class="sidebar-container"),
                    Div(
                        H1(product["name"]),
                        P(product["price"]),
                        P(product["category"]),
                        *content,
                        _class="main-content",
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
