

__all__ = [
    "TMPDIR_NAME",
    "DATADIR_DIRNAME",
    "SHARED_DATADIR_NAME",
]
# Root temp dir name to use for all pytest-datadir directories
TMPDIR_NAME = "pytest-datadir-extras"

# the datadir factory uses a tmp_path_factory to get a temp dir. This
# is the name of the dir within the tempdir tree to use for datadir,
# since these are potentially session scoped fixtures
DATADIR_DIRNAME = 'datadir'


# for the shared datadirs, to maintain backwards compatibility we set these to
# have the default behavior of using the shared data dir called "data"
SHARED_DATADIR_NAME = 'data'
