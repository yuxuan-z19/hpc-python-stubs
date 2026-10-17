"""
Type stubs for pyverbs.device — RDMA device context and attributes.
··
Provides Context (ibv_context), DeviceAttr (ibv_device_attr), and related
types for opening, querying, and managing RDMA devices.
"""

from typing import Any

from pyverbs.addr import GID
from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.cmid import CMID

class Device(PyverbsObject):
    """Represents the C ibv_device. Stores device properties.

    Not part of the object creation order — there is no need for the user
    to create it for such purposes.
    """

    def __init__(self, name: bytes, guid: int, node_type: int, transport_type: int, index: int) -> None: ...
    @property
    def name(self) -> bytes:
        """Device name (e.g. b'mlx5_0')."""
        ...
    @property
    def node_type(self) -> int:
        """Node type (IBV_NODE_*)."""
        ...
    @property
    def transport_type(self) -> int:
        """Transport type (IBV_TRANSPORT_*)."""
        ...
    @property
    def guid(self) -> int:
        """Device GUID."""
        ...
    @property
    def index(self) -> int:
        """Device index in the kernel device list."""
        ...

    def __str__(self) -> str: ...

class Context(PyverbsCM):
    """Represents the C ibv_context. Opens an RDMA device."""

    def __init__(
        self, *, name: str | None = None, attr: Any = None, cmid: CMID | None = None, cmd_fd: int | None = None
    ) -> None:
        """Open an RDMA device.

        Args:
            name: The device name (e.g. 'mlx5_0'). Required unless cmid or cmd_fd is given.
            attr: Provider-specific attributes for opening the device.
            cmid: A CMID object that already holds an ibv_context pointer.
            cmd_fd: A command file descriptor to import the device from.
        """
        ...
    def close(self) -> None:
        """Close the IB device and release all associated resources."""
        ...
    @property
    def context(self) -> int:
        """Underlying ibv_context pointer as integer."""
        ...
    @property
    def num_comp_vectors(self) -> int:
        """Number of completion vectors available on the device."""
        ...
    @property
    def cmd_fd(self) -> int:
        """Command file descriptor of the context."""
        ...
    @property
    def name(self) -> str:
        """Device name string."""
        ...
    def query_device(self) -> DeviceAttr:
        """Query the device's attributes.

        Returns:
            A DeviceAttr object holding the device's attributes as reported by hardware.
        """
        ...
    def query_device_ex(self, ex_input: QueryDeviceExInput | None = None) -> DeviceAttrEx:
        """Query the device's extended attributes.

        Args:
            ex_input: Extensible input struct for possible future extensions.

        Returns:
            DeviceAttrEx object with extended device attributes.
        """
        ...
    def query_comp_cntr_caps(self) -> CompCntrCaps:
        """Query completion counter capabilities.

        Returns:
            CompCntrCaps object.
        """
        ...
    def query_pkey(self, port_num: int, index: int) -> int:
        """Query a P_Key entry.

        Args:
            port_num: Port number to query.
            index: P_Key table index.

        Returns:
            P_Key value.
        """
        ...
    def get_pkey_index(self, port_num: int, pkey: int) -> int:
        """Get the index of a P_Key in the port's P_Key table.

        Args:
            port_num: Port number.
            pkey: P_Key value to look up.

        Returns:
            Index of the P_Key in the table.
        """
        ...
    def query_gid(self, port_num: int, index: int) -> GID:
        """Query a GID entry.

        Args:
            port_num: Port number.
            index: GID table index.

        Returns:
            GID object.
        """
        ...
    def query_gid_type(self, port_num: int, index: int) -> int:
        """Query the GID type at a given index.

        Args:
            port_num: Port number.
            index: GID table index.

        Returns:
            GID type (IBV_GID_TYPE_SYSFS_*).
        """
        ...
    def query_port(self, port_num: int) -> PortAttr:
        """Query port attributes.

        Args:
            port_num: Port number to query.

        Returns:
            PortAttr object on success.
        """
        ...
    def query_port_speed(self, port_num: int) -> int:
        """Query port speed in 100 Mb/s granularity.

        Args:
            port_num: Port number to query.

        Returns:
            Port speed value.
        """
        ...
    def query_gid_table(self, max_entries: int, flags: int = 0) -> list[GIDEntry]:
        """Query the GID tables of the device.

        Args:
            max_entries: Maximum number of GID entries to retrieve.
            flags: Specifies extra members of struct ibv_gid_entry to query.

        Returns:
            List of GIDEntry objects.
        """
        ...
    def query_gid_ex(self, port_num: int, gid_index: int, flags: int = 0) -> GIDEntry:
        """Query a specific GID table entry.

        Args:
            port_num: Port number to query.
            gid_index: Index in the GID table.
            flags: Extra members to query.

        Returns:
            GIDEntry object.
        """
        ...
    def query_rt_values_ex(self, comp_mask: int = 1) -> tuple[int, int]:
        """Query real-time values of an RDMA device.

        Args:
            comp_mask: Mask indicating which values to query (default: IBV_VALUES_MASK_RAW_CLOCK).

        Returns:
            Tuple of (seconds, nanoseconds) for the raw clock.
        """
        ...
    def get_async_event(self) -> AsyncEvent:
        """Get an asynchronous event from the device.

        Returns:
            AsyncEvent object.
        """
        ...

class DeviceAttr(PyverbsObject):
    """Represents ibv_device_attr. Exposes read-only device properties."""

    @property
    def fw_version(self) -> str:
        """Firmware version string."""
        ...
    @property
    def node_guid(self) -> int:
        """Node GUID."""
        ...
    @property
    def sys_image_guid(self) -> int:
        """System image GUID."""
        ...
    @property
    def max_mr_size(self) -> int:
        """Maximum MR size in bytes."""
        ...
    @property
    def page_size_cap(self) -> int:
        """Supported page size bitmask."""
        ...
    @property
    def vendor_id(self) -> int:
        """Vendor ID."""
        ...
    @property
    def vendor_part_id(self) -> int:
        """Vendor part ID."""
        ...
    @property
    def hw_ver(self) -> int:
        """Hardware version."""
        ...
    @property
    def max_qp(self) -> int:
        """Maximum number of QPs."""
        ...
    @property
    def max_qp_wr(self) -> int:
        """Maximum number of WRs per QP."""
        ...
    @property
    def device_cap_flags(self) -> int:
        """Device capability flags (IBV_DEVICE_*)."""
        ...
    @property
    def max_sge(self) -> int:
        """Maximum number of SGEs per WR."""
        ...
    @property
    def max_sge_rd(self) -> int:
        """Maximum number of SGEs per RDMA WR."""
        ...
    @property
    def max_cq(self) -> int:
        """Maximum number of CQs."""
        ...
    @property
    def max_cqe(self) -> int:
        """Maximum number of CQEs per CQ."""
        ...
    @property
    def max_mr(self) -> int:
        """Maximum number of MRs."""
        ...
    @property
    def max_pd(self) -> int:
        """Maximum number of PDs."""
        ...
    @property
    def max_qp_rd_atom(self) -> int:
        """Maximum number of outstanding RDMA read/atomic per QP."""
        ...
    @property
    def max_ee_rd_atom(self) -> int:
        """Max RDMA read/atomic per EE context."""
        ...
    @property
    def max_res_rd_atom(self) -> int:
        """Max total RDMA read/atomic resources."""
        ...
    @property
    def max_qp_init_rd_atom(self) -> int:
        """Maximum initial value of RDMA read/atomic outstanding per QP."""
        ...
    @property
    def max_ee_init_rd_atom(self) -> int:
        """max_ee_init_rd_atom attribute."""
        ...
    @property
    def atomic_caps(self) -> int:
        """Atomic operations capability (IBV_ATOMIC_*)."""
        ...
    @property
    def max_ee(self) -> int:
        """Maximum number of EE contexts."""
        ...
    @property
    def max_rdd(self) -> int:
        """Maximum number of RD domains."""
        ...
    @property
    def max_mw(self) -> int:
        """Maximum number of MWs."""
        ...
    @property
    def max_raw_ipv6_qps(self) -> int:
        """max_raw_ipv6_qps attribute."""
        ...
    @property
    def max_raw_ethy_qp(self) -> int:
        """Max raw Ethernet QPs."""
        ...
    @property
    def max_mcast_grp(self) -> int:
        """Maximum number of multicast groups."""
        ...
    @property
    def max_mcast_qp_attach(self) -> int:
        """Maximum number of QPs per multicast group."""
        ...
    @property
    def max_ah(self) -> int:
        """Maximum number of AHs."""
        ...
    @property
    def max_fmr(self) -> int:
        """max_fmr attribute."""
        ...
    @property
    def max_map_per_fmr(self) -> int:
        """max_map_per_fmr attribute."""
        ...
    @property
    def max_srq(self) -> int:
        """Maximum number of SRQs."""
        ...
    @property
    def max_srq_wr(self) -> int:
        """Maximum number of WRs per SRQ."""
        ...
    @property
    def max_srq_sge(self) -> int:
        """Maximum number of SGEs per SRQ WR."""
        ...
    @property
    def max_pkeys(self) -> int:
        """Maximum number of P_Keys."""
        ...
    @property
    def local_ca_ack_delay(self) -> int:
        """Local CA ACK delay."""
        ...
    @property
    def phys_port_cnt(self) -> int:
        """Number of physical ports."""
        ...

    def __str__(self) -> str: ...

class QueryDeviceExInput(PyverbsObject):
    """Extensible input structure for ibv_query_device_ex."""

    def __init__(self, comp_mask: int) -> None: ...

class ODPCaps(PyverbsObject):
    """On-Demand Paging capabilities."""

    @property
    def general_caps(self) -> int:
        """General ODP capabilities bitmask (IBV_ODP_SUPPORT_*)."""
        ...
    @property
    def rc_odp_caps(self) -> int:
        """Per-transport ODP caps for RC."""
        ...
    @property
    def uc_odp_caps(self) -> int:
        """Per-transport ODP caps for UC."""
        ...
    @property
    def ud_odp_caps(self) -> int:
        """Per-transport ODP caps for UD."""
        ...
    @property
    def xrc_odp_caps(self) -> int:
        """ODP caps for XRC."""
        ...
    @xrc_odp_caps.setter
    def xrc_odp_caps(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class PCIAtomicCaps(PyverbsObject):
    """PCI atomic operation capabilities."""

    @property
    def fetch_add(self) -> int:
        """fetch_add attribute."""
        ...
    @property
    def swap(self) -> int:
        """swap attribute."""
        ...
    @property
    def compare_swap(self) -> int:
        """compare_swap attribute."""
        ...

class TSOCaps(PyverbsObject):
    """TCP Segmentation Offload capabilities."""

    @property
    def max_tso(self) -> int:
        """Maximum TSO payload size."""
        ...
    @property
    def supported_qpts(self) -> int:
        """QP types supporting TSO."""
        ...

class RSSCaps(PyverbsObject):
    """Receive Side Scaling capabilities."""

    @property
    def supported_qpts(self) -> int:
        """supported_qpts attribute."""
        ...
    @property
    def max_rwq_indirection_tables(self) -> int:
        """max_rwq_indirection_tables attribute."""
        ...
    @property
    def rx_hash_fields_mask(self) -> int:
        """rx_hash_fields_mask attribute."""
        ...
    @property
    def rx_hash_function(self) -> int:
        """rx_hash_function attribute."""
        ...
    @property
    def max_rwq_indirection_table_size(self) -> int:
        """max_rwq_indirection_table_size attribute."""
        ...

class PacketPacingCaps(PyverbsObject):
    """Packet pacing rate limit capabilities."""

    @property
    def qp_rate_limit_min(self) -> int:
        """qp_rate_limit_min attribute."""
        ...
    @property
    def qp_rate_limit_max(self) -> int:
        """qp_rate_limit_max attribute."""
        ...
    @property
    def supported_qpts(self) -> int:
        """supported_qpts attribute."""
        ...

class TMCaps(PyverbsObject):
    """Tag Matching capabilities for RDMA tag matching."""

    @property
    def max_rndv_hdr_size(self) -> int:
        """max_rndv_hdr_size attribute."""
        ...
    @property
    def max_num_tags(self) -> int:
        """max_num_tags attribute."""
        ...
    @property
    def flags(self) -> int:
        """Flags."""
        ...
    @property
    def max_ops(self) -> int:
        """max_ops attribute."""
        ...
    @property
    def max_sge(self) -> int:
        """max_sge attribute."""
        ...

class CQModerationCaps(PyverbsObject):
    """CQ moderation capabilities."""

    @property
    def max_cq_count(self) -> int:
        """Maximum CQ moderation count."""
        ...
    @property
    def max_cq_period(self) -> int:
        """Maximum CQ moderation period."""
        ...

class CompCntrCaps(PyverbsObject):
    """Completion counter capabilities."""

    @property
    def max_counters(self) -> int:
        """Maximum number of completion counters."""
        ...
    @property
    def max_value(self) -> int:
        """Maximum counter value."""
        ...
    @property
    def supported_qp_attach_ops(self) -> int:
        """Supported QP attach operations bitmask."""
        ...

class DeviceAttrEx(PyverbsObject):
    """Extended device attributes (ibv_device_attr_ex)."""

    @property
    def orig_attr(self) -> DeviceAttr:
        """Original (non-extended) device attributes."""
        ...
    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    @property
    def odp_caps(self) -> ODPCaps:
        """On-Demand Paging capabilities."""
        ...
    @property
    def completion_timestamp_mask(self) -> int:
        """Completion timestamp mask."""
        ...
    @property
    def hca_core_clock(self) -> int:
        """HCA core clock frequency in kHz."""
        ...
    @property
    def device_cap_flags_ex(self) -> int:
        """Extended device capability flags."""
        ...
    @property
    def tso_caps(self) -> TSOCaps:
        """TSO capabilities."""
        ...
    @property
    def pci_atomic_caps(self) -> PCIAtomicCaps:
        """PCI atomic capabilities."""
        ...
    @property
    def rss_caps(self) -> RSSCaps:
        """RSS capabilities."""
        ...
    @property
    def max_wq_type_rq(self) -> int:
        """Max WQ type RQ."""
        ...
    @property
    def packet_pacing_caps(self) -> PacketPacingCaps:
        """Packet pacing capabilities."""
        ...
    @property
    def raw_packet_caps(self) -> int:
        """Raw packet capabilities."""
        ...
    @property
    def tm_caps(self) -> TMCaps:
        """Tag matching capabilities."""
        ...
    @property
    def cq_mod_caps(self) -> CQModerationCaps:
        """CQ moderation capabilities."""
        ...
    @property
    def max_dm_size(self) -> int:
        """Maximum device memory size in bytes."""
        ...
    @property
    def phys_port_cnt_ex(self) -> int:
        """Extended physical port count."""
        ...

class AllocDmAttr(PyverbsObject):
    """Attributes for allocating device memory (DM)."""

    def __init__(self, length: int, log_align_req: int = 0, comp_mask: int = 0) -> None:
        """Create allocation attributes for device memory.

        Args:
            length: Length of the device memory in bytes.
            log_align_req: log2 of address alignment requirement.
            comp_mask: Compatibility mask.
        """
        ...
    @property
    def length(self) -> int:
        """Length in bytes."""
        ...
    @length.setter
    def length(self, val: int) -> None: ...
    @property
    def log_align_req(self) -> int:
        """Log2 of alignment requirement."""
        ...
    @log_align_req.setter
    def log_align_req(self, val: int) -> None: ...
    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...

class DM(PyverbsCM):
    """Device Memory (DM) — direct device memory allocation (ibv_dm)."""

    def __init__(self, context: Context, dm_attr: AllocDmAttr | None = None, *, handle: int | None = None) -> None:
        """Allocate device memory.

        Args:
            context: The device context to allocate memory on.
            dm_attr: Attributes defining the DM allocation.
            handle: If given, import an existing DM by kernel handle via ibv_import_dm.
        """
        ...
    def close(self) -> None:
        """Free the device memory. Imported DMs are not freed (kept for original owner)."""
        ...
    def unimport(self) -> None:
        """Unimport an imported DM."""
        ...
    def copy_to_dm(self, dm_offset: int, data: bytes, length: int) -> None:
        """Copy data to device memory.

        Args:
            dm_offset: Offset in the device memory.
            data: Source data buffer.
            length: Number of bytes to copy.
        """
        ...
    def copy_from_dm(self, dm_offset: int, length: int) -> bytes:
        """Copy data from device memory.

        Args:
            dm_offset: Offset in the device memory.
            length: Number of bytes to copy.

        Returns:
            bytes containing the copied data.
        """
        ...
    def export_dmabuf_fd(self) -> int:
        """Export a dmabuf file descriptor for this DM.

        Returns:
            File descriptor (int) for the dmabuf.
        """
        ...
    @property
    def handle(self) -> int:
        """DM handle."""
        ...

class PortAttr(PyverbsObject):
    """Port attributes (ibv_port_attr)."""

    @property
    def state(self) -> int:
        """Port state (IBV_PORT_*)."""
        ...
    @property
    def max_mtu(self) -> int:
        """Maximum MTU (IBV_MTU_*)."""
        ...
    @property
    def active_mtu(self) -> int:
        """Active MTU."""
        ...
    @property
    def gid_tbl_len(self) -> int:
        """GID table length."""
        ...
    @property
    def port_cap_flags(self) -> int:
        """Port capability flags (IBV_PORT_*)."""
        ...
    @property
    def max_msg_sz(self) -> int:
        """Maximum message size."""
        ...
    @property
    def bad_pkey_cntr(self) -> int:
        """Bad P_Key counter."""
        ...
    @property
    def qkey_viol_cntr(self) -> int:
        """Q_Key violation counter."""
        ...
    @property
    def pkey_tbl_len(self) -> int:
        """P_Key table length."""
        ...
    @property
    def lid(self) -> int:
        """Local ID."""
        ...
    @property
    def sm_lid(self) -> int:
        """Subnet Manager LID."""
        ...
    @property
    def lmc(self) -> int:
        """Local Mask Count."""
        ...
    @property
    def max_vl_num(self) -> int:
        """Maximum number of Virtual Lanes."""
        ...
    @property
    def sm_sl(self) -> int:
        """Subnet Manager Service Level."""
        ...
    @property
    def subnet_timeout(self) -> int:
        """Subnet timeout."""
        ...
    @property
    def init_type_reply(self) -> int:
        """Init type reply."""
        ...
    @property
    def active_width(self) -> int:
        """Active link width."""
        ...
    @property
    def active_speed(self) -> int:
        """Active link speed."""
        ...
    @property
    def phys_state(self) -> int:
        """Physical state."""
        ...
    @property
    def link_layer(self) -> int:
        """Link layer type (IBV_LINK_LAYER_*)."""
        ...
    @property
    def flags(self) -> int:
        """Flags."""
        ...
    @property
    def port_cap_flags2(self) -> int:
        """Extended port capability flags."""
        ...
    @property
    def active_speed_ex(self) -> int:
        """Extended active speed."""
        ...

    def __str__(self) -> str: ...

class GIDEntry(PyverbsObject):
    """GID table entry (ibv_gid_entry)."""

    def __init__(
        self,
        subnet_prefix: int = 0,
        interface_id: int = 0,
        gid_index: int = 0,
        port_num: int = 0,
        gid_type: int = 0,
        ndev_ifindex: int = 0,
    ) -> None: ...
    @property
    def gid_subnet_prefix(self) -> int:
        """GID subnet prefix."""
        ...
    @property
    def gid_interface_id(self) -> int:
        """GID interface ID."""
        ...
    @property
    def gid_index(self) -> int:
        """Index in the GID table."""
        ...
    @property
    def port_num(self) -> int:
        """Port number this GID belongs to."""
        ...
    @property
    def gid_type(self) -> int:
        """GID type (IBV_GID_TYPE_*)."""
        ...
    @property
    def ndev_ifindex(self) -> int:
        """Network device interface index."""
        ...
    def gid_str(self) -> str:
        """Get string representation of the GID.

        Returns:
            GID in standard colon-separated hex format.
        """
        ...

    def __str__(self) -> str: ...

class AsyncEvent(PyverbsObject):
    """Asynchronous event (ibv_async_event)."""

    def __init__(self, event_type: int = 0) -> None: ...
    def ack(self) -> None:
        """Acknowledge the event. Must be called after handling."""
        ...
    @property
    def event_type(self) -> int:
        """Event type (IBV_EVENT_*)."""
        ...

    def __str__(self) -> str: ...

class FdArr(PyverbsObject):
    """Represents ibv_fd_arr struct — a file descriptor array."""

    def __init__(self, arr: list[int] | None = None, count: int = 0) -> None: ...
    def close(self) -> None:
        """Close and release resources."""
        ...
    @property
    def arr(self) -> list[int]:
        """List of file descriptors."""
        ...
    @property
    def count(self) -> int:
        """Number of file descriptors."""
        ...

    def __str__(self) -> str: ...

# ── Module-level utility functions ──

def get_device_list() -> list[Device]:
    """Get the list of IB devices on the current node.

    Returns:
        List of Device objects with name, node type, transport type, guid, and index.
    """
    ...

def rdma_get_devices() -> list[Device]:
    """Get RDMA devices via the RDMA CM API.

    Returns:
        List of Device objects.
    """
    ...

def translate_node_type(node_type: int) -> str:
    """Translate node type enum to string.

    Args:
        node_type: Node type enum value (``IBV_NODE_*``).

    Returns:
        String such as ``'CA'``, ``'Switch'``, ``'Router'``.
    """
    ...

def translate_transport_type(transport_type: int) -> str:
    """Translate transport type enum to string.

    Args:
        transport_type: Transport type enum value.

    Returns:
        String such as ``'IB'``, ``'IWARP'``.
    """
    ...

def guid_to_hex(node_guid: int) -> str:
    """Convert a node GUID to a colon-separated hex string.

    Args:
        node_guid: 64-bit node GUID value.

    Returns:
        Hex string in ``'xx:xx:xx:xx:xx:xx:xx:xx'`` format.
    """
    ...

def guid_format(num: int) -> str:
    """Get GUID representation with endianness change.

    Args:
        num: 64-bit GUID value.

    Returns:
        Formatted GUID string.
    """
    ...

def port_state_to_str(port_state: int) -> str:
    """Translate port state enum to string.

    Args:
        port_state: Port state enum value (``IBV_PORT_*``).

    Returns:
        String such as ``'ACTIVE'``, ``'INIT'``, ``'DOWN'``.
    """
    ...

def translate_mtu(mtu: int) -> str:
    """Translate MTU enum to string.

    Args:
        mtu: MTU enum value (``IBV_MTU_*``).

    Returns:
        String such as ``'256'``, ``'512'``, ``'1024'``, ``'2048'``, ``'4096'``.
    """
    ...

def translate_link_layer(ll: int) -> str:
    """Translate link layer enum to string.

    Args:
        ll: Link layer enum value (``IBV_LINK_LAYER_*``).

    Returns:
        String such as ``'InfiniBand'``, ``'Ethernet'``.
    """
    ...

def translate_port_cap_flags(flags: int) -> str:
    """Translate port capability flags to a comma-separated string.

    Args:
        flags: Port capability flags bitmask (``IBV_PORT_CAP_*``).

    Returns:
        Comma-separated capability names.
    """
    ...

def translate_port_cap_flags2(flags: int) -> str:
    """Translate extended port capability flags to a comma-separated string.

    Args:
        flags: Extended port capability flags bitmask.

    Returns:
        Comma-separated capability names.
    """
    ...

def translate_device_caps(flags: int) -> str:
    """Translate device capability flags to a comma-separated string.

    Args:
        flags: Device capability flags bitmask.

    Returns:
        Comma-separated capability names.
    """
    ...

def translate_event_type(event_type: int) -> str:
    """Translate async event type enum to string.

    Args:
        event_type: Event type enum value (``IBV_EVENT_*``).

    Returns:
        Human-readable event name string.
    """
    ...

def translate_gid_type(gid_type: int) -> str:
    """Translate GID type enum to string.

    Args:
        gid_type: GID type enum value (``IBV_GID_TYPE_*``).

    Returns:
        String such as ``'IB'``, ``'RoCE'``, ``'RoCEv2'``.
    """
    ...

def phys_state_to_str(phys: int) -> str:
    """Translate physical state enum to string.

    Args:
        phys: Physical state enum value.

    Returns:
        String such as ``'Sleep'``, ``'Polling'``, ``'Disabled'``.
    """
    ...

def width_to_str(width: int) -> str:
    """Translate link width enum to string.

    Args:
        width: Link width enum value.

    Returns:
        String such as ``'1x'``, ``'4x'``, ``'8x'``, ``'12x'``.
    """
    ...

def speed_to_str(active_speed: int, active_speed_ex: int) -> str:
    """Translate link speed to string.

    Args:
        active_speed: Legacy active speed enum value.
        active_speed_ex: Extended active speed enum value (takes precedence).

    Returns:
        String such as ``'2.5 Gbps'``, ``'10 Gbps'``, ``'100 Gbps'``.
    """
    ...

def str_from_flags(flags: int, dictionary: dict[int, str]) -> str:
    """Convert a flags bitmask to a human-readable multi-line string.

    Args:
        flags: Bitmask of flags.
        dictionary: Mapping from flag bit to flag name string.

    Returns:
        Newline-separated string of matched flag names.
    """
    ...

    def __str__(self) -> str: ...
