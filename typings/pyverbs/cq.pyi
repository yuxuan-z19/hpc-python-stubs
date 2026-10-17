"""
Type stubs for pyverbs.cq — Completion Queue (CQ) and Work Completion types.
"""

from typing import Any

from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.device import Context
from pyverbs.pd import ParentDomain

class CompChannel(PyverbsCM):
    """Completion channel (ibv_comp_channel) for CQ event notification.

    A completion channel is a file descriptor used to deliver completion
    notifications to a userspace process. When a completion event is generated
    for a CQ, the event is delivered via the completion channel attached to
    the CQ.
    """

    def __init__(self, context: Context) -> None:
        """Initialize a completion channel on the given device.

        Args:
            context: The device's Context object.
        """
        ...

    def get_cq_event(self, expected_cq: CQ | CQEX) -> None:
        """Wait for the next completion event in the completion event channel.

        Args:
            expected_cq: The CQ that is expected to get the event.

        Raises:
            PyverbsRDMAErrno: If ibv_get_cq_event fails or event on unexpected CQ.
        """
        ...

    @property
    def fd(self) -> int:
        """File descriptor for polling."""
        ...

class WC(PyverbsObject):
    """Work Completion (ibv_wc).

    Represents a single work completion entry returned by CQ polling.
    """

    def __init__(
        self,
        wr_id: int = 0,
        status: int = 0,
        opcode: int = 0,
        vendor_err: int = 0,
        byte_len: int = 0,
        qp_num: int = 0,
        src_qp: int = 0,
        imm_data: int = 0,
        wc_flags: int = 0,
        pkey_index: int = 0,
        slid: int = 0,
        sl: int = 0,
        dlid_path_bits: int = 0,
    ) -> None:
        """Initialize a Work Completion with the given fields.

        Args:
            wr_id: Work request ID.
            status: Completion status (ibv_wc_status).
            opcode: Work completion opcode (ibv_wc_opcode).
            vendor_err: Vendor-specific error code.
            byte_len: Number of bytes transferred.
            qp_num: QP number of the completed WR.
            src_qp: Source QP number (for UD).
            imm_data: Immediate data.
            wc_flags: Work completion flags (ibv_wc_flags).
            pkey_index: P_Key index.
            slid: Source LID.
            sl: Service level.
            dlid_path_bits: DLID path bits.
        """
        ...

    @property
    def wr_id(self) -> int:
        """Work request ID."""
        ...
    @wr_id.setter
    def wr_id(self, val: int) -> None: ...
    @property
    def status(self) -> int:
        """Completion status (ibv_wc_status enum)."""
        ...
    @status.setter
    def status(self, val: int) -> None: ...
    @property
    def opcode(self) -> int:
        """Work completion opcode (ibv_wc_opcode enum)."""
        ...
    @opcode.setter
    def opcode(self, val: int) -> None: ...
    @property
    def vendor_err(self) -> int:
        """Vendor-specific error code."""
        ...
    @vendor_err.setter
    def vendor_err(self, val: int) -> None: ...
    @property
    def byte_len(self) -> int:
        """Number of bytes transferred."""
        ...
    @byte_len.setter
    def byte_len(self, val: int) -> None: ...
    @property
    def qp_num(self) -> int:
        """QP number of the completed WR."""
        ...
    @qp_num.setter
    def qp_num(self, val: int) -> None: ...
    @property
    def src_qp(self) -> int:
        """Source QP number (for UD QPs)."""
        ...
    @src_qp.setter
    def src_qp(self, val: int) -> None: ...
    @property
    def imm_data(self) -> int:
        """Immediate data."""
        ...
    @imm_data.setter
    def imm_data(self, val: int) -> None: ...
    @property
    def wc_flags(self) -> int:
        """Work completion flags (ibv_wc_flags)."""
        ...
    @wc_flags.setter
    def wc_flags(self, val: int) -> None: ...
    @property
    def pkey_index(self) -> int:
        """P_Key index."""
        ...
    @pkey_index.setter
    def pkey_index(self, val: int) -> None: ...
    @property
    def slid(self) -> int:
        """Source LID."""
        ...
    @slid.setter
    def slid(self, val: int) -> None: ...
    @property
    def sl(self) -> int:
        """Service level."""
        ...
    @sl.setter
    def sl(self, val: int) -> None: ...
    @property
    def dlid_path_bits(self) -> int:
        """DLID path bits."""
        ...
    @dlid_path_bits.setter
    def dlid_path_bits(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class PollCqAttr(PyverbsObject):
    """Attributes for polling an extended CQ (ibv_poll_cq_attr).

    Used with CQEX.start_poll() for future extensibility.
    """

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...

class WcTmInfo(PyverbsObject):
    """Tag matching information from a work completion (ibv_wc_tm_info).

    Returned by CQEX.read_tm_info() for tag-matching completions.
    """

    @property
    def tag(self) -> int:
        """Tag value."""
        ...
    @tag.setter
    def tag(self, val: int) -> None: ...
    @property
    def priv(self) -> int:
        """Private driver data."""
        ...
    @priv.setter
    def priv(self, val: int) -> None: ...

class CqInitAttrEx(PyverbsObject):
    """Extended CQ initialization attributes (ibv_cq_init_attr_ex).

    Used to create an extended CQ (CQEX) with additional capabilities
    such as per-WC field selection and parent domain allocation.
    """

    def __init__(
        self,
        cqe: int = 100,
        channel: CompChannel | None = None,
        comp_vector: int = 0,
        wc_flags: int = 0,
        comp_mask: int = 0,
        flags: int = 0,
        parent_domain: ParentDomain | None = None,
    ) -> None:
        """Initialize extended CQ attributes.

        Args:
            cqe: CQ capacity (number of CQEs).
            channel: Completion channel for event delivery.
            comp_vector: Completion vector index (0..num_comp_vectors-1).
            wc_flags: WC fields to return in ibv_poll_cq_ex (OR of ibv_wc_flags_ex).
            comp_mask: Compatibility mask for extended verbs.
            flags: Creation flags (ibv_create_cq_attr_flags).
            parent_domain: Parent domain for custom CQ buffer allocation.
        """
        ...

    @property
    def cqe(self) -> int:
        """CQ capacity (number of CQEs)."""
        ...
    @cqe.setter
    def cqe(self, val: int) -> None: ...
    @property
    def comp_channel(self) -> CompChannel | None:
        """Completion channel for event delivery."""
        ...
    @comp_channel.setter
    def comp_channel(self, val: CompChannel) -> None: ...
    @property
    def comp_vector(self) -> int:
        """Completion vector index."""
        ...
    @comp_vector.setter
    def comp_vector(self, val: int) -> None: ...
    @property
    def wc_flags(self) -> int:
        """WC fields flags (OR of ibv_wc_flags_ex)."""
        ...
    @wc_flags.setter
    def wc_flags(self, val: int) -> None: ...
    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    @property
    def flags(self) -> int:
        """Creation flags (ibv_create_cq_attr_flags)."""
        ...
    @flags.setter
    def flags(self, val: int) -> None: ...
    @property
    def parent_domain(self) -> ParentDomain | None:
        """Parent domain for custom CQ buffer allocation."""
        ...
    @parent_domain.setter
    def parent_domain(self, val: ParentDomain) -> None: ...
    def __str__(self) -> str: ...

class CQ(PyverbsCM):
    """Completion Queue (ibv_cq).

    A CQ is the notification mechanism for work request completions. A CQ
    can have 0 or more associated QPs.
    """

    def __init__(
        self,
        context: Context,
        cqe: int,
        cq_context: Any = None,
        channel: CompChannel | None = None,
        comp_vector: int = 0,
    ) -> None:
        """Initialize a CQ on the given device.

        Args:
            context: The device's Context on which to open the CQ.
            cqe: CQ capacity (minimum number of CQEs).
            cq_context: Optional user context pointer.
            channel: Completion channel for event delivery.
            comp_vector: Completion vector index (0..num_comp_vectors-1).
        """
        ...

    def resize(self, cqe: int) -> None:
        """Resize the CQ to have at least *cqe* entries.

        Args:
            cqe: The requested new CQ depth.

        Raises:
            PyverbsRDMAError: If ibv_resize_cq fails.
        """
        ...

    def poll(self, num_entries: int = 1) -> tuple[int, list[WC]]:
        """Poll the CQ for completions.

        Args:
            num_entries: Maximum number of completions to poll.

        Returns:
            A tuple (npolled, wcs) where *npolled* is the number of polled
            completions and *wcs* is a list of WC objects.

        Raises:
            PyverbsRDMAError: If ibv_poll_cq returns a negative error.
        """
        ...

    def req_notify(self, solicited_only: bool = False) -> None:
        """Request completion notification on the CQ.

        Args:
            solicited_only: If True, only notify for send/RDMA write WRs
                with the solicited bit set.

        Raises:
            PyverbsRDMAError: If ibv_req_notify_cq fails.
        """
        ...

    def ack_events(self, num_events: int) -> None:
        """Acknowledge CQ events.

        Must be called after receiving events via CompChannel.get_cq_event().

        Args:
            num_events: Number of events to acknowledge.
        """
        ...

    @property
    def comp_channel(self) -> CompChannel | None:
        """The completion channel attached to this CQ."""
        ...

    @property
    def cqe(self) -> int:
        """CQ capacity (number of CQEs)."""
        ...

    @property
    def cq(self) -> int:
        """Underlying ibv_cq pointer as integer."""
        ...

    def __str__(self) -> str: ...

class CQEX(PyverbsCM):
    """Extended Completion Queue (ibv_cq_ex).

    Provides per-WC field selection and batch polling via
    start_poll / poll_next / end_poll.

    Note: CQEX does NOT inherit from CQ in the implementation.
    """

    def __init__(self, context: Context, init_attr: CqInitAttrEx) -> None:
        """Create an extended CQ.

        Args:
            context: The device's Context.
            init_attr: Extended CQ initialization attributes.
        """
        ...

    def start_poll(self, attr: PollCqAttr) -> int:
        """Start polling a batch of work completions.

        Args:
            attr: Poll attributes (reserved for future extension).

        Returns:
            0 on success, ENOENT when no completions are available.
        """
        ...

    def poll_next(self) -> int:
        """Move to the next work completion in the current batch.

        Returns:
            0 on success, ENOENT when no more completions in this batch.
        """
        ...

    def end_poll(self) -> None:
        """Indicate the end of polling a batch of work completions."""
        ...

    def read_opcode(self) -> int:
        """Read the opcode of the current work completion.

        Returns:
            Work completion opcode (``ibv_wc_opcode``).
        """
        ...

    def read_vendor_err(self) -> int:
        """Read the vendor-specific error of the current work completion.

        Returns:
            Vendor-specific error code.
        """
        ...

    def read_byte_len(self) -> int:
        """Read the byte length of the current work completion.

        Returns:
            Number of bytes transferred.
        """
        ...

    def read_imm_data(self) -> int:
        """Read the immediate data of the current work completion.

        Returns:
            Immediate data value.
        """
        ...

    def read_qp_num(self) -> int:
        """Read the QP number of the current work completion.

        Returns:
            QP number of the completed WR.
        """
        ...

    def read_src_qp(self) -> int:
        """Read the source QP number of the current work completion.

        Returns:
            Source QP number (for UD QPs).
        """
        ...

    def read_wc_flags(self) -> int:
        """Read the WC flags of the current work completion.

        Returns:
            Work completion flags (``ibv_wc_flags_ex``).
        """
        ...

    def read_slid(self) -> int:
        """Read the source LID of the current work completion.

        Returns:
            Source LID.
        """
        ...

    def read_sl(self) -> int:
        """Read the service level of the current work completion.

        Returns:
            Service level.
        """
        ...

    def read_dlid_path_bits(self) -> int:
        """Read the DLID path bits of the current work completion.

        Returns:
            DLID path bits.
        """
        ...

    def read_timestamp(self) -> int:
        """Read the completion timestamp of the current work completion.

        Returns:
            Completion timestamp (HCA clock value).
        """
        ...

    def read_cvlan(self) -> int:
        """Read the CVLAN of the current work completion.

        Returns:
            CVLAN ID.
        """
        ...

    def read_flow_tag(self) -> int:
        """Read the flow tag of the current work completion.

        Returns:
            Flow tag value.
        """
        ...

    def read_tm_info(self) -> WcTmInfo:
        """Read tag matching information of the current work completion.

        Returns:
            A WcTmInfo object with tag and priv fields.
        """
        ...

    def read_completion_wallclock_ns(self) -> int:
        """Read the wallclock timestamp of the current completion.

        Returns:
            Wallclock timestamp in nanoseconds.
        """
        ...

    @property
    def status(self) -> int:
        """Status of the current work completion."""
        ...
    @status.setter
    def status(self, val: int) -> None: ...
    @property
    def wr_id(self) -> int:
        """Work request ID of the current work completion."""
        ...
    @wr_id.setter
    def wr_id(self, val: int) -> None: ...
    def __str__(self) -> str: ...

# ---------------------------------------------------------------------------
# Module-level utility functions
# ---------------------------------------------------------------------------

def cqe_status_to_str(status: int) -> str:
    """Convert a CQE status code to a human-readable string.

    Args:
        status: CQE status code (``ibv_wc_status``).

    Returns:
        Human-readable status string.
    """
    ...

def cqe_opcode_to_str(opcode: int) -> str:
    """Convert a CQE opcode to a human-readable string.

    Args:
        opcode: Work completion opcode (``ibv_wc_opcode``).

    Returns:
        Human-readable opcode string.
    """
    ...

def cqe_flags_to_str(flags: int) -> str:
    """Convert WC flags to a human-readable string.

    Args:
        flags: Work completion flags bitmask.

    Returns:
        Comma-separated flag names.
    """
    ...

def create_wc_flags_to_str(flags: int) -> str:
    """Convert ``ibv_wc_flags_ex`` to a human-readable string.

    Args:
        flags: Extended WC creation flags bitmask.

    Returns:
        Comma-separated flag names.
    """
    ...

def flags_to_str(flags: int, dictionary: dict[int, str]) -> str:
    """Convert a flags bitmask to a human-readable string using a dictionary.

    Args:
        flags: Bitmask of flags.
        dictionary: Mapping from flag bit to flag name string.

    Returns:
        Space-separated string of matched flag names.
    """
    ...

    def __str__(self) -> str: ...
