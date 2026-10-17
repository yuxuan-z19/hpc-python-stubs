"""
Type stubs for pyverbs.providers.mlx5.dr_table — MLX5 Direct Rules Table.
"""

from pyverbs.base import PyverbsCM
from pyverbs.providers.mlx5.dr_domain import DrDomain

class DrTable(PyverbsCM):
    """MLX5 Direct Rules steering table (mlx5dv_dr_table).

    A table resides within a domain and contains matchers. Each table
    has a level that determines its position in the steering pipeline.
    """

    def __init__(self, domain: DrDomain, level: int) -> None:
        """Create a DR table within a domain.

        Args:
            domain: A DrDomain object where this table will be created.
            level: Table level in the steering pipeline. Lower levels
                are processed first.

        Raises:
            PyverbsRDMAErrno: If table creation fails.
        """
        ...
