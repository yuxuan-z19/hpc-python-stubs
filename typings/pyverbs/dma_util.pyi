"""
Type stubs for pyverbs.dma_util — DMA memory barrier and MMIO utilities.

Low-level utilities for DMA synchronization and MMIO writes, used by
device drivers for correct ordering of memory operations.
"""

def udma_to_dev_barrier() -> None:
    """User-space DMA write barrier before device reads.

    Ensures all preceding writes are visible to the device before
    subsequent doorbell writes.
    """
    ...

def udma_from_dev_barrier() -> None:
    """User-space DMA read barrier after device writes.

    Ensures all preceding device writes are visible before subsequent
    CPU reads.
    """
    ...

def mmio_write64_as_be(addr: int, val: int) -> None:
    """Write a 64-bit value as big-endian to an MMIO address.

    Args:
        addr: MMIO address (as integer).
        val: 64-bit value to write.
    """
    ...

def mmio_write32_as_be(addr: int, val: int) -> None:
    """Write a 32-bit value as big-endian to an MMIO address.

    Args:
        addr: MMIO address (as integer).
        val: 32-bit value to write.
    """
    ...
