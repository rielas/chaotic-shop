from dataclasses import dataclass
import random
import core

SECTIONS = ["description", "back_to_products", "leave_review", "checkout", "navigation"]


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


Mutation = Reorder | AddDescriptionId | AddBackToProductsId | AddLeaveReviewId


def choose_mutation(step: int, category: str) -> Mutation:
    """
    Choose a mutation based on the step and category.
    """
    category_index = core.ADJECTIVES.index(category)

    mutation = random_based_on_seed(
        category_index * 1000 + step, len(Mutation.__args__)
    )
    match mutation:
        case 0:
            return AddDescriptionId(step, category)
        case 1:
            return Reorder(step)
        case 2:
            return AddBackToProductsId(step, category)
        case 3:
            return AddLeaveReviewId(step, category)
        case _:
            raise ValueError(f"Invalid mutation type: {mutation}")


def generate_mutations(chaos_degree: int, category: str) -> list[Mutation]:
    """
    Generate a list of mutations based on the chaos degree and category.
    """
    mutations = []

    for i in range(chaos_degree):
        mutation = choose_mutation(i, category)
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
    def __init__(self, chaos_degree: int, category: str):
        if category not in core.ADJECTIVES:
            raise ValueError(f"Invalid category: {category}")

        if chaos_degree < 0:
            raise ValueError(f"Chaos degree must be non-negative, got {chaos_degree}")

        self.mutations = generate_mutations(chaos_degree, category)
        self.category = category
        self.sections = SECTIONS
        self.description_id = None
        self.back_to_products_id = None
        self.leave_review_id = None
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
