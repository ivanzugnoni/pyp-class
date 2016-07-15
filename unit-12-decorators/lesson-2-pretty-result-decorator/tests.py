import unittest

@pretty_result
def add(x, y):
    return x + y

@pretty_result
def subtract(x, y):
    return x - y


class AssignmentTestCase(unittest.TestCase):
    def test_add_function(self):
        self.assertEqual(add(2, 5), "The result of the function 'add' is: 7")

    def test_subtract_function(self):
        self.assertEqual(
            subtract(13, 8), "The result of the function 'subtract' is: 5")
