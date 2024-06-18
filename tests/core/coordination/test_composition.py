import pytest

from cifkit.coordination.composition import (
    get_bond_counts,
    get_bond_fractions,
    count_connections_per_site,
    compute_avg_CN,
    get_unique_CN_values,
)


def test_get_bond_counts(formula_URhIn, CN_connections_by_min_dist_URhIn):
    expected = {
        "In1": {("In", "In"): 4, ("In", "Rh"): 4, ("In", "U"): 6},
        "Rh1": {("In", "Rh"): 3, ("Rh", "U"): 6},
        "Rh2": {("In", "Rh"): 6, ("Rh", "U"): 3},
        "U1": {("In", "U"): 6, ("Rh", "U"): 5},
    }
    assert (
        get_bond_counts(formula_URhIn, CN_connections_by_min_dist_URhIn)
        == expected
    )


def test_get_bond_fraction(bond_counts_CN):
    # Expected output based on input data
    expected_fractions = {
        ("In", "In"): 4 / 43,
        ("In", "Rh"): 13 / 43,
        ("In", "U"): 12 / 43,
        ("Rh", "U"): 14 / 43,
    }

    # Testing the actual function output
    result = get_bond_fractions(bond_counts_CN)

    # Testing each bond fraction to ensure they are within a small tolerance
    for bond_type, expected_fraction in expected_fractions.items():
        assert pytest.approx(result[bond_type], 0.005) == expected_fraction

    # Testing to ensure the fractions sum approximately to 1
    assert pytest.approx(sum(result.values()), 0.005) == 1


def test_get_coordination_numbers(CN_connections_by_min_dist_URhIn):
    expected = {"In1": 14, "Rh1": 9, "Rh2": 9, "U1": 11}
    assert (
        count_connections_per_site(CN_connections_by_min_dist_URhIn)
        == expected
    )


def test_get_average_coordination_number(
    CN_connections_by_min_dist_URhIn,
):
    assert compute_avg_CN(CN_connections_by_min_dist_URhIn) == 10.75


def test_get_unique_coordination_number(
    CN_connections_by_min_dist_URhIn,
):
    assert get_unique_CN_values(CN_connections_by_min_dist_URhIn) == {
        9,
        11,
        14,
    }
