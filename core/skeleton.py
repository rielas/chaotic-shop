from dataclasses import dataclass
import random

SECTIONS = ["description", "back_to_products", "leave_review", "checkout", "navigation"]


@dataclass
class Reorder:
    pass


Mutation = Reorder


def generate_mutations(chaos_degree: int, category: str) -> list[Mutation]:
    """
    Generate a list of mutations based on the chaos degree and category.
    """
    mutations = []

    for _ in range(chaos_degree):
        mutation = Reorder
        mutations.append(mutation)

    return mutations


def make_random_move(elements: list[str], category: str) -> list[str]:
    moved = elements.copy()
    random_position = random.randint(0, len(moved) - 2)
    moved[random_position], moved[random_position + 1] = (
        moved[random_position + 1],
        moved[random_position],
    )
    return moved


class Skeleton:
    def __init__(self, chaos_degree: int, category: str):
        self.mutations = generate_mutations(chaos_degree, category)
        self.category = category
        self.elements = SECTIONS
        self._apply_mutation()

    def _apply_mutation(self):
        for mutation in self.mutations:
            match mutation:
                case Reorder:
                    self.elements = make_random_move(self.elements, self.category)

    def get_elements(self) -> list[str]:
        return self.elements
