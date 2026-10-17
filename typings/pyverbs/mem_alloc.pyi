"""
Type stubs for pyverbs.mem_alloc — Memory allocation utilities.

Provides Python wrappers for standard C memory allocation functions
(mmap, malloc, free, etc.) and helper functions for reading/writing
data at specific memory addresses.
"""

# -- mmap/mprotect protection flags --
PROT_EXEC_: int
PROT_READ_: int
PROT_WRITE_: int
PROT_NONE_: int

# -- mmap flags --
MAP_PRIVATE_: int
MAP_SHARED_: int
MAP_FIXED_: int
MAP_ANONYMOUS_: int
MAP_STACK_: int
MAP_LOCKED_: int
MAP_HUGETLB_: int
MAP_POPULATE_: int
MAP_NORESERVE_: int
MAP_GROWSDOWN_: int

def mmap(addr: int = 0, length: int = 100, prot: int = ..., flags: int = ..., fd: int = 0, offset: int = 0) -> int:
    """Map file or device into memory via ``mmap(2)``.

    Args:
        addr: Desired mapping address (0 for kernel choice).
        length: Length of the mapping in bytes.
        prot: Memory protection flags (``PROT_READ_``, ``PROT_WRITE_``, etc.).
        flags: Mapping flags (``MAP_PRIVATE_``, ``MAP_SHARED_``, etc.).
        fd: File descriptor to map (-1 for anonymous).
        offset: Offset within the file to map from.

    Returns:
        The starting address of the mapped region as an integer.
    """
    ...

def madvise(addr: int, length: int, flags: int = ...) -> None:
    """Advise the kernel about memory usage patterns via ``madvise(2)``.

    Args:
        addr: Start address of the memory region.
        length: Length of the memory region in bytes.
        flags: Advice flags (e.g. ``MADV_SEQUENTIAL``, ``MADV_HUGEPAGE``).
    """
    ...

def munmap(addr: int, length: int) -> None:
    """Unmap previously mapped memory via ``munmap(2)``.

    Args:
        addr: Starting address of the region to unmap.
        length: Length of the region in bytes.
    """
    ...

def malloc(size: int) -> int:
    """Allocate memory via ``malloc(3)``.

    Args:
        size: Number of bytes to allocate.

    Returns:
        The address of the allocated memory as an integer.
    """
    ...

def posix_memalign(size: int, alignment: int = 8) -> int:
    """Allocate aligned, zeroed memory via ``posix_memalign(3)``.

    Args:
        size: Number of bytes to allocate.
        alignment: Alignment boundary (must be a power of two).

    Returns:
        The address of the allocated memory as an integer.
    """
    ...

def free(ptr: int) -> None:
    """Free previously allocated memory via ``free(3)``.

    Args:
        ptr: Address returned by a previous ``malloc``/``posix_memalign`` call.
    """
    ...

def writebe32(addr: int, val: int, offset: int = 0) -> None:
    """Write a 32-bit value in big-endian byte order.

    Args:
        addr: Target memory address.
        val: 32-bit integer value to write.
        offset: Byte offset from *addr*.
    """
    ...

def writebe64(addr: int, val: int, offset: int = 0) -> None:
    """Write a 64-bit value in big-endian byte order.

    Args:
        addr: Target memory address.
        val: 64-bit integer value to write.
        offset: Byte offset from *addr*.
    """
    ...

def write(addr: int, data: bytes | str, length: int, offset: int = 0) -> None:
    """Write data to a memory address.

    Args:
        addr: Target memory address.
        data: Data to write (bytes or string).
        length: Number of bytes to write.
        offset: Byte offset from *addr*.
    """
    ...

def read32(addr: int, offset: int = 0) -> int:
    """Read a 32-bit value from the given address.

    Args:
        addr: Source memory address.
        offset: Byte offset from *addr*.

    Returns:
        The 32-bit integer value read.
    """
    ...

def read64(addr: int, offset: int = 0) -> int:
    """Read a 64-bit value from the given address.

    Args:
        addr: Source memory address.
        offset: Byte offset from *addr*.

    Returns:
        The 64-bit integer value read.
    """
    ...

def read(addr: int, length: int, offset: int = 0) -> bytes:
    """Read data from a memory address.

    Args:
        addr: Source memory address.
        length: Number of bytes to read.
        offset: Byte offset from *addr*.

    Returns:
        The data read as a ``bytes`` object.
    """
    ...
