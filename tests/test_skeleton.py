import pytest
from core.skeleton import Skeleton, SECTIONS


def test_skeleton_initialization():
    skeleton = Skeleton(chaos_degree=1, category="test")
    assert skeleton.category == "test"
    assert skeleton.elements != SECTIONS


def test_skeleton_multiple_mutations():
    skeleton = Skeleton(chaos_degree=1, category="test")
    initial_elements = skeleton.get_elements().copy()
    skeleton._apply_mutation()
    mutated_elements = skeleton.get_elements()
    assert initial_elements != mutated_elements
    assert set(initial_elements) == set(mutated_elements)
