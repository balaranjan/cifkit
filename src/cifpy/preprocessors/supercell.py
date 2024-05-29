import numpy as np
import gemmi
from gemmi.cif import Block
from cifpy.utils import cif_parser, string_parser
from cifpy.utils import error_messages


def get_supercell_points(
    block,
    supercell_generation_method,
) -> list[tuple[float, float, float, str]]:
    """
    Return supercell points
    """
    supercell_points = []
    loop_values = cif_parser.get_loop_values(block)
    all_coords_list = get_unitcell_coords_for_all_labels(block)
    # Get the total number of atoms in the unit cell

    for i, all_coords in enumerate(all_coords_list):
        points = flatten_original_coordinates(all_coords)
        atom_site_label = loop_values[0][i]
        atom_site_type = loop_values[1][i]

        supercell_points.extend(
            shift_and_append_points(
                points,
                atom_site_label,
                supercell_generation_method,
            )
        )

        if (
            string_parser.get_atom_type_from_label(atom_site_label)
            != atom_site_type
        ):
            raise RuntimeError(
                "Different elements found in atom site and label"
            )
    return list(set(supercell_points))


def get_unitcell_coords_for_all_labels(
    block: Block,
) -> list[tuple[float, float, float, str]]:
    """
    Compute the new coordinates after applying
    symmetry operations to the initial coordinates.
    """

    loop_values = cif_parser.get_loop_values(block)
    loop_length = len(loop_values[0])
    coords_list = []
    for i in range(loop_length):
        site_label, _, coordinates = (
            cif_parser.get_label_occupancy_coordinates(loop_values, i)
        )
        coords_after_symmetry_operations = (
            get_unitcell_coords_after_sym_operations_per_label(
                block,
                coordinates,
                site_label,
            )
        )
        coords_list.append(coords_after_symmetry_operations)

    return coords_list


def get_unitcell_coords_after_sym_operations_per_label(
    block: Block,
    atom_site_fracs: list[float],
    atom_site_label: str,
) -> list[tuple[float, float, float, str]]:
    """
    Generate a list of coordinates for each atom
    site after applying symmetry operations.
    """
    all_coords = set()
    for operation in block.find_loop(
        "_space_group_symop_operation_xyz"
    ):
        operation = operation.replace("'", "")
        try:
            op = gemmi.Op(operation)
            new_x, new_y, new_z = op.apply_to_xyz(
                [
                    atom_site_fracs[0],
                    atom_site_fracs[1],
                    atom_site_fracs[2],
                ]
            )

            all_coords.add(
                (
                    round(new_x, 5),
                    round(new_y, 5),
                    round(new_z, 5),
                    atom_site_label,
                )
            )

        except RuntimeError as e:
            print(f"Skipping operation '{operation}': {str(e)}")
            raise RuntimeError(
                error_messages.StringParserError.INVALID_PARSED_ELEMENT.value
            ) from e

    return list(all_coords)


def flatten_original_coordinates(all_coords):
    points = np.array(
        [list(map(float, coord[:-1])) for coord in all_coords]
    )
    return points


def shift_and_append_points(
    points,
    atom_site_label: str,
    supercell_generation_method: int,
):
    """
    Shift and duplicate points to create a supercell.
    """

    # Method 1 - No sfhits
    # Method 2 - +1 +1 +1 shifts
    # Method 3 - +-1 +-1 +-1 shifts

    if supercell_generation_method == 1:
        shifts = np.array([[0, 0, 0]])
        shifted_points = points[:, None, :] + shifts[None, :, :]
        all_points = []
        for point_group in shifted_points:
            for point in point_group:
                new_point = (*np.round(point, 5), atom_site_label)
                all_points.append(new_point)
        return all_points

    if supercell_generation_method == 2:
        shifts = np.array(
            [
                [0, 0, 0],
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [1, 1, 0],
                [1, 0, 1],
                [0, 1, 1],
                [1, 1, 1],
            ]
        )
        shifted_points = points[:, None, :] + shifts[None, :, :]
        all_points = []
        for point_group in shifted_points:
            for point in point_group:
                new_point = (*np.round(point, 5), atom_site_label)
                all_points.append(new_point)

        return all_points

    if supercell_generation_method == 3:
        shifts = np.array(
            [
                [0, 0, 0],
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [-1, 0, 0],
                [0, -1, 0],
                [0, 0, -1],
                [1, 1, 0],
                [1, -1, 0],
                [-1, 1, 0],
                [-1, -1, 0],
                [1, 0, 1],
                [1, 0, -1],
                [0, 1, 1],
                [0, 1, -1],
                [-1, 0, 1],
                [-1, 0, -1],
                [0, -1, 1],
                [0, -1, -1],
                [1, 1, 1],
                [1, 1, -1],
                [1, -1, 1],
                [1, -1, -1],
                [-1, 1, 1],
                [-1, 1, -1],
                [-1, -1, 1],
                [-1, -1, -1],
            ]
        )

        shifted_points = points[:, None, :] + shifts[None, :, :]
        all_points = []
        for point_group in shifted_points:
            for point in point_group:
                new_point = (*np.round(point, 5), atom_site_label)
                all_points.append(new_point)

        return all_points
