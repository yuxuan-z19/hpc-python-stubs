"""
Type stubs for pyverbs.providers.mlx5.mlx5dv_mkey — MLX5 Mkey operations.

Provides Mkey (Memory Key) management including indirect mkeys,
signature (T10-DIF/CRC), and error checking.
"""

from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.pd import PD

class Mlx5SigCrc(PyverbsObject):
    """CRC signature configuration (mlx5dv_sig_crc).

    Defines CRC type and seed for block-level CRC signature operations.
    """

    def __init__(self, crc_type: int = 0, seed: int = 0) -> None:
        """Initialize CRC signature configuration.

        Args:
            crc_type: The CRC type to use (e.g. MLX5DV_SIG_CRC_TYPE_CRC32).
                Default is 0.
            seed: A seed for the CRC calculation per block. Default is 0.
        """
        ...

class Mlx5SigT10Dif(PyverbsObject):
    """T10-DIF signature configuration (mlx5dv_sig_t10dif).

    Defines T10-DIF block guard, application tag, and reference tag
    for data integrity operations.
    """

    def __init__(self, bg_type: int = 0, bg: int = 0, app_tag: int = 0, ref_tag: int = 0, flags: int = 0) -> None:
        """Initialize T10-DIF signature configuration.

        Args:
            bg_type: The block guard type (e.g. MLX5DV_SIG_T10DIF_CRC).
                Default is 0.
            bg: A seed for the block guard calculation per block. Default is 0.
            app_tag: An application tag to generate or validate. Default is 0.
            ref_tag: A reference tag to generate or validate. Default is 0.
            flags: Flags for T10-DIF attributes. Default is 0.
        """
        ...

class Mlx5SigBlockDomain(PyverbsObject):
    """Signature block protection domain (mlx5dv_sig_block_domain).

    Defines the signature type and configuration for either the
    memory or wire domain in block signature operations.
    """

    def __init__(
        self,
        sig_type: int = 0,
        dif: Mlx5SigT10Dif | None = None,
        crc: Mlx5SigCrc | None = None,
        block_size: int = 0,
        comp_mask: int = 0,
    ) -> None:
        """Initialize a signature block domain.

        Args:
            sig_type: The signature type for this domain
                (e.g. MLX5DV_SIG_TYPE_T10DIF or MLX5DV_SIG_TYPE_CRC).
                Default is 0 (no signature).
            dif: A Mlx5SigT10Dif object for T10-DIF configuration.
                Mutually exclusive with crc.
            crc: A Mlx5SigCrc object for CRC configuration.
                Mutually exclusive with dif.
            block_size: The block size for this domain. Default is 0.
            comp_mask: Compatibility mask. Default is 0.
        """
        ...

class Mlx5SigBlockAttr(PyverbsObject):
    """Block signature attributes (mlx5dv_sig_block_attr).

    Configures signature operations across memory and wire domains,
    including check, copy, and compatibility masks.
    """

    def __init__(
        self,
        mem: Mlx5SigBlockDomain | None = None,
        wire: Mlx5SigBlockDomain | None = None,
        flags: int = 0,
        check_mask: int = 0,
        copy_mask: int = 0,
        comp_mask: int = 0,
    ) -> None:
        """Initialize block signature attributes.

        Args:
            mem: Mlx5SigBlockDomain for the memory domain signature
                configuration. None if the memory domain has no signature.
            wire: Mlx5SigBlockDomain for the wire domain signature
                configuration. None if the wire domain has no signature.
            flags: Flags for the block signature attributes. Default is 0.
            check_mask: Byte mask — each byte of the input signature is
                checked if the corresponding bit in check_mask is set.
                Default is 0.
            copy_mask: Byte mask — each byte of the signature is copied
                from source domain to destination domain if the
                corresponding bit is set. Default is 0.
            comp_mask: Compatibility mask. Default is 0.
        """
        ...

class Mlx5SigErr(PyverbsObject):
    """Signature error information (mlx5dv_sig_err).

    Contains actual vs. expected values and offset for signature errors.
    """

    def __init__(self, actual_value: int = 0, expected_value: int = 0, offset: int = 0) -> None:
        """Initialize signature error information.

        Args:
            actual_value: The actual value calculated from the transferred data.
            expected_value: The expected value from the signature field.
            offset: The offset within the transfer where the error occurred.
        """
        ...

    @property
    def actual_value(self) -> int:
        """The actual signature value calculated from transferred data."""
        ...

    @property
    def expected_value(self) -> int:
        """The expected signature value from the signature field."""
        ...

    @property
    def offset(self) -> int:
        """The offset within the transfer where the error occurred."""
        ...

class Mlx5MkeyErr(PyverbsObject):
    """Mkey error information (mlx5dv_mkey_err).

    Provides the error type and associated signature error details.
    """

    def __init__(self, sig_err: Mlx5SigErr = ..., err_type: int = ...) -> None:
        """Initialize Mkey error information.

        Args:
            sig_err: A Mlx5SigErr object with signature error details.
            err_type: The type of error (e.g. MLX5DV_MKEY_NO_ERR).
                Default is MLX5DV_MKEY_NO_ERR.
        """
        ...

    @property
    def err_type(self) -> int:
        """The type of Mkey error."""
        ...

    @property
    def sig_err(self) -> Mlx5SigErr:
        """The signature error details."""
        ...

class Mlx5MkeyConfAttr(PyverbsObject):
    """Mkey configuration attributes (mlx5dv_mkey_conf_attr).

    Used with wr_mkey_configure to set Mkey configuration flags.
    """

    def __init__(self, conf_flags: int = 0, comp_mask: int = 0) -> None:
        """Initialize Mkey configuration attributes.

        Args:
            conf_flags: Mkey configuration flags. Default is 0.
            comp_mask: Compatibility mask. Default is 0.
        """
        ...

class Mlx5MrInterleaved(PyverbsObject):
    """Interleaved MR layout for signature operations (mlx5dv_mr_interleaved).

    Describes a memory region layout with interleaved data and
    signature bytes for block signature operations.
    """

    def __init__(self, addr: int, bytes_count: int, bytes_skip: int, lkey: int) -> None:
        """Initialize an interleaved MR layout.

        Args:
            addr: The start address of the memory region.
            bytes_count: Number of bytes from the address that hold real data.
            bytes_skip: Number of bytes to skip after bytes_count
                (e.g. signature bytes).
            lkey: The local key of this memory.
        """
        ...

class Mlx5Mkey(PyverbsCM):
    """MLX5 indirect Memory Key (mlx5dv_mkey).

    An indirect mkey allows configuring advanced memory layouts
    including interleaved data with signatures, crypto operations,
    and more.
    """

    def __init__(self, pd: PD, create_flags: int, max_entries: int) -> None:
        """Create an indirect Mkey.

        Args:
            pd: A PD object for the protection domain.
            create_flags: Mkey creation flags.
            max_entries: Requested maximum number of entries pointed to
                by this indirect mkey. The actual max_entries may be
                adjusted by the device.

        Raises:
            PyverbsRDMAErrno: If mkey creation fails.
        """
        ...

    def mkey_check(self) -> Mlx5MkeyErr:
        """Check the mkey for errors.

        Queries the mkey for any errors and returns the result.

        Returns:
            A Mlx5MkeyErr object containing the error type and details.

        Raises:
            PyverbsRDMAError: If the check operation fails.
        """
        ...

    @property
    def lkey(self) -> int:
        """The local key of this mkey."""
        ...

    @property
    def rkey(self) -> int:
        """The remote key of this mkey."""
        ...

    @property
    def max_entries(self) -> int:
        """The actual maximum number of entries supported by this mkey."""
        ...
