import core.skeleton as skeleton
import core
from core.skeleton import Skeleton, SECTIONS


def test_skeleton_initialization():
    category = core.ADJECTIVES[3]
    skeleton = Skeleton(chaos_degree=2, category=category)
    assert skeleton.sections != SECTIONS


def test_skeleton_multiple_mutations():
    category = core.ADJECTIVES[2]
    skeleton_a = Skeleton(chaos_degree=5, category=category)
    assert skeleton.SECTIONS != skeleton_a.sections
    assert set(skeleton.SECTIONS) == set(skeleton_a.sections)
    skeleton_b = Skeleton(chaos_degree=5, category=category)
    assert skeleton_b.sections == skeleton_a.sections


def test_random_based_on_category():
    seed = 10
    random_number = skeleton.random_based_on_seed(seed)
    assert 0 <= random_number < 100
    assert skeleton.random_based_on_seed(seed) == random_number
