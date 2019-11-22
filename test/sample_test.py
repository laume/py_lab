import unittest

from ..src.options import file_a


class BasicTest(unittest.TestCase):
    """Basic test case"""

    def test_func(self):
        assert file_a.func_a()


if __name__ == '__main__':
    unittest.main()
