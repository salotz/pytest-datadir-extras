""""""

import shutil
from pathlib import Path
from typing import Optional

from .utils import win32_longpath
from .config import (
    TMPDIR_NAME,
    DATADIR_DIRNAME,
)

def get_original_datadir(request) -> Path:
    """For the current test get the original path to the corresponding
    conventional data directory."""

    test_module_path = Path(request.module.__file__)

    return Path(*test_module_path.parts[:-1]) / test_module_path.stem

class DatadirFactory(object):
    """Factory class for generating datadir fixtures."""

    def __init__(self, request, tmp_path_factory):

        self.tmp_path_factory = tmp_path_factory
        self.request = request


    def mkdatadir(self,
                  original_datadir: Optional[Path] = None,
                  ) -> Path:
        """Create a temporary directory for this factory's scope.
        """

        # special condition if the datadir is specified as None, which
        # automatically gets the path that matches the basename of the
        # module we are in
        if original_datadir is None:
            original_datadir = get_original_datadir(self.request)


        # get the path to the shared data dir
        original_path = Path(self.request.fspath.dirname) / original_datadir

        # make sure that the path exists and it is a directory
        exists = True
        if not original_path.exists():
            # raise the flag that it doesn't exist so we can generate
            # a directory for it instead of copying
            exists = False

        # make sure the path is a directory if it exists
        elif not original_path.is_dir():
            raise ValueError("datadir path is not a directory")

        # generate a base temporary directory and receive the path to it
        temp_path = self.tmp_path_factory.mktemp(TMPDIR_NAME)

        # in order to use the shutil.copytree util the target directory
        # must not exist so we specify a dir in the generated tempdir for it
        temp_data_path = temp_path / DATADIR_DIRNAME

        # windows-ify the paths
        original_path = Path(win32_longpath(original_path))
        temp_data_path = Path(win32_longpath(str(temp_data_path)))

        # copy or create empty directory depending on whether the
        # original one exists
        if exists:

            # copy all the files in the original data dir to the temp
            # dir
            shutil.copytree(original_path, temp_data_path)

        else:
            # otherwise just give them a fallback tmpdir
            temp_data_path.mkdir()

        return temp_data_path
