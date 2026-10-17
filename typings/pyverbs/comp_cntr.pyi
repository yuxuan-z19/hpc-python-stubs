"""
Type stubs for pyverbs.comp_cntr — Completion Counter types.
"""

from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.device import Context

class CompCntrInitAttr(PyverbsObject):
    """Completion counter initialization attributes (ibv_comp_cntr_init_attr)."""

    def __init__(self, comp_mask: int = 0, cntr_type: int = 0, flags: int = 0) -> None:
        """Initialize completion counter creation attributes.

        Args:
            comp_mask: Compatibility mask.
            cntr_type: Counter type.
            flags: Creation flags.
        """
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...

    @property
    def cntr_type(self) -> int:
        """Counter type."""
        ...

    @property
    def flags(self) -> int:
        """Creation flags."""
        ...

class CompCntr(PyverbsCM):
    """Completion Counter (ibv_comp_cntr).

    Tracks aggregate completion and error counts for RDMA operations.
    """

    def __init__(self, ctx: Context, attr: CompCntrInitAttr) -> None:
        """Create a completion counter.

        Args:
            ctx: Device Context to create the counter on.
            attr: Completion counter initialization attributes.

        Raises:
            PyverbsRDMAErrno: If ibv_create_comp_cntr fails.
        """
        ...

    def set(self, value: int) -> None:
        """Set the completion count to the given value.

        Args:
            value: New completion count.

        Raises:
            PyverbsRDMAError: If ibv_set_comp_cntr fails.
        """
        ...

    def set_err(self, value: int) -> None:
        """Set the error count to the given value.

        Args:
            value: New error count.

        Raises:
            PyverbsRDMAError: If ibv_set_err_comp_cntr fails.
        """
        ...

    def inc(self, amount: int) -> None:
        """Increment the completion count.

        Args:
            amount: Amount to increment by.

        Raises:
            PyverbsRDMAError: If ibv_inc_comp_cntr fails.
        """
        ...

    def inc_err(self, amount: int) -> None:
        """Increment the error count.

        Args:
            amount: Amount to increment by.

        Raises:
            PyverbsRDMAError: If ibv_inc_err_comp_cntr fails.
        """
        ...

    def read(self) -> int:
        """Read the current completion count.

        Returns:
            Current completion count.

        Raises:
            PyverbsRDMAError: If ibv_read_comp_cntr fails.
        """
        ...

    def read_err(self) -> int:
        """Read the current error count.

        Returns:
            Current error count.

        Raises:
            PyverbsRDMAError: If ibv_read_err_comp_cntr fails.
        """
        ...
