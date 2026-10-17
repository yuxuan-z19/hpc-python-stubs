"""
Type stubs for pyverbs.mr — Memory Region (MR) and Memory Window (MW) management.
"""

from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.cmid import CMID
from pyverbs.device import DM, Context
from pyverbs.dmabuf import DmaBuf
from pyverbs.pd import PD

class MR(PyverbsCM):
    """Memory Region (ibv_mr).

    Registers a region of memory for RDMA operations. Buffer allocation is
    done in the constructor; freeing is done in close().

    The creator can be a PD or a CMID object. When a CMID is used, the MR
    is registered via rdma_reg_msgs/write/read according to the access flags.
    """

    def __init__(
        self,
        creator: PD | CMID,
        length: int = 0,
        access: int = 0,
        address: int | None = None,
        implicit: bool = False,
        **kwargs,
    ) -> None:
        """Allocate a buffer and register a Memory Region.

        Args:
            creator: A PD or CMID object.
            length: Length (in bytes) of the MR's buffer.
            access: Access flags (see ibv_access_flags enum).
            address: Optional pre-allocated memory address to register.
            implicit: If True, register an implicit MR (full address space).
            **kwargs: Optional *handle* — a kernel handle to import an existing MR.

        Raises:
            PyverbsRDMAErrno: If registration fails.
        """
        ...

    def unimport(self) -> None:
        """Unimport the MR (calls ibv_unimport_mr then close)."""
        ...

    def write(self, data: bytes | str, length: int, offset: int = 0) -> None:
        """Write user data to the MR's buffer using memcpy.

        Args:
            data: User data to write (strings are auto-encoded to bytes).
            length: Number of bytes to write.
            offset: Write offset within the MR buffer.

        Raises:
            PyverbsUserError: If the MR buffer is unallocated or length is invalid.
        """
        ...

    def read(self, length: int, offset: int = 0) -> bytes:
        """Read data from the MR's buffer.

        Args:
            length: Number of bytes to read.
            offset: Read offset within the MR buffer.

        Returns:
            The data at the requested offset as bytes.

        Raises:
            PyverbsUserError: If the MR buffer is unallocated or length is invalid.
        """
        ...

    def rereg(self, flags: int, pd: PD | None = None, addr: int = 0, length: int = 0, access: int = 0) -> None:
        """Modify the attributes of an existing memory region.

        Args:
            flags: Bit-mask indicating which properties to modify
                (see ibv_rereg_mr_flags).
            pd: New PD (if changing PD).
            addr: New buffer address.
            length: New length.
            access: New access flags.

        Raises:
            PyverbsRDMAErrno: If ibv_rereg_mr fails.
        """
        ...

    @property
    def buf(self) -> int:
        """Pointer to the MR buffer as an integer."""
        ...

    @property
    def lkey(self) -> int:
        """Local access key (lkey)."""
        ...

    @property
    def rkey(self) -> int:
        """Remote access key (rkey)."""
        ...

    @property
    def length(self) -> int:
        """Length of the MR in bytes."""
        ...

    @property
    def handle(self) -> int:
        """MR handle."""
        ...

    def __str__(self) -> str: ...

class MWBindInfo(PyverbsCM):
    """Information for binding a Memory Window (ibv_mw_bind_info).

    Contains the MR, address, length, and access flags for an MW bind
    operation.
    """

    def __init__(self, mr: MR, addr: int, length: int, mw_access_flags: int) -> None:
        """Initialize MW bind info.

        Args:
            mr: The MR to bind.
            addr: Start address within the MR.
            length: Length of the binding.
            mw_access_flags: Access flags for the MW.
        """
        ...

    @property
    def mw_access_flags(self) -> int:
        """MW access flags."""
        ...

    @property
    def length(self) -> int:
        """Binding length."""
        ...

    @property
    def addr(self) -> int:
        """Binding start address."""
        ...

    def __str__(self) -> str: ...

class MWBind(PyverbsCM):
    """Bind operation parameters for a Memory Window (ibv_mw_bind).

    Combines MWBindInfo with WR-level parameters (wr_id, send_flags).
    """

    def __init__(self, info: MWBindInfo, send_flags: int, wr_id: int = 0) -> None:
        """Initialize MW bind parameters.

        Args:
            info: MWBindInfo with MR, address, and access info.
            send_flags: Send flags for the bind WR.
            wr_id: Work request ID.
        """
        ...

    def __str__(self) -> str: ...

class MW(PyverbsCM):
    """Memory Window (ibv_mw).

    Memory Windows provide a mechanism for registering regions of memory
    that can be accessed remotely with enhanced security.
    """

    def __init__(self, pd: PD, mw_type: int) -> None:
        """Allocate a Memory Window of the given type.

        Args:
            pd: A PD object.
            mw_type: MW type (IBV_MW_TYPE_1 or IBV_MW_TYPE_2).

        Raises:
            PyverbsRDMAErrno: If ibv_alloc_mw fails.
        """
        ...

    @property
    def handle(self) -> int:
        """MW handle."""
        ...

    @property
    def rkey(self) -> int:
        """MW remote key."""
        ...

    @property
    def type(self) -> int:
        """MW type (IBV_MW_TYPE_1 or IBV_MW_TYPE_2)."""
        ...

    def __str__(self) -> str: ...

class DMMR(MR):
    """Device Memory Memory Region.

    Registers device memory (DM) as an MR using ibv_reg_dm_mr.
    """

    def __init__(self, pd: PD, length: int, access: int, dm: DM, offset: int) -> None:
        """Register device memory as an MR.

        Args:
            pd: A PD object.
            length: Length in bytes.
            access: Access flags (see ibv_access_flags).
            dm: A DM (device memory) object.
            offset: Byte offset from the beginning of the DM buffer.

        Raises:
            PyverbsRDMAErrno: If ibv_reg_dm_mr fails.
        """
        ...

    def write(self, data: bytes | str, length: int, offset: int = 0) -> None:
        """Write data to device memory via DM copy.

        Args:
            data: User data to write.
            length: Number of bytes.
            offset: Offset within the DM buffer.
        """
        ...

    def read(self, length: int, offset: int = 0) -> bytes:
        """Read data from device memory via DM copy.

        Args:
            length: Number of bytes to read.
            offset: Offset within the DM buffer.

        Returns:
            Data read from device memory.
        """
        ...

class DmaBufMR(MR):
    """DMA-BUF Memory Region.

    Registers a DMA-BUF file descriptor as an MR using ibv_reg_dmabuf_mr.
    """

    def __init__(
        self,
        pd: PD,
        length: int,
        access: int,
        dmabuf: DmaBuf | None = None,
        offset: int = 0,
        gpu: int = 0,
        gtt: int = 0,
    ) -> None:
        """Register a DMA-BUF as an MR.

        Args:
            pd: A PD object.
            length: Length in bytes.
            access: Access flags (see ibv_access_flags).
            dmabuf: A DmaBuf object or FD. A DmaBuf is allocated if None.
            offset: Byte offset from the beginning of the dma-buf.
            gpu: GPU unit for internal dmabuf allocation.
            gtt: If True, allocate from GTT instead of VRAM.

        Raises:
            PyverbsRDMAErrno: If ibv_reg_dmabuf_mr fails.
        """
        ...

    def write(self, data: bytes | str, length: int, offset: int = 0) -> None:
        """Write user data to the dma-buf backing the MR.

        Args:
            data: User data to write.
            length: Number of bytes.
            offset: Write offset.
        """
        ...

    def read(self, length: int, offset: int = 0) -> bytes:
        """Read data from the dma-buf backing the MR.

        Args:
            length: Number of bytes to read.
            offset: Read offset.

        Returns:
            Data read from the dma-buf.
        """
        ...

    @property
    def offset(self) -> int:
        """DMA-BUF offset."""
        ...

    @property
    def dmabuf(self) -> DmaBuf | None:
        """The underlying DmaBuf object."""
        ...

class DmaHandleInitAttr(PyverbsObject):
    """DMA handle initialization attributes (ibv_dma_handle_init_attr)."""

    def __init__(self, comp_mask: int = 0, cpu_id: int = 0, ph: int = 0, tph_mem_type: int = 0) -> None:
        """Initialize DMA handle attributes.

        Args:
            comp_mask: Bitmask of initialization attributes.
            cpu_id: CPU identifier for DMA operations.
            ph: Processing hints for DMA operations.
            tph_mem_type: Type of target memory.
        """
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, value: int) -> None: ...
    @property
    def cpu_id(self) -> int:
        """CPU identifier."""
        ...
    @cpu_id.setter
    def cpu_id(self, value: int) -> None: ...
    @property
    def ph(self) -> int:
        """Processing hints."""
        ...
    @ph.setter
    def ph(self, value: int) -> None: ...
    @property
    def tph_mem_type(self) -> int:
        """Target memory type."""
        ...
    @tph_mem_type.setter
    def tph_mem_type(self, value: int) -> None: ...
    def __str__(self) -> str: ...

class DMAHandle(PyverbsCM):
    """DMA handle for MR registration with DMA-BUF (ibv_dma_handle).

    Created via ibv_alloc_dmah and used when registering MREx with
    DMA-BUF support.
    """

    def __init__(self, ctx: Context, init_attr: DmaHandleInitAttr) -> None:
        """Allocate a DMA handle.

        Args:
            ctx: A Context object.
            init_attr: DMA handle initialization attributes.

        Raises:
            PyverbsRDMAErrno: If ibv_alloc_dmah fails.
        """
        ...

class MREx(MR):
    """Extended Memory Region (ibv_reg_mr_ex).

    Provides extended MR registration with additional attributes such as
    IOVA, dma-buf FD, DMA handle, and Buf-backed registration.
    """

    def __init__(
        self,
        pd: PD,
        length: int = 0,
        access: int = 0,
        address: int | None = None,
        iova: int | None = None,
        fd: int | None = None,
        fd_offset: int = 0,
        dmah: DMAHandle | None = None,
        implicit: bool = False,
        buf: Buf | None = None,
        **kwargs,
    ) -> None:
        """Register a memory region using the extended API ibv_reg_mr_ex.

        Args:
            pd: A PD object.
            length: Length (in bytes) of the MR's buffer.
            access: Access flags (see ibv_access_flags).
            address: Memory address to register (optional).
            iova: IOVA address to register (optional).
            fd: File descriptor for dma-buf registration (optional).
            fd_offset: Offset in the dma-buf.
            dmah: DMA handle for registration (optional).
            implicit: If True, register an implicit MR.
            buf: A Buf object to register the MR on (optional).

        Raises:
            PyverbsRDMAErrno: If ibv_reg_mr_ex fails.
        """
        ...

    def __str__(self) -> str: ...

class Buf(PyverbsCM):
    """Provider-allocated buffer (ibv_buf).

    Represents a buffer allocated through a PD via ibv_alloc_buf. The device
    provider selects the backing memory for the given PD.
    """

    def __init__(self, pd: PD, size: int) -> None:
        """Allocate a buffer from the provider associated with the PD.

        Args:
            pd: A PD or ParentDomain object.
            size: Size (in bytes) of the buffer.

        Raises:
            PyverbsRDMAErrno: If ibv_alloc_buf fails.
        """
        ...

    def export_dmabuf_fd(self) -> int:
        """Export a dmabuf FD for this Buf object.

        Returns:
            A file descriptor (int) for the dmabuf.

        Raises:
            PyverbsRDMAErrno: If ibv_export_buf_dmabuf_fd fails.
        """
        ...

    @property
    def addr(self) -> int:
        """Buffer address as an integer."""
        ...

    @property
    def size(self) -> int:
        """Buffer size in bytes."""
        ...

    def __str__(self) -> str: ...

class BufMR(MR):
    """Memory Region registered for a Buf via ibv_reg_buf_mr.

    Unlike MR, the backing memory is owned by the Buf, so closing a BufMR
    only deregisters the MR and never frees the buffer.
    """

    def __init__(self, pd: PD, buf: Buf, length: int = 0, access: int = 0, offset: int = 0) -> None:
        """Register a memory region for (a subrange of) the given Buf.

        Args:
            pd: The same PD/ParentDomain used to allocate the Buf.
            buf: A Buf object allocated with ibv_alloc_buf.
            length: Length (in bytes) to register.
            access: Access flags (see ibv_access_flags).
            offset: Byte offset within the Buf.

        Raises:
            PyverbsRDMAErrno: If ibv_reg_buf_mr fails.
        """
        ...

def mwtype2str(mw_type: int) -> str:
    """Convert memory window type enum to string.

    Args:
        mw_type: MW type (1 or 2).

    Returns:
        String like ``'IBV_MW_TYPE_1'`` or ``'IBV_MW_TYPE_2'``.
    """
    ...
