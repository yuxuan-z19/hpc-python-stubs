"""
Type stubs for pyverbs.providers.mlx5.mlx5_vfio — MLX5 VFIO context.

Provides VFIO (Virtual Function I/O) support for direct device access
without kernel RDMA subsystem.
"""

from pyverbs.base import PyverbsObject
from pyverbs.providers.mlx5.mlx5dv import Mlx5Context

class Mlx5VfioAttr(PyverbsObject):
    """MLX5 VFIO context attributes (mlx5dv_vfio_context_attr).

    Holds the PCI device name and attributes for opening a VFIO device.
    """

    def __init__(self, pci_name: str, flags: int = 0, comp_mask: int = 0) -> None:
        """Create VFIO context attributes.

        Args:
            pci_name: PCI device name (e.g. '0000:04:00.0').
            flags: VFIO context attribute flags. Default is 0.
            comp_mask: Compatibility mask. Default is 0.
        """
        ...

    @property
    def flags(self) -> int:
        """VFIO context attribute flags."""
        ...
    @flags.setter
    def flags(self, val: int) -> None: ...
    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    @property
    def pci_name(self) -> bytes:
        """PCI device name as bytes."""
        ...
    @pci_name.setter
    def pci_name(self, val: str) -> None: ...

class Mlx5VfioContext(Mlx5Context):
    """MLX5 VFIO context for direct device access.

    Initializes and opens a context over an mlx5 VFIO device based on
    the provided Mlx5VfioAttr. Allows managing device events and
    performing DevX operations without the kernel RDMA stack.
    """

    def __init__(self, attr: Mlx5VfioAttr) -> None:
        """Open an mlx5 VFIO device context.

        Args:
            attr: Mlx5VfioAttr containing the PCI device name and flags.

        Raises:
            PyverbsRDMAErrno: If getting the VFIO device list or opening
                the device fails.
            PyverbsRDMAError: If no VFIO device is found.
        """
        ...

    def get_events_fd(self) -> int:
        """Get the file descriptor for managing driver events.

        Returns:
            The file descriptor to be used for managing driver events.

        Raises:
            PyverbsRDMAError: If getting the events FD fails.
        """
        ...

    def process_events(self) -> None:
        """Process events on the VFIO device.

        This method should be called from the application thread to
        maintain device events.

        Raises:
            PyverbsRDMAError: If event processing fails.
        """
        ...
