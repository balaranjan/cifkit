class Cif:
    def __init__(self, file_path: str) -> None:
        """Initialize the Cif object with the file path."""
        self.file_path = file_path
        self.connections = None  # Private attribute to store connections
        self._shortest_pair_distance = None
        self._preprocess()
        self._load_data()

    def _preprocess(self):
        """Preprocess each .cif file and check any error."""
        check_unique_atom_site_labels(self.file_path)
        remove_author_loop(self.file_path)
        preprocess_label_element_loop_values(self.file_path)

    def _load_data(self):
        """Load data from the .cif file and process it."""

        self._block = get_cif_block(self.file_path)
        self._parse_cif_data()
        self._generate_supercell()

    def _parse_cif_data(self):
        """Parse the main CIF data from the block."""
        self._loop_values = get_loop_values(self._block)
        self.unitcell_lengths = get_unitcell_lengths(self._block)
        self.unitcell_angles = get_unitcell_angles_rad(self._block)
        self.site_labels = get_unique_site_labels(self._loop_values)
        self.unique_elements = get_unique_elements_from_loop(self._loop_values)
        (
            self.formula,
            self.structure,
            self.weight,
            self.space_group_number,
            self.space_group_name,
        ) = get_formula_structure_weight_s_group(self._block)
        self.tag = get_tag_from_third_line(self.file_path)
        self.atom_site_info = parse_atom_site_occupancy_info(self.file_path)
        self.heterogeneous_bond_pairs = get_heterogenous_element_pairs(
            self.formula
        )
        self.homogenous_bond_pairs = get_homogenous_element_pairs(self.formula)
        self.all_bond_pairs = get_all_bond_pairs(self.formula)

    def _generate_supercell(self):
        """Generate supercell information based on the unit cell data."""
        self.unitcell_points = get_supercell_points(self._block, 1)
        self.supercell_points = get_supercell_points(self._block, 3)
        self.unitcell_atom_count = get_cell_atom_count(self.unitcell_points)
        self.supercell_atom_count = get_cell_atom_count(self.supercell_points)

    def compute_connections(self, cutoff_radius=10.0):
        """Compute nearest neighbor connections per site label."""
        self.connections = get_site_connections(
            [
                self.site_labels,
                self.unitcell_lengths,
                self.unitcell_angles,
            ],
            self.unitcell_points,
            self.supercell_points,
            cutoff_radius=cutoff_radius,
        )
        self._shortest_pair_distance = get_shortest_distance(self.connections)
        self._connections_CN = filter_connections_with_cn(self.connections)
        self._shortest_distance_per_label = get_shortest_distance_per_label(
            self.connections
        )
        self._bond_counts_CN = get_bond_counts_CN(
            self.formula, self.connections_CN
        )
        self._bond_fraction_CN = get_bond_fraction_CN(self.bond_counts_CN)

    def get_polyhedron_labels_from_site(
        self, label: str
    ) -> tuple[list[list[float]], list[str]]:
        if self.compute_connections is None:
            self.compute_connections()
        return get_polyhedron_coordinates_labels(self.connections_CN, label)

    def plot_polyhedron(self, site_label, output_dir=None):
        if self.connections is None:
            self.compute_connections()
        coords, labels = get_polyhedron_coordinates_labels(
            self.connections_CN, site_label
        )
        polyhedron.plot(coords, labels, self.file_path, output_dir)

    @property
    def shortest_pair_distance(self):
        """Property that checks if connections are computed and computes them if not."""
        if self.connections is None:
            self.compute_connections()
        return self._shortest_pair_distance

    @property
    def connections_CN(self):
        """Property that checks if connections are computed and computes them if not."""
        if self.connections is None:
            self.compute_connections()
        return self._connections_CN

    def print_connected_points(self):
        prompt.log_connected_points(self.connections)

    @property
    def shortest_distance_per_label(self):
        if self.connections is None:
            self.compute_connections()
        return self._shortest_distance_per_label

    @property
    def bond_counts_CN(self):
        if self.connections is None:
            self.compute_connections()
        return self._bond_counts_CN

    @property
    def bond_fraction_CN(self):
        if self.connections is None:
            self.compute_connections()
        return self._bond_fraction_CN


"""
Import statements placed bottom to avoid cluttering.
"""

# Polyhedron
from cifpy.figures import polyhedron


# Parser .cif file
from cifpy.utils.cif_parser import (
    get_cif_block,
    get_loop_values,
    get_unitcell_lengths,
    get_unitcell_angles_rad,
    get_unique_site_labels,
    get_unique_elements_from_loop,
    get_formula_structure_weight_s_group,
    get_tag_from_third_line,
    parse_atom_site_occupancy_info,
    check_unique_atom_site_labels,
)

# Edit .cif file
from cifpy.preprocessors.format import preprocess_label_element_loop_values
from cifpy.utils.cif_editor import remove_author_loop


from cifpy.coordination.distance import (
    get_shortest_distance,
    get_shortest_distance_per_label,
)
from cifpy.coordination.composition import (
    get_bond_counts_CN,
    get_bond_fraction_CN,
)
from cifpy.coordination.coordinate import get_polyhedron_coordinates_labels
from cifpy.preprocessors.supercell import get_supercell_points

from cifpy.preprocessors.supercell_util import get_cell_atom_count
from cifpy.preprocessors.environment import (
    get_site_connections,
    filter_connections_with_cn,
)

from cifpy.utils import prompt
from cifpy.utils.bond_pair import (
    get_heterogenous_element_pairs,
    get_homogenous_element_pairs,
    get_all_bond_pairs,
)
