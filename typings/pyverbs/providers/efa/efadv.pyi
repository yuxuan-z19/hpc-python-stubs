"""
Type stubs for pyverbs.providers.efa.efadv — Amazon EFA driver verbs.

This module provides Python bindings for the Amazon Elastic Fabric Adapter (EFA)
provider-specific extensions, including:

- **EfaContext**: EFA device context for querying device capabilities.
- **SRDQP / SRDQPEx**: Scalable Reliable Datagram (SRD) Queue Pair
  implementations (basic and extended with processing hints).
- **EfaCQ**: EFA-specific Completion Queue with source GID readback and
  unsolicited RDMA write detection.
- **EfaMR**: EFA Memory Region with interconnect ID query support.
- **EfaCompCntr**: EFA Completion Counter with external memory support.
- Various attribute classes for device, QP, CQ, MR, AH, and queue depth queries.

The SRD protocol is Amazon's custom transport designed for scalable, lossless
communication over EFA hardware, optimized for HPC and ML workloads.

Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx``
"""

from pyverbs.addr import AH, GID
from pyverbs.base import PyverbsObject
from pyverbs.comp_cntr import CompCntr, CompCntrInitAttr
from pyverbs.cq import CQEX, CqInitAttrEx
from pyverbs.device import Context
from pyverbs.mr import MR
from pyverbs.pd import PD
from pyverbs.qp import QP, QPEx, QPInitAttr, QPInitAttrEx

# ---------------------------------------------------------------------------
# Module-level utility functions
# ---------------------------------------------------------------------------

def dev_cap_to_str(flags: int) -> str:
    """Convert EFA device capability flags to a human-readable string.

    Decodes the ``device_caps`` bitmask returned by
    :py:meth:`EfaContext.query_efa_device` / :py:class:`EfaDVDeviceAttr`
    into a comma-separated list of capability names.

    Recognised capability flags:

    - ``EFADV_DEVICE_ATTR_CAPS_RDMA_READ`` — RDMA Read
    - ``EFADV_DEVICE_ATTR_CAPS_RNR_RETRY`` — RNR Retry
    - ``EFADV_DEVICE_ATTR_CAPS_CQ_WITH_SGID`` — CQ entries with source GID
    - ``EFADV_DEVICE_ATTR_CAPS_RDMA_WRITE`` — RDMA Write
    - ``EFADV_DEVICE_ATTR_CAPS_UNSOLICITED_WRITE_RECV`` — Unsolicited RDMA Write receive
    - ``EFADV_DEVICE_ATTR_CAPS_CQ_WITH_EXT_MEM_DMABUF`` — CQ with external memory
    - ``EFADV_DEVICE_ATTR_CAPS_COMP_CNTR`` — Completion Counters

    Args:
        flags: Bitmask of ``EFADV_DEVICE_ATTR_CAPS_*`` capability flags
            from the ``device_caps`` field of :class:`EfaDVDeviceAttr`.

    Returns:
        A comma-separated string of recognised capability names followed by
        the hex value of the original bitmask.  Unrecognised bits are shown
        as ``??(<hex>)``.  Returns ``"None (0)"`` when *flags* is zero.

    Example::

        >>> from pyverbs.providers.efa.efadv import dev_cap_to_str
        >>> dev_cap_to_str(0x01 | 0x08)
        'RDMA Read, RDMA Write (9)'
    """
    ...

def bitmask_to_str(bits: int, values: dict[int, str]) -> str:
    """Convert a generic bitmask to a comma-separated string of flag names.

    Iterates over *values* in sorted key order, appending the name for each
    bit that is set in *bits*.  Any remaining bits not covered by *values*
    are reported as ``??(<hex>)``.

    Args:
        bits: The bitmask to decode.
        values: Mapping from individual bit values (powers of two) to their
            human-readable names.  Must not be ``None``.

    Returns:
        A comma-separated string of matched flag names followed by the hex
        representation of the original *bits*.  Returns ``"None (0)"`` when
        no bits match.

    Example::

        >>> bitmask_to_str(0x03, {0x01: 'A', 0x02: 'B', 0x04: 'C'})
        'A, B (3)'
    """
    ...

# ---------------------------------------------------------------------------
# EFA Device Context
# ---------------------------------------------------------------------------

class EfaContext(Context):
    """EFA device context, extending the base :class:`~pyverbs.device.Context`.

    Provides EFA-specific device operations on top of the standard RDMA
    device context.  The EFA context is the entry point for opening an
    Amazon EFA device and querying its provider-specific capabilities.

    Inherits all standard RDMA operations (PD/CQ/QP/MR creation, etc.)
    from :class:`~pyverbs.device.Context`.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class EfaContext``
    """

    def __init__(self, name: str = "") -> None:
        """Open an EFA RDMA device.

        Delegates to the parent :class:`~pyverbs.device.Context` constructor
        to open the device identified by *name*.

        Args:
            name: The RDMA device name (e.g. ``"efa_0"``).  An empty string
                opens the first available device.  Passed directly to the
                parent class.
        """
        ...

    def query_efa_device(self) -> EfaDVDeviceAttr:
        """Query EFA-specific device attributes via ``efadv_query_device``.

        Retrieves provider-specific capabilities and limits of the EFA
        device, such as maximum queue depths, inline buffer sizes, and
        supported features (RDMA Read/Write, completion counters, etc.).

        Returns:
            An :class:`EfaDVDeviceAttr` instance populated with the
            device's EFA-specific attributes.

        Raises:
            PyverbsRDMAError: If the underlying ``efadv_query_device`` call
                fails (non-zero return code from the driver).

        Example::

            ctx = EfaContext('efa_0')
            attr = ctx.query_efa_device()
            print(f"Max SQ WR: {attr.max_sq_wr}")
            print(f"Device caps: {dev_cap_to_str(attr.device_caps)}")
        """
        ...

# ---------------------------------------------------------------------------
# EFA Device Attributes
# ---------------------------------------------------------------------------

class EfaDVDeviceAttr(PyverbsObject):
    """EFA-specific device attributes.

    Represents the ``efadv_device_attr`` C structure, which exposes
    EFA-specific capabilities and limits reported by
    :py:meth:`EfaContext.query_efa_device`.

    All attributes are read-only and populated by the driver query.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class EfaDVDeviceAttr``

    Attributes:
        comp_mask: Compatibility mask for forward compatibility of the
            attribute structure.
        max_sq_wr: Maximum number of send queue work requests.
        max_rq_wr: Maximum number of receive queue work requests.
        max_sq_sge: Maximum number of scatter/gather entries per send WR.
        max_rq_sge: Maximum number of scatter/gather entries per receive WR.
        inline_buf_size: Size of the inline data buffer (bytes).
        inline_buf_size_ex: Extended inline data buffer size (bytes).
        device_caps: Bitmask of ``EFADV_DEVICE_ATTR_CAPS_*`` capability flags.
            Use :func:`dev_cap_to_str` for human-readable output.
        max_rdma_size: Maximum RDMA transfer size (bytes).
    """

    @property
    def comp_mask(self) -> int:
        """Compatibility mask (``uint64_t``).

        Used for forward compatibility when the attribute structure is
        extended with new fields in future driver versions.
        """
        ...

    @property
    def max_sq_wr(self) -> int:
        """Maximum send queue work requests (``uint32_t``).

        The largest number of WRs that can be posted to a send queue
        on this device.
        """
        ...

    @property
    def max_rq_wr(self) -> int:
        """Maximum receive queue work requests (``uint32_t``).

        The largest number of WRs that can be posted to a receive queue
        on this device.
        """
        ...

    @property
    def max_sq_sge(self) -> int:
        """Maximum scatter/gather entries per send WR (``uint16_t``).

        The maximum number of data buffers that can be referenced by
        a single send work request.
        """
        ...

    @property
    def max_rq_sge(self) -> int:
        """Maximum scatter/gather entries per receive WR (``uint16_t``).

        The maximum number of data buffers that can be referenced by
        a single receive work request.
        """
        ...

    @property
    def inline_buf_size(self) -> int:
        """Inline data buffer size in bytes (``uint16_t``).

        Maximum amount of data that can be inlined directly into
        send work requests using the standard inline buffer.
        """
        ...

    @property
    def inline_buf_size_ex(self) -> int:
        """Extended inline data buffer size in bytes (``uint16_t``).

        Maximum amount of data that can be inlined using the extended
        inline buffer mechanism, available on newer EFA hardware.
        """
        ...

    @property
    def device_caps(self) -> int:
        """Device capability bitmask (``uint32_t``).

        A combination of ``EFADV_DEVICE_ATTR_CAPS_*`` flags indicating
        which optional features the device supports.  Decode with
        :func:`dev_cap_to_str`.
        """
        ...

    @property
    def max_rdma_size(self) -> int:
        """Maximum RDMA transfer size in bytes (``uint32_t``).

        The largest single RDMA Read or Write operation supported
        by the device.
        """
        ...

    def __str__(self) -> str:
        """Return a formatted multi-line string of all device attributes."""
        ...

# ---------------------------------------------------------------------------
# EFA Address Handle
# ---------------------------------------------------------------------------

class EfaAH(AH):
    """EFA-specific Address Handle, extending the base :class:`~pyverbs.addr.AH`.

    Provides EFA-specific AH query functionality on top of the standard
    address handle used for addressing remote endpoints.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class EfaAH``
    """

    def query_efa_ah(self) -> EfaDVAHAttr:
        """Query EFA-specific Address Handle attributes via ``efadv_query_ah``.

        Retrieves the EFA-specific attributes associated with this address
        handle, including the address handle number (AHN).

        Returns:
            An :class:`EfaDVAHAttr` instance containing the EFA AH attributes.

        Raises:
            PyverbsRDMAError: If the underlying ``efadv_query_ah`` call fails.
        """
        ...

class EfaDVAHAttr(PyverbsObject):
    """EFA-specific Address Handle attributes.

    Represents the ``efadv_ah_attr`` C structure, exposing EFA-specific
    attributes of an Address Handle as reported by
    :py:meth:`EfaAH.query_efa_ah`.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class EfaDVAHAttr``

    Attributes:
        comp_mask: Compatibility mask for forward compatibility.
        ahn: Address Handle Number.
    """

    @property
    def comp_mask(self) -> int:
        """Compatibility mask (``uint64_t``).

        Used for forward compatibility of the AH attribute structure.
        """
        ...

    @property
    def ahn(self) -> int:
        """Address Handle Number (``uint16_t``).

        The hardware-assigned handle number for this address handle,
        used by the EFA device to reference the AH internally.
        """
        ...

    def __str__(self) -> str:
        """Return a formatted string of the EFA AH attributes."""
        ...

# ---------------------------------------------------------------------------
# SRD Queue Pairs
# ---------------------------------------------------------------------------

class SRDQP(QP):
    """Scalable Reliable Datagram (SRD) Queue Pair.

    Creates a basic SRD QP using the EFA driver's ``efadv_create_driver_qp``
    with ``EFADV_QP_DRIVER_TYPE_SRD``.  SRD is Amazon's custom transport
    protocol designed for scalable, lossless communication over EFA hardware.

    This basic variant supports standard QP operations.  For processing
    hints support, use :class:`SRDQPEx` instead.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class SRDQP``
    """

    def __init__(self, pd: PD, init_attr: QPInitAttr) -> None:
        """Create an SRD Queue Pair.

        Calls ``efadv_create_driver_qp`` internally with
        ``EFADV_QP_DRIVER_TYPE_SRD`` to create the SRD transport QP,
        then initialises the base :class:`~pyverbs.qp.QP`.

        Args:
            pd: Protection Domain for the QP.  Must not be ``None``.
            init_attr: QP initial attributes including send/receive queue
                sizes, completion queue references, and QP type.  Must not
                be ``None``.

        Raises:
            PyverbsRDMAErrno: If ``efadv_create_driver_qp`` fails (returns
                ``NULL``).
        """
        ...

class EfaQPInitAttr(PyverbsObject):
    """EFA-specific QP initialization attributes.

    Represents the ``efadv_qp_init_attr`` C structure, which carries
    provider-specific parameters for creating an :class:`SRDQPEx`.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class EfaQPInitAttr``

    Attributes:
        comp_mask: Compatibility mask for forward compatibility.
        driver_qp_type: Driver QP type identifier.
        flags: QP creation flags (e.g. ``EFADV_QP_FLAGS_*``).
        sl: Service Level for the QP.
        wr_flags: Default work request flags (e.g. processing hints).
    """

    @property
    def comp_mask(self) -> int:
        """Compatibility mask (``uint64_t``).

        Used for forward compatibility of the QP init attribute structure.
        Read-only.
        """
        ...

    @property
    def driver_qp_type(self) -> int:
        """Driver QP type (``uint32_t``).

        Identifies the transport type for the QP (e.g.
        ``EFADV_QP_DRIVER_TYPE_SRD``).  Read-write.
        """
        ...

    @driver_qp_type.setter
    def driver_qp_type(self, val: int) -> None: ...
    @property
    def flags(self) -> int:
        """QP creation flags (``uint16_t``).

        Combination of ``EFADV_QP_FLAGS_*`` values controlling QP
        behaviour (e.g. unsolicited write recv, inline write).
        Read-write.
        """
        ...

    @flags.setter
    def flags(self, val: int) -> None: ...
    @property
    def sl(self) -> int:
        """Service Level (``uint8_t``).

        The service level for traffic prioritisation.  Read-write.
        """
        ...

    @sl.setter
    def sl(self, val: int) -> None: ...
    @property
    def wr_flags(self) -> int:
        """Default work request flags (``uint64_t``).

        Flags applied to work requests posted to this QP, such as
        ``EFADV_WR_EX_WITH_PROCESSING_HINTS``.  Read-write.
        """
        ...

    @wr_flags.setter
    def wr_flags(self, val: int) -> None: ...

class SRDQPEx(QPEx):
    """Extended Scalable Reliable Datagram (SRD) Queue Pair.

    Creates an extended SRD QP via ``efadv_create_qp_ex`` with support
    for EFA-specific processing hints that can optimise work request
    handling (e.g. burst PPS sensitivity).

    Inherits all extended QP operations (``wr_*`` methods) from
    :class:`~pyverbs.qp.QPEx`.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class SRDQPEx``
    """

    def __init__(self, ctx: Context, attr_ex: QPInitAttrEx, efa_init_attr: EfaQPInitAttr) -> None:
        """Create an extended SRD Queue Pair.

        Calls ``efadv_create_qp_ex`` internally with the EFA-specific
        init attributes, then initialises the base :class:`~pyverbs.qp.QPEx`.

        Args:
            ctx: Device context.  Must not be ``None``.
            attr_ex: Extended QP initialization attributes including PD,
                send/receive CQ, and queue sizes.  Must not be ``None``.
            efa_init_attr: EFA-specific QP initialization attributes
                containing driver QP type, flags, SL, and WR flags.
                Must not be ``None``.

        Raises:
            PyverbsRDMAErrno: If ``efadv_create_qp_ex`` fails (returns
                ``NULL``).
        """
        ...

    def wr_set_processing_hints(self, hints: int) -> None:
        """Set processing hints for the next work request on this QP.

        Calls ``efadv_wr_set_processing_hints`` to attach processing
        hints to the next WR to be posted.  Hints allow the application
        to communicate workload characteristics to the hardware for
        optimisation (e.g. burst PPS sensitivity).

        Args:
            hints: Processing hints bitmask (``uint32_t``), e.g.
                ``EFADV_WR_PROCESSING_HINT_BURST_PPS_SENSITIVE``.
        """
        ...

    def _get_comp_mask(self, dst: str) -> int:
        """Compute the QP attribute mask for SRD state transitions.

        Internal helper that returns the ``ibv_qp_attr_mask`` bitmask
        appropriate for transitioning this SRD QP to the given target
        state.  SRD QPs use a simplified transition model:

        - ``"INIT"``: ``IBV_QP_STATE | IBV_QP_PKEY_INDEX | IBV_QP_PORT | IBV_QP_QKEY``
        - ``"RTR"``: ``IBV_QP_STATE`` (no additional attributes)
        - ``"RTS"``: ``IBV_QP_STATE | IBV_QP_SQ_PSN``

        Args:
            dst: Target QP state string.  One of ``"INIT"``, ``"RTR"``,
                or ``"RTS"``.

        Returns:
            The combined ``ibv_qp_attr_mask`` bitmask for the transition.
        """
        ...

# ---------------------------------------------------------------------------
# EFA Completion Queue
# ---------------------------------------------------------------------------

class EfaDVCQInitAttr(PyverbsObject):
    """EFA-specific Completion Queue initialization attributes.

    Represents the ``efadv_cq_init_attr`` C structure, carrying
    provider-specific parameters for creating an :class:`EfaCQ`.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class EfaDVCQInitAttr``

    Attributes:
        comp_mask: Compatibility mask for forward compatibility.
        wc_flags: Work completion flags controlling CQ behaviour.
    """

    def __init__(self, wc_flags: int = 0) -> None:
        """Initialise EFA CQ attributes with the given work completion flags.

        Args:
            wc_flags: Work completion flags (``uint64_t``).  Common values
                include ``EFADV_WC_EX_WITH_SGID`` (enable source GID in WC)
                and ``EFADV_WC_EX_WITH_IS_UNSOLICITED`` (enable unsolicited
                write detection).  Defaults to 0.
        """
        ...

    @property
    def comp_mask(self) -> int:
        """Compatibility mask (``uint64_t``).

        Used for forward compatibility of the CQ init attribute structure.
        Read-only.
        """
        ...

    @property
    def wc_flags(self) -> int:
        """Work completion flags (``uint64_t``).

        Controls which extended work completion information the CQ
        provides.  Use ``EFADV_WC_EX_WITH_*`` constants.  Read-write.
        """
        ...

    @wc_flags.setter
    def wc_flags(self, val: int) -> None: ...

class EfaCQ(CQEX):
    """EFA-specific Completion Queue, extending :class:`~pyverbs.cq.CQEX`.

    Creates an EFA CQ via ``efadv_create_cq`` with support for:

    - Reading the source GID from the last work completion
      (:py:meth:`read_sgid`).
    - Detecting unsolicited RDMA write completions
      (:py:meth:`is_unsolicited`).

    These features require the corresponding ``EFADV_WC_EX_WITH_*`` flags
    to be set in the :class:`EfaDVCQInitAttr` passed at creation time.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class EfaCQ``
    """

    def __init__(self, ctx: Context, attr_ex: CqInitAttrEx, efa_init_attr: EfaDVCQInitAttr | None = None) -> None:
        """Create an EFA Completion Queue.

        Calls ``efadv_create_cq`` internally with the EFA-specific
        init attributes, then initialises the base
        :class:`~pyverbs.cq.CQEX`.

        Args:
            ctx: Device context.  Must not be ``None``.
            attr_ex: Extended CQ initialization attributes including CQ
                size, completion channel, and vector.  Must not be ``None``.
            efa_init_attr: EFA-specific CQ initialization attributes
                controlling WC flags (SGID, unsolicited detection).
                If ``None``, a default :class:`EfaDVCQInitAttr` with
                ``wc_flags=0`` is used.
                *Note*: the Cython source accepts ``None`` and silently
                creates a default; the type hint reflects this.

        Raises:
            PyverbsRDMAErrno: If ``efadv_create_cq`` fails (returns ``NULL``).
        """
        ...

    def read_sgid(self) -> GID | None:
        """Read the source GID from the last work completion.

        Calls ``efadv_wc_read_sgid`` to retrieve the source GID
        (``ibv_gid``) associated with the most recently polled work
        completion.  This is useful when the AH is unknown and the
        application needs to identify the sender.

        Requires ``EFADV_WC_EX_WITH_SGID`` to have been set in the
        CQ's ``wc_flags`` at creation time.

        Returns:
            A :class:`~pyverbs.addr.GID` object containing the source
            GID, or ``None`` if the SGID is not available for the
            current work completion (e.g. the underlying call returned
            a non-zero error code).
        """
        ...

    def is_unsolicited(self) -> bool:
        """Check if the current work completion is an unsolicited RDMA write.

        Calls ``efadv_wc_is_unsolicited`` to determine whether the
        most recently polled work completion corresponds to an
        unsolicited RDMA write — a write that arrives without a
        preceding receive WR.

        Requires ``EFADV_WC_EX_WITH_IS_UNSOLICITED`` to have been set
        in the CQ's ``wc_flags`` at creation time.

        Returns:
            ``True`` if the current WC is an unsolicited RDMA write,
            ``False`` otherwise.
        """
        ...

# ---------------------------------------------------------------------------
# EFA Memory Region
# ---------------------------------------------------------------------------

class EfaMR(MR):
    """EFA-specific Memory Region with interconnect ID query support.

    Extends the standard :class:`~pyverbs.mr.MR` with the ability to
    query EFA-specific MR attributes, including interconnect IDs for
    the receive, RDMA read, and RDMA receive paths.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class EfaMR``
    """

    def query(self) -> EfaDVMRAttr:
        """Query EFA-specific MR attributes via ``efadv_query_mr``.

        Retrieves provider-specific attributes for this memory region,
        including interconnect IDs used by the EFA hardware for
        data movement operations.

        Returns:
            An :class:`EfaDVMRAttr` instance populated with the MR's
            EFA-specific attributes.

        Raises:
            PyverbsRDMAError: If the underlying ``efadv_query_mr`` call
                fails (non-zero return code).
        """
        ...

class EfaDVMRAttr(PyverbsObject):
    """EFA-specific Memory Region attributes.

    Represents the ``efadv_mr_attr`` C structure, exposing EFA-specific
    MR attributes as reported by :py:meth:`EfaMR.query`.

    The interconnect IDs identify the hardware interconnect paths used
    for different data movement operations on this MR.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class EfaDVMRAttr``

    Attributes:
        comp_mask: Compatibility mask for forward compatibility.
        ic_id_validity: Bitmask indicating which interconnect ID fields
            contain valid values.  Use ``EFADV_MR_ATTR_VALIDITY_*`` constants.
        recv_ic_id: Receive interconnect ID.
        rdma_read_ic_id: RDMA read interconnect ID.
        rdma_recv_ic_id: RDMA receive interconnect ID.
    """

    @property
    def comp_mask(self) -> int:
        """Compatibility mask (``uint64_t``).

        Used for forward compatibility of the MR attribute structure.
        Read-only.
        """
        ...

    @property
    def ic_id_validity(self) -> int:
        """Interconnect ID validity bitmask (``uint16_t``).

        Indicates which of the interconnect ID fields (``recv_ic_id``,
        ``rdma_read_ic_id``, ``rdma_recv_ic_id``) contain valid values.
        Check against ``EFADV_MR_ATTR_VALIDITY_RECV_IC_ID``,
        ``EFADV_MR_ATTR_VALIDITY_RDMA_READ_IC_ID``, and
        ``EFADV_MR_ATTR_VALIDITY_RDMA_RECV_IC_ID``.  Read-only.
        """
        ...

    @property
    def recv_ic_id(self) -> int:
        """Receive interconnect ID (``uint16_t``).

        The interconnect ID used for the receive path.  Valid when
        ``ic_id_validity`` has ``EFADV_MR_ATTR_VALIDITY_RECV_IC_ID`` set.
        Read-only.
        """
        ...

    @property
    def rdma_read_ic_id(self) -> int:
        """RDMA read interconnect ID (``uint16_t``).

        The interconnect ID used for RDMA read operations.  Valid when
        ``ic_id_validity`` has
        ``EFADV_MR_ATTR_VALIDITY_RDMA_READ_IC_ID`` set.  Read-only.
        """
        ...

    @property
    def rdma_recv_ic_id(self) -> int:
        """RDMA receive interconnect ID (``uint16_t``).

        The interconnect ID used for RDMA receive operations.  Valid when
        ``ic_id_validity`` has
        ``EFADV_MR_ATTR_VALIDITY_RDMA_RECV_IC_ID`` set.  Read-only.
        """
        ...

    def __str__(self) -> str:
        """Return a formatted multi-line string of the EFA MR attributes."""
        ...

# ---------------------------------------------------------------------------
# EFA Queue Depth Attributes
# ---------------------------------------------------------------------------

class EfaDVSQDepthAttr(PyverbsObject):
    """EFA send queue depth attributes.

    Represents the ``efadv_sq_depth_attr`` C structure, used to query
    the maximum send queue depth and related parameters from the EFA
    device via ``efadv_get_max_sq_depth``.

    Fields are set by the caller to specify constraints (e.g. inline
    data size), and the driver fills in the resulting maximum depths.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class EfaDVSQDepthAttr``

    Attributes:
        comp_mask: Compatibility mask for forward compatibility.
        flags: SQ depth query flags (e.g. ``EFADV_SQ_DEPTH_ATTR_INLINE_WRITE``).
        max_send_sge: Maximum number of send scatter/gather entries.
        max_rdma_sge: Maximum number of RDMA scatter/gather entries.
        max_inline_data: Maximum inline data size in bytes.
    """

    @property
    def comp_mask(self) -> int:
        """Compatibility mask (``uint64_t``).

        Used for forward compatibility of the SQ depth attribute structure.
        Read-write.
        """
        ...

    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    @property
    def flags(self) -> int:
        """SQ depth query flags (``uint32_t``).

        Controls which aspects of the SQ depth are queried.
        Use ``EFADV_SQ_DEPTH_ATTR_*`` constants.  Read-write.
        """
        ...

    @flags.setter
    def flags(self, val: int) -> None: ...
    @property
    def max_send_sge(self) -> int:
        """Maximum send scatter/gather entries (``uint32_t``).

        The maximum number of SGEs per send WR, constrained by the
        other parameters.  Read-write.
        """
        ...

    @max_send_sge.setter
    def max_send_sge(self, val: int) -> None: ...
    @property
    def max_rdma_sge(self) -> int:
        """Maximum RDMA scatter/gather entries (``uint32_t``).

        The maximum number of SGEs per RDMA WR, constrained by the
        other parameters.  Read-write.
        """
        ...

    @max_rdma_sge.setter
    def max_rdma_sge(self, val: int) -> None: ...
    @property
    def max_inline_data(self) -> int:
        """Maximum inline data size in bytes (``uint32_t``).

        The maximum amount of data that can be inlined in send WRs,
        constrained by the other parameters.  Read-write.
        """
        ...

    @max_inline_data.setter
    def max_inline_data(self, val: int) -> None: ...

class EfaDVRQDepthAttr(PyverbsObject):
    """EFA receive queue depth attributes.

    Represents the ``efadv_rq_depth_attr`` C structure, used to query
    the maximum receive queue depth from the EFA device via
    ``efadv_get_max_rq_depth``.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class EfaDVRQDepthAttr``

    Attributes:
        comp_mask: Compatibility mask for forward compatibility.
        max_recv_sge: Maximum number of receive scatter/gather entries.
    """

    @property
    def comp_mask(self) -> int:
        """Compatibility mask (``uint64_t``).

        Used for forward compatibility of the RQ depth attribute structure.
        Read-write.
        """
        ...

    @comp_mask.setter
    def comp_mask(self, val: int) -> None: ...
    @property
    def max_recv_sge(self) -> int:
        """Maximum receive scatter/gather entries (``uint32_t``).

        The maximum number of SGEs per receive WR.  Read-write.
        """
        ...

    @max_recv_sge.setter
    def max_recv_sge(self, val: int) -> None: ...

# ---------------------------------------------------------------------------
# EFA Completion Counter
# ---------------------------------------------------------------------------

class EfaCompCntrInitAttr(PyverbsObject):
    """EFA-specific Completion Counter initialization attributes.

    Represents the ``efadv_comp_cntr_init_attr`` C structure, providing
    optional external memory pointers for the completion and error
    counters.  When external memory is provided, the counter values
    are written directly to the specified memory locations, enabling
    efficient polling without driver calls.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class EfaCompCntrInitAttr``

    Attributes:
        comp_mask: Compatibility mask (internal, not directly settable).
    """

    def __init__(self, comp_ext_mem_ptr: int | None = None, err_ext_mem_ptr: int | None = None) -> None:
        """Initialise EFA completion counter attributes.

        Optionally configures external memory locations for the completion
        and error counters.  When a pointer is provided, the corresponding
        ``EFADV_COMP_CNTR_INIT_WITH_*`` flag is set and the memory location
        type is set to ``EFADV_MEMORY_LOCATION_VA`` (virtual address).

        Args:
            comp_ext_mem_ptr: Virtual address of external memory for the
                completion counter (``uintptr_t``).  ``None`` to omit.
            err_ext_mem_ptr: Virtual address of external memory for the
                error counter (``uintptr_t``).  ``None`` to omit.
        """
        ...

    def set_comp_ext_mem_va(self, ptr: int) -> None:
        """Set the completion counter external memory virtual address.

        Configures the completion counter to write its value to the
        specified virtual address.  Sets the
        ``EFADV_COMP_CNTR_INIT_WITH_COMP_EXTERNAL_MEM`` flag and the
        memory location type to ``EFADV_MEMORY_LOCATION_VA``.

        Args:
            ptr: Virtual address of the external memory (``uintptr_t``).
                Must point to a valid, accessible memory region of
                sufficient size.
        """
        ...

    def set_err_ext_mem_va(self, ptr: int) -> None:
        """Set the error counter external memory virtual address.

        Configures the error counter to write its value to the
        specified virtual address.  Sets the
        ``EFADV_COMP_CNTR_INIT_WITH_ERR_EXTERNAL_MEM`` flag and the
        memory location type to ``EFADV_MEMORY_LOCATION_VA``.

        Args:
            ptr: Virtual address of the external memory (``uintptr_t``).
                Must point to a valid, accessible memory region of
                sufficient size.
        """
        ...

class EfaCompCntr(CompCntr):
    """EFA-specific Completion Counter with external memory support.

    Creates an EFA completion counter via ``efadv_create_comp_cntr``,
    optionally backed by external memory for efficient counter polling.

    Extends the base :class:`~pyverbs.comp_cntr.CompCntr` with EFA-specific
    initialisation attributes.

    Source: ``rdma-core/pyverbs/providers/efa/efadv.pyx`` — ``cdef class EfaCompCntr``
    """

    def __init__(self, ctx: Context, attr: CompCntrInitAttr, efa_attr: EfaCompCntrInitAttr | None = None) -> None:
        """Create an EFA Completion Counter.

        Calls ``efadv_create_comp_cntr`` internally with the base and
        EFA-specific initialization attributes.

        Args:
            ctx: Device context.  Must not be ``None``.
            attr: Base completion counter initialization attributes.
                Must not be ``None``.
            efa_attr: EFA-specific initialization attributes, optionally
                providing external memory pointers for the completion
                and error counters.  If ``None``, a default
                :class:`EfaCompCntrInitAttr` with no external memory is
                used.

        Raises:
            PyverbsRDMAErrno: If ``efadv_create_comp_cntr`` fails
                (returns ``NULL``).

        Example::

            from pyverbs.comp_cntr import CompCntrInitAttr
            from pyverbs.providers.efa.efadv import EfaCompCntr, EfaCompCntrInitAttr

            ctx = EfaContext('efa_0')
            base_attr = CompCntrInitAttr()
            efa_attr = EfaCompCntrInitAttr()
            cntr = EfaCompCntr(ctx, base_attr, efa_attr)
        """
        ...
