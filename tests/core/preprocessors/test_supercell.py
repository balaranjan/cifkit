import pytest

from cifkit.preprocessors.supercell import (
    get_supercell_points,
    get_unitcell_coords_for_all_labels,
)


@pytest.fixture
def unitcell_points_URhIn():
    unitcell_points = set(
        (
            (-0.2505, -0.2505, 0.5, "In1"),
            (0.0, 0.2505, 0.5, "In1"),
            (0.2505, 0.0, 0.5, "In1"),
            (-0.2505, -0.2505, -0.5, "In1"),
            (0.0, 0.2505, -0.5, "In1"),
            (0.2505, 0.0, -0.5, "In1"),
            (0.5925, 0.0, 0.0, "U1"),
            (-0.5925, -0.5925, 0.0, "U1"),
            (0.0, 0.5925, 0.0, "U1"),
            (0.33333, -0.33333, -0.5, "Rh1"),
            (0.66667, 0.33333, -0.5, "Rh1"),
            (0.33333, 0.66667, -0.5, "Rh1"),
            (-0.33333, 0.33333, 0.5, "Rh1"),
            (-0.66667, -0.33333, 0.5, "Rh1"),
            (-0.33333, -0.66667, -0.5, "Rh1"),
            (-0.33333, -0.66667, 0.5, "Rh1"),
            (-0.66667, -0.33333, -0.5, "Rh1"),
            (0.33333, -0.33333, 0.5, "Rh1"),
            (-0.33333, 0.33333, -0.5, "Rh1"),
            (0.66667, 0.33333, 0.5, "Rh1"),
            (0.33333, 0.66667, 0.5, "Rh1"),
            (0.0, 0.0, 0.0, "Rh2"),
        )
    )
    yield unitcell_points


@pytest.fixture
def supercell_2_points_URhIn():
    unitcell_points = set(
        (
            (0.2505, 1.0, 1.5, "In1"),
            (-0.33333, -0.66667, -0.5, "Rh1"),
            (0.33333, -0.33333, 0.5, "Rh1"),
            (0.7495, -0.2505, 1.5, "In1"),
            (0.66667, -0.66667, 1.5, "Rh1"),
            (1.0, 0.2505, 0.5, "In1"),
            (1.0, 1.5925, 1.0, "U1"),
            (1.0, 1.2505, -0.5, "In1"),
            (1.66667, 0.33333, 0.5, "Rh1"),
            (0.7495, -0.2505, -0.5, "In1"),
            (0.33333, -0.33333, 1.5, "Rh1"),
            (1.33333, 0.66667, -0.5, "Rh1"),
            (-0.5925, -0.5925, 0.0, "U1"),
            (-0.33333, 0.33333, 1.5, "Rh1"),
            (0.0, 1.2505, 1.5, "In1"),
            (1.2505, 1.0, 1.5, "In1"),
            (0.33333, 0.66667, 0.5, "Rh1"),
            (0.66667, 0.33333, 0.5, "Rh1"),
            (0.0, 1.0, 1.0, "Rh2"),
            (0.33333, -0.33333, -0.5, "Rh1"),
            (1.0, 0.2505, -0.5, "In1"),
            (1.5925, 1.0, 1.0, "U1"),
            (1.0, 0.0, 0.0, "Rh2"),
            (-0.2505, 0.7495, 1.5, "In1"),
            (0.4075, -0.5925, 0.0, "U1"),
            (0.0, 1.2505, -0.5, "In1"),
            (1.33333, -0.33333, 1.5, "Rh1"),
            (0.33333, 1.66667, 0.5, "Rh1"),
            (1.66667, 0.33333, -0.5, "Rh1"),
            (-0.2505, -0.2505, 0.5, "In1"),
            (0.2505, 0.0, 1.5, "In1"),
            (0.7495, 0.7495, 0.5, "In1"),
            (0.66667, 1.33333, 0.5, "Rh1"),
            (0.66667, 0.33333, 1.5, "Rh1"),
            (0.5925, 0.0, 1.0, "U1"),
            (0.33333, 1.66667, 1.5, "Rh1"),
            (0.66667, 0.33333, -0.5, "Rh1"),
            (0.33333, 0.66667, -0.5, "Rh1"),
            (-0.5925, 0.4075, 0.0, "U1"),
            (-0.33333, -0.66667, 0.5, "Rh1"),
            (0.0, 0.2505, 1.5, "In1"),
            (1.0, 1.2505, 1.5, "In1"),
            (0.0, 0.5925, 0.0, "U1"),
            (0.66667, 1.33333, 1.5, "Rh1"),
            (0.33333, 1.66667, -0.5, "Rh1"),
            (1.66667, 1.33333, 1.5, "Rh1"),
            (-0.2505, -0.2505, -0.5, "In1"),
            (-0.33333, 1.33333, 0.5, "Rh1"),
            (0.66667, -0.66667, 0.5, "Rh1"),
            (0.7495, 0.7495, -0.5, "In1"),
            (1.2505, 0.0, 0.5, "In1"),
            (0.66667, 1.33333, -0.5, "Rh1"),
            (-0.66667, -0.33333, 0.5, "Rh1"),
            (0.0, 1.5925, 1.0, "U1"),
            (0.4075, 0.4075, 1.0, "U1"),
            (0.5925, 1.0, 1.0, "U1"),
            (1.0, 0.5925, 0.0, "U1"),
            (0.33333, 0.66667, 1.5, "Rh1"),
            (-0.33333, 0.33333, 0.5, "Rh1"),
            (1.66667, 0.33333, 1.5, "Rh1"),
            (1.2505, 1.0, 0.5, "In1"),
            (0.0, 1.0, 0.0, "Rh2"),
            (-0.5925, -0.5925, 1.0, "U1"),
            (0.66667, -0.66667, -0.5, "Rh1"),
            (0.4075, -0.5925, 1.0, "U1"),
            (1.2505, 0.0, -0.5, "In1"),
            (-0.2505, 0.7495, 0.5, "In1"),
            (1.33333, 1.66667, 0.5, "Rh1"),
            (-0.66667, 0.66667, 0.5, "Rh1"),
            (1.0, 1.0, 1.0, "Rh2"),
            (0.0, 0.0, 0.0, "Rh2"),
            (0.2505, 1.0, 0.5, "In1"),
            (0.4075, 0.4075, 0.0, "U1"),
            (1.33333, 0.66667, 1.5, "Rh1"),
            (1.0, 0.0, 1.0, "Rh2"),
            (1.0, 1.5925, 0.0, "U1"),
            (-0.33333, 0.33333, -0.5, "Rh1"),
            (-0.2505, -0.2505, 1.5, "In1"),
            (1.2505, 1.0, -0.5, "In1"),
            (1.0, 0.2505, 1.5, "In1"),
            (0.0, 0.5925, 1.0, "U1"),
            (0.0, 0.2505, 0.5, "In1"),
            (1.33333, 1.66667, -0.5, "Rh1"),
            (-0.66667, 0.66667, -0.5, "Rh1"),
            (-0.33333, -0.66667, 1.5, "Rh1"),
            (-0.33333, 1.33333, 1.5, "Rh1"),
            (1.66667, 1.33333, 0.5, "Rh1"),
            (0.2505, 1.0, -0.5, "In1"),
            (1.5925, 0.0, 1.0, "U1"),
            (1.2505, 0.0, 1.5, "In1"),
            (1.5925, 1.0, 0.0, "U1"),
            (1.33333, -0.33333, 0.5, "Rh1"),
            (0.0, 1.2505, 0.5, "In1"),
            (-0.33333, 1.33333, -0.5, "Rh1"),
            (0.0, 1.5925, 0.0, "U1"),
            (0.2505, 0.0, 0.5, "In1"),
            (0.5925, 1.0, 0.0, "U1"),
            (0.0, 0.2505, -0.5, "In1"),
            (-0.66667, -0.33333, 1.5, "Rh1"),
            (1.5925, 0.0, 0.0, "U1"),
            (-0.66667, -0.33333, -0.5, "Rh1"),
            (1.66667, 1.33333, -0.5, "Rh1"),
            (1.0, 0.5925, 1.0, "U1"),
            (0.7495, 0.7495, 1.5, "In1"),
            (1.0, 1.2505, 0.5, "In1"),
            (-0.5925, 0.4075, 1.0, "U1"),
            (0.7495, -0.2505, 0.5, "In1"),
            (1.33333, -0.33333, -0.5, "Rh1"),
            (0.5925, 0.0, 0.0, "U1"),
            (1.0, 1.0, 0.0, "Rh2"),
            (1.33333, 0.66667, 0.5, "Rh1"),
            (0.2505, 0.0, -0.5, "In1"),
            (-0.2505, 0.7495, -0.5, "In1"),
            (1.33333, 1.66667, 1.5, "Rh1"),
            (-0.66667, 0.66667, 1.5, "Rh1"),
            (0.0, 0.0, 1.0, "Rh2"),
        )
    )
    yield unitcell_points


def test_get_unit_cell_coordinates(cif_block_URhIn, unitcell_points_URhIn):
    coordinates = get_unitcell_coords_for_all_labels(cif_block_URhIn)

    # Flatten the coordinates for comparision with the expected
    coordinates_set = set(
        tuple(coord) for sublist in coordinates for coord in sublist
    )

    # Compare the two sets
    assert coordinates_set == unitcell_points_URhIn


def test_get_supercell_points_full_shift(cif_block_URhIn):
    # +-1 +-1 +-1 shifts
    supercell_points = get_supercell_points(cif_block_URhIn, 3)
    assert len(supercell_points) == 336


def test_get_supercell_points_one_direction_shift(
    cif_block_URhIn, supercell_2_points_URhIn
):
    # +1 +1 +1 shifts
    supercell_points = get_supercell_points(cif_block_URhIn, 2)
    assert set(supercell_points) == supercell_2_points_URhIn
    assert len(supercell_points) == 116


def test_get_supercell_points_no_shift(cif_block_URhIn, unitcell_points_URhIn):
    # No sfhits
    supercell_points = get_supercell_points(cif_block_URhIn, 1)
    assert set(supercell_points) == unitcell_points_URhIn
    assert len(supercell_points) == 22
