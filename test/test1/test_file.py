import unittest


class BasicTest(unittest.TestCase):
    """Basic test case"""

    def test_func(self):
        assert True


# def func_test():
#     return f'func_test name {__name__}, and a: {a.func_a()} and b: {src.func_b()}'


if __name__ == '__main__':
    unittest.main()
