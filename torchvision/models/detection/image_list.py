# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
from __future__ import division

import torch


class ImageList(object):
    """
    Structure that holds a list of images (of possibly
    varying sizes) as a single tensor.
    This works by padding the images to the same size,
    and storing in a field the original sizes of each image
    """

    def __init__(self, tensors, image_sizes):
        # type: (Tensor, List[List[int]])
        """
        Arguments:
            tensors (Tensor)
            image_sizes (List[Tuple[int, int]])
        """
        self.tensors = tensors
        self.image_sizes = image_sizes

    # TODO: Can't TorchScript this due to https://github.com/pytorch/pytorch/issues/25462
    # def to(self, *args, **kwargs):
    #     cast_tensor = self.tensors.to(*args, **kwargs)
    #     return ImageList(cast_tensor, self.image_sizes)
