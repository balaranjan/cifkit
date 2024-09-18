# cifkit

![Integration Tests](https://github.com/bobleesj/cifkit/actions/workflows/python-run-pytest.yml/badge.svg)
[![codecov](https://codecov.io/gh/bobleesj/cifkit/graph/badge.svg?token=AN2YAC337A)](https://codecov.io/gh/bobleesj/cifkit)
![Python - Version](https://img.shields.io/pypi/pyversions/quacc)
[![PyPi version](https://img.shields.io/pypi/v/cifkit.svg)](https://pypi.python.org/pypi/cifkit)

<a href="https://joss.theoj.org/papers/9016ae27b8c6fddffaae5aeb8be18d19"><img src="https://joss.theoj.org/papers/9016ae27b8c6fddffaae5aeb8be18d19/status.svg"></a>

![Logo light mode](assets/img/logo-black.png#gh-light-mode-only "cifkit logo light")
![Logo dark mode](assets/img/logo-color.png#gh-dark-mode-only "cifkit logo dark")

`cifkit` is designed to provide a set of fully-tested utility functions and
variables for handling large datasets, on the order of tens of thousands, of
`.cif` files.

> The current codebase and documentation are actively being improved as of Sep
> 18, 2024.

## What cifkit does

`cifkit` provides higher-level functions in just a few lines of code.

- **Coordination geometry** - `cifkit` provides fuctions for visualing
  coordination geometry from each site and extracts physics-based features like
  volume and packing efficiency in each polyhedron.
- **Atomic mixing** - `cifkit` extracts atomic mixing information at the bond
  pair level—tasks that would otherwise require extensive manual effort using
  GUI-based tools like VESTA, Diamond, and CrystalMaker.
- **Filter** - `cifkit` offers features for preprocessing. It systematically
  addresses common issues in CIF files from databases, such as incorrect loop
  values and missing fractional coordinates, by standardizing and filtering out
  ill-formatted files. It also preprocesses atomic site labels, transforming
  labels such as 'M1' to 'Fe1' in files with atomic mixing.
- **Sort** - `cifkit` allows you to copy, move, and sort `.cif` files based on
  attributes such as coordination numbers, space groups, unit cells, shortest
  distances, elements, and more.

### Example usage 1

The example below uses `cifkit` to visualize the polyhedron generated from each atomic site based on the
coordination number geometry.

```python
from cifkit import Cif

cif = Cif("your_cif_file_path")
site_labels = cif.site_labels

# Loop through each site label
for label in site_labels:
    # Dipslay each polyhedron, .png saved for each label
    cif.plot_polyhedron(label, is_displayed=True)
```

![Polyhedron generation](assets/img/ErCoIn_polyhedron.png)

### Example Usage 2

The following example generates a distribution of structure.

```python
from cifkit import CifEnsemble

ensemble = CifEnsemble("cif_containing_folder_path")
ensemble.generate_structure_histogram()
```

![structure distribution](assets/img/histogram-structure.png)

To learn more, please read the official documention here:
https://bobleesj.github.io/cifkit.

## Documentation

- [Official documentation](https://bobleesj.github.io/cifkit)
- [Developer guide](https://github.com/bobleesj/cifkit/blob/main/CONTRIBUTING.md)
- [MIT license](https://github.com/bobleesj/cifkit/blob/main/LICENSE)

## How to contribute

Here is how you can contribute to the `cifkit` project if you found it helpful:

- Star the repository on GitHub and recommend it to your colleagues who might
  find `cifkit` helpful as well.
  [![Star GitHub repository](https://img.shields.io/github/stars/bobleesj/cifkit.svg?style=social)](https://github.com/bobleesj/cifkit/stargazers)
- Create a new issue for any bugs or feature requests
  [here](https://github.com/bobleesj/cifkit/issues)
- Fork the repository and consider contributing changes via a pull request.
  [![Fork GitHub repository](https://img.shields.io/github/forks/bobleesj/cifkit?style=social)](https://github.com/bobleesj/cifkit/fork).
  Check out
  [CONTRIBUTING.md](https://github.com/bobleesj/cifkit/blob/main/CONTRIBUTING.md)
  for instructions.
- If you have any suggestions or need further clarification on how to use
  `cifkit`, please reach out to Bob Lee
  ([@bobleesj](https://github.com/bobleesj)).
