from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

import onnx
from ..base import Base
from . import expect


class Log(Base):

    @staticmethod
    def export():
        node = onnx.helper.make_node(
            'Log',
            inputs=['x'],
            outputs=['y'],
        )

        x = np.exp(np.random.randn(3, 4, 5).astype(np.float32))
        y = np.log(x)
        expect(node, inputs=[x], outputs=[y],
               name='test_log')