"""
Type stubs for pyverbs.providers.mlx5.mlx5dv — MLX5 Direct Verbs API.

Provides MLX5 provider-specific extensions including DevX commands,
DC (Dynamic Connection) QPs, VAR/PP/UAR resources, WQE segments,
UMEM, CQE64, MSI vectors, EQs, and command completions.
"""

from pyverbs.addr import AH
from pyverbs.base import PyverbsCM, PyverbsObject
from pyverbs.cq import CQEX, CqInitAttrEx
from pyverbs.device import DM, Context, FdArr
from pyverbs.providers.mlx5.mlx5dv_crypto import Mlx5CryptoAttr, Mlx5CryptoLoginAttr
from pyverbs.providers.mlx5.mlx5dv_mkey import Mlx5Mkey, Mlx5MkeyConfAttr, Mlx5MrInterleaved, Mlx5SigBlockAttr
from pyverbs.providers.mlx5.mlx5dv_sched import Mlx5dvSchedLeaf
from pyverbs.qp import QP, QPEx, QPInitAttrEx
from pyverbs.wr import SGE

# --- Attribute classes ---

class Mlx5DVContextAttr(PyverbsObject):
    """MLX5 device open attributes (mlx5dv_context_attr).

    Used to open an mlx5 device with provider-specific options.
    """

    def __init__(self, flags: int = 0, comp_mask: int = 0, fds: FdArr | None = None) -> None:
        """Initialize MLX5 device open attributes.

        Args:
            flags: Device open flags. Default is 0.
            comp_mask: Compatibility mask. Default is 0.
            fds: Optional FdArr for file descriptors. Default is None.
        """
        ...

    @property
    def flags(self) -> int:
        """Device open flags."""
        ...
    @flags.setter
    def flags(self, val: int) -> None: ...
    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class Mlx5DVContext(PyverbsObject):
    """MLX5 device context attributes (mlx5dv_context).

    Contains mlx5-specific capabilities reported by mlx5dv_query_device
    including CQE compression, SW parsing, tunnel offloads, etc.
    """

    @property
    def version(self) -> int:
        """The device version."""
        ...

    @property
    def flags(self) -> int:
        """Device flags."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask indicating which fields are valid."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    @property
    def cqe_comp_caps(self) -> int:
        """CQE compression capabilities."""
        ...

    @property
    def sw_parsing_caps(self) -> int:
        """SW parsing offload capabilities."""
        ...

    @property
    def striding_rq_caps(self) -> int:
        """Striding RQ capabilities."""
        ...

    @property
    def tunnel_offload_caps(self) -> int:
        """Tunnel offload capabilities."""
        ...

    @property
    def max_dynamic_bfregs(self) -> int:
        """Maximum number of dynamic blue flame registers."""
        ...

    @property
    def max_clock_info_update_nsec(self) -> int:
        """Maximum clock info update interval in nanoseconds."""
        ...

    @property
    def flow_action_flags(self) -> int:
        """Supported flow action flags."""
        ...

    @property
    def dc_odp_caps(self) -> int:
        """DC on-demand paging capabilities."""
        ...

    @property
    def crypto_caps(self) -> int:
        """Crypto offload capabilities."""
        ...

    @property
    def num_lag_ports(self) -> int:
        """Number of LAG ports."""
        ...

    @property
    def dci_streams_caps(self) -> int:
        """DCI streams capabilities."""
        ...

    @property
    def max_wr_memcpy_length(self) -> int:
        """Maximum WR memcpy length."""
        ...

    @property
    def max_dc_rd_atom(self) -> int:
        """Maximum DC read atomic."""
        ...

    @property
    def max_dc_init_rd_atom(self) -> int:
        """Maximum DC init read atomic."""
        ...

    @property
    def ooo_recv_wrs_caps(self) -> int:
        """Out-of-order receive WRs capabilities."""
        ...

    def __str__(self) -> str: ...

class Mlx5DVPortAttr(PyverbsObject):
    """MLX5-specific port attributes (mlx5dv_port).

    Exposes vport, steering ICM, and RegC0 information.
    """

    def __init__(self) -> None: ...
    @property
    def flags(self) -> int:
        """Flags."""
        ...
    @property
    def vport(self) -> int:
        """Vport number."""
        ...
    @property
    def vport_vhca_id(self) -> int:
        """Vport VHCA ID."""
        ...
    @property
    def esw_owner_vhca_id(self) -> int:
        """E-switch owner VHCA ID."""
        ...
    @property
    def vport_steering_icm_rx(self) -> int:
        """Vport steering ICM RX address."""
        ...
    @property
    def vport_steering_icm_tx(self) -> int:
        """Vport steering ICM TX address."""
        ...
    @property
    def reg_c0_value(self) -> int:
        """Register C0 value."""
        ...
    @property
    def reg_c0_mask(self) -> int:
        """Register C0 mask."""
        ...

    def __str__(self) -> str: ...

class Mlx5DCIStreamInitAttr(PyverbsObject):
    """DCI stream initialization attributes.

    Defines concurrent and errored stream channel counts for DC QP creation.
    """

    def __init__(self, log_num_concurent: int = 0, log_num_errored: int = 0) -> None:
        """Initialize DCI stream attributes.

        Args:
            log_num_concurent: Log2 number of DCI stream channels. Default is 0.
            log_num_errored: Log2 number of DCI error stream channels before
                moving DCI to error state. Default is 0.
        """
        ...

    @property
    def log_num_concurent(self) -> int:
        """Log2 number of DCI stream channels."""
        ...
    @log_num_concurent.setter
    def log_num_concurent(self, val: int) -> None: ...
    @property
    def log_num_errored(self) -> int:
        """Log2 number of DCI error stream channels."""
        ...
    @log_num_errored.setter
    def log_num_errored(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class Mlx5DVDCInitAttr(PyverbsObject):
    """DC (Dynamic Connection) initialization attributes (mlx5dv_dc_init_attr).

    Defines DC type (DCI/DCT), access key, and stream configuration.
    """

    def __init__(
        self, dc_type: int = ..., dct_access_key: int = 0, dci_streams: Mlx5DCIStreamInitAttr | None = None
    ) -> None:
        """Initialize DC attributes.

        Args:
            dc_type: Which DC QP to create (MLX5DV_DCTYPE_DCI or
                MLX5DV_DCTYPE_DCT). Default is DCI.
            dct_access_key: Access key for DCT. Default is 0.
            dci_streams: Optional Mlx5DCIStreamInitAttr for DCI streams.
        """
        ...

    @property
    def dc_type(self) -> int:
        """DC type (DCI or DCT)."""
        ...
    @dc_type.setter
    def dc_type(self, val: int) -> None: ...
    @property
    def dct_access_key(self) -> int:
        """DCT access key."""
        ...
    @dct_access_key.setter
    def dct_access_key(self, val: int) -> None: ...
    @property
    def dci_streams(self) -> int:
        """DCI streams configuration (mlx5dv_dci_streams C struct)."""
        ...
    @dci_streams.setter
    def dci_streams(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class Mlx5DVQPInitAttr(PyverbsObject):
    """MLX5 QP initialization attributes (mlx5dv_qp_init_attr).

    Provider-specific attributes for mlx5 QP creation including
    DC, send ops flags, and create flags.
    """

    def __init__(
        self,
        comp_mask: int = 0,
        create_flags: int = 0,
        send_ops_flags: int = 0,
        dc_init_attr: Mlx5DVDCInitAttr | None = None,
        dci_streams: Mlx5DCIStreamInitAttr | None = None,
    ) -> None:
        """Initialize MLX5 QP attributes.

        Args:
            comp_mask: Bitmask specifying which fields are valid.
            create_flags: Bitwise OR of mlx5dv_qp_create_flags.
            send_ops_flags: Bitwise OR of mlx5dv_qp_create_send_ops_flags.
            dc_init_attr: Optional Mlx5DVDCInitAttr for DC QP creation.
            dci_streams: Optional Mlx5DCIStreamInitAttr (used when
                comp_mask includes MLX5DV_QP_INIT_ATTR_MASK_DCI_STREAMS).
        """
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    @property
    def create_flags(self) -> int:
        """Creation flags."""
        ...
    @create_flags.setter
    def create_flags(self, val: int) -> None: ...
    @property
    def send_ops_flags(self) -> int:
        """Send operations flags."""
        ...
    @send_ops_flags.setter
    def send_ops_flags(self, val: int) -> None: ...
    @property
    def dc_type(self) -> int:
        """DC type (DCI or DCT)."""
        ...
    @dc_type.setter
    def dc_type(self, val: int) -> None: ...
    @property
    def dct_access_key(self) -> int:
        """DCT access key."""
        ...
    @dct_access_key.setter
    def dct_access_key(self, val: int) -> None: ...
    @property
    def dci_streams(self) -> int:
        """DCI streams configuration (mlx5dv_dci_streams C struct)."""
        ...
    @dci_streams.setter
    def dci_streams(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class Mlx5DVCQInitAttr(PyverbsObject):
    """MLX5 CQ initialization attributes (mlx5dv_cq_init_attr).

    Provider-specific attributes for mlx5 CQ creation including
    CQE compression format, flags, and CQE size.
    """

    def __init__(self, comp_mask: int = 0, cqe_comp_res_format: int = 0, flags: int = 0, cqe_size: int = 0) -> None:
        """Initialize MLX5 CQ attributes.

        Args:
            comp_mask: Bitmask specifying which fields are valid
                (use mlx5dv_cq_init_attr_mask enum).
            cqe_comp_res_format: CQE compression response format
                (use mlx5dv_cqe_comp_res_format enum).
            flags: Bitwise OR of mlx5dv_cq_init_attr_flags.
            cqe_size: CQE size in bytes (64 or 128). Valid when
                MLX5DV_CQ_INIT_ATTR_MASK_CQE_SIZE is set in comp_mask.
        """
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...
    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    @property
    def cqe_comp_res_format(self) -> int:
        """CQE compression response format."""
        ...
    @cqe_comp_res_format.setter
    def cqe_comp_res_format(self, val: int) -> None: ...
    @property
    def flags(self) -> int:
        """Flags."""
        ...
    @flags.setter
    def flags(self, val: int) -> None: ...
    @property
    def cqe_size(self) -> int:
        """CQE size in bytes."""
        ...
    @cqe_size.setter
    def cqe_size(self, val: int) -> None:
        ...

        # --- Main resource classes ---

    def __str__(self) -> str: ...

class Mlx5QP(QPEx):
    """MLX5 extended QP with provider-specific features.

    Supports DC QPs, DevX, signature, crypto, and advanced WQE operations
    like memcpy, MR interleaved, MR list, and Mkey configuration.
    """

    def __init__(self, context: Context, init_attr: QPInitAttrEx, dv_init_attr: Mlx5DVQPInitAttr | None = None) -> None:
        """Create an MLX5 QP.

        Args:
            context: A Context object.
            init_attr: A QPInitAttrEx with base QP attributes.
            dv_init_attr: Optional Mlx5DVQPInitAttr for MLX5-specific features.

        Raises:
            PyverbsRDMAErrno: If QP creation fails.
        """
        ...

    def wr_set_dc_addr(self, ah: AH, remote_dctn: int, remote_dc_key: int) -> None:
        """Attach DC info to the last work request.

        Args:
            ah: An AH (Address Handle) to the target DCT.
            remote_dctn: The remote DCT number.
            remote_dc_key: The remote DC key.
        """
        ...

    def wr_raw_wqe(self, wqe: Wqe) -> None:
        """Post a raw WQE (Work Queue Element).

        Args:
            wqe: A Wqe object containing the work queue element.
        """
        ...

    def wr_mr_interleaved(
        self, mkey: Mlx5Mkey, access_flags: int, repeat_count: int, mr_interleaved_lst: list[Mlx5MrInterleaved]
    ) -> None:
        """Register an interleaved memory layout via an indirect mkey.

        Args:
            mkey: A Mlx5Mkey instance.
            access_flags: The mkey access flags.
            repeat_count: Number of times to repeat the interleaved layout.
            mr_interleaved_lst: List of Mlx5MrInterleaved objects.
        """
        ...

    def wr_mr_list(self, mkey: Mlx5Mkey, access_flags: int, sge_list: list[SGE]) -> None:
        """Register a memory layout based on a list of SGEs.

        Args:
            mkey: A Mlx5Mkey instance.
            access_flags: The mkey access flags.
            sge_list: List of SGE objects.
        """
        ...

    def wr_mkey_configure(self, mkey: Mlx5Mkey, num_setters: int, mkey_config: Mlx5MkeyConfAttr) -> None:
        """Create a WR to configure an Mkey.

        Args:
            mkey: A Mlx5Mkey instance to configure.
            num_setters: Number of setter calls that follow this WR.
            mkey_config: A Mlx5MkeyConfAttr with configuration attributes.
        """
        ...

    def wr_set_mkey_access_flags(self, access_flags: int) -> None:
        """Set memory protection attributes for an Mkey.

        Args:
            access_flags: The mkey access flags.
        """
        ...

    def wr_set_mkey_layout_list(self, sge_list: list[SGE]) -> None:
        """Set Mkey memory layout based on SGE list.

        Args:
            sge_list: List of SGE objects.
        """
        ...

    def wr_set_mkey_layout_interleaved(self, repeat_count: int, mr_interleaved_lst: list[Mlx5MrInterleaved]) -> None:
        """Set interleaved memory layout for an Mkey.

        Args:
            repeat_count: Number of times to repeat the layout.
            mr_interleaved_lst: List of Mlx5MrInterleaved objects.
        """
        ...

    def wr_set_mkey_crypto(self, attr: Mlx5CryptoAttr) -> None:
        """Configure an MKey for crypto operation.

        Args:
            attr: A Mlx5CryptoAttr with crypto attributes to set.
        """
        ...

    def wr_set_mkey_sig_block(self, block_attr: Mlx5SigBlockAttr) -> None:
        """Configure an MKey for block signature (data integrity).

        Args:
            block_attr: A Mlx5SigBlockAttr with signature attributes.
        """
        ...

    def wr_memcpy(self, dest_lkey: int, dest_addr: int, src_lkey: int, src_addr: int, length: int) -> None:
        """Copy memory on PCI bus using DMA.

        Args:
            dest_lkey: Local key of the destination mkey.
            dest_addr: Memory address to copy data to.
            src_lkey: Local key of the source mkey.
            src_addr: Memory address to copy data from.
            length: Length of data to copy.
        """
        ...

    def cancel_posted_send_wrs(self, wr_id: int) -> int:
        """Cancel pending send WRs with the given wr_id.

        Only works on QPs in SQD state.

        Args:
            wr_id: The WR ID to cancel.

        Returns:
            Number of work requests that were canceled.

        Raises:
            PyverbsRDMAError: If cancellation fails.
        """
        ...

    def wr_set_dc_addr_stream(self, ah: AH, remote_dctn: int, remote_dc_key: int, stream_id: int) -> None:
        """Attach DC info to the last WR with a stream channel ID.

        Args:
            ah: An AH to the target DCT.
            remote_dctn: The remote DCT number.
            remote_dc_key: The remote DC key.
            stream_id: DCI stream channel ID.
        """
        ...

    @staticmethod
    def query_lag_port(qp: QP) -> tuple[int, int]:
        """Query the LAG port for a QP.

        Args:
            qp: The QP to query.

        Returns:
            Tuple of (desired_port, active_port_num).

        Raises:
            PyverbsRDMAError: If the query fails.
        """
        ...

    @staticmethod
    def modify_lag_port(qp: QP, port_num: int) -> None:
        """Modify the LAG port for a QP.

        Args:
            qp: The QP to modify.
            port_num: The desired port for LAG traffic.

        Raises:
            PyverbsRDMAError: If modification fails.
        """
        ...

    @staticmethod
    def modify_qp_sched_elem(
        qp: QP, req_sched_leaf: Mlx5dvSchedLeaf | None = None, resp_sched_leaf: Mlx5dvSchedLeaf | None = None
    ) -> None:
        """Connect a QP with scheduling elements.

        Args:
            qp: The QP to connect.
            req_sched_leaf: Mlx5dvSchedLeaf for the send queue.
            resp_sched_leaf: Mlx5dvSchedLeaf for the recv queue.

        Raises:
            PyverbsRDMAError: If modification fails.
        """
        ...

    @staticmethod
    def modify_udp_sport(qp: QP, udp_sport: int) -> None:
        """Modify the UDP source port of a QP.

        Args:
            qp: A QP in RTS state.
            udp_sport: The desired UDP source port.

        Raises:
            PyverbsRDMAError: If modification fails.
        """
        ...

    @staticmethod
    def map_ah_to_qp(ah: AH, qp_num: int) -> None:
        """Map address handle destination to QP-extracted path info.

        Args:
            ah: The target's address handle.
            qp_num: The traffic initiator QP number.

        Raises:
            PyverbsRDMAError: If mapping fails.
        """
        ...

    @staticmethod
    def modify_dci_stream_channel_id(qp: QP, stream_id: int) -> None:
        """Reset an errored stream_id in the HW DCI context.

        Args:
            qp: A DCI QP in RTS state.
            stream_id: The stream_id to reset.

        Raises:
            PyverbsRDMAError: If reset fails.
        """
        ...

class Mlx5CQ(CQEX):
    """MLX5 extended CQ with provider-specific features.

    Creates a CQ with MLX5-specific attributes like CQE compression
    and CQE size configuration.
    """

    def __init__(self, context: Context, init_attr: CqInitAttrEx, dv_init_attr: Mlx5DVCQInitAttr | None = None) -> None:
        """Create an MLX5 CQ.

        Args:
            context: A Mlx5Context object.
            init_attr: A CqInitAttrEx with base CQ attributes.
            dv_init_attr: Optional Mlx5DVCQInitAttr for MLX5-specific features.

        Raises:
            PyverbsRDMAErrno: If CQ creation fails.
        """
        ...

    def __str__(self) -> str: ...

class Mlx5VAR(PyverbsObject):
    """Variable Address Region (mlx5dv_var) for direct hardware access.

    Allocates a VAR for doorbell ringing or other direct hardware operations.
    Supports export/import for cross-process sharing.
    """

    def __init__(self, context: Context, flags: int = 0) -> None:
        """Allocate a VAR.

        Args:
            context: A Context object.
            flags: VAR allocation flags. Default is 0.

        Raises:
            PyverbsRDMAErrno: If allocation fails.
        """
        ...

    def free(self) -> None:
        """Free the allocated VAR."""
        ...

    def unimport_var(self) -> None:
        """Release an imported VAR without freeing the underlying object."""
        ...

    @staticmethod
    def get_export_size() -> int:
        """Get the buffer size required for VAR export/import.

        Returns:
            Export buffer size in bytes.
        """
        ...

    def export(self) -> bytes:
        """Export the VAR for cross-process sharing.

        Returns:
            Bytes containing the exported VAR data.

        Raises:
            PyverbsRDMAError: If export fails.
        """
        ...

    @staticmethod
    def import_var(context: Context, data: bytes) -> Mlx5VAR:
        """Import a VAR from an exported data buffer.

        Args:
            context: Device context for the import.
            data: Bytes buffer from Mlx5VAR.export().

        Returns:
            An Mlx5VAR representing the imported VAR.

        Raises:
            PyverbsRDMAErrno: If import fails.
        """
        ...

    @property
    def page_id(self) -> int:
        """The VAR page ID."""
        ...

    @property
    def length(self) -> int:
        """The VAR length."""
        ...

    @property
    def mmap_off(self) -> int:
        """The mmap offset."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...

    def __str__(self) -> str: ...

class Mlx5PP(PyverbsObject):
    """Padding Pattern (mlx5dv_pp) for WQE construction."""

    def __init__(self, context: Context, pp_context: bytes | list[int], flags: int = 0) -> None:
        """Allocate a Padding Pattern entry.

        Args:
            context: A DevX context.
            pp_context: Packet pacing context bytes per device specs.
            flags: Allocation flags. Default is 0.

        Raises:
            PyverbsRDMAErrno: If allocation fails.
        """
        ...

    @property
    def index(self) -> int:
        """The PP entry index."""
        ...

class Mlx5UAR(PyverbsObject):
    """User Access Region (mlx5dv_devx_uar) for doorbell ringing.

    Allocates a UAR for DevX operations. Supports dmabuf FD export.
    """

    def __init__(self, context: Context, flags: int = 0) -> None:
        """Allocate a UAR.

        Args:
            context: A Context object.
            flags: UAR allocation flags. Default is 0.

        Raises:
            PyverbsRDMAErrno: If allocation fails.
        """
        ...

    def export_dmabuf_fd(self) -> int:
        """Export a dmabuf FD for this UAR object.

        Returns:
            A file descriptor for the dmabuf.

        Raises:
            PyverbsRDMAErrno: If export fails.
        """
        ...

    @property
    def reg_addr(self) -> int:
        """The register address."""
        ...

    @property
    def base_addr(self) -> int:
        """The base address."""
        ...

    @property
    def page_id(self) -> int:
        """The page ID."""
        ...

    @property
    def mmap_off(self) -> int:
        """The mmap offset."""
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask."""
        ...

    @property
    def uar(self) -> int:
        """The UAR pointer as integer."""
        ...

    def __str__(self) -> str: ...

class Mlx5DmOpAddr(PyverbsCM):
    """DM operation address (mlx5dv_dm_map_op_addr) for device memory access.

    Wraps the mapped operation address of a DM for direct read/write.
    """

    def __init__(self, dm: DM, op: int = 0) -> None:
        """Get the DM operation address.

        Args:
            dm: A DM (Device Memory) instance.
            op: DM operation type. Default is 0.

        Raises:
            PyverbsRDMAErrno: If mapping fails.
        """
        ...

    def unmap(self, length: int) -> None:
        """Unmap the DM operation address.

        Args:
            length: Length of the mapped region to unmap.
        """
        ...

    def write(self, data: bytes) -> None:
        """Write data to the DM operation address.

        Args:
            data: Bytes of data to write. Length must be a power of two, up to 8 bytes.
        """
        ...

    def read(self, length: int) -> bytes:
        """Read data from the DM operation address.

        Args:
            length: Number of bytes to read. Must be a power of two, up to 8 bytes.

        Returns:
            The read data as bytes.
        """
        ...

    @property
    def addr(self) -> int:
        """The mapped address as integer."""
        ...

# --- WQE segments ---

class WqeSeg(PyverbsCM):
    """Abstract base class for WQE segments.

    Each WQE segment (control, data, etc.) inherits from this class.
    """

    @staticmethod
    def sizeof() -> int:
        """Return the segment size in bytes.

        Returns:
            Size of one WQE segment in bytes.
        """
        ...

    def _copy_to_buffer(self, addr: int) -> None:
        """Copy segment data to the given buffer address."""
        ...

class WqeCtrlSeg(WqeSeg):
    """WQE control segment (mlx5_wqe_ctrl_seg).

    Contains opcode, QP number, signature, and other control fields.
    """

    def __init__(
        self,
        pi: int = 0,
        opcode: int = 0,
        opmod: int = 0,
        qp_num: int = 0,
        fm_ce_se: int = 0,
        ds: int = 0,
        signature: int = 0,
        imm: int = 0,
    ) -> None:
        """Create a WQE control segment.

        Args:
            pi: Post index.
            opcode: Operation opcode.
            opmod: Operation modifier.
            qp_num: QP number.
            fm_ce_se: Fence, CE, SE flags.
            ds: Data segment size in octawords.
            signature: Signature value.
            imm: Immediate data.
        """
        ...

    def set_ctrl_seg(
        self, pi: int, opcode: int, opmod: int, qp_num: int, fm_ce_se: int, ds: int, signature: int, imm: int
    ) -> None:
        """Set control segment fields.

        Args:
            pi: Post index.
            opcode: Operation opcode.
            opmod: Operation modifier.
            qp_num: QP number.
            fm_ce_se: Fence, CE, SE flags.
            ds: Data segment size in octawords.
            signature: Signature value.
            imm: Immediate data.
        """
        ...

    @staticmethod
    def sizeof() -> int:
        """Return the control segment size in bytes.

        Returns:
            Size of ``mlx5_wqe_ctrl_seg`` in bytes.
        """
        ...
    @property
    def addr(self) -> int:
        """The segment address."""
        ...

    @property
    def opmod_idx_opcode(self) -> int:
        """Opcode modifier, index, and opcode."""
        ...
    @opmod_idx_opcode.setter
    def opmod_idx_opcode(self, val: int) -> None: ...
    @property
    def qpn_ds(self) -> int:
        """QP number and data segment size."""
        ...
    @qpn_ds.setter
    def qpn_ds(self, val: int) -> None: ...
    @property
    def signature(self) -> int:
        """Signature value."""
        ...
    @signature.setter
    def signature(self, val: int) -> None: ...
    @property
    def fm_ce_se(self) -> int:
        """Fence, CE, and SE flags."""
        ...
    @fm_ce_se.setter
    def fm_ce_se(self, val: int) -> None: ...
    @property
    def imm(self) -> int:
        """Immediate data."""
        ...
    @imm.setter
    def imm(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class WqeDataSeg(WqeSeg):
    """WQE data segment (mlx5_wqe_data_seg).

    Contains byte count, lkey, and address for a data buffer.
    """

    def __init__(self, length: int = 0, lkey: int = 0, addr: int = 0) -> None:
        """Create a WQE data segment.

        Args:
            length: Data length in bytes.
            lkey: Local key for the memory region.
            addr: Memory address.
        """
        ...

    def set_data_seg(self, length: int, lkey: int, addr: int) -> None:
        """Set data segment fields.

        Args:
            length: Data length in bytes.
            lkey: Local key for the memory region.
            addr: Memory address.
        """
        ...

    @staticmethod
    def sizeof() -> int:
        """Return the data segment size in bytes.

        Returns:
            Size of ``mlx5_wqe_data_seg`` in bytes.
        """
        ...

    @property
    def byte_count(self) -> int:
        """Data length in bytes."""
        ...
    @byte_count.setter
    def byte_count(self, val: int) -> None: ...
    @property
    def lkey(self) -> int:
        """Local key."""
        ...
    @lkey.setter
    def lkey(self, val: int) -> None: ...
    @property
    def addr(self) -> int:
        """Memory address."""
        ...
    @addr.setter
    def addr(self, val: int) -> None: ...
    def __str__(self) -> str: ...

class Wqe(PyverbsCM):
    """Raw WQE (Work Queue Element) for direct posting.

    Chains one or more WQE segments (control, data) into a single WQE
    that can be posted directly to a QP.
    """

    def __init__(self, segments: list[WqeSeg], addr: int = 0) -> None:
        """Create a WQE.

        Args:
            segments: List of WqeSeg instances or PRM-format bytes.
            addr: Optional user address to write the WQE on. If not
                provided, memory is allocated automatically.
        """
        ...

    @property
    def address(self) -> int:
        """The WQE buffer address as integer."""
        ...

    # --- UMEM ---

    def __str__(self) -> str: ...

class Mlx5UMEM(PyverbsCM):
    """User Memory (mlx5dv_devx_umem) for DevX operations.

    Registers user memory for use with DevX commands. Supports
    export/import for cross-process sharing.
    """

    def __init__(
        self,
        context: Context,
        size: int,
        addr: int | None = None,
        alignment: int = 64,
        access: int = 0,
        pgsz_bitmap: int = 0,
        comp_mask: int = 0,
        dmabuf_fd: int = 0,
    ) -> None:
        """Register user memory for DevX.

        Args:
            context: RDMA device context.
            size: Size of the buffer.
            addr: Optional memory start address. If None, memory is
                allocated internally with the given alignment.
            alignment: Alignment for internally allocated buffer. Default 64.
            access: Memory protection attributes. Default is 0.
            pgsz_bitmap: Required page sizes. Default is 0.
            comp_mask: Compatibility mask. Default is 0.
            dmabuf_fd: FD of a dmabuf. Default is 0.

        Raises:
            PyverbsRDMAErrno: If registration fails.
        """
        ...

    def dereg(self) -> None:
        """Deregister the UMEM."""
        ...

    def unimport_umem(self) -> None:
        """Release an imported UMEM without deregistering."""
        ...

    def export(self) -> bytes:
        """Export UMEM for cross-process sharing.

        Returns:
            Bytes containing the exported UMEM data.

        Raises:
            PyverbsRDMAError: If export fails.
        """
        ...

    @staticmethod
    def import_umem(context: Context, data: bytes) -> Mlx5UMEM:
        """Import a UMEM from an exported data buffer.

        Args:
            context: Device context for the import.
            data: Bytes from Mlx5UMEM.export().

        Returns:
            An Mlx5UMEM representing the imported UMEM.

        Raises:
            PyverbsRDMAErrno: If import fails.
        """
        ...

    @staticmethod
    def get_export_size() -> int:
        """Get the buffer size required for UMEM export/import.

        Returns:
            Export buffer size in bytes.
        """
        ...

    @property
    def umem_id(self) -> int:
        """The UMEM ID."""
        ...

    @property
    def umem_addr(self) -> int | None:
        """The UMEM registered address."""
        ...
    @umem_addr.setter
    def umem_addr(self, addr: int) -> None:
        ...

        # --- CQE64 ---

    def __str__(self) -> str: ...

class Mlx5Cqe64(PyverbsObject):
    """64-byte CQE (Completion Queue Entry) for MLX5.

    Provides access to individual CQE fields for parsing completions.
    """

    def __init__(self, addr: int) -> None:
        """Wrap a CQE at the given memory address.

        Args:
            addr: Memory address of the 64-byte CQE.
        """
        ...

    def dump(self) -> str:
        """Dump the CQE contents as a hex string.

        Returns:
            Hexadecimal string representation of the 64-byte CQE.
        """
        ...

    def is_empty(self) -> bool:
        """Check if the CQE is empty (all zeros).

        Returns:
            ``True`` if all CQE fields are zero, ``False`` otherwise.
        """
        ...

    @property
    def owner(self) -> int:
        """Owner bit."""
        ...
    @owner.setter
    def owner(self, val: int) -> None: ...
    @property
    def se(self) -> int:
        """Solicited event."""
        ...
    @property
    def format(self) -> int:
        """CQE format."""
        ...
    @property
    def opcode(self) -> int:
        """Completion opcode."""
        ...
    @property
    def imm_inval_pkey(self) -> int:
        """Immediate/invalidate/P_Key data."""
        ...
    @property
    def wqe_id(self) -> int:
        """WQE ID."""
        ...
    @property
    def byte_cnt(self) -> int:
        """Byte count."""
        ...
    @property
    def timestamp(self) -> int:
        """Completion timestamp."""
        ...
    @property
    def wqe_counter(self) -> int:
        """WQE counter."""
        ...
    @property
    def signature(self) -> int:
        """Signature value."""
        ...
    @property
    def op_own(self) -> int:
        """Opcode and owner."""
        ...

    # --- DevX infrastructure ---

    def __str__(self) -> str: ...

class Mlx5DevxMsiVector(PyverbsCM):
    """DevX MSI Vector (mlx5dv_devx_msi_vector) for interrupt handling."""

    def __init__(self, context: Context) -> None:
        """Allocate an MSI vector.

        Args:
            context: A Context object.

        Raises:
            PyverbsRDMAErrno: If allocation fails.
        """
        ...

    @property
    def vector(self) -> int:
        """The MSI vector number."""
        ...

    @property
    def fd(self) -> int:
        """The event file descriptor for this MSI vector."""
        ...

class Mlx5DevxEq(PyverbsCM):
    """DevX Event Queue (mlx5dv_devx_eq).

    Creates an asynchronous EQ via DevX commands.
    """

    def __init__(self, context: Context, in_: bytes | list[int], outlen: int) -> None:
        """Create a DevX EQ.

        Args:
            context: A Context object.
            in_: Input command data in device specification format.
            outlen: Expected output length in bytes.

        Raises:
            PyverbsRDMAErrno: If EQ creation fails.
            PyverbsRDMAError: If the command returns non-zero status.
        """
        ...

    @property
    def out_view(self) -> memoryview:
        """Memoryview of the creation command output."""
        ...

    @property
    def vaddr(self) -> int:
        """The EQ virtual address."""
        ...

class Mlx5DevxCmdComp(PyverbsCM):
    """DevX Command Completion (mlx5dv_devx_cmd_comp).

    Provides asynchronous command completion via a file descriptor.
    """

    def __init__(self, context: Context) -> None:
        """Create a command completion object.

        Args:
            context: A Context object.

        Raises:
            PyverbsRDMAErrno: If creation fails.
        """
        ...

    def get_async_cmd_comp(self, cmd_resp_len: int = 1024) -> tuple[int, bytes]:
        """Get an asynchronous command completion.

        Args:
            cmd_resp_len: Expected response data length. Default is 1024.

        Returns:
            Tuple of (wr_id, out_data) where wr_id identifies the completed
            command and out_data is the response bytes.

        Raises:
            PyverbsError: If getting the completion fails.
        """
        ...

    @property
    def fd(self) -> int:
        """The completion file descriptor."""
        ...

    # --- Mlx5Context ---

    def __str__(self) -> str: ...

class Mlx5Context(Context):
    """MLX5 device context extending base Context with provider-specific APIs.

    Opens an MLX5 device using mlx5dv_open_device and provides access to
    DevX commands, DC QPs, crypto operations, and other MLX5 features.
    """

    def __init__(self, attr: Mlx5DVContextAttr, name: str = "") -> None:
        """Open an MLX5 device context.

        Args:
            attr: MLX5-specific device attributes.
            name: The RDMA device name (used by parent class). Default is ''.

        Raises:
            PyverbsUserError: If the device is not an MLX5 device.
            PyverbsRDMAErrno: If opening the context fails.
        """
        ...

    def query_mlx5_device(self, comp_mask: int = -1) -> Mlx5DVContext:
        """Query MLX5-specific device attributes.

        Args:
            comp_mask: Which attributes to query. Default is -1 (all).
                If not changed, pyverbs passes a bitwise OR of all available
                enum entries.

        Returns:
            A Mlx5DVContext containing the device attributes.

        Raises:
            PyverbsRDMAError: If the query fails.
        """
        ...

    @staticmethod
    def query_mlx5_port(ctx: Context, port_num: int) -> Mlx5DVPortAttr:
        """Query MLX5-specific port attributes.

        Args:
            ctx: A Context object.
            port_num: Port number to query.

        Returns:
            A Mlx5DVPortAttr containing the port attributes.

        Raises:
            PyverbsRDMAError: If the query fails.
        """
        ...

    @staticmethod
    def reserved_qpn_alloc(ctx: Context) -> int:
        """Allocate a reserved QP number from firmware.

        Args:
            ctx: The device context.

        Returns:
            The reserved QP number.

        Raises:
            PyverbsRDMAError: If allocation fails.
        """
        ...

    @staticmethod
    def reserved_qpn_dealloc(ctx: Context, qpn: int) -> None:
        """Release a reserved QP number.

        Args:
            ctx: The device context.
            qpn: The QP number to release.

        Raises:
            PyverbsRDMAError: If release fails.
        """
        ...

    @staticmethod
    def crypto_login(ctx: Context, login_attr: Mlx5CryptoLoginAttr) -> None:
        """Create a crypto login session.

        Args:
            ctx: The device context.
            login_attr: A Mlx5CryptoLoginAttr with credentials.

        Raises:
            PyverbsRDMAError: If login fails.
        """
        ...

    @staticmethod
    def query_login_state(ctx: Context) -> int:
        """Query the crypto login session state.

        Args:
            ctx: The device context.

        Returns:
            The login state.

        Raises:
            PyverbsRDMAError: If the query fails.
        """
        ...

    @staticmethod
    def crypto_logout(ctx: Context) -> None:
        """Logout from the crypto login session.

        Args:
            ctx: The device context.

        Raises:
            PyverbsRDMAError: If logout fails.
        """
        ...

    def devx_general_cmd(self, in_: bytes | list[int], outlen: int) -> bytes:
        """Execute a DevX general command.

        Args:
            in_: Input command data in device specification format.
            outlen: Expected output length in bytes.

        Returns:
            Output data bytes in device specification format.

        Raises:
            PyverbsRDMAError: If the command fails.
        """
        ...

    @staticmethod
    def device_timestamp_to_ns(ctx: Context, device_timestamp: int) -> int:
        """Convert device timestamp to nanoseconds.

        Uses mlx5dv_get_clock_info and mlx5dv_ts_to_ns.

        Args:
            ctx: The device context.
            device_timestamp: The device timestamp to convert.

        Returns:
            Timestamp in nanoseconds.

        Raises:
            PyverbsRDMAError: If getting clock info fails.
        """
        ...

    def devx_query_eqn(self, vector: int) -> int:
        """Query EQN for a given completion vector.

        Args:
            vector: Completion vector number.

        Returns:
            The device EQ number for the given vector.

        Raises:
            PyverbsRDMAError: If the query fails.
        """
        ...

    def get_data_direct_sysfs_path(self, length: int = 512) -> str:
        """Get the sysfs path for data direct access.

        Args:
            length: Buffer length for the path. Default is 512.

        Returns:
            The sysfs path as a string.

        Raises:
            PyverbsRDMAError: If the query fails.
        """
        ...

# --- Mlx5DevxObj ---

class Mlx5DevxObj(PyverbsCM):
    """DevX object (mlx5dv_devx_obj) for direct device command interface.

    Enables creation and management of arbitrary device objects via
    mailbox commands. Supports export/import for cross-process sharing.
    """

    def __init__(self, context: Context, in_: bytes | list[int], outlen: int) -> None:
        """Create a DevX object.

        Args:
            context: A Context object.
            in_: Input command data in device specification format.
            outlen: Expected output length in bytes.

        Raises:
            PyverbsRDMAErrno: If object creation fails.
            PyverbsRDMAError: If the command returns non-zero status.
        """
        ...

    def query(self, in_: bytes | list[int], outlen: int) -> bytes:
        """Query the DevX object.

        Args:
            in_: Input query data in device specification format.
            outlen: Expected output length in bytes.

        Returns:
            Output data bytes.

        Raises:
            PyverbsRDMAError: If the query fails.
        """
        ...

    def query_async(self, in_: bytes | list[int], outlen: int, wr_id: int, cmd_comp: Mlx5DevxCmdComp) -> None:
        """Asynchronously query the DevX object.

        Args:
            in_: Input query data in device specification format.
            outlen: Expected output length in bytes.
            wr_id: Command identifier for matching the completion.
            cmd_comp: A Mlx5DevxCmdComp for receiving the completion.

        Raises:
            PyverbsRDMAError: If the async query fails.
        """
        ...

    def modify(self, in_: bytes | list[int], outlen: int) -> bytes:
        """Modify the DevX object.

        Args:
            in_: Input modify data in device specification format.
            outlen: Expected output length in bytes.

        Returns:
            Output data bytes.

        Raises:
            PyverbsRDMAError: If the modify fails.
        """
        ...

    def destroy(self) -> None:
        """Destroy the DevX object.

        Raises:
            PyverbsRDMAError: If destruction fails.
        """
        ...

    def unimport_obj(self) -> None:
        """Release an imported DevX object without destroying the kernel object."""
        ...

    def export(self) -> bytes:
        """Export the DevX object for cross-process sharing.

        Returns:
            Bytes containing the exported DevX object data.

        Raises:
            PyverbsRDMAError: If export fails.
        """
        ...

    @staticmethod
    def get_export_size() -> int:
        """Get the buffer size required for DevX object export/import.

        Returns:
            Export buffer size in bytes.
        """
        ...

    @staticmethod
    def import_obj(context: Context, data: bytes) -> Mlx5DevxObj:
        """Import a DevX object from an exported data buffer.

        Args:
            context: Device context to import on.
            data: Opaque bytes from Mlx5DevxObj.export().

        Returns:
            An Mlx5DevxObj representing the imported object.

        Raises:
            PyverbsRDMAErrno: If import fails.
        """
        ...

    @property
    def out_view(self) -> memoryview:
        """Memoryview of the last command output."""
        ...

    @property
    def obj(self) -> int:
        """Underlying mlx5dv_devx_obj pointer as integer."""
        ...

# --- Module-level utility functions ---

def qpts_to_str(qp_types: int) -> str:
    """Convert a QP types bitmask to a human-readable string.

    Args:
        qp_types: Bitmask of QP type bits.

    Returns:
        Comma-separated QP type names with numeric value.
    """
    ...

def bitmask_to_str(bits: int, values: dict[int, str]) -> str:
    """Convert a generic bitmask to string using a dictionary mapping.

    Args:
        bits: Bitmask value.
        values: Mapping from bit values to name strings.

    Returns:
        Comma-separated names with numeric value.
    """
    ...

def context_comp_mask_to_str(mask: int) -> str:
    """Convert MLX5DV context comp_mask to string."""
    ...

def context_flags_to_str(flags: int) -> str:
    """Convert MLX5DV context flags to string."""
    ...

def swp_to_str(swps: int) -> str:
    """Convert SW parsing capability flags to string."""
    ...

def cqe_comp_to_str(cqe: int) -> str:
    """Convert CQE compression format flags to string."""
    ...

def tunnel_offloads_to_str(tun: int) -> str:
    """Convert tunnel offload capability flags to string."""
    ...

def dc_type_to_str(dctype: int) -> str:
    """Convert DC type enum to string (``'DCT'`` or ``'DCI'``)."""
    ...

def qp_comp_mask_to_str(flags: int) -> str:
    """Convert MLX5DV QP init attr comp_mask to string."""
    ...

def qp_create_flags_to_str(flags: int) -> str:
    """Convert MLX5DV QP create flags to string."""
    ...

def send_ops_flags_to_str(flags: int) -> str:
    """Convert MLX5DV QP send ops flags to string."""
    ...
