# Python module template

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-1c4a6c.svg)](https://flake8.pycqa.org/en/latest/)

<!-- ![ci](https://github.com/Tomansion/Python-module-template/actions/workflows/pull-request-checks.yml/badge.svg) -->
<!-- ![cd](https://github.com/tomansion/Python-module-template/actions/workflows/continuous-deployment.yml/badge.svg) -->

---

This project is a template for Python module. It includes a basic example of functions that allows users to do some simple arithmetic operations.

## Template features

- Documentation:

  - [**Docstring**](https://www.python.org/dev/peps/pep-0257/): A way to document the code using comments.
  - [**Sphinx**](https://www.sphinx-doc.org/): A tool that makes it easy to create intelligent and beautiful documentation.
  - [**Templates for pull requests & issues**](https://github.com/Tomansion/Python-module-template/tree/main/.github/ISSUE_TEMPLATE): A collection of templates for creating pull requests and issues.

- Code Quality:

  - [**Black**](https://pypi.org/project/black/): A code formatters that automatically format the Python code.
  - [**Flake8**](https://flake8.pycqa.org/en/latest/): A tool that checks the code for style and quality.
  - [**Cspell**](https://cspell.org/): A spell checker that checks the spelling in the code, edit the [`cspell.json`](cspell.json) file to add custom words or languages.

- Testing:

  - [**Pytest**](https://docs.pytest.org/): A testing framework for Python that makes it easy to write small tests.

- Continuous Integration and Continuous Deployment:

  - **GitHub Actions**: This project includes a GitHub Actions workflow that runs the tests, linters, pushes the Python module to the PyPI repository, and deploys the documentation to GitHub Pages.

## Python module documentation

The documentation is available at [https://tomansion.github.io/Python-module-template/](https://tomansion.github.io/Python-module-template/).

## Getting started

To use this Python module template, follow these steps:

```bash
# Clone the repository
git clone https://github.com/Tomansion/Python-module-template.git

# Install the python module
cd Python-module-template
pip install .
```

## Automatic documentation generation

Available at: [https://tomansion.github.io/Git-course-CentraleSupelec-09-2025/](https://tomansion.github.io/Git-course-CentraleSupelec-09-2025/)

### Setup

1. Create a `gh-pages` branch in your repository.
2. Go to the repository settings, then to the "Pages" section, and select the `gh-pages` branch as the source for GitHub Pages.
3. Go into Settings > actions > General and make sure that "Workflow permissions" is set to "Read and write permissions".

When you push a commit to the `main` branch, the documentation will be automatically generated and deployed to GitHub Pages.

## Test

To run the tests using Pytest, follow these steps:

```bash
# Install the required dependencies:
pip install -r requirements.txt

# Run the tests
pytest

# Run the tests with coverage
pytest --cov=python_module_template

# In case of issues with the pytest module not found, you can try:
python -m pytest
python -m pytest --cov=python_module_template
python -m pytest --cov=python_module_template --cov-report=html
```

> Note: The tests will be run automatically in the CI/CD pipeline for each pull request. The coverage must be at least 80% to pass the tests.

## Quality check

This project uses Black, Flake8 and Cspell to check the code quality. To run the quality check, follow these steps:

### Linters

```bash
# Install the required dependencies:
pip install -r requirements.txt

# Run Black
black .
# or
python -m black .

# Run Flake8
flake8 .
# or
python -m flake8 .
```

### Spell check

Install [Cspell](https://cspell.org/docs/installation) first, then run:

```bash
# Run Cspell
cspell .
```

## TODO

- [x] Create basic functions
- [x] Add unit tests with pytest
- [x] Add tests CI/CD pipeline
- [x] Add Sphinx documentation
- [x] Add documentation CI/CD pipeline with GitHub Pages
- [ ] Pipelines badges
- [ ] Coverage check pipeline and display in the README badge
- [ ] Add to Pypi
- [ ] Pypi upload pipeline
