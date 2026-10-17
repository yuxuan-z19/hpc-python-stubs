"""
Type stubs for pyverbs.providers.mlx5.mlx5dv_crypto — MLX5 crypto operations.

Provides Data Encryption Key (DEK) management, crypto login sessions,
and crypto attributes for QP configuration.
"""

from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.device import Context
from pyverbs.pd import PD

class Mlx5CryptoLoginAttr(PyverbsObject):
    """Crypto login attributes (mlx5dv_crypto_login_attr).

    Used for creating a crypto login session with the legacy API.
    Contains credential, credential ID, and import KEK ID.
    """

    def __init__(self, credential: bytes, credential_id: int = 0, import_kek_id: int = 0) -> None:
        """Initialize crypto login attributes.

        Args:
            credential: The credential to login with (48 bytes). Must be
                wrapped by the AES key wrap algorithm using the import KEK
                indicated by import_kek_id.
            credential_id: The index of the credential stored on the device.
                Default is 0.
            import_kek_id: The index of the import KEK stored on the device.
                Default is 0.
        """
        ...

    @property
    def credential_id(self) -> int:
        """The credential index stored on the device."""
        ...

    @property
    def import_kek_id(self) -> int:
        """The import KEK index stored on the device."""
        ...

    @property
    def credential(self) -> bytes:
        """The credential bytes."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...

    def __str__(self) -> str: ...

class Mlx5CryptoExtLoginAttr(PyverbsObject):
    """Extended crypto login attributes (mlx5dv_crypto_login_attr_ex).

    Used with Mlx5CryptoLogin for creating crypto login objects with
    variable-length credentials.
    """

    def __init__(self, credential: bytes, credential_len: int, credential_id: int = 0, import_kek_id: int = 0) -> None:
        """Initialize extended crypto login attributes.

        Args:
            credential: The credential to login with.
            credential_len: The credential length in bytes. Must be provided.
            credential_id: The index of the credential stored on the device.
                Default is 0.
            import_kek_id: The index of the import KEK stored on the device.
                Default is 0.
        """
        ...

    @property
    def credential_id(self) -> int:
        """The credential index stored on the device."""
        ...

    @property
    def import_kek_id(self) -> int:
        """The import KEK index stored on the device."""
        ...

    @property
    def credential(self) -> bytes:
        """The credential bytes."""
        ...

    @property
    def credential_len(self) -> int:
        """The credential length."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...

    def __str__(self) -> str: ...

class Mlx5DEKInitAttr(PyverbsObject):
    """Data Encryption Key initialization attributes (mlx5dv_dek_init_attr).

    Defines all parameters needed to create a DEK including key size,
    purpose, and the encrypted key itself.
    """

    def __init__(
        self,
        pd: PD,
        key_size: int,
        has_keytag: bool = False,
        key_purpose: int = 0,
        opaque: bytes = b"",
        key: bytes = b"",
        comp_mask: int = 0,
        crypto_login: Mlx5CryptoLogin | None = None,
    ) -> None:
        """Initialize DEK creation attributes.

        Args:
            pd: The protection domain to associate with the DEK.
            key_size: Size of the key (e.g. MLX5DV_CRYPTO_KEY_SIZE_128/256).
            has_keytag: Whether the DEK has a keytag. If True, the key
                should include an 8-byte keytag. Default is False.
            key_purpose: The crypto purpose of the key. Default is 0.
            opaque: Plaintext metadata to describe the key (8 bytes).
                Default is empty.
            key: The key itself, wrapped by the crypto login session's
                import KEK (up to 128 bytes). Default is empty.
            comp_mask: Reserved for future extension. Default is 0.
            crypto_login: A Mlx5CryptoLogin object. Default is None.
        """
        ...

    @property
    def key_size(self) -> int:
        """The size of the key."""
        ...

    @property
    def has_keytag(self) -> bool:
        """Whether the DEK has a keytag."""
        ...

    @property
    def key_purpose(self) -> int:
        """The crypto purpose of the key."""
        ...

    @property
    def opaque(self) -> str:
        """Plaintext metadata describing the key."""
        ...

    @property
    def key(self) -> str:
        """The key in hex format."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...

    def __str__(self) -> str: ...

class Mlx5DEKAttr(PyverbsObject):
    """Data Encryption Key attributes (mlx5dv_dek_attr).

    Contains the DEK state and opaque metadata returned by DEK query.
    """

    @property
    def state(self) -> int:
        """The current state of the DEK."""
        ...

    @property
    def opaque(self) -> bytes:
        """The opaque metadata of the DEK."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...

class Mlx5CryptoAttr(PyverbsObject):
    """Crypto attributes for QP configuration (mlx5dv_crypto_attr).

    Defines encryption standard, direction, data unit size, tweak,
    and DEK for crypto operations on a QP.
    """

    def __init__(
        self,
        crypto_standard: int = 0,
        encrypt_on_tx: bool = False,
        signature_crypto_order: int = 0,
        data_unit_size: int = 0,
        initial_tweak: bytes = b"",
        dek: Mlx5DEK | None = None,
        keytag: bytes = b"",
        comp_mask: int = 0,
    ) -> None:
        """Initialize crypto attributes.

        Args:
            crypto_standard: The encryption standard to use. Default is 0.
            encrypt_on_tx: If True, memory data is encrypted during TX
                and wire data is decrypted during RX. Default is False.
            signature_crypto_order: Controls the order between crypto and
                signature operations. Relevant only if signature is configured.
                Default is 0.
            data_unit_size: The tweak is incremented after each data_unit_size
                during encryption. Default is 0.
            initial_tweak: A value used during encryption of each data unit
                (16 bytes). The device increments this for every data unit.
                Default is empty.
            dek: The Mlx5DEK to use for crypto operations. Default is None.
            keytag: A tag that verifies the correct DEK is being used
                (8 bytes). Default is empty.
            comp_mask: Reserved for future extension. Default is 0.
        """
        ...

    @property
    def crypto_standard(self) -> int:
        """The encryption standard."""
        ...

    @property
    def encrypt_on_tx(self) -> bool:
        """Whether encryption happens on TX direction."""
        ...

    @property
    def signature_crypto_order(self) -> int:
        """The order between crypto and signature operations."""
        ...

    @property
    def data_unit_size(self) -> int:
        """The data unit size for tweak increment."""
        ...

    @property
    def initial_tweak(self) -> str:
        """The initial tweak value in hex format."""
        ...

    @property
    def keytag(self) -> str:
        """The keytag in hex format."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...

    def __str__(self) -> str: ...

class Mlx5DEK(PyverbsCM):
    """Data Encryption Key object (mlx5dv_dek).

    Represents a DEK used for crypto operations on QPs.
    """

    def __init__(self, ctx: Context, dek_init_attr: Mlx5DEKInitAttr) -> None:
        """Create a DEK.

        Args:
            ctx: A Context to create the DEK on.
            dek_init_attr: A Mlx5DEKInitAttr containing the DEK attributes.

        Raises:
            PyverbsRDMAErrno: If DEK creation fails.
        """
        ...

    def query(self) -> Mlx5DEKAttr:
        """Query the DEK state and attributes.

        Returns:
            A Mlx5DEKAttr containing the DEK state and opaque metadata.

        Raises:
            PyverbsRDMAError: If the query fails.
        """
        ...

class Mlx5CryptoLogin(PyverbsCM):
    """Crypto login session object (mlx5dv_crypto_login_obj).

    Represents a crypto login session for secured communications
    with the device.
    """

    def __init__(self, context: Context, crypto_attr: Mlx5CryptoExtLoginAttr) -> None:
        """Create a crypto login session.

        Args:
            context: A Context to create the login session on.
            crypto_attr: A Mlx5CryptoExtLoginAttr containing the credential.

        Raises:
            PyverbsRDMAErrno: If login session creation fails.
        """
        ...

    def query(self) -> int:
        """Query the state of the current crypto login session.

        Returns:
            The login state as an integer.
        """
        ...
