"""
Type stubs for pyverbs.base — Base classes for all pyverbs objects.
"""

import logging
from typing import Self

from pyverbs.pyverbs_error import PyverbsRDMAError

def inc_rkey(rkey: int) -> int:
    """Increment an rkey (for re-registration).

    Args:
        rkey: The remote key to increment.

    Returns:
        The incremented rkey.
    """
    ...

def PyverbsRDMAErrno(msg: str) -> PyverbsRDMAError:
    """Create a PyverbsRDMAError with the current errno appended.

    Args:
        msg: Error message.

    Returns:
        A PyverbsRDMAError exception with errno.
    """
    ...

class PyverbsObject:
    """Base class for all pyverbs objects. Provides weakref support and logging."""

    logger: logging.Logger | None

    def __init__(self) -> None: ...
    def set_log_level(self, val: int) -> None:
        """Set the logging level for this object.

        Args:
            val: Logging level (e.g. logging.DEBUG).
        """
        ...

class PyverbsCM(PyverbsObject):
    """Base class for pyverbs objects that manage C resources with a close() method."""

    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: object | None,
    ) -> None: ...
    def close(self) -> None:
        """Release the underlying C resources."""
        ...
