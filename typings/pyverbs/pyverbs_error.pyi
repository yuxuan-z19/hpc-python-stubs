"""
Type stubs for pyverbs.pyverbs_error — Exception classes for pyverbs.
"""

class PyverbsError(Exception):
    """Base exception for all pyverbs errors."""

    ...

class PyverbsRDMAError(PyverbsError):
    """Raised when an RDMA verbs operation fails with an error code."""

    def __init__(self, msg: str, rc: int = 0) -> None: ...

class PyverbsUserError(PyverbsError):
    """Raised on invalid user input to pyverbs APIs."""

    ...

class PyverbsRDMAErrno(PyverbsError):
    """Raised when an RDMA operation fails with a system errno."""

    ...
