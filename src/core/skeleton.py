from dataclasses import dataclass
import random
import core

SECTIONS = [
    "image",
    "price",
    "description",
    "checkout",
    "leave_review",
    "back_to_products",
    "navigation",
]


@dataclass
class Reorder:
    step: int


@dataclass
class AddDescriptionId:
    step: int
    category: str

    def get_id(self) -> str:
        """
        Get id for description section.
        """
        category_index = core.ADJECTIVES.index(self.category)
        random = random_based_on_seed(category_index * 1000, 1000)
        return f"{self.category.lower()}_{random}"


@dataclass
class AddBackToProductsId:
    step: int
    category: str

    def get_id(self) -> str:
        """
        Get id for back_to_products section.
        """
        category_index = core.ADJECTIVES.index(self.category)
        random = random_based_on_seed(category_index * 1000, 1000)
        return f"{self.category.lower()}_{random}"


@dataclass
class AddLeaveReviewId:
    step: int
    category: str

    def get_id(self) -> str:
        """
        Get id for leave_review section.
        """
        category_index = core.ADJECTIVES.index(self.category)
        random = random_based_on_seed(category_index * 1000, 1000)
        return f"{self.category.lower()}_{random}"


@dataclass
class AddCheckoutId:
    step: int
    category: str

    def get_id(self) -> str:
        """
        Get id for checkout section.
        """
        category_index = core.ADJECTIVES.index(self.category)
        random = random_based_on_seed(category_index * 1000, 1000)
        return f"{self.category.lower()}_{random}"


@dataclass
class AddNavigationId:
    step: int
    category: str

    def get_id(self) -> str:
        """
        Get id for navigation section.
        """
        category_index = core.ADJECTIVES.index(self.category)
        random = random_based_on_seed(category_index * 1000, 1000)
        return f"{self.category.lower()}_{random}"


@dataclass
class AddPriceId:
    step: int
    category: str

    def get_id(self) -> str:
        """
        Get id for price section.
        """
        category_index = core.ADJECTIVES.index(self.category)
        random = random_based_on_seed(category_index * 1000, 1000)
        return f"{self.category.lower()}_{random}"


@dataclass
class AddImageId:
    step: int
    category: str

    def get_id(self) -> str:
        """
        Get id for image section.
        """
        category_index = core.ADJECTIVES.index(self.category)
        random = random_based_on_seed(category_index * 1000, 1000)
        return f"{self.category.lower()}_{random}"


@dataclass
class ChangeCheckoutText:
    step: int
    product_id: int

    def get_text(self) -> str:
        """
        Get the modified checkout text.
        """
        return f"Checkout now! (only {self.product_id} items left!)"


@dataclass
class ChangeLeaveReviewText:
    step: int
    product_id: int

    def get_text(self) -> str:
        """
        Get the modified leave review text.
        """
        return f"Share your thoughts about product #{self.product_id}!"


@dataclass
class FlipLastName:
    step: int

    def flip(self) -> bool:
        """
        Flip the last name flag based on the step.
        """
        return self.step % 2 == 0


@dataclass
class FlipEmail:
    step: int

    def flip(self) -> bool:
        """
        Flip the email flag based on the step.
        """
        return self.step % 2 == 0


Mutation = (
    Reorder
    | AddDescriptionId
    | AddBackToProductsId
    | AddLeaveReviewId
    | AddCheckoutId
    | AddNavigationId
    | AddPriceId
    | AddImageId
    | ChangeCheckoutText
    | ChangeLeaveReviewText
    | FlipLastName
    | FlipEmail
)


def choose_mutation(step: int, category: str, product_id: int = 0) -> Mutation:
    """
    Choose a mutation based on the step and category.
    """
    category_index = core.ADJECTIVES.index(category)

    mutation = random_based_on_seed(
        category_index * 1000 + product_id + step, len(Mutation.__args__) + 4
    )
    match mutation:
        case 0:
            return AddDescriptionId(step, category)
        case 1:
            return AddBackToProductsId(step, category)
        case 2:
            return AddLeaveReviewId(step, category)
        case 3:
            return AddCheckoutId(step, category)
        case 4:
            return AddNavigationId(step, category)
        case 5:
            return AddPriceId(step, category)
        case 6:
            return AddImageId(step, category)
        case 7:
            return ChangeCheckoutText(step, product_id)
        case 8:
            return ChangeLeaveReviewText(step, product_id)
        case 9:
            return FlipLastName(step)
        case 10:
            return FlipEmail(step)
        case _:
            return Reorder(step)


def generate_mutations(
    category_chaos: int,
    category: str,
    product_chaos: int = 0,
    product_id: int | None = None,
) -> list[Mutation]:
    """
    Generate a list of mutations based on the chaos degree and category.
    """
    mutations = []

    for i in range(category_chaos):
        mutation = choose_mutation(i, category)
        mutations.append(mutation)

    for i in range(product_chaos):
        mutation = choose_mutation(i, category, product_id)
        mutations.append(mutation)

    return mutations


def random_based_on_seed(seed: int, end: int = 100) -> int:
    """
    Generate a random number based on the seed
    """
    random.seed(seed)
    return random.randint(0, end - 1)


def make_random_move(i: int, elements: list[str], category: str) -> list[str]:
    moved = elements.copy()
    category_index = core.ADJECTIVES.index(category)
    random_position = random_based_on_seed(category_index * 1000 + i, len(moved) - 1)
    assert 0 <= random_position < len(moved) - 1
    moved[random_position], moved[random_position + 1] = (
        moved[random_position + 1],
        moved[random_position],
    )
    return moved


class Skeleton:
    def __init__(
        self, chaos_degree: int, category: str, product_id: int, product_chaos: int = 0
    ):
        if category not in core.ADJECTIVES:
            raise ValueError(f"Invalid category: {category}")

        if chaos_degree < 0:
            raise ValueError(f"Chaos degree must be non-negative, got {chaos_degree}")

        self.mutations = generate_mutations(
            chaos_degree, category, product_chaos, product_id
        )
        self.category = category
        self.sections = SECTIONS
        self.description_id = None
        self.back_to_products_id = None
        self.leave_review_id = None
        self.checkout_id = None
        self.checkout_text = None
        self.leave_review_text = None
        self.last_name = False
        self.email = False
        self.navigation_id = None
        self.price_id = None
        self.image_id = None
        self._apply_mutation()

    def _apply_mutation(self):
        for i, mutation in enumerate(self.mutations):
            match mutation:
                case Reorder(step):
                    self.sections = make_random_move(step, self.sections, self.category)
                case AddDescriptionId(step, _):
                    self.description_id = mutation.get_id()
                case AddBackToProductsId(step, _):
                    self.back_to_products_id = mutation.get_id()
                case AddLeaveReviewId(step, _):
                    self.leave_review_id = mutation.get_id()
                case AddCheckoutId(step, _):
                    self.checkout_id = mutation.get_id()
                case AddNavigationId(step, _):
                    self.navigation_id = mutation.get_id()
                case AddPriceId(step, _):
                    self.price_id = mutation.get_id()
                case AddImageId(step, _):
                    self.image_id = mutation.get_id()
                case ChangeCheckoutText(step, product_id):
                    self.checkout_text = mutation.get_text()
                case ChangeLeaveReviewText(step, product_id):
                    self.leave_review_text = mutation.get_text()
                case FlipLastName(step):
                    self.last_name = mutation.flip()
                case FlipEmail(step):
                    self.email = mutation.flip()
