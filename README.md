# Enasis Network Project Basics

> This project has not released its first major version.

Support functions useful in a wide variety of development projects.

<a href="https://pypi.org/project/enbasics"><img src="https://enasisnetwork.github.io/enbasics/badges/pypi.png"></a><br>
<a href="https://enasisnetwork.github.io/enbasics/validate/flake8.txt"><img src="https://enasisnetwork.github.io/enbasics/badges/flake8.png"></a><br>
<a href="https://enasisnetwork.github.io/enbasics/validate/pylint.txt"><img src="https://enasisnetwork.github.io/enbasics/badges/pylint.png"></a><br>
<a href="https://enasisnetwork.github.io/enbasics/validate/ruff.txt"><img src="https://enasisnetwork.github.io/enbasics/badges/ruff.png"></a><br>
<a href="https://enasisnetwork.github.io/enbasics/validate/mypy.txt"><img src="https://enasisnetwork.github.io/enbasics/badges/mypy.png"></a><br>
<a href="https://enasisnetwork.github.io/enbasics/validate/yamllint.txt"><img src="https://enasisnetwork.github.io/enbasics/badges/yamllint.png"></a><br>
<a href="https://enasisnetwork.github.io/enbasics/validate/pytest.txt"><img src="https://enasisnetwork.github.io/enbasics/badges/pytest.png"></a><br>
<a href="https://enasisnetwork.github.io/enbasics/validate/coverage.txt"><img src="https://enasisnetwork.github.io/enbasics/badges/coverage.png"></a><br>
<a href="https://enasisnetwork.github.io/enbasics/validate/sphinx.txt"><img src="https://enasisnetwork.github.io/enbasics/badges/sphinx.png"></a><br>

## Documentation
Read [project documentation](https://enasisnetwork.github.io/enbasics/sphinx)
built using the [Sphinx](https://www.sphinx-doc.org/) project.
Should you venture into the sections below you will be able to use the
`sphinx` recipe to build documention in the `sphinx/html` directory.

## Installing the package
Installing stable from the PyPi repository
```
pip install enbasics
```
Installing latest from GitHub repository
```
pip install git+https://github.com/enasisnetwork/enbasics
```

## Additional package dependencies
- `enbasics[badges]` for constructing project badges.

## Constructing project badges
```python
python -m enbasics.execution.badges \
  --output "path/to/badge.png" \
  --label "Badge" \
  --value "failure"
```
See this project's [document.yml](.github/workflows/document.yml) for ideas!

## Quick start for local development
Start by cloning the repository to your local machine.
```
git clone https://github.com/enasisnetwork/enbasics.git
```
Set up the Python virtual environments expected by the Makefile.
```
make -s venv-create
```

### Execute the linters and tests
The comprehensive approach is to use the `check` recipe. This will stop on
any failure that is encountered.
```
make -s check
```
However you can run the linters in a non-blocking mode.
```
make -s linters-pass
```
And finally run the various tests to validate the code and produce coverage
information found in the `htmlcov` folder in the root of the project.
```
make -s pytest
```

## Version management
> :warning: Ensure that no changes are pending.

1. Rebuild the environment.
   ```
   make -s check-revenv
   ```

1. Update the [version.txt](enbasics/version.txt) file.

1. Push to the `main` branch.

1. Create [repository](https://github.com/enasisnetwork/enbasics) release.

1. Build the Python package.<br>Be sure no uncommited files in tree.
   ```
   make -s pypackage
   ```

1. Upload Python package to PyPi test.
   ```
   make -s pypi-upload-test
   ```

1. Upload Python package to PyPi prod.
   ```
   make -s pypi-upload-prod
   ```
