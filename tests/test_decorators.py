import unittest

from _decorators import prototype


class TestDecorators(unittest.TestCase):
    def test_prototype_raise(self):
        @prototype
        def stub():
            pass

        with self.assertRaises(NotImplementedError):
            stub()

if __name__ == "__main__":
    unittest.main()
