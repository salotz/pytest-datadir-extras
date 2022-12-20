"""The fixtures for inclusion in the pytest plugin."""

from pathlib import Path

import pytest

from .config import (
    SHARED_DATADIR_NAME,
)
from .factories import (
    get_original_datadir,
    DatadirFactory,
)

__all__ = [
    "original_datadir",
    "datadir_factory",
    "module_datadir",
    "class_datadir",
    "function_datadir",
    "datadir",
    "module_shared_datadir",
    "class_shared_datadir",
    "function_shared_datadir",
    "shared_datadir",
]

@pytest.fixture
def original_datadir(request) -> Path:
    """Get the path to the actual data directory. WARNING.

    Mostly used for testing the fixtures themselves.

    """
    return get_original_datadir(request)

# scoped factories

# we must provide a module scoped factory because a session scoped one
# cannot work with the module filename for that is used for module
# named datadirs
@pytest.fixture(scope='module')
def datadir_factory(request, tmp_path_factory):

    return DatadirFactory(request, tmp_path_factory)

@pytest.fixture(scope='module')
def module_datadir(request, datadir_factory):

    return datadir_factory.mkdatadir()

@pytest.fixture(scope='class')
def class_datadir(request, datadir_factory):

    return datadir_factory.mkdatadir()

@pytest.fixture(scope='function')
def function_datadir(request, datadir_factory):

    return datadir_factory.mkdatadir()

# for backwards compatibility
datadir = function_datadir

# shared datadirs, to maintain backwards compatibility we set these to
# have the default behavior of saving the data dir with the name 'data'

@pytest.fixture(scope='module')
def module_shared_datadir(request, datadir_factory):

    return datadir_factory.mkdatadir(original_datadir=SHARED_DATADIR_NAME)

@pytest.fixture(scope='class')
def class_shared_datadir(request, datadir_factory):

    return datadir_factory.mkdatadir(original_datadir=SHARED_DATADIR_NAME)

@pytest.fixture(scope='function')
def function_shared_datadir(request, datadir_factory):

    return datadir_factory.mkdatadir(original_datadir=SHARED_DATADIR_NAME)

# for backwards compatibility
shared_datadir = function_shared_datadir
