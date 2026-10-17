"""
Type stubs for pyverbs.pd — Protection Domain (PD) management.
"""

from typing import Any, Callable

from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.cmid import CMID
from pyverbs.device import Context
from pyverbs.wr import SGE

class PD(PyverbsCM):
    """Protection Domain (ibv_pd).

    A PD groups memory regions, QPs, and other resources to ensure that
    only QPs within the same PD can access the corresponding memory regions.
    """

    def __init__(self, creator: Context | CMID, **kwargs: Any) -> None:
        """Create a Protection Domain.

        Args:
            creator: A Context or CMID object that will own this PD.
            **kwargs: Optional *handle* — a kernel handle to import an existing PD.

        Raises:
            PyverbsRDMAErrno: If ibv_alloc_pd or ibv_import_pd fails.
            PyverbsUserError: If creator type is unsupported.
        """
        ...

    def advise_mr(self, advise: int, flags: int, sg_list: list[SGE]) -> int:
        """Give advice or directions to the kernel about an address range
        belonging to a MR.

        Args:
            advise: The requested advise value.
            flags: Describes the properties of the advise operation.
            sg_list: The scatter-gather list.

        Returns:
            0 on success.

        Raises:
            PyverbsRDMAError: If ibv_advise_mr fails.
        """
        ...

    def unimport(self) -> None:
        """Unimport the PD (calls ibv_unimport_pd then close)."""
        ...

    @property
    def handle(self) -> int:
        """PD handle."""
        ...

    @property
    def pd(self) -> int:
        """Underlying ibv_pd pointer as integer."""
        ...

class ParentDomainContext(PyverbsObject):
    """Context for parent domain alloc/free callbacks.

    Holds the Python alloc and free functions that are called by the
    parent domain allocator when custom memory allocation is needed.
    """

    def __init__(
        self,
        pd: PD,
        alloc_func: Callable[[PD, object, int, int, int], int],
        free_func: Callable[[PD, object, int, int], None],
        user_data: Any = None,
    ) -> None:
        """Initialize the parent domain context.

        Args:
            pd: PD that represents the ibv_pd passed to Parent Domain creation.
            alloc_func: Python alloc function signature:
                (pd, context, size, alignment, resource_type) -> int
            free_func: Python free function signature:
                (pd, context, ptr, resource_type) -> None
            user_data: Additional user-specific data.
        """
        ...

    @property
    def user_data(self) -> Any:
        """Additional user-specific data."""
        ...
    @user_data.setter
    def user_data(self, val: Any) -> None: ...

class ParentDomainInitAttr(PyverbsObject):
    """Initialization attributes for a Parent Domain
    (ibv_parent_domain_init_attr).
    """

    def __init__(self, pd: PD, pd_context: ParentDomainContext | None = None, comp_mask: int = 0) -> None:
        """Initialize parent domain creation attributes.

        Args:
            pd: PD to initialize the ParentDomain with.
            pd_context: ParentDomainContext with alloc/free Python callbacks.
            comp_mask: Bit-mask of optional fields. The ALLOCATORS and
                PD_CONTEXT bits are set automatically when pd_context is given.

        Raises:
            PyverbsUserError: If comp_mask has PD_CONTEXT bits but no pd_context.
        """
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...

class ParentDomain(PD):
    """Parent Domain — an extended PD with custom allocators.

    A Parent Domain allows custom memory allocation for CQs and other
    resources via user-defined alloc/free callbacks.
    """

    def __init__(self, context: Context, attr: ParentDomainInitAttr) -> None:
        """Allocate a Parent Domain.

        Args:
            context: Device Context.
            attr: Attributes to initialize the ParentDomain with.

        Raises:
            PyverbsRDMAErrno: If ibv_alloc_parent_domain fails.
        """
        ...
