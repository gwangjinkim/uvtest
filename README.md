This repository is just some experimentation about how to use pyproject.toml
and how to make subpackages visible within a `uv` folder.

uvtest
├── README.md
├── git
├── init
├── pyproject.toml
├── src
│   ├── uvtest
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   └── main.cpython-310.pyc
│   │   ├── config
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   └── main.cpython-310.pyc
│   │   │   └── main.py
│   │   ├── main.py
│   │   ├── pkg1
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   └── main.cpython-310.pyc
│   │   │   └── main.py
│   │   └── services
│   │       └── data_ingestion
│   │           ├── __init__.py
│   │           ├── __pycache__
│   │           │   ├── __init__.cpython-310.pyc
│   │           │   └── ingest_data.cpython-310.pyc
│   │           └── ingest_data.py
│   └── uvtest.egg-info
│       ├── PKG-INFO
│       ├── SOURCES.txt
│       ├── dependency_links.txt
│       └── top_level.txt
└── tests
    ├── __pycache__
    │   └── test_imports.cpython-310-pytest-8.3.3.pyc
    └── test_imports.py

```
[project]
name = "uvtest"
version = "0.2.0"
description = "Test uv packaging with subpackages"
readme = "README.md"
requires-python = ">=3.9"
dependencies = []

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]
include = ["uvtest*"]
exclude = ["tests*"]

[tool.pytest.ini_options]
pythonpath = "src"
```
The first commit is this architecture together with this `pyproject.toml`.
One can add more subpackages in the `src/uvtest/` folder and it will be
detected.

It is:
```
commit 526b0535d955f73db17992bac03489eb146c1d9a
```

We want all subpackages in a folder `packages`:

```
.
├── README.md
├── git
├── init
├── pyproject.toml
├── src
│   ├── uvtest
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── main.cpython-310.pyc
│   │   │   └── main.cpython-312.pyc
│   │   ├── config
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── main.cpython-310.pyc
│   │   │   │   └── main.cpython-312.pyc
│   │   │   └── main.py
│   │   ├── main.py
│   │   ├── packages
│   │   │   └── pkg1
│   │   │       ├── __init__.py
│   │   │       ├── __pycache__
│   │   │       │   ├── __init__.cpython-310.pyc
│   │   │       │   ├── __init__.cpython-312.pyc
│   │   │       │   ├── main.cpython-310.pyc
│   │   │       │   └── main.cpython-312.pyc
│   │   │       └── main.py
│   │   └── services
│   │       └── data_ingestion
│   │           ├── __init__.py
│   │           ├── __pycache__
│   │           │   ├── __init__.cpython-310.pyc
│   │           │   ├── __init__.cpython-312.pyc
│   │           │   ├── ingest_data.cpython-310.pyc
│   │           │   └── ingest_data.cpython-312.pyc
│   │           └── ingest_data.py
│   └── uvtest.egg-info
│       ├── PKG-INFO
│       ├── SOURCES.txt
│       ├── dependency_links.txt
│       └── top_level.txt
├── tests
│   ├── __pycache__
│   │   ├── test_imports.cpython-310-pytest-8.3.3.pyc
│   │   └── test_imports.cpython-312-pytest-8.3.5.pyc
│   └── test_imports.py
└── uv.lock
```
It is in:
```
commit 43681c686959dafe36af0ca1966c5f78312057a9
```



Now, we want to try:

```
uvtest/
├── config/
│   ├── __init__.py
│   ├── connection_config.py
│   └── env/
│       └── ... (can have config files, etc.)
├── packages/
│   └── src/
│       ├── __init__.py
│       ├── pkg1/
│       │   ├── __init__.py
│       │   └── utils.py
│       ├── pkg2/
│       │   ├── __init__.py
│       │   └── core.py
│       └── ... (other packages)
├── services/
│   └── data_ingestion/
│       ├── __init__.py
│       └── ingest_data.py
├── pyproject.toml
└── .venv/
```
The packages are however not under `uvtest` any more.
But are first-level independent packages.
They are installed when doing
```
uv pip install uvtest
```



Let's add `ingest_data.ingest()` as a CLI command:
```
uvtest-ingest
```

For that, add:
```
[project.scripts]
uvtest-ingest = "services.data_ingestion.ingest_data:ingest"
```
After
```
uv pip install -e .
```
We can invoke ingest() in the submodule `data_ingestion` by:
```
uvtest-ingest
```
from the commandline!

