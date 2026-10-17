"""
Type stubs for pyverbs.providers.mlx5.dr_domain — MLX5 Direct Rules Domain.
"""

from pyverbs.base import PyverbsCM
from pyverbs.device import Context

class DrDomain(PyverbsCM):
    """MLX5 Direct Rules steering domain (mlx5dv_dr_domain).

    A steering domain is the top-level object in the DR hierarchy.
    It encapsulates the steering logic for a specific device context
    and contains tables, matchers, rules, and actions.
    """

    def __init__(self, context: Context, domain_type: int) -> None:
        """Create a DR domain over an mlx5 device context.

        Args:
            context: A Mlx5Context object representing the opened device.
            domain_type: Type of the domain, one of MLX5DV_DR_DOMAIN_*
                (e.g. MLX5DV_DR_DOMAIN_NIC_RX, MLX5DV_DR_DOMAIN_NIC_TX,
                MLX5DV_DR_DOMAIN_FDB).

        Raises:
            PyverbsRDMAErrno: If domain creation fails.
        """
        ...

    def allow_duplicate_rules(self, allow: bool) -> None:
        """Enable or disable duplicate rule insertion detection.

        By default, duplicate rule insertion is allowed. When disabled,
        attempting to insert a rule that already exists will fail.

        Args:
            allow: True to allow duplicate rules, False to prevent them.
        """
        ...

    def sync(self, flags: int = ...) -> None:
        """Flush the rule submission queue and synchronize the domain.

        Sync is used to ensure all queued rules are applied. It can flush
        software queued tasks, clear hardware steering cache, and/or
        sync device memory to free cached memory.

        Args:
            flags: Combination of MLX5DV_DR_DOMAIN_SYNC_FLAGS_*:
                - MLX5DV_DR_DOMAIN_SYNC_FLAGS_SW: Block until all SW tasks complete.
                - MLX5DV_DR_DOMAIN_SYNC_FLAGS_HW: Clear HW steering cache.
                - MLX5DV_DR_DOMAIN_SYNC_FLAGS_MEM: Sync device memory to free cache.
                Default is SW | HW.

        Raises:
            PyverbsRDMAErrno: If the sync operation fails.
        """
        ...

    def dump(self, filepath: str) -> None:
        """Dump debug information of the domain into a file.

        Args:
            filepath: Path to the output file for domain debug dump.

        Raises:
            PyverbsError: If opening the dump file fails.
            PyverbsRDMAError: If the dump operation itself fails.
        """
        ...
