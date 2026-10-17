"""
Type stubs for pyverbs.providers.mlx5.mlx5dv_dmabuf — MLX5 DMA-BUF MR extension.
"""

from pyverbs.mr import DmaBufMR
from pyverbs.pd import PD

class Mlx5DmaBufMR(DmaBufMR):
    """MLX5-specific DMA-BUF Memory Region.

    Extends the base DmaBufMR with mlx5dv_reg_dmabuf_mr for
    registering DMA-BUF memory regions with MLX5-specific access flags.
    """

    def __init__(
        self,
        pd: PD,
        offset: int,
        length: int,
        iova: int = 0,
        fd: int | None = None,
        access: int = 0,
        mlx5_access: int = 0,
    ) -> None:
        """Register an MLX5 DMA-BUF Memory Region.

        Args:
            pd: A PD object for the protection domain.
            offset: Byte offset from the beginning of the dma-buf.
            length: Length of the MR in bytes.
            iova: Virtual base address of the MR when accessed through
                a lkey or rkey. Default is 0.
            fd: FD representing a dmabuf, or a DmaBuf object.
            access: Access flags, see ibv_access_flags enum. Default is 0.
            mlx5_access: MLX5-specific device access flags. Default is 0.

        Raises:
            PyverbsRDMAErrno: If MR registration fails.
        """
        ...
