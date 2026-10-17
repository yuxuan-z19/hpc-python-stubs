"""
Type stubs for pyverbs.providers.mlx5.mlx5dv_event — MLX5 DevX event channel.

Provides asynchronous event notification through DevX event channels,
event headers, and eventfd support.
"""

from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.device import Context
from pyverbs.providers.mlx5.mlx5dv import Mlx5DevxObj

class EventChannel(PyverbsCM):
    """DevX event channel (mlx5dv_devx_event_channel).

    Allows subscribing to and receiving asynchronous events from
    DevX objects. Supports both standard subscription and eventfd-based
    notification.
    """

    def __init__(self, context: Context, flags: int = 0) -> None:
        """Create a DevX event channel.

        Args:
            context: A Context object to create the event channel on.
            flags: Create flags for the event channel. Default is 0.

        Raises:
            PyverbsRDMAErrno: If event channel creation fails.
        """
        ...

    def subscribe(
        self,
        events_num: int | list[int],
        cookie: int | None = None,
        obj: Mlx5DevxObj | None = None,
        fd: EventFD | None = None,
    ) -> None:
        """Subscribe to events on this channel.

        Two modes of subscription:
        1. Standard: Provide cookie (required) and optionally obj for
           affiliated events.
        2. EventFD: Provide fd for eventfd-based notification. Only one
           event number is supported in this mode.

        Args:
            events_num: Event type number(s) to subscribe to. Can be a
                single int or a list of ints. For fd subscription, only
                one event number is allowed.
            cookie: A 64-bit ID for the subscription. Required for
                standard subscription, ignored for fd subscription.
            obj: The Mlx5DevxObj related to the subscribed event.
                None for unaffiliated events.
            fd: An EventFD for fd-based subscription. If given, uses
                the eventfd subscription API.

        Raises:
            PyverbsError: If cookie is not provided for standard subscription,
                or if more than one event number is given for fd subscription.
            PyverbsRDMAErrno: If subscription fails.
        """
        ...

    def get_event(self, event_resp_len: int = 1024, fd: EventFD | None = None) -> EventHeader | int:
        """Get a pending event from the channel.

        Blocks until an event arrives if none are pending.

        Args:
            event_resp_len: Size in bytes of the allocated event response
                buffer. Default is 1024, sufficient for all current event types.
            fd: An EventFD. If given, reads directly from the eventfd
                and returns the read value as int.

        Returns:
            An EventHeader object containing cookie and data (standard mode),
            or an int (the eventfd read value) when fd is provided.

        Raises:
            PyverbsRDMAErrno: If getting the event fails.
        """
        ...

    @property
    def fd(self) -> int:
        """The underlying file descriptor of the event channel."""
        ...

class EventHeader(PyverbsObject):
    """Event header containing cookie and data from a received event.

    Returned by EventChannel.get_event() to represent the event in a
    Python-friendly manner.
    """

    def __init__(self, cookie: int, data: bytes) -> None:
        """Create an EventHeader.

        Args:
            cookie: Cookie retrieved from the event (matches the value
                provided during subscription).
            data: Raw event data bytes.
        """
        ...

    @property
    def cookie(self) -> int:
        """The subscription cookie associated with this event."""
        ...

    @property
    def data(self) -> bytes:
        """The raw event data."""
        ...

class EventFD(PyverbsObject):
    """Event file descriptor (eventfd) for event notification.

    Wraps a Linux eventfd for use with EventChannel fd-based subscription.
    """

    def __init__(self, initval: int = 0, flags: int = 0) -> None:
        """Create an eventfd.

        Args:
            initval: Initial counter value for the eventfd. Default is 0.
            flags: Flags for the eventfd (e.g. EFD_NONBLOCK, EFD_CLOEXEC).
                Default is 0.

        Raises:
            PyverbsRDMAErrno: If eventfd creation fails.
        """
        ...

    @property
    def fd(self) -> int:
        """The eventfd file descriptor."""
        ...
