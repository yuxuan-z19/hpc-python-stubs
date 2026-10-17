"""
Type stubs for pyverbs.providers.mlx5.dr_action — MLX5 Direct Rules Actions.

Provides various steering action types for DR flow rules including
redirect, modify header, drop, tag, VLAN, packet reformat, and more.
"""

from pyverbs.base import PyverbsCM
from pyverbs.providers.mlx5.dr_domain import DrDomain
from pyverbs.providers.mlx5.dr_table import DrTable
from pyverbs.providers.mlx5.mlx5dv import Mlx5DevxObj
from pyverbs.qp import QP

class DrAction(PyverbsCM):
    """Base class for all DR steering actions (mlx5dv_dr_action).

    All specific action types inherit from this class. An action defines
    what to do with a packet when it matches a DR rule.
    """

    def __init__(self) -> None: ...

class DrActionQp(DrAction):
    """DR action: redirect traffic to an IBV QP.

    Creates a destination action that directs matched packets to the
    specified Queue Pair.
    """

    def __init__(self, qp: QP) -> None:
        """Create a DR action to redirect to a QP.

        Args:
            qp: A QP object to redirect matched traffic to.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class DrActionFlowCounter(DrAction):
    """DR action: attach a flow counter to matched traffic.

    Creates a flow counter action using a DevX counter object.
    """

    def __init__(self, devx_obj: Mlx5DevxObj, offset: int = 0) -> None:
        """Create a DR flow counter action.

        Args:
            devx_obj: A Mlx5DevxObj representing the flow counter object.
            offset: Offset of the specific counter within the counter object.
                Default is 0.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class DrActionDrop(DrAction):
    """DR action: drop matched packets.

    Creates a drop action that discards all matching packets.
    """

    def __init__(self) -> None:
        """Create a DR flow drop action.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class DrActionModify(DrAction):
    """DR action: modify packet header fields.

    Creates a modify-header action that can set, add, or copy
    fields in the packet header.
    """

    def __init__(self, domain: DrDomain, flags: int = 0, actions: list[bytes] = ...) -> None:
        """Create a DR modify header action.

        Args:
            domain: A DrDomain object where the action should be located.
            flags: Modify action flags. Default is 0.
            actions: List of modify action commands as bytes-like objects
                (each in device specification format, 8 bytes each).
                Default is an empty list.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
            MemoryError: If memory allocation fails.
        """
        ...

class DrActionTag(DrAction):
    """DR action: set a tag on matched packets.

    Tags can be used for subsequent matching or identification.
    """

    def __init__(self, tag: int) -> None:
        """Create a DR tag action.

        Args:
            tag: Tag value to set on matched packets.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class DrActionDestTable(DrAction):
    """DR action: forward packets to another DR table.

    Creates a destination table action for steering traffic to
    a different table in the steering pipeline.
    """

    def __init__(self, table: DrTable) -> None:
        """Create a DR destination table action.

        Args:
            table: A DrTable to forward matched packets to.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class DrActionPushVLan(DrAction):
    """DR action: push a VLAN header onto matched packets."""

    def __init__(self, domain: DrDomain, vlan_hdr: int) -> None:
        """Create a DR push VLAN action.

        Args:
            domain: A DrDomain object where the action should be located.
            vlan_hdr: VLAN header value (32-bit) to push.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class DrActionPopVLan(DrAction):
    """DR action: pop a VLAN header from matched packets."""

    def __init__(self) -> None:
        """Create a DR pop VLAN action.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class DrActionDestAttr(PyverbsCM):
    """Multi-destination attribute for DR destination array actions.

    Used to compose destination + optional reformat actions into
    a single entry for the destination array action.
    """

    def __init__(self, action_type: int, dest: DrAction, reformat: DrAction | None = None) -> None:
        """Create a multi-destination attribute.

        Args:
            action_type: Type of destination action, either
                MLX5DV_DR_ACTION_DEST or MLX5DV_DR_ACTION_DEST_REFORMAT.
            dest: A DrAction for the destination.
            reformat: Optional DrAction for reformat (encap) before
                the destination. Required when action_type is
                MLX5DV_DR_ACTION_DEST_REFORMAT.

        Raises:
            PyverbsRDMAErrno: If memory allocation fails.
            PyverbsError: If an unsupported action type is provided.
        """
        ...

class DrActionDestArray(DrAction):
    """DR action: destination array (multi-destination forwarding).

    Creates an action that forwards packets to multiple destinations
    simultaneously.
    """

    def __init__(self, domain: DrDomain, actions_num: int, dest_actions: list[DrActionDestAttr]) -> None:
        """Create a DR destination array action.

        Args:
            domain: A DrDomain object where the action should be located.
            actions_num: Number of destination actions in the array.
            dest_actions: List of DrActionDestAttr objects representing
                the destinations.

        Raises:
            PyverbsError: If required parameters are missing or memory
                allocation fails.
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class DrActionDefMiss(DrAction):
    """DR action: default miss (return to regular pipeline).

    Creates a default miss action that returns unmatched or
    explicitly missed packets to the regular steering pipeline.
    """

    def __init__(self) -> None:
        """Create a DR default miss action.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class DrActionVPort(DrAction):
    """DR action: forward to a virtual port (vport)."""

    def __init__(self, domain: DrDomain, vport: int) -> None:
        """Create a DR vport destination action.

        Args:
            domain: A DrDomain object where the action should be placed.
            vport: Virtual port number to forward to.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class DrActionIBPort(DrAction):
    """DR action: forward to an InfiniBand port."""

    def __init__(self, domain: DrDomain, ib_port: int) -> None:
        """Create a DR IB port destination action.

        Args:
            domain: A DrDomain object where the action should be placed.
            ib_port: IB port number to forward to.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class DrActionDestTir(DrAction):
    """DR action: forward to a TIR (Transport Interface Receive) DevX object."""

    def __init__(self, devx_tir: Mlx5DevxObj) -> None:
        """Create a DR dest DevX TIR action.

        Args:
            devx_tir: A Mlx5DevxObj representing the destination TIR.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class DrActionPacketReformat(DrAction):
    """DR action: packet reformat (encapsulation/decapsulation).

    Supports L2/L3 tunnel encap and decap operations.
    """

    def __init__(
        self, domain: DrDomain, flags: int = 0, reformat_type: int = ..., data: bytes | list[int] | None = None
    ) -> None:
        """Create a DR packet reformat action.

        Args:
            domain: A DrDomain object where the action should be placed.
            flags: Packet reformat action flags. Default is 0.
            reformat_type: Reformat type, one of
                MLX5DV_FLOW_ACTION_PACKET_REFORMAT_TYPE_*:
                - L2_TUNNEL_TO_L2 (decap)
                - L2_TO_L2_TUNNEL (encap)
                - L3_TUNNEL_TO_L2 (decap)
                - L2_TO_L3_TUNNEL (encap)
                Default is L2_TUNNEL_TO_L2.
            data: Encapsulation headers as bytes (optional). Required for
                encap operations.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class DrFlowSamplerAttr(PyverbsCM):
    """Attributes for DR flow sampler action.

    Defines sampling ratio, default next table, and sample actions
    for the flow sampler.
    """

    def __init__(
        self,
        sample_ratio: int,
        default_next_table: DrTable,
        sample_actions: list[DrAction],
        action: bytes | None = None,
    ) -> None:
        """Create flow sampler attributes.

        Args:
            sample_ratio: Probability for a packet to be sampled is
                1/sample_ratio.
            default_next_table: A DrTable that all non-sampled packets
                continue to.
            sample_actions: List of DrAction objects to perform on the
                replicated sampled packets.
            action: Optional action for FDB table type (SetActionIn).

        Raises:
            MemoryError: If memory allocation fails.
        """
        ...

class DrActionFlowSample(DrAction):
    """DR action: flow sampling.

    Samples packets at a configurable ratio and performs specified
    actions on sampled packets.
    """

    def __init__(self, attr: DrFlowSamplerAttr) -> None:
        """Create a DR flow sample action.

        Args:
            attr: A DrFlowSamplerAttr containing sampling configuration.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

class DrFlowMeterAttr(PyverbsCM):
    """Attributes for DR flow meter (policer) action.

    Defines metering parameters including rates, colors, and the
    destination table after metering.
    """

    def __init__(
        self,
        next_table: DrTable,
        active: int = 1,
        reg_c_index: int = 0,
        flow_meter_parameter: bytes | list[int] | None = None,
    ) -> None:
        """Create flow meter attributes.

        Args:
            next_table: A DrTable to redirect packets to after metering.
            active: When set (default 1), the monitor is considered
                connected and should be monitored.
            reg_c_index: Index of Register C where the packet color will
                be set after metering. Valid values depend on
                QUERY_HCA_CAP.flow_meter_reg_id. Result is in the 8 LSB.
            flow_meter_parameter: PRM data bytes defining meter behavior
                (rates, colors, etc.).

        Raises:
            MemoryError: If memory allocation fails.
        """
        ...

class DrActionFlowMeter(DrAction):
    """DR action: flow metering (policing).

    Meters traffic according to configured rates and colors.
    """

    def __init__(self, attr: DrFlowMeterAttr) -> None:
        """Create a DR flow meter action.

        Args:
            attr: A DrFlowMeterAttr containing metering configuration.

        Raises:
            PyverbsRDMAErrno: If action creation fails.
        """
        ...

    def modify(self, attr: DrFlowMeterAttr, modify_field_select: int) -> None:
        """Modify flow meter action parameters.

        Args:
            attr: A DrFlowMeterAttr with the new metering parameters.
            modify_field_select: Bitmask selecting which fields to modify:
                - Bit 0: Active
                - Bit 1: CBS (cbs_exponent and cbs_mantissa)
                - Bit 2: CIR (cir_exponent and cir_mantissa)
                - Bit 3: EBS (ebs_exponent and ebs_mantissa)
                - Bit 4: EIR (eir_exponent and eir_mantissa)

        Raises:
            PyverbsRDMAErrno: If modification fails.
        """
        ...
