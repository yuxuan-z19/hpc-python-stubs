"""
Type stubs for pyverbs.srq — Shared Receive Queue (SRQ) types.
"""

from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.cq import CQ, CQEX
from pyverbs.device import Context
from pyverbs.pd import PD
from pyverbs.wr import SGE, RecvWR
from pyverbs.xrcd import XRCD

class SrqAttr(PyverbsObject):
    """SRQ attributes (ibv_srq_attr)."""

    def __init__(self, max_wr: int = 100, max_sge: int = 1, srq_limit: int = 0) -> None:
        """Initialize SRQ attributes.

        Args:
            max_wr: Maximum number of outstanding WRs in the SRQ.
            max_sge: Maximum number of scatter-gather elements per WR.
            srq_limit: The SRQ limit.
        """
        ...

    @property
    def max_wr(self) -> int:
        """Maximum number of outstanding WRs."""
        ...
    @max_wr.setter
    def max_wr(self, val: int) -> None: ...
    @property
    def max_sge(self) -> int:
        """Maximum number of scatter-gather elements per WR."""
        ...
    @max_sge.setter
    def max_sge(self, val: int) -> None: ...
    @property
    def srq_limit(self) -> int:
        """SRQ limit."""
        ...
    @srq_limit.setter
    def srq_limit(self, val: int) -> None: ...

class SrqInitAttr(PyverbsObject):
    """Basic SRQ initialization attributes (ibv_srq_init_attr).

    Used when creating a basic SRQ via PD.
    """

    def __init__(self, attr: SrqAttr | None = None) -> None:
        """Initialize basic SRQ creation attributes.

        Args:
            attr: Optional SrqAttr with initial values.
        """
        ...

    @property
    def max_wr(self) -> int:
        """Maximum number of outstanding WRs."""
        ...

    @property
    def max_sge(self) -> int:
        """Maximum number of scatter-gather elements per WR."""
        ...

    @property
    def srq_limit(self) -> int:
        """SRQ limit."""
        ...

class SrqInitAttrEx(PyverbsObject):
    """Extended SRQ initialization attributes (ibv_srq_init_attr_ex).

    Used when creating an SRQ via Context (SRQ_EX), supporting additional
    features like XRC, tag matching, and custom CQ/PD association.
    """

    def __init__(self, max_wr: int = 100, max_sge: int = 1, srq_limit: int = 0) -> None:
        """Initialize extended SRQ creation attributes.

        Args:
            max_wr: Maximum number of outstanding WRs.
            max_sge: Maximum number of scatter-gather elements per WR.
            srq_limit: The SRQ limit.
        """
        ...

    @property
    def max_wr(self) -> int:
        """Maximum number of outstanding WRs."""
        ...

    @property
    def max_sge(self) -> int:
        """Maximum number of scatter-gather elements per WR."""
        ...

    @property
    def srq_limit(self) -> int:
        """SRQ limit."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    @property
    def srq_type(self) -> int:
        """SRQ type (ibv_srq_type)."""
        ...
    @srq_type.setter
    def srq_type(self, val: int) -> None: ...
    @property
    def pd(self) -> PD | None:
        """Protection Domain to associate with the SRQ."""
        ...
    @pd.setter
    def pd(self, val: PD) -> None: ...
    @property
    def xrcd(self) -> XRCD | None:
        """XRC domain to associate with the SRQ."""
        ...
    @xrcd.setter
    def xrcd(self, val: XRCD) -> None: ...
    @property
    def max_num_tags(self) -> int:
        """Maximum number of tags for tag matching."""
        ...
    @max_num_tags.setter
    def max_num_tags(self, val: int) -> None: ...
    @property
    def max_ops(self) -> int:
        """Maximum number of outstanding tag matching operations."""
        ...
    @max_ops.setter
    def max_ops(self, val: int) -> None: ...
    @property
    def cq(self) -> CQ | CQEX | None:
        """CQ or CQEX for tag matching completions."""
        ...
    @cq.setter
    def cq(self, val: CQ | CQEX) -> None: ...

class OpsWr(PyverbsCM):
    """Operations work request for SRQ tagged matching (ibv_ops_wr).

    Used with SRQ.post_srq_ops() for tag add/delete/sync operations.
    """

    def __init__(
        self,
        wr_id: int = 0,
        opcode: int = 0,
        flags: int = 0,
        next_wr: OpsWr | None = None,
        unexpected_cnt: int = 0,
        recv_wr_id: int = 0,
        num_sge: int | None = None,
        tag: int = 0,
        mask: int = 0,
        sg_list: list[SGE] | None = None,
    ) -> None:
        """Initialize an operations WR.

        Args:
            wr_id: Work request ID.
            opcode: Operation opcode (ibv_ops_wr_opcode).
            flags: Operation flags (ibv_ops_flags).
            next_wr: Next OpsWr in the chain.
            unexpected_cnt: Unexpected count for sync operations.
            recv_wr_id: Receive WR ID for tag add operations.
            num_sge: Number of scatter-gather elements.
            tag: Tag value for tag add/delete.
            mask: Tag mask for tag add.
            sg_list: Scatter-gather list.
        """
        ...

    @property
    def wr_id(self) -> int:
        """Work request ID."""
        ...
    @wr_id.setter
    def wr_id(self, val: int) -> None: ...
    @property
    def next_wr(self) -> OpsWr | None:
        """Next OpsWr in the chain."""
        ...
    @next_wr.setter
    def next_wr(self, val: OpsWr) -> None: ...
    @property
    def opcode(self) -> int:
        """Operation opcode."""
        ...
    @opcode.setter
    def opcode(self, val: int) -> None: ...
    @property
    def flags(self) -> int:
        """Operation flags."""
        ...
    @flags.setter
    def flags(self, val: int) -> None: ...
    @property
    def unexpected_cnt(self) -> int:
        """Unexpected count."""
        ...
    @unexpected_cnt.setter
    def unexpected_cnt(self, val: int) -> None: ...
    @property
    def recv_wr_id(self) -> int:
        """Receive WR ID for tag add."""
        ...
    @recv_wr_id.setter
    def recv_wr_id(self, val: int) -> None: ...
    @property
    def tag(self) -> int:
        """Tag value."""
        ...
    @tag.setter
    def tag(self, val: int) -> None: ...
    @property
    def handle(self) -> int:
        """Tag matching handle."""
        ...
    @handle.setter
    def handle(self, val: int) -> None: ...
    @property
    def mask(self) -> int:
        """Tag mask."""
        ...
    @mask.setter
    def mask(self, val: int) -> None: ...

class SRQ(PyverbsCM):
    """Shared Receive Queue (ibv_srq).

    An SRQ enables sharing of receive buffers across multiple QPs,
    reducing memory consumption and improving resource utilization.
    """

    def __init__(self, creator: PD | Context, attr: SrqInitAttr | SrqInitAttrEx) -> None:
        """Create a Shared Receive Queue.

        Args:
            creator: A PD (basic SRQ) or Context (extended SRQ).
            attr: SrqInitAttr (for PD) or SrqInitAttrEx (for Context).

        Raises:
            PyverbsRDMAError: If creator type is unsupported.
            PyverbsRDMAErrno: If SRQ creation fails.
        """
        ...

    def get_srq_num(self) -> int:
        """Get the SRQ number.

        Returns:
            The SRQ number.

        Raises:
            PyverbsRDMAError: If ibv_get_srq_num fails.
        """
        ...

    def modify(self, attr: SrqAttr, comp_mask: int) -> None:
        """Modify SRQ attributes.

        Args:
            attr: New SRQ attributes.
            comp_mask: Which attributes to modify.

        Raises:
            PyverbsRDMAError: If ibv_modify_srq fails.
        """
        ...

    def query(self) -> SrqAttr:
        """Query SRQ attributes.

        Returns:
            An SrqAttr with the current SRQ attributes.

        Raises:
            PyverbsRDMAError: If ibv_query_srq fails.
        """
        ...

    def post_srq_ops(self, wr: OpsWr, bad_wr: OpsWr | None = None) -> None:
        """Perform tag matching configuration operations on the SRQ.

        Args:
            wr: Ops Work Requests to post to the TM-SRQ.
            bad_wr: Filled with the first Ops WR that failed (on error).

        Raises:
            PyverbsRDMAError: If ibv_post_srq_ops fails.
        """
        ...

    def post_recv(self, wr: RecvWR, bad_wr: RecvWR | None = None) -> None:
        """Post a receive WR to the SRQ.

        Args:
            wr: A RecvWR to post.
            bad_wr: Filled with the first RecvWR that failed (on error).

        Raises:
            PyverbsRDMAError: If ibv_post_srq_recv fails.
        """
        ...

    @property
    def srq(self) -> int:
        """Underlying ibv_srq pointer as integer."""
        ...
