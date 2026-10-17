"""
Type stubs for pyverbs.providers.mlx5.dr_matcher — MLX5 Direct Rules Matcher.
"""

from pyverbs.base import PyverbsCM
from pyverbs.providers.mlx5.dr_table import DrTable
from pyverbs.providers.mlx5.mlx5dv_flow import Mlx5FlowMatchParameters

class DrMatcher(PyverbsCM):
    """MLX5 Direct Rules matcher (mlx5dv_dr_matcher).

    A matcher defines the criteria for matching packets within a table.
    It specifies which header fields to match on and creates rules
    that associate matched packets with actions.
    """

    def __init__(
        self, table: DrTable, priority: int, match_criteria_enable: int, mask: Mlx5FlowMatchParameters
    ) -> None:
        """Create a DR matcher within a table.

        Args:
            table: A DrTable object to create the matcher on.
            priority: Matcher priority within the table. Lower values
                are matched first.
            match_criteria_enable: Bitmask indicating which header/parameter
                groups are used for matching:
                - Bit 0: outer_headers
                - Bit 1: misc_parameters
                - Bit 2: inner_headers
                - Bit 3: misc_parameters_2
                - Bit 4: misc_parameters_3
                - Bit 5: misc_parameters_4
            mask: A Mlx5FlowMatchParameters object defining the match mask.

        Raises:
            PyverbsRDMAErrno: If matcher creation fails.
        """
        ...

    def set_layout(self, log_num_of_rules: int = 0, flags: int = ...) -> None:
        """Set the matcher layout for optimized rule insertion.

        Provides a hint to the driver about the expected number of rules
        and matcher layout flags for optimization.

        Args:
            log_num_of_rules: Log2 of the expected number of rules.
                Relevant when MLX5DV_DR_MATCHER_LAYOUT_NUM_RULE flag is set.
            flags: Matcher layout flags (e.g. MLX5DV_DR_MATCHER_LAYOUT_NUM_RULE).
                Default is MLX5DV_DR_MATCHER_LAYOUT_NUM_RULE.

        Raises:
            PyverbsRDMAError: If setting the layout fails.
        """
        ...
