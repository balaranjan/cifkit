from cifpy.utils import formula
from itertools import combinations


def get_possible_heterogenous_element_pairs(
    formula_str: str,
) -> list[tuple[str, str]]:
    """
    Generate all possible unique alphabetically sorted heterogenious pairs.
    """
    elements = formula.get_unique_elements(formula_str)

    # Generate all possible pairs using combinations ensuring uniqueness
    all_pairs = list(combinations(sorted(elements), 2))

    # 'combinations' already sorts them alphabetically, see the test
    return all_pairs


def get_possible_homogenous_element_pairs(
    formula_str: str,
) -> list[tuple[str, str]]:
    """
    Generate all possible sorted homogenous bonding pairs from a formula.
    """
    elements = formula.get_unique_elements(formula_str)
    # Sort the elements alphabetically
    elements.sort()
    homogenous_pairs = [(element, element) for element in elements]
    return homogenous_pairs
