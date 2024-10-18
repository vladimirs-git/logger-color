"""Test package"""

import re
from pathlib import Path

from vhelpers import vdate, vdict, vpath, vre

ROOT = Path(__file__).parent.parent.resolve()
PYPROJECT_D = vdict.pyproject_d(ROOT)


def test__version__tar():
    """Version in tar.gz."""
    expected = PYPROJECT_D["tool"]["poetry"]["version"]
    package = PYPROJECT_D["tool"]["poetry"]["name"].replace("_", "-")
    regex_tar = fr"{package}.+/(.+?)\.tar\.gz"

    # pyproject.toml
    text = PYPROJECT_D["tool"]["poetry"]["urls"]["Download URL"]
    actual = vre.find1(regex_tar, text)
    assert actual == expected


def test__version__changelog():
    """Version in CHANGELOG."""
    path = Path.joinpath(ROOT, "CHANGELOG.rst")
    text = path.read_text(encoding="utf-8")
    regex = r"(.+)\s\(\d\d\d\d-\d\d-\d\d\)$"
    actual = vre.find1(regex, text, re.M)

    expected = PYPROJECT_D["tool"]["poetry"]["version"]
    assert actual == expected, f"version in {path=}"


def test__last_modified_date():
    """Last modified date in CHANGELOG."""
    path = Path.joinpath(ROOT, "CHANGELOG.rst")
    text = path.read_text(encoding="utf-8")
    regex = r".+\((\d\d\d\d-\d\d-\d\d)\)$"
    actual = vre.find1(regex, text, re.M)
    files = vpath.get_files(root=ROOT, pattern="\.py$")
    expected = vdate.last_modified(files)
    assert actual == expected, "last modified file"
