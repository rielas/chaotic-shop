from fasthtml.common import (
    Title,
    Main,
    Strong,
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
                        _class="back-to-products",
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
                        _class="leave-review container",
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
                    Nav(
                        Ul(
                            Li(
                                (
                                    A(
                                        "Previous",
                                        href=f"/product/{previous_id}",
                                    )
                                    if previous_id is not None
                                    else ""
                                ),
                                _class="navigation-left",
                            ),
                            Li(
                                (
                                    A("Next", href=f"/product/{next_id}")
                                    if next_id is not None
                                    else ""
                                ),
                                _class="navigation-right",
                            ),
                            _class="navigation-previous-next",
                        ),
                        _class="navigation",
                        id=skeleton.navigation_id if skeleton.navigation_id else None,
                    )
                )
            elif element == "price":
                content.append(
                    P(
                        Strong(product["price"]),
                        _class="product-price",
                        id=skeleton.price_id if skeleton.price_id else None,
                    )
                )
            elif element == "image":
                content.append(
                    Img(
                        src=f"https://picsum.photos/id/{product['id'] % 1000}/300/200",
                        id=skeleton.image_id if skeleton.image_id else None,
                        _class="product-image",
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
                        chaotic_shop.breadcrumbs(
                            [
                                ("Categories", "/"),
                                (category, f"/category/{category}"),
                                product["name"],
                            ]
                        ),
                        P(product["category"]),
                        *content,
                        _class="main-content centered container",
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
