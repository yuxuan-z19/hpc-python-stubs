"""
Type stubs for pyverbs.flow — Flow steering types.
"""

from typing import Any

from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.qp import QP

class FlowAttr(PyverbsObject):
    """Flow steering attributes (ibv_flow_attr).

    Contains attributes for creating a steering flow rule, including
    flow type, priority, port, and a list of flow specs.
    """

    def __init__(
        self, num_of_specs: int = 0, flow_type: int = 0, priority: int = 0, port: int = 1, flags: int = 0
    ) -> None:
        """Initialize flow steering attributes.

        Args:
            num_of_specs: Number of flow specs to attach.
            flow_type: Flow type (IBV_FLOW_ATTR_NORMAL, etc.).
            priority: Flow priority (lower = higher priority).
            port: Port number.
            flags: Flow flags.
        """
        ...

    @property
    def type(self) -> int:
        """Flow type."""
        ...
    @type.setter
    def type(self, val: int) -> None: ...
    @property
    def priority(self) -> int:
        """Flow priority."""
        ...
    @priority.setter
    def priority(self, val: int) -> None: ...
    @property
    def num_of_specs(self) -> int:
        """Number of flow specs."""
        ...
    @num_of_specs.setter
    def num_of_specs(self, val: int) -> None: ...
    @property
    def port(self) -> int:
        """Port number."""
        ...
    @port.setter
    def port(self, val: int) -> None: ...
    @property
    def flags(self) -> int:
        """Flow flags."""
        ...
    @flags.setter
    def flags(self, val: int) -> None: ...
    @property
    def specs(self) -> list[Any]:
        """List of flow spec objects attached to this flow."""
        ...

class Flow(PyverbsCM):
    """Flow steering rule (ibv_flow).

    Represents a steering flow that directs matching incoming packets
    to a specific QP.
    """

    def __init__(self, qp: QP, flow_attr: FlowAttr) -> None:
        """Create a flow steering rule.

        Args:
            qp: QP to steer matching traffic to.
            flow_attr: Flow attributes with specs.

        Raises:
            PyverbsRDMAErrno: If ibv_create_flow fails.
        """
        ...

class FlowAction(PyverbsObject):
    """Flow action for hardware offload (ibv_flow_action).

    Base class for vendor-specific flow actions.
    """

    ...
