"""
Type stubs for pyverbs.qp — Queue Pair (QP) types and operations.

Provides QP creation, state transitions, work request posting, and the
extended QP (QPEx) batch work request API.
"""

from typing import Any

from pyverbs.addr import AH, AHAttr
from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.comp_cntr import CompCntr
from pyverbs.cq import CQ, CQEX
from pyverbs.device import Context
from pyverbs.mr import MW, MWBind
from pyverbs.pd import PD
from pyverbs.srq import SRQ
from pyverbs.wq import RwqIndTable
from pyverbs.wr import SGE, RecvWR, SendWR
from pyverbs.xrcd import XRCD

class QPCap(PyverbsObject):
    """QP capabilities (ibv_qp_cap)."""

    def __init__(
        self,
        max_send_wr: int = 1,
        max_recv_wr: int = 10,
        max_send_sge: int = 1,
        max_recv_sge: int = 1,
        max_inline_data: int = 0,
    ) -> None:
        """Initialize QP capabilities.

        Args:
            max_send_wr: Max outstanding WRs in the send queue.
            max_recv_wr: Max outstanding WRs in the receive queue.
            max_send_sge: Max scatter-gather elements per WR in the SQ.
            max_recv_sge: Max scatter-gather elements per WR in the RQ.
            max_inline_data: Max inline data bytes in the SQ (0 to disable).
        """
        ...
    @property
    def max_send_wr(self) -> int:
        """Maximum send work requests."""
        ...
    @max_send_wr.setter
    def max_send_wr(self, val: int) -> None: ...
    @property
    def max_recv_wr(self) -> int:
        """Maximum receive work requests."""
        ...
    @max_recv_wr.setter
    def max_recv_wr(self, val: int) -> None: ...
    @property
    def max_send_sge(self) -> int:
        """Maximum send scatter/gather entries."""
        ...
    @max_send_sge.setter
    def max_send_sge(self, val: int) -> None: ...
    @property
    def max_recv_sge(self) -> int:
        """Maximum receive scatter/gather entries."""
        ...
    @max_recv_sge.setter
    def max_recv_sge(self, val: int) -> None: ...
    @property
    def max_inline_data(self) -> int:
        """Maximum inline data size in bytes."""
        ...
    @max_inline_data.setter
    def max_inline_data(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class QPInitAttr(PyverbsObject):
    """QP initialization attributes (ibv_qp_init_attr)."""

    def __init__(
        self,
        qp_type: int = 4,
        qp_context: Any = None,
        scq: CQ | CQEX | None = None,
        rcq: CQ | CQEX | None = None,
        srq: SRQ | None = None,
        cap: QPCap | None = None,
        sq_sig_all: int = 1,
    ) -> None:
        """Initialize QP creation attributes.

        Args:
            qp_type: QP type (IBV_QPT_RC, IBV_QPT_UC, IBV_QPT_UD, etc.).
            qp_context: Associated QP context (opaque).
            scq: Send CQ (CQ or CQEX).
            rcq: Receive CQ (CQ or CQEX).
            srq: Shared receive queue to use as RQ.
            cap: QPCap object with queue dimensions.
            sq_sig_all: If set, every send WR generates a completion.
        """
        ...
    @property
    def send_cq(self) -> CQ | CQEX | None:
        """Send completion queue."""
        ...
    @send_cq.setter
    def send_cq(self, val: CQ | CQEX) -> None: ...
    @property
    def recv_cq(self) -> CQ | CQEX | None:
        """Receive completion queue."""
        ...
    @recv_cq.setter
    def recv_cq(self, val: CQ | CQEX) -> None: ...
    @property
    def srq(self) -> SRQ | None:
        """Shared receive queue."""
        ...
    @srq.setter
    def srq(self, val: SRQ) -> None: ...
    @property
    def cap(self) -> QPCap:
        """QP capabilities."""
        ...
    @cap.setter
    def cap(self, val: QPCap) -> None: ...
    @property
    def qp_type(self) -> int:
        """QP type."""
        ...
    @qp_type.setter
    def qp_type(self, val: int) -> None: ...
    @property
    def sq_sig_all(self) -> int:
        """Whether all send WRs are signalled."""
        ...
    @sq_sig_all.setter
    def sq_sig_all(self, val: int) -> None: ...
    @property
    def max_send_wr(self) -> int:
        """Maximum send work requests."""
        ...
    @max_send_wr.setter
    def max_send_wr(self, val: int) -> None: ...
    @property
    def max_recv_wr(self) -> int:
        """Maximum receive work requests."""
        ...
    @max_recv_wr.setter
    def max_recv_wr(self, val: int) -> None: ...
    @property
    def max_send_sge(self) -> int:
        """Maximum send scatter/gather entries."""
        ...
    @max_send_sge.setter
    def max_send_sge(self, val: int) -> None: ...
    @property
    def max_recv_sge(self) -> int:
        """Maximum receive scatter/gather entries."""
        ...
    @max_recv_sge.setter
    def max_recv_sge(self, val: int) -> None: ...
    @property
    def max_inline_data(self) -> int:
        """Maximum inline data size in bytes."""
        ...
    @max_inline_data.setter
    def max_inline_data(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class QPInitAttrEx(PyverbsObject):
    """Extended QP initialization attributes (ibv_qp_init_attr_ex)."""

    def __init__(
        self,
        qp_type: int = 4,
        qp_context: Any = None,
        scq: CQ | CQEX | None = None,
        rcq: CQ | CQEX | None = None,
        srq: SRQ | None = None,
        cap: QPCap | None = None,
        sq_sig_all: int = 0,
        pd: PD | None = None,
        xrcd: XRCD | None = None,
        create_flags: int = 0,
        max_tso_header: int = 0,
        comp_mask: int = 0,
        source_qpn: int = 0,
        ind_table: RwqIndTable | None = None,
    ) -> None:
        """Initialize extended QP creation attributes.

        Args:
            qp_type: QP type.
            qp_context: Opaque QP context.
            scq: Send CQ.
            rcq: Receive CQ.
            srq: Shared receive queue.
            cap: QPCap object.
            sq_sig_all: If set, every send WR generates a completion.
            pd: Protection Domain (required for ibv_create_qp_ex).
            xrcd: XRC domain (for XRC QPs).
            create_flags: QP creation flags (IBV_QP_CREATE_*).
            max_tso_header: Max TSO header size.
            comp_mask: Compatibility mask (IBV_QP_INIT_ATTR_*).
            source_qpn: Source QP number (for IBV_QP_CREATE_SOURCE_QPN).
            ind_table: RWQ indirection table (for RSS).
        """
        ...
    @property
    def send_cq(self) -> CQ | CQEX | None:
        """Send completion queue."""
        ...
    @send_cq.setter
    def send_cq(self, val: CQ | CQEX) -> None: ...
    @property
    def recv_cq(self) -> CQ | CQEX | None:
        """Receive completion queue."""
        ...
    @recv_cq.setter
    def recv_cq(self, val: CQ | CQEX) -> None: ...
    @property
    def cap(self) -> QPCap:
        """QP capabilities."""
        ...
    @cap.setter
    def cap(self, val: QPCap) -> None: ...
    @property
    def qp_type(self) -> int:
        """QP type."""
        ...
    @qp_type.setter
    def qp_type(self, val: int) -> None: ...
    @property
    def sq_sig_all(self) -> int:
        """Whether all send WRs are signalled."""
        ...
    @sq_sig_all.setter
    def sq_sig_all(self, val: int) -> None: ...
    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    @property
    def pd(self) -> PD | None:
        """Protection domain."""
        ...
    @pd.setter
    def pd(self, val: PD) -> None: ...
    @property
    def xrcd(self) -> XRCD | None:
        """XRC domain."""
        ...
    @xrcd.setter
    def xrcd(self, val: XRCD) -> None: ...
    @property
    def srq(self) -> SRQ | None:
        """Shared receive queue."""
        ...
    @srq.setter
    def srq(self, val: SRQ) -> None: ...
    @property
    def create_flags(self) -> int:
        """Creation flags."""
        ...
    @create_flags.setter
    def create_flags(self, val: int) -> None: ...
    @property
    def max_tso_header(self) -> int:
        """Maximum TSO header size."""
        ...
    @max_tso_header.setter
    def max_tso_header(self, val: int) -> None: ...
    @property
    def source_qpn(self) -> int:
        """Source QP number."""
        ...
    @source_qpn.setter
    def source_qpn(self, val: int) -> None: ...
    @property
    def max_send_wr(self) -> int:
        """Maximum send work requests."""
        ...
    @max_send_wr.setter
    def max_send_wr(self, val: int) -> None: ...
    @property
    def max_recv_wr(self) -> int:
        """Maximum receive work requests."""
        ...
    @max_recv_wr.setter
    def max_recv_wr(self, val: int) -> None: ...
    @property
    def max_send_sge(self) -> int:
        """Maximum send scatter/gather entries."""
        ...
    @max_send_sge.setter
    def max_send_sge(self, val: int) -> None: ...
    @property
    def max_recv_sge(self) -> int:
        """Maximum receive scatter/gather entries."""
        ...
    @max_recv_sge.setter
    def max_recv_sge(self, val: int) -> None: ...
    @property
    def max_inline_data(self) -> int:
        """Maximum inline data size in bytes."""
        ...
    @max_inline_data.setter
    def max_inline_data(self, val: int) -> None: ...
    @property
    def ind_table(self) -> RwqIndTable | None:
        """RWQ indirection table."""
        ...
    @ind_table.setter
    def ind_table(self, val: RwqIndTable) -> None: ...
    def mask_to_str(self, mask: int) -> str:
        """Convert a comp_mask bitmask to a human-readable string.

        Args:
            mask: Compatibility mask value.

        Returns:
            Space-separated string of mask component names.
        """
        ...

    def flags_to_str(self, flags: int) -> str:
        """Convert QP creation flags to a human-readable string.

        Args:
            flags: QP create flags bitmask.

        Returns:
            Space-separated string of flag names.
        """
        ...

    def __str__(self) -> str: ...

class QPAttr(PyverbsObject):
    """QP attributes for modify/query (ibv_qp_attr)."""

    def __init__(self, qp_state: int = 1, cur_qp_state: int = 0, port_num: int = 1, path_mtu: int = 3) -> None:
        """Initialize QP attributes with defaults for reset-to-init transition.

        Args:
            qp_state: Desired QP state (IBV_QPS_*).
            cur_qp_state: Current QP state.
            port_num: Port number.
            path_mtu: Path MTU (IBV_MTU_*).
        """
        ...
    @property
    def qp_state(self) -> int:
        """Current QP state."""
        ...
    @qp_state.setter
    def qp_state(self, val: int) -> None: ...
    @property
    def cur_qp_state(self) -> int:
        """Current QP state."""
        ...
    @cur_qp_state.setter
    def cur_qp_state(self, val: int) -> None: ...
    @property
    def path_mtu(self) -> int:
        """Path MTU."""
        ...
    @path_mtu.setter
    def path_mtu(self, val: int) -> None: ...
    @property
    def path_mig_state(self) -> int:
        """Path migration state."""
        ...
    @path_mig_state.setter
    def path_mig_state(self, val: int) -> None: ...
    @property
    def qkey(self) -> int:
        """Q_Key for UD/QP1."""
        ...
    @qkey.setter
    def qkey(self, val: int) -> None: ...
    @property
    def rq_psn(self) -> int:
        """Receive queue packet sequence number."""
        ...
    @rq_psn.setter
    def rq_psn(self, val: int) -> None: ...
    @property
    def sq_psn(self) -> int:
        """Send queue packet sequence number."""
        ...
    @sq_psn.setter
    def sq_psn(self, val: int) -> None: ...
    @property
    def dest_qp_num(self) -> int:
        """Destination QP number."""
        ...
    @dest_qp_num.setter
    def dest_qp_num(self, val: int) -> None: ...
    @property
    def qp_access_flags(self) -> int:
        """QP access flags (IBV_ACCESS_*)."""
        ...
    @qp_access_flags.setter
    def qp_access_flags(self, val: int) -> None: ...
    @property
    def cap(self) -> QPCap:
        """QP capabilities."""
        ...
    @cap.setter
    def cap(self, val: QPCap) -> None: ...
    @property
    def ah_attr(self) -> AHAttr:
        """Primary address handle attributes."""
        ...
    @ah_attr.setter
    def ah_attr(self, val: AHAttr) -> None: ...
    @property
    def alt_ah_attr(self) -> AHAttr:
        """Alternate path address handle attributes."""
        ...
    @alt_ah_attr.setter
    def alt_ah_attr(self, val: AHAttr) -> None: ...
    @property
    def pkey_index(self) -> int:
        """P_Key index."""
        ...
    @pkey_index.setter
    def pkey_index(self, val: int) -> None: ...
    @property
    def alt_pkey_index(self) -> int:
        """Alternate P_Key index."""
        ...
    @alt_pkey_index.setter
    def alt_pkey_index(self, val: int) -> None: ...
    @property
    def en_sqd_async_notify(self) -> int:
        """Enable SQD async notification."""
        ...
    @en_sqd_async_notify.setter
    def en_sqd_async_notify(self, val: int) -> None: ...
    @property
    def sq_draining(self) -> int:
        """Whether the send queue is draining."""
        ...
    @sq_draining.setter
    def sq_draining(self, val: int) -> None: ...
    @property
    def max_rd_atomic(self) -> int:
        """Max outstanding RDMA read/atomic operations initiated by this QP."""
        ...
    @max_rd_atomic.setter
    def max_rd_atomic(self, val: int) -> None: ...
    @property
    def max_dest_rd_atomic(self) -> int:
        """Max outstanding RDMA read/atomic operations from remote."""
        ...
    @max_dest_rd_atomic.setter
    def max_dest_rd_atomic(self, val: int) -> None: ...
    @property
    def min_rnr_timer(self) -> int:
        """Minimum RNR NAK timer."""
        ...
    @min_rnr_timer.setter
    def min_rnr_timer(self, val: int) -> None: ...
    @property
    def port_num(self) -> int:
        """Port number."""
        ...
    @port_num.setter
    def port_num(self, val: int) -> None: ...
    @property
    def timeout(self) -> int:
        """Local ACK timeout."""
        ...
    @timeout.setter
    def timeout(self, val: int) -> None: ...
    @property
    def retry_cnt(self) -> int:
        """Retry count."""
        ...
    @retry_cnt.setter
    def retry_cnt(self, val: int) -> None: ...
    @property
    def rnr_retry(self) -> int:
        """RNR retry count."""
        ...
    @rnr_retry.setter
    def rnr_retry(self, val: int) -> None: ...
    @property
    def alt_port_num(self) -> int:
        """Alternate port number."""
        ...
    @alt_port_num.setter
    def alt_port_num(self, val: int) -> None: ...
    @property
    def alt_timeout(self) -> int:
        """Alternate timeout."""
        ...
    @alt_timeout.setter
    def alt_timeout(self, val: int) -> None: ...
    @property
    def rate_limit(self) -> int:
        """Rate limit in kbps."""
        ...
    @rate_limit.setter
    def rate_limit(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class ECE(PyverbsCM):
    """Enhanced Connection Establishment (ECE) options."""

    def __init__(self, vendor_id: int = 0, options: int = 0, comp_mask: int = 0) -> None:
        """Initialize ECE options.

        Args:
            vendor_id: Unique identifier of the provider vendor.
            options: Provider-specific attributes to enable.
            comp_mask: Bitmask specifying which ECE options are valid.
        """
        ...
    @property
    def vendor_id(self) -> int:
        """Vendor ID."""
        ...
    @vendor_id.setter
    def vendor_id(self, val: int) -> None: ...
    @property
    def options(self) -> int:
        """ECE options."""
        ...
    @options.setter
    def options(self, val: int) -> None: ...
    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class QPRateLimitAttr(PyverbsObject):
    """QP rate limiting attributes (ibv_qp_rate_limit_attr)."""

    def __init__(self, rate_limit: int = 0, max_burst_sz: int = 0, typical_pkt_sz: int = 0, comp_mask: int = 0) -> None:
        """Initialize rate limit attributes.

        Args:
            rate_limit: Rate limit in kbps (0 = unlimited).
            max_burst_sz: Maximum burst size in bytes.
            typical_pkt_sz: Typical packet size in bytes.
            comp_mask: Compatibility mask.
        """
        ...
    @property
    def rate_limit(self) -> int:
        """Rate limit."""
        ...
    @rate_limit.setter
    def rate_limit(self, val: int) -> None: ...
    @property
    def max_burst_sz(self) -> int:
        """Maximum burst size."""
        ...
    @max_burst_sz.setter
    def max_burst_sz(self, val: int) -> None: ...
    @property
    def typical_pkt_sz(self) -> int:
        """Typical packet size."""
        ...
    @typical_pkt_sz.setter
    def typical_pkt_sz(self, val: int) -> None: ...
    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class QPAttachCompCntrAttr(PyverbsObject):
    """Attributes for attaching a completion counter to a QP."""

    def __init__(self, op_mask: int = 0) -> None: ...
    @property
    def op_mask(self) -> int:
        """Bitmask of operations to count."""
        ...

class DataBuffer(PyverbsCM):
    """Data buffer descriptor for inline data list."""

    def __init__(self, addr: int, length: int) -> None: ...

class QP(PyverbsCM):
    """Queue Pair (ibv_qp). Core data path object for RDMA operations."""

    def __init__(
        self, creator: PD | Context, init_attr: QPInitAttr | QPInitAttrEx, qp_attr: QPAttr | None = None
    ) -> None:
        """Create a QP and optionally transition it toward RTS.

        Args:
            creator: PD (uses ibv_create_qp) or Context (uses ibv_create_qp_ex).
            init_attr: QPInitAttr or QPInitAttrEx with initial configuration.
            qp_attr: If provided, pyverbs will transition the QP state as far
                     as possible toward RTS. UD/Raw Packet reach RTS; RC/UC
                     reach INIT (remote QPN needed for RTR).
        """
        ...
    def close(self) -> None:
        """Destroy the QP."""
        ...
    def to_init(self, qp_attr: QPAttr) -> None:
        """Transition QP to INIT state.

        Args:
            qp_attr: QPAttr with attributes for the RESET→INIT transition.
        """
        ...
    def to_rtr(self, qp_attr: QPAttr) -> None:
        """Transition QP to RTR state (via INIT if needed).

        Args:
            qp_attr: QPAttr with attributes for the INIT→RTR transition.
        """
        ...
    def to_rts(self, qp_attr: QPAttr) -> None:
        """Transition QP to RTS state (via RTR if needed).

        Args:
            qp_attr: QPAttr with attributes for the RTR→RTS transition.
        """
        ...
    def query(self, attr_mask: int) -> tuple[QPAttr, QPInitAttr]:
        """Query the QP.

        Args:
            attr_mask: Minimum attributes to retrieve (ibv_qp_attr_mask).

        Returns:
            Tuple of (QPAttr, QPInitAttr) with current QP state.
        """
        ...
    def modify(self, qp_attr: QPAttr, comp_mask: int) -> None:
        """Modify the QP.

        Args:
            qp_attr: QPAttr with updated values.
            comp_mask: Bitmask of attributes to modify (ibv_qp_attr_mask).
        """
        ...
    def modify_rate_limit(self, attr: QPRateLimitAttr) -> None:
        """Modify QP rate limit (lightweight, no other attributes affected).

        Args:
            attr: QPRateLimitAttr with rate limiting parameters.
        """
        ...
    def attach_comp_cntr(self, comp_cntr: CompCntr, attr: QPAttachCompCntrAttr) -> None:
        """Attach a completion counter to this QP.

        Args:
            comp_cntr: CompCntr to attach.
            attr: Attach attributes including op_mask.
        """
        ...
    def post_recv(self, wr: RecvWR, bad_wr: RecvWR | None = None) -> None:
        """Post a receive work request.

        Args:
            wr: RecvWR to post.
            bad_wr: RecvWR to hold the first failed WR on error.
        """
        ...
    def post_send(self, wr: SendWR, bad_wr: SendWR | None = None) -> None:
        """Post a send work request.

        Args:
            wr: SendWR to post.
            bad_wr: SendWR to hold the first failed WR on error.
        """
        ...
    def set_ece(self, ece: ECE) -> None:
        """Set ECE options for QP configuration.

        Args:
            ece: ECE object with the requested values.
        """
        ...
    def query_ece(self) -> ECE:
        """Query the QP's ECE options.

        Returns:
            ECE object with this QP's ECE configuration.
        """
        ...
    def bind_mw(self, mw: MW, mw_bind: MWBind) -> None:
        """Bind a type 1 memory window.

        Args:
            mw: Memory window to bind.
            mw_bind: MWBind with bind attributes.
        """
        ...
    def query_data_in_order(self, op: int, flags: int = 0) -> int:
        """Query if QP data is guaranteed to be in order.

        Args:
            op: Operation type.
            flags: Query flags (ibv_query_qp_data_in_order_flags).

        Returns:
            Capability bitmask or 0/1 depending on flags.
        """
        ...
    @property
    def qp_type(self) -> int:
        """QP type (IBV_QPT_*)."""
        ...
    @property
    def qp_state(self) -> int:
        """Current QP state (IBV_QPS_*)."""
        ...
    @property
    def qp_num(self) -> int:
        """QP number."""
        ...
    @property
    def qp(self) -> int:
        """Underlying ibv_qp pointer as integer."""
        ...

    def __str__(self) -> str: ...

class QPEx(QP):
    """Extended Queue Pair (ibv_qp_ex) with batch WR API."""

    def __init__(
        self, creator: PD | Context, init_attr: QPInitAttr | QPInitAttrEx, qp_attr: QPAttr | None = None
    ) -> None:
        """Create an extended QP.

        Args:
            creator: PD or Context.
            init_attr: QPInitAttr or QPInitAttrEx.
            qp_attr: Optional QPAttr for state transitions.
        """
        ...
    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    @property
    def wr_id(self) -> int:
        """Current work request ID."""
        ...
    @wr_id.setter
    def wr_id(self, val: int) -> None: ...
    @property
    def wr_flags(self) -> int:
        """Current work request flags (IBV_SEND_*)."""
        ...
    @wr_flags.setter
    def wr_flags(self, val: int) -> None: ...
    @property
    def ind_table(self) -> RwqIndTable | None:
        """RWQ indirection table (read-only)."""
        ...
    # ── Batch WR API (ibv_wr_*) ──
    def wr_start(self) -> None:
        """Start a new work request batch."""
        ...
    def wr_complete(self) -> None:
        """Complete the current work request batch."""
        ...
    def wr_abort(self) -> None:
        """Abort the current work request batch."""
        ...
    def wr_send(self) -> None:
        """Build a send WR."""
        ...
    def wr_send_imm(self, data: int) -> None:
        """Build a send-with-immediate WR.

        Args:
            data: 32-bit immediate data value.
        """
        ...
    def wr_send_inv(self, invalidate_rkey: int) -> None:
        """Build a send-with-invalidate WR.

        Args:
            invalidate_rkey: Remote memory key to invalidate.
        """
        ...
    def wr_send_tso(self, hdr: int, hdr_sz: int, mss: int) -> None:
        """Build a TSO send WR.

        Args:
            hdr: Pointer to the header buffer.
            hdr_sz: Header size in bytes.
            mss: Maximum segment size.
        """
        ...
    def wr_rdma_read(self, rkey: int, remote_addr: int) -> None:
        """Build an RDMA read WR.

        Args:
            rkey: Remote memory key.
            remote_addr: Remote virtual address.
        """
        ...
    def wr_rdma_write(self, rkey: int, remote_addr: int) -> None:
        """Build an RDMA write WR.

        Args:
            rkey: Remote memory key.
            remote_addr: Remote virtual address.
        """
        ...
    def wr_rdma_write_imm(self, rkey: int, remote_addr: int, data: int) -> None:
        """Build an RDMA write-with-immediate WR.

        Args:
            rkey: Remote memory key.
            remote_addr: Remote virtual address.
            data: 32-bit immediate data value.
        """
        ...
    def wr_flush(self, rkey: int, remote_addr: int, length: int, ptype: int, level: int) -> None:
        """Build a flush WR.

        Args:
            rkey: Remote memory key.
            remote_addr: Remote virtual address.
            length: Flush length in bytes.
            ptype: Flush placement type.
            level: Flush select level.
        """
        ...
    def wr_atomic_cmp_swp(self, rkey: int, remote_addr: int, compare: int, swap: int) -> None:
        """Build an atomic compare-and-swap WR.

        Args:
            rkey: Remote memory key.
            remote_addr: Remote virtual address.
            compare: Expected value for comparison.
            swap: Value to swap in if comparison succeeds.
        """
        ...
    def wr_atomic_fetch_add(self, rkey: int, remote_addr: int, add: int) -> None:
        """Build an atomic fetch-and-add WR.

        Args:
            rkey: Remote memory key.
            remote_addr: Remote virtual address.
            add: Value to add to the remote data.
        """
        ...
    def wr_atomic_write(self, rkey: int, remote_addr: int, atomic_wr: bytes) -> None:
        """Build an atomic write WR.

        Args:
            rkey: Remote memory key.
            remote_addr: Remote virtual address.
            atomic_wr: Atomic write data (up to 16 bytes).
        """
        ...
    def wr_bind_mw(self, mw: MW, rkey: int, bind_info: MWBind) -> None:
        """Build a bind-memory-window WR.

        Args:
            mw: Memory window to bind.
            rkey: New rkey for the bound window.
            bind_info: MWBind information (MR, address, length, access).
        """
        ...
    def wr_local_inv(self, invalidate_rkey: int) -> None:
        """Build a local-invalidate WR.

        Args:
            invalidate_rkey: Memory key to invalidate locally.
        """
        ...
    def wr_set_ud_addr(self, ah: AH, remote_qpn: int, remote_rkey: int) -> None:
        """Set UD address for the current WR.

        Args:
            ah: Address handle.
            remote_qpn: Remote QP number.
            remote_rkey: Remote Q_Key.
        """
        ...
    def wr_set_xrc_srqn(self, remote_srqn: int) -> None:
        """Set XRC SRQ number for the current WR.

        Args:
            remote_srqn: Remote SRQ number for XRC.
        """
        ...
    def wr_set_sge(self, sge: SGE) -> None:
        """Set a single SGE for the current WR.

        Args:
            sge: An SGE object with addr, length, and lkey.
        """
        ...
    def wr_set_sge_list(self, num_sge: int, sg_list: list[SGE]) -> None:
        """Set the SGE list for the current WR.

        Args:
            num_sge: Number of SGEs.
            sg_list: List of SGE objects.
        """
        ...
    def wr_set_inline_data(self, addr: int, length: int) -> None:
        """Set inline data for the current WR.

        Args:
            addr: Pointer to the inline data buffer.
            length: Data length in bytes.
        """
        ...
    def wr_set_inline_data_list(self, num_buf: int, buf_list: list[DataBuffer]) -> None:
        """Set inline data buffer list for the current WR.

        Args:
            num_buf: Number of buffers.
            buf_list: List of DataBuffer objects.
        """
        ...
