"""
Type stubs for pyverbs.fork — RDMA fork support.

Provides functions to enable RDMA memory registration to survive fork()
calls, which is needed when using fork-based process models with RDMA.
"""

def fork_init() -> None:
    """Initialize fork support (calls ibv_fork_init).

    Must be called before any MR registration if the process will fork.

    Raises:
        PyverbsRDMAError: If ibv_fork_init fails.
    """
    ...

def is_fork_initialized() -> bool:
    """Check if fork support has been initialized.

    Returns:
        True if ibv_fork_init has been called successfully.
    """
    ...
