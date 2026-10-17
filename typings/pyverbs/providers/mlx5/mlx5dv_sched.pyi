"""
Type stubs for pyverbs.providers.mlx5.mlx5dv_sched — MLX5 scheduling elements.

Provides hierarchical QoS scheduling with nodes and leaves for
bandwidth allocation and rate limiting.
"""

from pyverbs.base import PyverbsObject
from pyverbs.device import Context

class Mlx5dvSchedAttr(PyverbsObject):
    """Scheduling element attributes (mlx5dv_sched_attr).

    Configures bandwidth share, max average bandwidth, and parent
    node for hierarchical scheduling.
    """

    def __init__(
        self,
        parent_sched_node: Mlx5dvSchedNode | None = None,
        bw_share: int = 0,
        max_avg_bw: int = 0,
        flags: int = 0,
        comp_mask: int = 0,
    ) -> None:
        """Create scheduling element attributes.

        Args:
            parent_sched_node: The parent Mlx5dvSchedNode. None if this
                attr is for the root node.
            bw_share: The relative bandwidth share allocated for this element.
                Default is 0.
            max_avg_bw: The maximal transmission rate allowed for the element,
                averaged over time. Default is 0 (unlimited).
            flags: Bitmask specifying which attributes are valid. Default is 0.
            comp_mask: Reserved for future extension. Default is 0.
        """
        ...

    @property
    def bw_share(self) -> int:
        """The relative bandwidth share allocated for this element."""
        ...

    @property
    def max_avg_bw(self) -> int:
        """The maximal transmission rate allowed, averaged over time."""
        ...

    @property
    def flags(self) -> int:
        """Bitmask of valid attributes."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask (reserved for future extension)."""
        ...

    def __str__(self) -> str: ...

class Mlx5dvSchedNode(PyverbsObject):
    """Scheduling node (mlx5dv_sched_node) for hierarchical QoS.

    A node in the scheduling hierarchy that can have child nodes or leaves.
    Used for bandwidth allocation and rate limiting.
    """

    def __init__(self, context: Context, sched_attr: Mlx5dvSchedAttr) -> None:
        """Create a scheduling node.

        Args:
            context: A Context to create the scheduling resources on.
            sched_attr: Mlx5dvSchedAttr containing the scheduling attributes.

        Raises:
            PyverbsRDMAErrno: If scheduling node creation fails.
        """
        ...

    def modify(self, sched_attr: Mlx5dvSchedAttr) -> None:
        """Modify scheduling parameters of this node.

        Args:
            sched_attr: Mlx5dvSchedAttr with the new scheduling parameters.
        """
        ...

    @property
    def sched_attr(self) -> Mlx5dvSchedAttr:
        """The scheduling attributes used at creation."""
        ...

    @property
    def bw_share(self) -> int:
        """The relative bandwidth share."""
        ...

    @property
    def max_avg_bw(self) -> int:
        """The maximal transmission rate allowed."""
        ...

    @property
    def flags(self) -> int:
        """Bitmask of valid attributes."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...

    def __str__(self) -> str: ...

class Mlx5dvSchedLeaf(PyverbsObject):
    """Scheduling leaf (mlx5dv_sched_leaf) attached to a QP.

    A leaf in the scheduling hierarchy that is directly associated
    with a QP's send or receive queue.
    """

    def __init__(self, context: Context, sched_attr: Mlx5dvSchedAttr) -> None:
        """Create a scheduling leaf.

        Args:
            context: A Context to create the scheduling resources on.
            sched_attr: Mlx5dvSchedAttr containing the scheduling attributes.

        Raises:
            PyverbsRDMAErrno: If scheduling leaf creation fails.
        """
        ...

    def modify(self, sched_attr: Mlx5dvSchedAttr) -> None:
        """Modify scheduling parameters of this leaf.

        Args:
            sched_attr: Mlx5dvSchedAttr with the new scheduling parameters.
        """
        ...

    @property
    def sched_attr(self) -> Mlx5dvSchedAttr:
        """The scheduling attributes used at creation."""
        ...

    @property
    def bw_share(self) -> int:
        """The relative bandwidth share."""
        ...

    @property
    def max_avg_bw(self) -> int:
        """The maximal transmission rate allowed."""
        ...

    @property
    def flags(self) -> int:
        """Bitmask of valid attributes."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...

    def __str__(self) -> str: ...
