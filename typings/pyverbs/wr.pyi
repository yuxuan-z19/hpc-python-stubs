"""
Type stubs for pyverbs.wr — Work Request types (SGE, SendWR, RecvWR).
"""

from pyverbs.addr import AH
from pyverbs.base import PyverbsCM
from pyverbs.mr import MW, MWBindInfo

class SGE(PyverbsCM):
    """Scatter/Gather Element (ibv_sge).

    Represents a scatter-gather entry with address, length, and local key.
    Provides a read function to track data written to the SGE address.
    """

    def __init__(self, addr: int, length: int, lkey: int) -> None:
        """Initialize a scatter-gather element.

        Args:
            addr: The address to use for read/write.
            length: Available buffer size.
            lkey: Local key of the used MR/DMMR.

        Raises:
            PyverbsError: If SGE allocation fails.
        """
        ...

    def read(self, length: int, offset: int = 0) -> bytes:
        """Read data from the SGE's address.

        Args:
            length: Number of bytes to read.
            offset: Offset from the SGE's address in bytes.

        Returns:
            The data at the SGE address + offset.
        """
        ...

    @property
    def addr(self) -> int:
        """SGE address."""
        ...
    @addr.setter
    def addr(self, val: int) -> None: ...
    @property
    def length(self) -> int:
        """SGE buffer length."""
        ...
    @length.setter
    def length(self, val: int) -> None: ...
    @property
    def lkey(self) -> int:
        """SGE local key."""
        ...
    @lkey.setter
    def lkey(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class RecvWR(PyverbsCM):
    """Receive Work Request (ibv_recv_wr)."""

    def __init__(
        self, wr_id: int = 0, num_sge: int = 0, sg: list[SGE] | None = None, next_wr: RecvWR | None = None
    ) -> None:
        """Initialize a receive WR.

        Args:
            wr_id: A user-defined WR ID.
            num_sge: Size of the scatter-gather array.
            sg: A scatter-gather array (list of SGE objects).
            next_wr: The next RecvWR in the linked list.

        Raises:
            PyverbsRDMAErrno: If SG buffer allocation fails.
        """
        ...

    @property
    def wr_id(self) -> int:
        """User-defined WR ID."""
        ...
    @wr_id.setter
    def wr_id(self, val: int) -> None: ...
    @property
    def num_sge(self) -> int:
        """Number of scatter-gather elements."""
        ...
    @num_sge.setter
    def num_sge(self, val: int) -> None: ...
    @property
    def sg_list(self) -> int:
        """Pointer to the scatter-gather list as integer."""
        ...

    @property
    def next_wr(self) -> RecvWR | None:
        """Next RecvWR in the linked list."""
        ...
    @next_wr.setter
    def next_wr(self, val: RecvWR) -> None: ...
    def __str__(self) -> str: ...

class SendWR(PyverbsCM):
    """Send Work Request (ibv_send_wr)."""

    def __init__(
        self,
        wr_id: int = 0,
        opcode: int = 0,
        num_sge: int = 0,
        imm_data: int = 0,
        sg: list[SGE] | None = None,
        send_flags: int = 0,
        next_wr: SendWR | None = None,
    ) -> None:
        """Initialize a send WR.

        Args:
            wr_id: A user-defined WR ID.
            opcode: The WR opcode (ibv_wr_opcode).
            num_sge: Number of scatter-gather elements.
            imm_data: Immediate data.
            sg: Scatter-gather list (list of SGE objects).
            send_flags: Send flags (ibv_send_flags).
            next_wr: The next SendWR in the linked list.

        Raises:
            PyverbsUserError: If num_sge < 1 or sg is None for non-MW opcodes.
            PyverbsRDMAErrno: If SG buffer allocation fails.
        """
        ...

    def set_wr_ud(self, ah: AH, rqpn: int, rqkey: int) -> None:
        """Set UD-specific addressing in the send WR.

        Args:
            ah: An Address Handle object.
            rqpn: The remote QP number.
            rqkey: The remote QKey, authorizing access to the destination QP.
        """
        ...

    def set_wr_rdma(self, rkey: int, addr: int) -> None:
        """Set RDMA remote address and key for RDMA operations.

        Args:
            rkey: Key to access the specified remote memory address.
            addr: Start address of the remote buffer.
        """
        ...

    def set_wr_atomic(self, rkey: int, addr: int, compare_add: int, swap: int = 0) -> None:
        """Set atomic operation parameters.

        Args:
            rkey: Key to access the specified remote memory address.
            addr: Start address of the remote buffer.
            compare_add: Data operand for the compare portion of CAS.
            swap: For CAS: value swapped into the buffer.
                For FAA: value added to the buffer contents.
        """
        ...

    def set_bind_wr(self, mw: MW, bind_info: MWBindInfo) -> None:
        """Set MW bind work request parameters.

        Args:
            mw: The MW to bind.
            bind_info: MWBindInfo with bind attributes.
        """
        ...

    def set_qp_type_xrc(self, remote_srqn: int) -> None:
        """Set XRC remote SRQ number for XRC transport.

        Args:
            remote_srqn: The XRC SRQ number for the responder.
        """
        ...

    @property
    def wr_id(self) -> int:
        """User-defined WR ID."""
        ...
    @wr_id.setter
    def wr_id(self, val: int) -> None: ...
    @property
    def opcode(self) -> int:
        """WR opcode (ibv_wr_opcode)."""
        ...
    @opcode.setter
    def opcode(self, val: int) -> None: ...
    @property
    def num_sge(self) -> int:
        """Number of scatter-gather elements."""
        ...
    @num_sge.setter
    def num_sge(self, val: int) -> None: ...
    @property
    def imm_data(self) -> int:
        """Immediate data."""
        ...
    @imm_data.setter
    def imm_data(self, val: int) -> None: ...
    @property
    def send_flags(self) -> int:
        """Send flags (ibv_send_flags)."""
        ...
    @send_flags.setter
    def send_flags(self, val: int) -> None: ...
    @property
    def sg_list(self) -> int:
        """Pointer to the scatter-gather list as integer."""
        ...
    @sg_list.setter
    def sg_list(self, val: SGE) -> None: ...
    @property
    def rkey(self) -> int:
        """Bound MW rkey (after set_bind_wr)."""
        ...

    @property
    def rdma_remote_addr(self) -> int:
        """RDMA remote address (after set_wr_rdma)."""
        ...

    @property
    def rdma_rkey(self) -> int:
        """RDMA remote rkey (after set_wr_rdma)."""
        ...

    @property
    def next_wr(self) -> SendWR | None:
        """Next SendWR in the linked list."""
        ...
    @next_wr.setter
    def next_wr(self, val: SendWR) -> None: ...
    def __str__(self) -> str: ...

def send_flags_to_str(flags: int) -> str:
    """Convert send flags bitmask to a human-readable string.

    Args:
        flags: Send flags bitmask (OR of ``IBV_SEND_*``).

    Returns:
        Space-separated string of flag names.
    """
    ...
