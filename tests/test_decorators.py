import unittest

import os
import sys

sys.path.append(os.getcwd())

from ..strlib._decorators import prototype


class TestDecorators(unittest.TestCase):
    def test_prototype_raise(self):
        @prototype
        def stub():
            pass

        with self.assertRaises(NotImplementedError):
            stub()


if __name__ == "__main__":
    unittest.main()
