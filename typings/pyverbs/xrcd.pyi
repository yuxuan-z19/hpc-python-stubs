"""
Type stubs for pyverbs.xrcd — XRC Domain (XRCD) types.
"""

from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.device import Context

class XRCDInitAttr(PyverbsObject):
    """XRC Domain initialization attributes (ibv_xrcd_init_attr)."""

    def __init__(self, comp_mask: int, oflags: int, fd: int) -> None:
        """Initialize XRCD creation attributes.

        Args:
            comp_mask: Compatibility mask.
            oflags: Open flags (O_CREAT, O_RDWR, etc.).
            fd: File descriptor for an existing XRCD (or new if O_CREAT).
        """
        ...

    @property
    def fd(self) -> int:
        """File descriptor."""
        ...
    @fd.setter
    def fd(self, val: int) -> None: ...
    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    @property
    def oflags(self) -> int:
        """Open flags."""
        ...
    @oflags.setter
    def oflags(self, val: int) -> None: ...

class XRCD(PyverbsCM):
    """XRC Domain (ibv_xrcd).

    An XRC Domain is used with XRC transport to share resources across
    multiple initiator and target QPs.
    """

    def __init__(self, context: Context, init_attr: XRCDInitAttr) -> None:
        """Open or create an XRC Domain.

        Args:
            context: The Context creating the XRCD.
            init_attr: XRCD initialization attributes.

        Raises:
            PyverbsRDMAErrno: If ibv_open_xrcd fails.
        """
        ...
