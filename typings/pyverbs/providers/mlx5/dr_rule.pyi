"""
Type stubs for pyverbs.providers.mlx5.dr_rule — MLX5 Direct Rules Rule.
"""

from pyverbs.base import PyverbsCM
from pyverbs.providers.mlx5.dr_action import DrAction
from pyverbs.providers.mlx5.dr_matcher import DrMatcher
from pyverbs.providers.mlx5.mlx5dv_flow import Mlx5FlowMatchParameters

class DrRule(PyverbsCM):
    """MLX5 Direct Rules steering rule (mlx5dv_dr_rule).

    A rule associates a set of match values with a list of actions.
    When a packet matches the rule's criteria, the specified actions
    are performed on it.
    """

    def __init__(
        self, matcher: DrMatcher, value: Mlx5FlowMatchParameters, actions: list[DrAction] | None = None
    ) -> None:
        """Create a DR rule on a matcher.

        Args:
            matcher: A DrMatcher that defines the fields to match on.
            value: A Mlx5FlowMatchParameters with the values to match on.
            actions: Optional list of DrAction objects specifying the
                actions to perform when the rule matches. Default is None
                (no actions).

        Raises:
            PyverbsRDMAErrno: If rule creation fails.
            PyverbsError: If memory allocation for actions fails.
        """
        ...
