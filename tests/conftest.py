# conftest.py
import pytest
from cifpy.preprocessors import (
    supercell,
    environment,
    environment_util,
)
from cifpy.utils import cif_parser, folder
from cifpy.models.cif import Cif
from cifpy.models.cif_ensemble import CifEnsemble
from cifpy.preprocessors import environment
from cifpy.coordination import composition


"""
CifEnsemble - histogram test
"""


@pytest.fixture(scope="module")
def cif_ensemble_histogram_test() -> CifEnsemble:
    return CifEnsemble("tests/data/cif/histogram")


"""
CifEnsemble - test folder
"""


@pytest.fixture(scope="module")
def cif_ensemble_test() -> CifEnsemble:
    return CifEnsemble("tests/data/cif/ensemble_test")


# Folder
@pytest.fixture(scope="module")
def cif_folder_path_test():
    return "tests/data/cif/folder"


# Multiple files
@pytest.fixture(scope="module")
def parsed_formula_weight_structure_s_group_data(
    cif_folder_path_test,
):
    results = cif_parser.get_unique_formulas_structures_weights_s_groups(
        cif_folder_path_test
    )
    return results


@pytest.fixture(scope="module")
def file_paths_test(cif_folder_path_test):
    return folder.get_file_path_list(cif_folder_path_test)


"""
Cif - URhIn
"""


@pytest.fixture(scope="module")
def file_path_URhIn():
    return "tests/data/cif/URhIn.cif"


@pytest.fixture(scope="module")
def formula_URhIn():
    return "URhIn"


@pytest.fixture(scope="module")
def cif_block_URhIn(file_path_URhIn):
    return cif_parser.get_cif_block(file_path_URhIn)


@pytest.fixture(scope="module")
def unique_site_labels_URhIn(loop_values_URhIn):
    return cif_parser.get_unique_site_labels(loop_values_URhIn)


@pytest.fixture(scope="module")
def loop_values_URhIn(cif_block_URhIn):
    return cif_parser.get_loop_values(cif_block_URhIn)


@pytest.fixture(scope="module")
def unitcell_coords_URhIn(cif_block_URhIn):
    return supercell.get_unitcell_coords_for_all_labels(cif_block_URhIn)


@pytest.fixture(scope="module")
def unitcell_points_URhIn(cif_block_URhIn):
    return supercell.get_supercell_points(cif_block_URhIn, 1)


@pytest.fixture(scope="module")
def supercell_points_URhIn(cif_block_URhIn):
    return supercell.get_supercell_points(cif_block_URhIn, 3)


@pytest.fixture(scope="module")
def lenghts_URhIn(cif_block_URhIn) -> list[float]:
    lenghts = cif_parser.get_unitcell_lengths(cif_block_URhIn)
    return lenghts


@pytest.fixture(scope="module")
def angles_rad_URhIn(cif_block_URhIn) -> list[float]:
    angles_rad = cif_parser.get_unitcell_angles_rad(cif_block_URhIn)
    return angles_rad


@pytest.fixture(scope="module")
def site_labels_URhIn(loop_values_URhIn):
    return cif_parser.get_unique_site_labels(loop_values_URhIn)


@pytest.fixture(scope="module")
def parsed_cif_data_URhIn(
    unique_site_labels_URhIn, lenghts_URhIn, angles_rad_URhIn
) -> tuple[list[str], list[float], list[float]]:
    return (unique_site_labels_URhIn, lenghts_URhIn, angles_rad_URhIn)


@pytest.fixture(scope="module")
def radii_data_URhIn() -> dict:
    return {
        "In": {
            "CIF_radius": 1.624,
            "CIF_radius_refined": 1.3283,
            "Pauling_radius_CN12": 1.66,
        },
        "Rh": {
            "CIF_radius": 1.345,
            "CIF_radius_refined": 1.3687,
            "Pauling_radius_CN12": 1.342,
        },
        "U": {
            "CIF_radius": 1.377,
            "CIF_radius_refined": 1.6143,
            "Pauling_radius_CN12": 1.51,
        },
    }


# Init
@pytest.fixture(scope="module")
def cif_URhIn(file_path_URhIn):
    return Cif(file_path_URhIn)


@pytest.fixture(scope="module")
def connections_URhIn(
    parsed_cif_data_URhIn,
    unitcell_points_URhIn,
    supercell_points_URhIn,
):

    return environment.get_site_connections(
        parsed_cif_data_URhIn,
        unitcell_points_URhIn,
        supercell_points_URhIn,
        cutoff_radius=10.0,
    )


@pytest.fixture(scope="module")
def connections_CN_URhIn(connections_URhIn):
    return environment.filter_connections_with_cn(connections_URhIn)


@pytest.fixture(scope="module")
def flattened_connections_URhIn(connections_URhIn):
    return environment_util.flat_site_connections(connections_URhIn)


@pytest.fixture(scope="module")
def bond_counts_CN(formula_URhIn, connections_CN_URhIn):
    return composition.get_bond_counts(formula_URhIn, connections_CN_URhIn)
