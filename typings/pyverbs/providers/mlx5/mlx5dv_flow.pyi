"""
Type stubs for pyverbs.providers.mlx5.mlx5dv_flow — MLX5 flow matching and steering.

Provides flow match parameters, matcher attributes, flow matchers,
flow actions (reformat, modify), and MLX5 flow creation.
"""

from typing import Any

from pyverbs.base import PyverbsObject
from pyverbs.device import Context
from pyverbs.flow import Flow, FlowAction
from pyverbs.providers.mlx5.mlx5dv import Mlx5DevxObj
from pyverbs.qp import QP

class Mlx5FlowMatchParameters(PyverbsObject):
    """Flow match parameters (mlx5dv_flow_match_parameters).

    Defines the match mask or values for flow steering using
    PRM Flow Table Entry Match Parameters Format.
    """

    def __init__(self, size: int, values: bytes | list[int] | Any) -> None:
        """Initialize flow match parameters.

        Args:
            size: Length of the mask/value in bytes.
            values: Bytes or bytes-like object with mask/value in PRM
                Flow Table Entry Match Parameters Format, or an instance
                of FlowTableEntryMatchParam.

        Raises:
            PyverbsError: If memory allocation fails.
        """
        ...

    def close(self) -> None:
        """Release the underlying C structure."""
        ...

class Mlx5FlowMatcherAttr(PyverbsObject):
    """Flow matcher attributes (mlx5dv_flow_matcher_attr).

    Defines matcher type, flags, priority, match criteria, and
    flow table type for hardware steering.
    """

    def __init__(
        self,
        match_mask: Mlx5FlowMatchParameters,
        attr_type: int = ...,
        flags: int = 0,
        priority: int = 0,
        match_criteria_enable: int = 0,
        comp_mask: int = 0,
        ft_type: int = 0,
        ib_port: int = 0,
    ) -> None:
        """Initialize flow matcher attributes.

        Args:
            match_mask: A Mlx5FlowMatchParameters defining the match mask.
            attr_type: Type of matcher (e.g. IBV_FLOW_ATTR_NORMAL).
                Default is IBV_FLOW_ATTR_NORMAL.
            flags: Special flags to control the matcher:
                - 0 or None: Ingress flow rules.
                - IBV_FLOW_ATTR_FLAGS_EGRESS: Egress flow rules.
                Default is 0.
            priority: Matcher priority. Default is 0.
            match_criteria_enable: Bitmask of header/parameter groups used:
                - Bit 0: outer_headers
                - Bit 1: misc_parameters
                - Bit 2: inner_headers
                - Bit 3: misc_parameters_2
                - Bit 4: misc_parameters_3
                - Bit 5: misc_parameters_4
                Default is 0.
            comp_mask: MLX5DV_FLOW_MATCHER_MASK_FT_TYPE for ft_type,
                MLX5DV_FLOW_MATCHER_MASK_IB_PORT for ib_port. Default is 0.
            ft_type: Flow table type for the matcher:
                - MLX5DV_FLOW_TABLE_TYPE_NIC_RX: Ingress rules.
                - MLX5DV_FLOW_TABLE_TYPE_NIC_TX: Egress rules.
                - MLX5DV_FLOW_TABLE_TYPE_FDB: FDB rules.
                - MLX5DV_FLOW_TABLE_TYPE_RDMA_RX: Ingress RDMA rules.
                - MLX5DV_FLOW_TABLE_TYPE_RDMA_TX: Egress RDMA rules.
                Default is 0.
            ib_port: Specifies which vport to attach the matcher to.
                Default is 0.
        """
        ...

class Mlx5FlowMatcher(PyverbsObject):
    """MLX5 flow matcher (mlx5dv_flow_matcher) for hardware steering.

    Creates a flow matcher that defines matching criteria for steering
    flow rules.
    """

    def __init__(self, context: Context, attr: Mlx5FlowMatcherAttr) -> None:
        """Create a flow matcher.

        Args:
            context: A Context object.
            attr: A Mlx5FlowMatcherAttr defining the matcher attributes.

        Raises:
            PyverbsRDMAErrno: If matcher creation fails.
        """
        ...

    def close(self) -> None:
        """Destroy the flow matcher."""
        ...

class Mlx5FlowActionAttr(PyverbsObject):
    """Flow action attribute (mlx5dv_flow_action_attr) for MLX5 flow creation.

    Defines a single action for flow creation, supporting QP destination,
    flow action, DevX object, and counter actions.
    """

    def __init__(
        self,
        action_type: int | None = None,
        qp: QP | None = None,
        flow_action: FlowAction | None = None,
        obj: Mlx5DevxObj | None = None,
        offset: int = 0,
    ) -> None:
        """Initialize a flow action attribute.

        Args:
            action_type: Type of the action, one of:
                - MLX5DV_FLOW_ACTION_DEST_IBV_QP: Destination QP.
                - MLX5DV_FLOW_ACTION_IBV_FLOW_ACTION: Flow action.
                - MLX5DV_FLOW_ACTION_DEST_DEVX: DevX destination.
                - MLX5DV_FLOW_ACTION_COUNTERS_DEVX: DevX counter.
                - MLX5DV_FLOW_ACTION_COUNTERS_DEVX_WITH_OFFSET: DevX counter with offset.
            qp: A QP for destination QP action.
            flow_action: A FlowAction for flow action type.
            obj: A Mlx5DevxObj for DevX actions.
            offset: Offset for counter with offset action. Default is 0.

        Raises:
            PyverbsUserError: If an unsupported action type is provided.
        """
        ...

    @property
    def type(self) -> int:
        """The action type."""
        ...
    @type.setter
    def type(self, action_type: int) -> None: ...
    @property
    def qp(self) -> QP | None:
        """The destination QP (only for DEST_IBV_QP type)."""
        ...
    @qp.setter
    def qp(self, qp: QP) -> None: ...
    @property
    def devx_obj(self) -> Mlx5DevxObj | None:
        """The DevX object (for DEST_DEVX, COUNTERS_DEVX types)."""
        ...
    @devx_obj.setter
    def devx_obj(self, devx_obj: Mlx5DevxObj) -> None: ...
    @property
    def action(self) -> FlowAction:
        """The flow action (only for IBV_FLOW_ACTION type)."""
        ...
    @action.setter
    def action(self, action: FlowAction) -> None: ...
    @property
    def offset(self) -> int:
        """The counter offset (only for COUNTERS_DEVX_WITH_OFFSET type)."""
        ...
    @offset.setter
    def offset(self, offset: int) -> None: ...

class Mlx5Flow(Flow):
    """MLX5 extended flow rule (extends Flow) with DevX support.

    Creates a flow rule using an Mlx5FlowMatcher with support for
    DevX destination objects and counters.
    """

    def __init__(
        self,
        matcher: Mlx5FlowMatcher,
        match_value: Mlx5FlowMatchParameters,
        action_attrs: list[Mlx5FlowActionAttr] | None = None,
        num_actions: int = 0,
    ) -> None:
        """Create an MLX5 flow rule.

        Args:
            matcher: A Mlx5FlowMatcher defining the fields to match on.
            match_value: A Mlx5FlowMatchParameters with values to match on.
            action_attrs: List of Mlx5FlowActionAttr defining the actions.
                Default is None (no actions).
            num_actions: Expected number of actions. Default is 0.

        Raises:
            PyverbsRDMAErrno: If flow creation fails.
            PyverbsUserError: If an unsupported action type is provided.
        """
        ...

class Mlx5PacketReformatFlowAction(FlowAction):
    """Packet reformat flow action (encap/decap).

    Creates a flow action for adding or removing packet headers
    (L2/L3 tunnel encap/decap).
    """

    def __init__(
        self, context: Context, data: bytes | list[int] | None = None, reformat_type: int = ..., ft_type: int = ...
    ) -> None:
        """Create a packet reformat flow action.

        Args:
            context: A Context object.
            data: Encapsulation headers as bytes (optional). Required for
                encap operations.
            reformat_type: Reformat type, one of
                MLX5DV_FLOW_ACTION_PACKET_REFORMAT_TYPE_*.
                Default is L2_TUNNEL_TO_L2.
            ft_type: Flow table type, e.g.
                MLX5DV_FLOW_TABLE_TYPE_NIC_RX or MLX5DV_FLOW_TABLE_TYPE_NIC_TX.
                Default is NIC_RX.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class Mlx5ModifyFlowAction(FlowAction):
    """Modify header flow action.

    Creates a flow action for modifying packet header fields using
    a list of set/add/copy commands.
    """

    def __init__(self, ctx: Context, ft_type: int = ..., actions: list[Any] = ...) -> None:
        """Create a modify header flow action.

        Args:
            ctx: A Context object.
            ft_type: Flow table type (e.g. MLX5DV_FLOW_TABLE_TYPE_NIC_RX
                or MLX5DV_FLOW_TABLE_TYPE_NIC_TX). Default is NIC_RX.
            actions: List of modify action commands (AddActionIn, SetActionIn,
                CopyActionIn) as bytes-like objects. Default is empty list.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
            MemoryError: If memory allocation fails.
        """
        ...
