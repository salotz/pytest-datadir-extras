# pytest-datadir-extras

Pytest plugin for cleanly injecting files into your tests. This is a friendly
fork of the popular
[pytest-datadir](https://github.com/gabrielcnr/pytest-datadir) that adds extra
functionality. In addition to the data-directories by convention in the original
this package provides you with programmable factories for generating datadir's
against any folder and with any scope you wish.

[![PyPI - Version](https://img.shields.io/pypi/v/pytest-datadir-extras.svg)](https://pypi.org/project/pytest-datadir-extras)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytest-datadir-extras.svg)](https://pypi.org/project/pytest-datadir-extras)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install pytest-datadir-extras
```

## License

`pytest-datadir-extras` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.


# Usage

In this document we refer to a "datadir" as a pytest fixture that provides a
copy of an existing file or directory into a safe, configurable location that is
automatically scoped according to normal pytest fixture scopes.

## Traditional Behavior by Convention

Using the existing `pytest-datadir` behavior you can look up for a directory
with the name of your module or the global `data` folder. Let's say you have a
structure like this:

```
.
├── data/
│   └── hello.txt
├── other_data/
│   └── other_data.txt
├── test_hello/
│   └── spam.txt
└── test_hello.py
```

You can access the contents of these files using injected variables `datadir` (for *test_* folder) or `shared_datadir`
(for *data* folder):

```python
def test_read_global(shared_datadir):
    contents = (shared_datadir / 'hello.txt').read_text()
    assert contents == 'Hello World!\n'

def test_read_module(datadir):
    contents = (datadir / 'spam.txt').read_text()
    assert contents == 'eggs\n'
```

pytest-datadir will copy the original file to a temporary folder, so changing the file contents won't change the original data file.

Both `datadir` and `shared_datadir` fixtures are `pathlib.Path` objects.

The `other_data` folder on the other hand is innaccessible with this legacy
behavior.


## Extra Configurable Functionality

By default `datadir` and `shared_datadir` are scoped by function and are actually aliases for `function_datadir` and `function_shared_datadir`.

This library provides scoped `datadirs` and `shared_datadirs` for:

- module
- class
- function

If your data files are large then each test will need to copy them which can be
very slow. If you know you will not be writing back to a file you can use a
higher scoped fixture will only copy them once for e.g. the module. Be careful
though, as any changes to the directory will be seen by other tests in the
scope.

TODO


## Datadir factory

Similar to how `tmp_path_factory` works you can also generate temporary datadirs in your code:

```python

def test_read_module(datadir_factory):

    datadir0 = datadir_factory.mkdatadir()
    contents = (datadir0 / 'spam.txt').read_text()
    assert contents == 'eggs\n'
    
    with open((datadir0 / 'spam.txt'), 'w') as wf:
        wf.write('ham\n')

    # with a fresh temp datadir
    datadir1 = datadir_factory.mkdatadir()
    contents = (datadir1 / 'spam.txt').read_text()
    assert contents == 'eggs\n'

```


Additionally you can also specify which folder you actually want to pull data from beyond the default 'data' dir from the `shared_datadir` fixture:

```python

def test_factory_module(datadir_factory):

    datadir = datadir_factory.mkdatadir('other_data')
    contents = (datadir / 'other_data.txt').read_text()
    assert contents == 'fun stuff\n'
    
```

# TODO

- [ ] session scopes for files
- [ ] permissions manipulation
- [ ] Support for customizing link/copy behavior. I.e. reflinks.
