"""
Type stubs for pyverbs.spec — Flow specification types.
"""

from typing import ClassVar

from pyverbs.base import PyverbsObject

class Spec(PyverbsObject):
    """Abstract base class for all flow specifications."""

    def __init__(self) -> None:
        raise NotImplementedError("This class is abstract.")

    @property
    def size(self) -> int:
        """Size in bytes."""
        ...
    def _copy_data(self, ptr: int) -> None:
        """Copy spec data to the given address. Must be implemented by subclass."""
        ...

    @staticmethod
    def type_to_str(spec_type: int) -> str:
        """Convert flow spec type to human-readable string.

        Args:
            spec_type: Flow spec type enum value.

        Returns:
            Human-readable type name string.
        """
        ...

    def __str__(self) -> str: ...

class EthSpec(Spec):
    """Ethernet header flow specification (ibv_flow_spec_eth)."""

    MAC_LEN: ClassVar[int]
    MAC_MASK: ClassVar[str]
    ZERO_MAC: ClassVar[list[int]]

    def __init__(
        self,
        dst_mac: str | None = None,
        dst_mac_mask: str | None = None,
        src_mac: str | None = None,
        src_mac_mask: str | None = None,
        ether_type: int | None = None,
        ether_type_mask: int | None = None,
        vlan_tag: int | None = None,
        vlan_tag_mask: int | None = None,
        is_inner: int = 0,
    ) -> None: ...
    @property
    def dst_mac(self) -> str:
        """Destination MAC address."""
        ...
    @dst_mac.setter
    def dst_mac(self, val: str) -> None: ...
    @property
    def dst_mac_mask(self) -> str:
        """Destination MAC mask."""
        ...
    @dst_mac_mask.setter
    def dst_mac_mask(self, val: str) -> None: ...
    @property
    def src_mac(self) -> str:
        """Source MAC address."""
        ...
    @src_mac.setter
    def src_mac(self, val: str) -> None: ...
    @property
    def src_mac_mask(self) -> str:
        """Source MAC mask."""
        ...
    @src_mac_mask.setter
    def src_mac_mask(self, val: str) -> None: ...
    @property
    def ether_type(self) -> int:
        """EtherType."""
        ...
    @ether_type.setter
    def ether_type(self, val: int) -> None: ...
    @property
    def ether_type_mask(self) -> int:
        """EtherType mask."""
        ...
    @ether_type_mask.setter
    def ether_type_mask(self, val: int) -> None: ...
    @property
    def vlan_tag(self) -> int:
        """VLAN tag."""
        ...
    @vlan_tag.setter
    def vlan_tag(self, val: int) -> None: ...
    @property
    def vlan_tag_mask(self) -> int:
        """VLAN tag mask."""
        ...
    @vlan_tag_mask.setter
    def vlan_tag_mask(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class Ipv4ExtSpec(Spec):
    """Extended IPv4 header flow specification (ibv_flow_spec_ipv4_ext)."""

    def __init__(
        self,
        dst_ip: str | None = None,
        dst_ip_mask: str | None = None,
        src_ip: str | None = None,
        src_ip_mask: str | None = None,
        proto: int | None = None,
        proto_mask: int | None = None,
        tos: int | None = None,
        tos_mask: int | None = None,
        ttl: int | None = None,
        ttl_mask: int | None = None,
        flags: int | None = None,
        flags_mask: int | None = None,
        is_inner: bool = False,
    ) -> None: ...
    @property
    def dst_ip(self) -> str:
        """Destination IP address."""
        ...
    @dst_ip.setter
    def dst_ip(self, val: str) -> None: ...
    @property
    def dst_ip_mask(self) -> str:
        """Destination IP mask."""
        ...
    @dst_ip_mask.setter
    def dst_ip_mask(self, val: str) -> None: ...
    @property
    def src_ip(self) -> str:
        """Source IP address."""
        ...
    @src_ip.setter
    def src_ip(self, val: str) -> None: ...
    @property
    def src_ip_mask(self) -> str:
        """Source IP mask."""
        ...
    @src_ip_mask.setter
    def src_ip_mask(self, val: str) -> None: ...
    @property
    def proto(self) -> int:
        """Protocol."""
        ...
    @proto.setter
    def proto(self, val: int) -> None: ...
    @property
    def proto_mask(self) -> int:
        """Protocol mask."""
        ...
    @proto_mask.setter
    def proto_mask(self, val: int) -> None: ...
    @property
    def tos(self) -> int:
        """Type of service."""
        ...
    @tos.setter
    def tos(self, val: int) -> None: ...
    @property
    def tos_mask(self) -> int:
        """Type of service mask."""
        ...
    @tos_mask.setter
    def tos_mask(self, val: int) -> None: ...
    @property
    def ttl(self) -> int:
        """Time to live."""
        ...
    @ttl.setter
    def ttl(self, val: int) -> None: ...
    @property
    def ttl_mask(self) -> int:
        """Time to live mask."""
        ...
    @ttl_mask.setter
    def ttl_mask(self, val: int) -> None: ...
    @property
    def flags(self) -> int:
        """Flags."""
        ...
    @flags.setter
    def flags(self, val: int) -> None: ...
    @property
    def flags_mask(self) -> int:
        """Flags mask."""
        ...
    @flags_mask.setter
    def flags_mask(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class TcpUdpSpec(Spec):
    """TCP/UDP header flow specification (ibv_flow_spec_tcp_udp)."""

    def __init__(
        self,
        spec_type: int,
        dst_port: int | None = None,
        dst_port_mask: int | None = None,
        src_port: int | None = None,
        src_port_mask: int | None = None,
        is_inner: bool = False,
    ) -> None: ...
    @property
    def dst_port(self) -> int:
        """Destination port."""
        ...
    @dst_port.setter
    def dst_port(self, val: int) -> None: ...
    @property
    def dst_port_mask(self) -> int:
        """Destination port mask."""
        ...
    @dst_port_mask.setter
    def dst_port_mask(self, val: int) -> None: ...
    @property
    def src_port(self) -> int:
        """Source port."""
        ...
    @src_port.setter
    def src_port(self, val: int) -> None: ...
    @property
    def src_port_mask(self) -> int:
        """Source port mask."""
        ...
    @src_port_mask.setter
    def src_port_mask(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class Ipv6Spec(Spec):
    """IPv6 header flow specification (ibv_flow_spec_ipv6)."""

    EMPTY_IPV6: ClassVar[str]
    IPV6_MASK: ClassVar[str]
    FLOW_LABEL_MASK: ClassVar[int]

    def __init__(
        self,
        dst_ip: str | None = None,
        dst_ip_mask: str | None = None,
        src_ip: str | None = None,
        src_ip_mask: str | None = None,
        flow_label: int | None = None,
        flow_label_mask: int | None = None,
        next_hdr: int | None = None,
        next_hdr_mask: int | None = None,
        traffic_class: int | None = None,
        traffic_class_mask: int | None = None,
        hop_limit: int | None = None,
        hop_limit_mask: int | None = None,
        is_inner: bool = False,
    ) -> None: ...
    @property
    def dst_ip(self) -> str:
        """Destination IP address."""
        ...
    @dst_ip.setter
    def dst_ip(self, val: str) -> None: ...
    @property
    def dst_ip_mask(self) -> str:
        """Destination IP mask."""
        ...
    @dst_ip_mask.setter
    def dst_ip_mask(self, val: str) -> None: ...
    @property
    def src_ip(self) -> str:
        """Source IP address."""
        ...
    @src_ip.setter
    def src_ip(self, val: str) -> None: ...
    @property
    def src_ip_mask(self) -> str:
        """Source IP mask."""
        ...
    @src_ip_mask.setter
    def src_ip_mask(self, val: str) -> None: ...
    @property
    def flow_label(self) -> int:
        """IPv6 flow label."""
        ...
    @flow_label.setter
    def flow_label(self, val: int) -> None: ...
    @property
    def flow_label_mask(self) -> int:
        """IPv6 flow label mask."""
        ...
    @flow_label_mask.setter
    def flow_label_mask(self, val: int) -> None: ...
    @property
    def next_hdr(self) -> int:
        """Next header."""
        ...
    @next_hdr.setter
    def next_hdr(self, val: int) -> None: ...
    @property
    def next_hdr_mask(self) -> int:
        """Next header mask."""
        ...
    @next_hdr_mask.setter
    def next_hdr_mask(self, val: int) -> None: ...
    @property
    def traffic_class(self) -> int:
        """Traffic class."""
        ...
    @traffic_class.setter
    def traffic_class(self, val: int) -> None: ...
    @property
    def traffic_class_mask(self) -> int:
        """Traffic class mask."""
        ...
    @traffic_class_mask.setter
    def traffic_class_mask(self, val: int) -> None: ...
    @property
    def hop_limit(self) -> int:
        """Hop limit."""
        ...
    @hop_limit.setter
    def hop_limit(self, val: int) -> None: ...
    @property
    def hop_limit_mask(self) -> int:
        """Hop limit mask."""
        ...
    @hop_limit_mask.setter
    def hop_limit_mask(self, val: int) -> None: ...
    def __str__(self) -> str: ...
