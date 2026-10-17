# HPC Python Stubs

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)

Typed stubs for Python bindings or wrappers over HPC packages and libraries.

This repository provides `.pyi` files for CUDA Python packages/bindings that do not ship complete type information, enabling accurate type hints and static type checking with tools such as [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), [BasedPyright](https://github.com/DetachHead/basedpyright), and [mypy](https://www.mypy-lang.org/). The stubs are compatible with Python 3.9+.

> **This is a [template repository](https://github.com/yuxuan-z19/hpc-python-stubs).** Click ["Use this template"](https://github.com/yuxuan-z19/hpc-python-stubs/generate) to create your own copy with custom stubs.

## Supported Packages

| Package                                                                                                    | Description                              | Stub Path                | Status |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------ | ------ |
| [nvCOMP](https://docs.nvidia.com/cuda/nvcomp/installation.html#installing-the-nvcomp-library-through-pypi) | NVIDIA high-performance GPU compression  | `typings/nvidia/nvcomp/` | ✅      |
| [pyverbs (rdma-core)](https://github.com/linux-rdma/rdma-core/blob/master/Documentation/pyverbs.md)        | Python bindings for RDMA verbs & RDMA CM | `typings/pyverbs/`       | ✅      |

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/hpc-python-stubs.git
```

### 2. Add `typings/` to Your Type Checker Configuration

The stubs mirror the corresponding Python module hierarchy. For example:

```text
typings/
├── nvidia/
│   └── nvcomp/
│       └── nvcomp_impl.pyi
└── pyverbs/
    ├── device.pyi
    ├── qp.pyi
    ├── cq.pyi
    ├── mr.pyi
    ├── cmid.pyi
    ├── ...
    └── providers/
        ├── mlx5/
        │   └── ...
        └── efa/
            └── ...
```

provides type information for:

```python
import nvidia.nvcomp.nvcomp_impl
import pyverbs.device
import pyverbs.providers.mlx5.mlx5dv
```

#### Pylance / VS Code

Add the `typings/` directory to [`python.analysis.extraPaths`](https://code.visualstudio.com/docs/python/settings-reference) in your `.vscode/settings.json`:

```json
{
    "python.analysis.extraPaths": ["./typings"]
}
```

#### BasedPyright

Add the path in `pyrightconfig.json`:

```json
{
    "extraPaths": ["./typings"]
}
```

Or in `pyproject.toml`:

```toml
[tool.basedpyright]
extraPaths = ["./typings"]
```

#### mypy

Use the [`MYPYPATH`](https://mypy.readthedocs.io/en/stable/running_mypy.html#finding-imports) environment variable:

```bash
MYPYPATH=./typings mypy your_script.py
```

Or configure it in `mypy.ini`:

```ini
[mypy]
mypy_path = typings
```

### 3. Install the Actual Python Package

The stubs only provide type information — the runtime packages must be installed separately.

## Contributing

Contributions are welcome! To add stubs for a new package or extend existing ones:

1. **Create the stub file** under `typings/` following the module hierarchy. For example, stubs for `nvidia.cuda.cudart` should be placed at `typings/nvidia/cuda/cudart`.

2. **Follow PEP 484 conventions** — use `.pyi` extension, type annotations only (no implementation bodies), and `...` for method bodies.

3. **Add docstrings** for all public classes, methods, and functions. Include parameter descriptions and return types.

4. **Update the Supported Packages table** in this README to reflect the new coverage.

5. **Open a Pull Request** with a clear description of the added stubs and the source package version they target.

### Stub File Conventions

- Use `ClassVar` for enum-like class members.
- Use `@overload` for functions with multiple signatures.
- Use `Self` (from `typing`) for methods returning the same type.
- Prefer concrete types over `Any` whenever possible.
- Mark read-only properties with `@property` and no setter.
- Include a module-level docstring describing the stub's scope.

## License

See [LICENSE](LICENSE).
