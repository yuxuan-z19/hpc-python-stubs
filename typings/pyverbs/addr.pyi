"""
Type stubs for pyverbs.addr — Address Handle and GID types.
"""

from typing import Any

from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.pd import PD

class GID(PyverbsObject):
    """Global Identifier (GID) — represents ibv_gid.

    Enables querying and setting GID values in the standard
    'xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx' format.
    """

    def __init__(self, val: str | None = None) -> None:
        """Initialize a GID.

        Args:
            val: Optional GID string in 8-word format.
        """
        ...

    @property
    def gid(self) -> str:
        """GID as a string in 'xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx' format."""
        ...
    @gid.setter
    def gid(self, val: str) -> None: ...
    def __str__(self) -> str: ...

class GRH(PyverbsObject):
    """Global Route Header (ibv_grh).

    Used when creating or initializing an Address Handle from a Work Completion.
    """

    def __init__(
        self,
        sgid: GID | None = None,
        dgid: GID | None = None,
        version_tclass_flow: int = 0,
        paylen: int = 0,
        next_hdr: int = 0,
        hop_limit: int = 1,
    ) -> None:
        """Initialize a Global Route Header.

        Args:
            sgid: Source GID.
            dgid: Destination GID.
            version_tclass_flow: 32-bit big endian for service level.
            paylen: 16-bit big endian packet length in bytes.
            next_hdr: 8-bit next header (0x1B for non-raw).
            hop_limit: 8-bit max number of hops before discard.
        """
        ...

    @property
    def dgid(self) -> str:
        """Destination GID as string."""
        ...
    @dgid.setter
    def dgid(self, val: str) -> None: ...
    @property
    def sgid(self) -> str:
        """Source GID as string."""
        ...
    @sgid.setter
    def sgid(self, val: str) -> None: ...
    @property
    def version_tclass_flow(self) -> int:
        """Version / traffic class / flow label (32-bit)."""
        ...
    @version_tclass_flow.setter
    def version_tclass_flow(self, val: int) -> None: ...
    @property
    def paylen(self) -> int:
        """Payload length in bytes (16-bit)."""
        ...
    @paylen.setter
    def paylen(self, val: int) -> None: ...
    @property
    def next_hdr(self) -> int:
        """Next header (8-bit)."""
        ...
    @next_hdr.setter
    def next_hdr(self, val: int) -> None: ...
    @property
    def hop_limit(self) -> int:
        """Hop limit (8-bit)."""
        ...
    @hop_limit.setter
    def hop_limit(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class GlobalRoute(PyverbsObject):
    """Global routing parameters (ibv_global_route).

    Describes the values for the GRH of packets sent using an Address Handle.
    """

    def __init__(
        self,
        dgid: GID | None = None,
        flow_label: int = 0,
        sgid_index: int = 0,
        hop_limit: int = 1,
        traffic_class: int = 0,
    ) -> None:
        """Initialize global route parameters.

        Args:
            dgid: Destination GID.
            flow_label: 20-bit flow label for in-order delivery hint.
            sgid_index: Index in the port's GID table identifying the originator.
            hop_limit: 8-bit max number of hops before discard.
            traffic_class: 8-bit delivery priority for routers.
        """
        ...

    @property
    def dgid(self) -> str:
        """Destination GID as string."""
        ...
    @dgid.setter
    def dgid(self, val: str) -> None: ...
    @property
    def flow_label(self) -> int:
        """Flow label (20-bit)."""
        ...
    @flow_label.setter
    def flow_label(self, val: int) -> None: ...
    @property
    def sgid_index(self) -> int:
        """Source GID index."""
        ...
    @sgid_index.setter
    def sgid_index(self, val: int) -> None: ...
    @property
    def hop_limit(self) -> int:
        """Hop limit (8-bit)."""
        ...
    @hop_limit.setter
    def hop_limit(self, val: int) -> None: ...
    @property
    def traffic_class(self) -> int:
        """Traffic class (8-bit)."""
        ...
    @traffic_class.setter
    def traffic_class(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class AHAttr(PyverbsObject):
    """Address Handle Attributes (ibv_ah_attr).

    Contains all parameters needed to create an Address Handle, including
    optional global routing header attributes for cross-subnet communication.
    """

    def __init__(
        self,
        dlid: int = 0,
        sl: int = 0,
        src_path_bits: int = 0,
        static_rate: int = 0,
        is_global: int = 0,
        port_num: int = 1,
        gr: GlobalRoute | None = None,
    ) -> None:
        """Initialize address handle attributes.

        Args:
            dlid: Destination LID (16-bit).
            sl: Service level (8-bit).
            src_path_bits: Source path bits for LMC (8-bit).
            static_rate: Static rate limit (8-bit).
            is_global: Non-zero if GRH information is present.
            port_num: Local physical port number.
            gr: Global route attributes (required if is_global != 0).

        Raises:
            PyverbsUserError: If is_global is set but gr is None.
        """
        ...

    @property
    def port_num(self) -> int:
        """Port number."""
        ...
    @port_num.setter
    def port_num(self, val: int) -> None: ...
    @property
    def sl(self) -> int:
        """Service level."""
        ...
    @sl.setter
    def sl(self, val: int) -> None: ...
    @property
    def src_path_bits(self) -> int:
        """Source path bits."""
        ...
    @src_path_bits.setter
    def src_path_bits(self, val: int) -> None: ...
    @property
    def dlid(self) -> int:
        """Destination LID."""
        ...
    @dlid.setter
    def dlid(self, val: int) -> None: ...
    @property
    def static_rate(self) -> int:
        """Static rate limit."""
        ...
    @static_rate.setter
    def static_rate(self, val: int) -> None: ...
    @property
    def is_global(self) -> int:
        """Whether global routing is enabled."""
        ...
    @is_global.setter
    def is_global(self, val: int) -> None: ...
    @property
    def dgid(self) -> str | None:
        """Destination GID (only if is_global)."""
        ...
    @dgid.setter
    def dgid(self, val: str) -> None: ...
    @property
    def flow_label(self) -> int | None:
        """Flow label (only if is_global)."""
        ...
    @flow_label.setter
    def flow_label(self, val: int) -> None: ...
    @property
    def sgid_index(self) -> int | None:
        """Source GID index (only if is_global)."""
        ...
    @sgid_index.setter
    def sgid_index(self, val: int) -> None: ...
    @property
    def hop_limit(self) -> int | None:
        """Hop limit (only if is_global)."""
        ...
    @hop_limit.setter
    def hop_limit(self, val: int) -> None: ...
    @property
    def traffic_class(self) -> int | None:
        """Traffic class (only if is_global)."""
        ...
    @traffic_class.setter
    def traffic_class(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class AH(PyverbsCM):
    """Address Handle (ibv_ah).

    An Address Handle provides the addressing information needed for
    sending unreliable datagrams (UD).
    """

    def __init__(self, pd: PD, **kwargs: Any) -> None:
        """Create an Address Handle.

        Two creation methods are supported:
        - Via AHAttr (calls ibv_create_ah)
        - Via a WC (calls ibv_create_ah_from_wc)

        Args:
            pd: PD this AH belongs to.

        Keyword Args:
            attr: An AHAttr object.
            wc: A WC object for AH initialization from work completion.
            grh: A GRH pointer (for wc-based creation).
            port_num: Port number (for wc-based creation).

        Raises:
            PyverbsRDMAErrno: If AH creation fails.
        """
        ...
