"""
Type stubs for pyverbs.dmabuf — DMA-BUF allocation for GPU memory.

Provides DMA-BUF allocation via the DRI device interface for GPU-direct
RDMA memory registration.
"""

class DmaBuf:
    """DMA-BUF object for GPU memory allocation via DRI interface.

    Allocates a DMA-BUF from a GPU device, which can then be registered
    as a DMA-BUF MR for RDMA operations. Usually requires the effective
    user ID to be a member of the 'render' group.
    """

    def __init__(self, size: int, gpu: int = 0, gtt: int = 0) -> None:
        """Allocate a DMA-BUF from a GPU device.

        Args:
            size: Buffer size in bytes.
            gpu: GPU unit to allocate from.
            gtt: If True, allocate from GTT instead of VRAM.

        Raises:
            PyverbsRDMAErrno: If dmabuf_alloc fails.
        """
        ...

    def close(self) -> None:
        """Free the DMA-BUF and release associated resources."""
        ...

    @property
    def drm_fd(self) -> int:
        """DRM file descriptor."""
        ...

    @property
    def handle(self) -> int:
        """DMA-BUF handle."""
        ...

    @property
    def fd(self) -> int:
        """DMA-BUF file descriptor."""
        ...

    @property
    def size(self) -> int:
        """Buffer size in bytes."""
        ...

    @property
    def map_offset(self) -> int:
        """Mapping offset for mmap."""
        ...
