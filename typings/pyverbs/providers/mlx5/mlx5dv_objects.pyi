"""
Type stubs for pyverbs.providers.mlx5.mlx5dv_objects — MLX5 DV object wrappers.

Wraps mlx5dv_<obj> C structs (mlx5dv_cq, mlx5dv_qp, etc.) to expose
mlx5 driver-specific attributes for ibv objects via mlx5dv_init_obj().
"""

from typing import Any

from pyverbs.base import PyverbsObject

class Mlx5DvPD(PyverbsObject):
    """MLX5 DV Protection Domain wrapper (mlx5dv_pd).

    Exposes mlx5-specific PD attributes like the PD object number.
    """

    @property
    def pdn(self) -> int:
        """The protection domain object number."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...

class Mlx5DvCQ(PyverbsObject):
    """MLX5 DV Completion Queue wrapper (mlx5dv_cq).

    Exposes mlx5-specific CQ attributes including CQE size, count,
    buffer address, and UAR.
    """

    @property
    def cqe_size(self) -> int:
        """The CQE size in bytes."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...

    @property
    def cqn(self) -> int:
        """The CQ number."""
        ...

    @property
    def buf(self) -> int:
        """The CQ buffer address as an integer."""
        ...

    @property
    def cq_uar(self) -> int:
        """The CQ UAR address as an integer."""
        ...

    @property
    def dbrec(self) -> int:
        """The doorbell record address as an integer."""
        ...

    @property
    def cqe_cnt(self) -> int:
        """The number of CQEs."""
        ...

class Mlx5DvQP(PyverbsObject):
    """MLX5 DV Queue Pair wrapper (mlx5dv_qp).

    Exposes mlx5-specific QP attributes including queue numbers,
    TIR/TIS numbers, and UAR mmap offset.
    """

    @property
    def rqn(self) -> int:
        """The receive queue number of the QP."""
        ...

    @property
    def sqn(self) -> int:
        """The send queue number of the QP."""
        ...

    @property
    def tirn(self) -> int:
        """The transport interface receive object number attached to the RQ."""
        ...

    @property
    def tisn(self) -> int:
        """The transport interface send object number attached to the SQ."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    @property
    def uar_mmap_offset(self) -> int:
        """The UAR mmap offset."""
        ...

class Mlx5DvSRQ(PyverbsObject):
    """MLX5 DV Shared Receive Queue wrapper (mlx5dv_srq).

    Exposes mlx5-specific SRQ attributes including stride, head, tail,
    and SRQ number.
    """

    @property
    def stride(self) -> int:
        """The SRQ stride."""
        ...

    @property
    def head(self) -> int:
        """The SRQ head index."""
        ...

    @property
    def tail(self) -> int:
        """The SRQ tail index."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    @property
    def srqn(self) -> int:
        """The shared receive queue object number."""
        ...

class Mlx5DvObj(PyverbsObject):
    """Container for querying multiple DV objects at once (mlx5dv_obj).

    Retrieves driver-specific attributes from ibv objects using
    mlx5dv_init_obj(). Supports CQ, QP, PD, and SRQ objects.
    The extracted attributes can be accessed via dvcq, dvqp, dvpd, dvsrq.
    """

    def __init__(self, obj_type: int | None = None, **kwargs: Any) -> None:
        """Retrieve DV objects from ibv objects.

        Args:
            obj_type: Bitmask specifying which objects to extract:
                MLX5DV_OBJ_CQ, MLX5DV_OBJ_QP, MLX5DV_OBJ_PD, MLX5DV_OBJ_SRQ.
                None to create an empty container.
            kwargs: Objects to extract from:
                - cq: A CQ object (for MLX5DV_OBJ_CQ).
                - qp: A QP object (for MLX5DV_OBJ_QP).
                - pd: A PD object (for MLX5DV_OBJ_PD).
                - srq: A SRQ object (for MLX5DV_OBJ_SRQ).
                - qp_comp_mask: QP comp_mask override.
                - srq_comp_mask: SRQ comp_mask override.

        Raises:
            PyverbsUserError: If an invalid obj_type is provided or
                no objects are provided.
            PyverbsRDMAError: If initialization fails.
        """
        ...

    def init_obj(self, obj_type: int, **kwargs: Any) -> None:
        """Initialize DV objects.

        Re-initializes if objects are already extracted.

        Args:
            obj_type: Bitmask of object types to extract.
            kwargs: Same as __init__ kwargs.

        Raises:
            PyverbsUserError: If invalid parameters are provided.
            PyverbsRDMAError: If initialization fails.
        """
        ...

    @property
    def dvcq(self) -> Mlx5DvCQ | None:
        """The extracted DV CQ object, or None if not extracted."""
        ...

    @property
    def dvqp(self) -> Mlx5DvQP | None:
        """The extracted DV QP object, or None if not extracted."""
        ...

    @property
    def dvpd(self) -> Mlx5DvPD | None:
        """The extracted DV PD object, or None if not extracted."""
        ...

    @property
    def dvsrq(self) -> Mlx5DvSRQ | None:
        """The extracted DV SRQ object, or None if not extracted."""
        ...
