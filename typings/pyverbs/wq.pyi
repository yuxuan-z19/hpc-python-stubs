"""
Type stubs for pyverbs.wq — Work Queue (WQ) and RSS indirection types.
"""

from typing import Any

from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.cq import CQ, CQEX
from pyverbs.device import Context
from pyverbs.pd import PD
from pyverbs.wr import RecvWR

class WQInitAttr(PyverbsObject):
    """Work Queue initialization attributes (ibv_wq_init_attr)."""

    def __init__(
        self,
        wq_context: Any = None,
        wq_pd: PD | None = None,
        wq_cq: CQ | CQEX | None = None,
        wq_type: int = 0,
        max_wr: int = 100,
        max_sge: int = 1,
        comp_mask: int = 0,
        create_flags: int = 0,
    ) -> None:
        """Initialize WQ creation attributes.

        Args:
            wq_context: Associated WQ context.
            wq_pd: PD to associate with the WQ.
            wq_cq: CQ or CQEX to associate with the WQ.
            wq_type: Desired WQ type (ibv_wq_type).
            max_wr: Max outstanding WRs in the WQ.
            max_sge: Max scatter/gather elements per WR.
            comp_mask: Identifies valid fields.
            create_flags: Creation flags for the WQ.
        """
        ...

    @property
    def wq_type(self) -> int:
        """WQ type."""
        ...
    @wq_type.setter
    def wq_type(self, val: int) -> None: ...
    @property
    def pd(self) -> PD | None:
        """Associated PD."""
        ...
    @pd.setter
    def pd(self, val: PD) -> None: ...
    @property
    def cq(self) -> CQ | CQEX | None:
        """Associated CQ or CQEX."""
        ...
    @cq.setter
    def cq(self, val: CQ | CQEX) -> None: ...

class WQAttr(PyverbsObject):
    """Work Queue attributes (ibv_wq_attr).

    Used to modify a WQ's state and flags.
    """

    def __init__(
        self, attr_mask: int = 0, wq_state: int = 0, curr_wq_state: int = 0, flags: int = 0, flags_mask: int = 0
    ) -> None:
        """Initialize WQ modification attributes.

        Args:
            attr_mask: Identifies valid fields.
            wq_state: Desired WQ state.
            curr_wq_state: Current WQ state.
            flags: Flags values to modify.
            flags_mask: Which flags to modify.
        """
        ...

    @property
    def wq_state(self) -> int:
        """Desired WQ state."""
        ...
    @wq_state.setter
    def wq_state(self, val: int) -> None: ...
    @property
    def attr_mask(self) -> int:
        """Attribute mask."""
        ...
    @attr_mask.setter
    def attr_mask(self, val: int) -> None: ...
    @property
    def curr_wq_state(self) -> int:
        """Current WQ state."""
        ...
    @curr_wq_state.setter
    def curr_wq_state(self, val: int) -> None: ...
    @property
    def flags(self) -> int:
        """Flags to modify."""
        ...
    @flags.setter
    def flags(self, val: int) -> None: ...
    @property
    def flags_mask(self) -> int:
        """Flags mask."""
        ...
    @flags_mask.setter
    def flags_mask(self, val: int) -> None: ...

class WQ(PyverbsCM):
    """Work Queue (ibv_wq).

    A standalone Work Queue that can be used for RSS indirection tables.
    """

    def __init__(self, ctx: Context, attr: WQInitAttr) -> None:
        """Create a Work Queue.

        Args:
            ctx: The Context the WQ will be associated with.
            attr: WQ initial attributes.

        Raises:
            PyverbsRDMAErrno: If ibv_create_wq fails.
        """
        ...

    def modify(self, wq_attr: WQAttr) -> None:
        """Modify the WQ.

        Args:
            wq_attr: A WQAttr with updated values.

        Raises:
            PyverbsRDMAError: If ibv_modify_wq fails.
        """
        ...

    def post_recv(self, wr: RecvWR, bad_wr: RecvWR | None = None) -> None:
        """Post a receive WR on the WQ.

        Args:
            wr: The RecvWR to post.
            bad_wr: Filled with the bad WR on failure.

        Raises:
            PyverbsRDMAError: If ibv_post_wq_recv fails.
        """
        ...

    @property
    def wqn(self) -> int:
        """WQ number."""
        ...

class RwqIndTableInitAttr(PyverbsObject):
    """RWQ indirection table initialization attributes
    (ibv_rwq_ind_table_init_attr).
    """

    def __init__(self, log_ind_tbl_size: int = 5, wqs_list: list[WQ] | None = None, comp_mask: int = 0) -> None:
        """Initialize indirection table attributes.

        Args:
            log_ind_tbl_size: Log base 2 of the indirection table size.
            wqs_list: List of WQs to populate the table.
            comp_mask: Identifies valid fields.

        Raises:
            PyverbsUserError: If log_ind_tbl_size <= 0 or table too small.
        """
        ...

class RwqIndTable(PyverbsCM):
    """RWQ Indirection Table (ibv_rwq_ind_table).

    Used for RSS to distribute incoming packets across multiple WQs.
    """

    def __init__(self, ctx: Context, attr: RwqIndTableInitAttr) -> None:
        """Create an RWQ indirection table.

        Args:
            ctx: The Context the table will be associated with.
            attr: Initialization attributes.

        Raises:
            PyverbsRDMAErrno: If ibv_create_rwq_ind_table fails.
        """
        ...

    @property
    def wqs(self) -> list[WQ]:
        """List of WQs in the table."""
        ...

class RxHashConf(PyverbsObject):
    """RX Hash configuration (ibv_rx_hash_conf).

    Configures the RSS hash function, key, and fields for packet distribution.
    """

    def __init__(
        self,
        rx_hash_function: int = 0,
        rx_hash_key_len: int = 0,
        rx_hash_key: list[int] | None = None,
        rx_hash_fields_mask: int = 0,
    ) -> None:
        """Initialize RX hash configuration.

        Args:
            rx_hash_function: Hash function (ibv_rx_hash_function_flags).
            rx_hash_key_len: Hash key length in bytes.
            rx_hash_key: Hash key data as list of byte values.
            rx_hash_fields_mask: RX fields participating in hashing.

        Raises:
            PyverbsUserError: If key length doesn't match rx_hash_key_len.
        """
        ...

    @property
    def rx_hash_function(self) -> int:
        """Hash function."""
        ...
    @rx_hash_function.setter
    def rx_hash_function(self, val: int) -> None: ...
    @property
    def rx_hash_key_len(self) -> int:
        """Hash key length."""
        ...
    @rx_hash_key_len.setter
    def rx_hash_key_len(self, val: int) -> None: ...
    @property
    def rx_hash_fields_mask(self) -> int:
        """Hash fields mask."""
        ...
    @rx_hash_fields_mask.setter
    def rx_hash_fields_mask(self, val: int) -> None: ...
    @property
    def rx_hash_key(self) -> int:
        """Hash key (internal pointer)."""
        ...
    @rx_hash_key.setter
    def rx_hash_key(self, vals_list: list[int]) -> None: ...
