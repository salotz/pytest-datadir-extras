
from pathlib import Path

from pytest_datadir_extras.factories import (
    get_original_datadir,
    DatadirFactory,
)

def test_get_original_datadir(request):

    assert get_original_datadir(request) == Path.cwd() / "tests/test_factories"

def test_factory(
        request,
        tmp_path_factory,
):

    datadir_factory = DatadirFactory(
        request,
        tmp_path_factory,
    )

    datadir = datadir_factory.mkdatadir(
        original_datadir=None,
    )

    assert datadir.stem == "test_factories"

    datadir = datadir_factory.mkdatadir(
        original_datadir="something_else",
    )

    assert datadir.stem == "something_else"
