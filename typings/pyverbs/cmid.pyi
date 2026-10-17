"""
Type stubs for pyverbs.cmid — RDMA Connection Manager (CM) types.
"""

from pyverbs.addr import AH, AHAttr
from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.cq import WC
from pyverbs.device import Context
from pyverbs.mr import MR
from pyverbs.pd import PD
from pyverbs.qp import ECE, QPAttr, QPInitAttr

class ConnParam(PyverbsObject):
    """Connection parameters for RDMA CM (rdma_conn_param).

    Contains connection parameters for RDMA_PS_TCP port space, resembling
    RC QP connection parameters (responder resources, initiator depth, etc.).
    """

    def __init__(
        self,
        resources: int = 1,
        depth: int = 1,
        flow_control: int = 0,
        retry: int = 5,
        rnr_retry: int = 5,
        srq: int = 0,
        qp_num: int = 0,
        data_len: int = 0,
    ) -> None:
        """Initialize connection parameters.

        Args:
            resources: Max outstanding RDMA read/atomic ops the local side
                will accept from the remote side.
            depth: Max outstanding RDMA read/atomic ops to the remote side.
            flow_control: Whether hardware flow control is available.
            retry: Max retries for send/RDMA/atomic ops from remote peer.
            rnr_retry: Max retries on RNR errors from remote peer.
            srq: Whether the QP uses shared receive queue.
            qp_num: QP number (ignored if QP created by CMID).
            data_len: Private data length in bytes.
        """
        ...

    @property
    def qpn(self) -> int:
        """QP number."""
        ...
    @qpn.setter
    def qpn(self, val: int) -> None: ...
    @property
    def private_data(self) -> bytes:
        """Private data bytes."""
        ...

    def set_private_data(self, data: bytes) -> None:
        """Set private data for the connection.

        Args:
            data: Private data bytes.
        """
        ...

    def __str__(self) -> str: ...

class JoinMCAttrEx(PyverbsObject):
    """Extended join multicast attributes (rdma_cm_join_mc_attr_ex)."""

    def __init__(self, addr: AddrInfo, comp_mask: int = 0, join_flags: int = 0) -> None:
        """Initialize extended join multicast attributes.

        Args:
            addr: Multicast address identifying the group to join.
            comp_mask: Bitwise OR of rdma_cm_join_mc_attr_mask.
            join_flags: Single flag from rdma_cm_mc_join_flags.
        """
        ...

    @property
    def join_flags(self) -> int:
        """Join flags."""
        ...
    @join_flags.setter
    def join_flags(self, val: int) -> None: ...
    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...

class UDParam(PyverbsObject):
    """UD connection parameters from a CM event (rdma_ud_param).

    Contains UD QP number, QKey, and AH attributes from a connection
    establishment event.
    """

    def __init__(self, cm_event: CMEvent) -> None:
        """Initialize UD parameters from a CM event.

        Args:
            cm_event: The CM event containing UD parameters.
        """
        ...

    @property
    def qp_num(self) -> int:
        """Remote QP number."""
        ...

    @property
    def qkey(self) -> int:
        """Remote QKey."""
        ...

    @property
    def ah_attr(self) -> AHAttr:
        """Address Handle attributes (AHAttr)."""
        ...

class AddrInfo(PyverbsObject):
    """RDMA address information (rdma_addrinfo).

    Contains information needed to establish communication, resolved
    from IP addresses to RDMA addresses.
    """

    def __init__(
        self,
        src: str | None = None,
        dst: str | None = None,
        src_service: str | int | None = None,
        dst_service: str | int | None = None,
        port_space: int = 0,
        flags: int = 0,
    ) -> None:
        """Resolve source and destination addresses.

        Args:
            src: Name, dotted-decimal IPv4 or IPv6 hex address to bind.
            dst: Name, dotted-decimal IPv4 or IPv6 hex address to connect.
            src_service: Service name or port number of the source.
            dst_service: Service name or port number of the destination.
            port_space: RDMA port space (RDMA_PS_UDP, RDMA_PS_TCP, etc.).
            flags: Hint flags controlling the operation.

        Raises:
            PyverbsRDMAErrno: If address resolution fails.
        """
        ...

    def get_addrinfo(
        self,
        src: str | None = None,
        dst: str | None = None,
        src_service: str | int | None = None,
        dst_service: str | int | None = None,
        port_space: int = 0,
        flags: int = 0,
    ) -> None:
        """Resolve source and destination addresses.

        Args:
            src: Source address.
            dst: Destination address.
            src_service: Source service/port.
            dst_service: Destination service/port.
            port_space: RDMA port space.
            flags: Hint flags.

        Raises:
            PyverbsRDMAErrno: If resolution fails.
        """
        ...

class CMEvent(PyverbsObject):
    """RDMA CM event (rdma_cm_event).

    Represents a communication event received on an event channel.
    """

    def __init__(self, channel: CMEventChannel) -> None:
        """Retrieve the next event from the channel.

        Args:
            channel: Event channel to receive from.

        Raises:
            PyverbsRDMAErrno: If rdma_get_cm_event fails.
        """
        ...

    def ack_cm_event(self) -> None:
        """Free the communication event and associated memory.

        Raises:
            PyverbsRDMAErrno: If rdma_ack_cm_event fails.
        """
        ...

    def event_str(self) -> str:
        """Return a string description of the event type.

        Returns:
            Human-readable string representation of the CM event type.
        """
        ...

    @property
    def event_type(self) -> int:
        """Event type (rdma_cm_event_type)."""
        ...

    @property
    def private_data(self) -> bytes:
        """Private data from the event."""
        ...

class CMEventChannel(PyverbsObject):
    """RDMA CM event channel (rdma_event_channel).

    Used to receive communication events.
    """

    def __init__(self) -> None:
        """Create an event channel.

        Raises:
            PyverbsRDMAErrno: If rdma_create_event_channel fails.
        """
        ...

class CMID(PyverbsCM):
    """RDMA CM identifier (rdma_cm_id).

    The main object for RDMA connection management. Supports both synchronous
    and event-driven connection establishment. Currently only synchronous
    RDMA_PS_TCP communication is fully supported.
    """

    def __init__(
        self,
        creator: AddrInfo | CMEventChannel | CMEvent | None = None,
        qp_init_attr: QPInitAttr | None = None,
        pd: PD | None = None,
        port_space: int = 0,
        listen_id: CMID | None = None,
    ) -> None:
        """Create a CMID.

        Args:
            creator: An AddrInfo, CMEventChannel, or CMEvent object.
                None is allowed for internal use (get_request).
            qp_init_attr: Optional QP initialization attributes.
            pd: Optional PD to associate.
            port_space: RDMA port space (e.g. RDMA_PS_TCP).
            listen_id: Parent listen CMID (for new connections from events).

        Raises:
            PyverbsRDMAErrno: If rdma_create_ep/id fails.
            PyverbsRDMAErrno: If creator type is unsupported.
        """
        ...

    def get_request(self) -> CMID:
        """Retrieve the next pending connection request (listen side only).

        Returns:
            A new CMID representing the connection request.

        Raises:
            PyverbsRDMAErrno: If rdma_get_request fails.
        """
        ...

    def bind_addr(self, lai: AddrInfo) -> None:
        """Associate a source address with this CMID.

        Args:
            lai: Local address information.

        Raises:
            PyverbsRDMAErrno: If rdma_bind_addr fails.
        """
        ...

    def resolve_addr(self, rai: AddrInfo, timeout_ms: int = 2000) -> None:
        """Resolve destination and optional source addresses.

        Args:
            rai: Remote address information.
            timeout_ms: Timeout in milliseconds.

        Raises:
            PyverbsRDMAErrno: If rdma_resolve_addr fails.
        """
        ...

    def join_multicast(
        self, addr: AddrInfo | None = None, mc_attr: JoinMCAttrEx | None = None, context: int = 0
    ) -> None:
        """Join a multicast group.

        Args:
            addr: Multicast address (for basic join).
            mc_attr: Extended join attributes (for join_ex).
            context: User-defined context.

        Raises:
            PyverbsUserError: If neither addr nor mc_attr is given.
            PyverbsRDMAErrno: If join fails.
        """
        ...

    def leave_multicast(self, addr: AddrInfo) -> None:
        """Leave a multicast group.

        Args:
            addr: Multicast address identifying the group.

        Raises:
            PyverbsRDMAErrno: If rdma_leave_multicast fails.
        """
        ...

    def resolve_route(self, timeout_ms: int = 2000) -> None:
        """Resolve an RDMA route to the destination address.

        Args:
            timeout_ms: Timeout in milliseconds.

        Raises:
            PyverbsRDMAErrno: If rdma_resolve_route fails.
        """
        ...

    def listen(self, backlog: int = 0) -> None:
        """Listen for incoming connection requests.

        Args:
            backlog: Max pending connection requests.

        Raises:
            PyverbsRDMAErrno: If rdma_listen fails.
        """
        ...

    def connect(self, param: ConnParam | None = None) -> None:
        """Initiate an active connection request.

        Args:
            param: Optional connection parameters.

        Raises:
            PyverbsRDMAErrno: If rdma_connect fails.
        """
        ...

    def disconnect(self) -> None:
        """Disconnect and transition associated QP to error state.

        Raises:
            PyverbsRDMAErrno: If rdma_disconnect fails.
        """
        ...

    def accept(self, param: ConnParam | None = None) -> None:
        """Accept an incoming connection request (listening side).

        Args:
            param: Optional connection parameters.

        Raises:
            PyverbsRDMAErrno: If rdma_accept fails.
        """
        ...

    def establish(self) -> None:
        """Complete an active connection request.

        Should be called by the active side after connect response event
        when no QP was created on the CMID.

        Raises:
            PyverbsRDMAErrno: If rdma_establish fails.
        """
        ...

    def set_local_ece(self, ece: ECE) -> None:
        """Set local ECE parameters for REQ/REP communication.

        Args:
            ece: An ECE object with the requested configuration.

        Raises:
            PyverbsRDMAErrno: If rdma_set_local_ece fails.
        """
        ...

    def get_remote_ece(self) -> ECE:
        """Get ECE parameters received from the communication peer.

        Returns:
            An ECE object with the received configuration.

        Raises:
            PyverbsRDMAErrno: If rdma_get_remote_ece fails.
        """
        ...

    def create_qp(self, qp_init: QPInitAttr) -> None:
        """Create a QP associated with this CMID.

        If both CMID and qp_init provide CQs they must be the same.
        If only qp_init provides CQs, they won't be associated with CMID.

        Args:
            qp_init: QPInitAttr for QP creation.

        Raises:
            PyverbsRDMAErrno: If rdma_create_qp fails.
        """
        ...

    def query_qp(self, attr_mask: int) -> tuple[QPAttr, QPInitAttr]:
        """Query the CMID's QP attributes.

        Args:
            attr_mask: Which attributes to query.

        Returns:
            A (QPAttr, QPInitAttr) tuple.

        Raises:
            PyverbsRDMAError: If ibv_query_qp fails.
        """
        ...

    def init_qp_attr(self, qp_state: int) -> tuple[QPAttr, int]:
        """Get QP attributes for state transition of an external QP.

        Both sides must call this before transitioning external QPs to
        RTR/RTS when connecting via CMIDs.

        Args:
            qp_state: The QP's destination state.

        Returns:
            A (QPAttr, attr_mask) tuple.

        Raises:
            PyverbsRDMAErrno: If rdma_init_qp_attr fails.
        """
        ...

    def reg_msgs(self, size: int) -> MR:
        """Register an MR for sending/receiving messages.

        Args:
            size: Length of memory to register.

        Returns:
            The registered MR.
        """
        ...

    def reg_read(self, size: int = 0) -> MR:
        """Register an MR for remote read operations.

        Args:
            size: Length of memory to register.

        Returns:
            The registered MR.
        """
        ...

    def reg_write(self, size: int = 0) -> MR:
        """Register an MR for remote write operations.

        Args:
            size: Length of memory to register.

        Returns:
            The registered MR.
        """
        ...

    def post_recv(self, mr: MR, length: int | None = None) -> None:
        """Post a receive WR via the CMID's associated QP.

        Args:
            mr: A valid MR object.
            length: Buffer length to receive (default: MR length).

        Raises:
            PyverbsRDMAErrno: If rdma_post_recv fails.
        """
        ...

    def post_send(self, mr: MR, flags: int = 0, length: int | None = None) -> None:
        """Post a send WR via the CMID's associated QP.

        Args:
            mr: A valid MR containing the message to send.
            flags: Send work request flags.
            length: Buffer length to send (default: MR length).

        Raises:
            PyverbsRDMAErrno: If rdma_post_send fails.
        """
        ...

    def post_read(self, mr: MR, length: int, remote_addr: int, rkey: int, flags: int = 0) -> None:
        """Post an RDMA read WR via the CMID's internal QP.

        Args:
            mr: A valid MR for the local buffer.
            length: Length of data to read.
            remote_addr: Remote MR address.
            rkey: Remote MR rkey.
            flags: Send work request flags.

        Raises:
            PyverbsRDMAErrno: If rdma_post_read fails.
        """
        ...

    def post_write(self, mr: MR, length: int, remote_addr: int, rkey: int, flags: int = 0) -> None:
        """Post an RDMA write WR via the CMID's internal QP.

        Args:
            mr: A valid MR for the local buffer.
            length: Length of data to write.
            remote_addr: Remote MR address.
            rkey: Remote MR rkey.
            flags: Send work request flags.

        Raises:
            PyverbsRDMAErrno: If rdma_post_write fails.
        """
        ...

    def post_ud_send(
        self,
        mr: MR,
        ah: AH,
        rqpn: int = 0,
        flags: int = 0,
        length: int | None = None,
    ) -> None:
        """Post a UD send via the CMID's associated UD QP.

        Args:
            mr: A valid MR containing the message.
            ah: Destination Address Handle.
            rqpn: Remote QP number.
            flags: Send work request flags.
            length: Buffer length (default: MR length).

        Raises:
            PyverbsRDMAErrno: If rdma_post_ud_send fails.
        """
        ...

    def get_recv_comp(self) -> WC | None:
        """Poll the receive CQ for a work completion.

        Returns:
            A WC object, or None if no completions available.

        Raises:
            PyverbsRDMAErrno: If rdma_get_recv_comp fails.
        """
        ...

    def get_send_comp(self) -> WC | None:
        """Poll the send CQ for a work completion.

        Returns:
            A WC object, or None if no completions available.

        Raises:
            PyverbsRDMAErrno: If rdma_get_send_comp fails.
        """
        ...

    def set_option(self, level: int, optname: int, optval: int, optlen: int) -> None:
        """Set communication options for this CMID.

        Currently only RDMA_OPTION_ID_ACK_TIMEOUT is supported.

        Args:
            level: Protocol level.
            optname: Option name.
            optval: Option data.
            optlen: Size of the data.

        Raises:
            PyverbsUserError: If optname is unsupported.
            PyverbsRDMAErrno: If rdma_set_option fails.
        """
        ...

    def reject(self, private_data: bytes | None = None) -> None:
        """Reject a connection or datagram service lookup request.

        Args:
            private_data: Optional private data to send with the reject.

        Raises:
            PyverbsRDMAErrno: If rdma_reject fails.
        """
        ...

    def resolve_addrinfo(
        self, node: str | None = None, service: str | int | None = None, port_space: int = 0, flags: int = 0
    ) -> None:
        """Resolve address information using RDMA CM.

        Args:
            node: Address to connect to.
            service: Service name or port number.
            port_space: RDMA port space.
            flags: Resolution flags (RAI_PASSIVE, RAI_NUMERICHOST, etc.).

        Raises:
            PyverbsRDMAErrno: If rdma_resolve_addrinfo fails.
        """
        ...

    def query_addrinfo(self) -> AddrInfo:
        """Query the resolved address info from this CMID.

        Returns:
            An AddrInfo with the resolved address information.

        Raises:
            PyverbsRDMAErrno: If rdma_query_addrinfo fails.
        """
        ...

    @property
    def dev_name(self) -> str:
        """RDMA device name."""
        ...

    @property
    def port_num(self) -> int:
        """Port number."""
        ...

    @property
    def event_channel(self) -> CMEventChannel | None:
        """Associated event channel."""
        ...

    @property
    def context(self) -> Context | None:
        """Associated Context."""
        ...

    @property
    def pd(self) -> PD | None:
        """Associated PD."""
        ...

    @property
    def qpn(self) -> int | None:
        """QP number, or None if no QP is created."""
        ...
