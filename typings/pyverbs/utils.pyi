"""
Type stubs for pyverbs.utils — GID/QP/utility conversion functions.
"""

def be64toh(num: int) -> int:
    """Convert a 64-bit value from big-endian to host byte order.

    Args:
        num: 64-bit big-endian integer.

    Returns:
        The value in host byte order.
    """
    ...

def gid_str(subnet_prefix: int, interface_id: int) -> str:
    """Convert a GID (subnet_prefix + interface_id) to its string representation.

    Args:
        subnet_prefix: 64-bit subnet prefix.
        interface_id: 64-bit interface ID.

    Returns:
        GID in 'xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx' format.
    """
    ...

def gid_str_to_array(val: str) -> list[str]:
    """Split a GID string into an array of hex byte strings.

    Args:
        val: GID in 'xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx' format.

    Returns:
        List of 16 two-character hex strings (e.g. ['fe', '80', ...]).

    Raises:
        PyverbsUserError: If the GID format is invalid.
    """
    ...

def qp_type_to_str(qp_type: int) -> str:
    """Convert QP type enum value to a human-readable string.

    Args:
        qp_type: QP type (e.g. IBV_QPT_RC).

    Returns:
        String like 'RC', 'UC', 'UD', etc.
    """
    ...

def qp_state_to_str(qp_state: int) -> str:
    """Convert QP state enum value to a human-readable string.

    Args:
        qp_state: QP state (e.g. IBV_QPS_INIT).

    Returns:
        String like 'Reset', 'Init', 'RTR', 'RTS', etc.
    """
    ...

def mtu_to_str(mtu: int) -> int:
    """Convert MTU enum value to its byte size.

    Args:
        mtu: MTU enum (1=256, 2=512, 3=1024, 4=2048, 5=4096).

    Returns:
        MTU size in bytes, or 0 if unknown.
    """
    ...

def access_flags_to_str(flags: int) -> str:
    """Convert MR access flags to a human-readable string.

    Args:
        flags: MR access flags (OR of ibv_access_flags).

    Returns:
        Space-separated string of flag names.
    """
    ...

def mig_state_to_str(mig: int) -> str:
    """Convert path migration state to a human-readable string.

    Args:
        mig: Migration state enum value.

    Returns:
        String like 'Migrated', 'Re-arm', 'Armed'.
    """
    ...

def rereg_error_to_str(error: int) -> str:
    """Convert MR re-registration error code to a human-readable string.

    Args:
        error: Error code from ibv_rereg_mr.

    Returns:
        String like 'IBV_REREG_MR_ERR_INPUT', etc.
    """
    ...
