import unittest


@small_numbers(limit=100)
def f1(a_str, a_float):
    return 'mock1 - {} {}'.format(a_str, a_float)


@small_numbers()
def f2(an_int, a_str):
    return 'mock2 - {} {}'.format(an_int, a_str)


class AssignmentTestCase(unittest.TestCase):
    def test_default_limit_is_respected(self):
        self.assertEqual(f2(50, 'hello'), "mock2 - 50 hello")

    def test_default_limit_raises(self):
        with self.assertRaises(ValueError):
            f2(51, 'hello')

    def test_specified_limit_is_respected(self):
        self.assertEqual(f1('world', 100.0), "mock1 - world 100.0")

    def test_specified_limit_raises(self):
        with self.assertRaises(ValueError):
            f1('world', 100.1)
