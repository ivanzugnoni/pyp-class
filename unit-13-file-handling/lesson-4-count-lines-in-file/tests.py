import unittest
import tempfile


class AssignmentTestCase(unittest.TestCase):
    def setUp(self):
        self.fp = tempfile.NamedTemporaryFile(mode="w")
        self.fp.write('this is line 1\n')
        self.fp.write('this is line 2\n')
        self.fp.write('this is line 3\n')
        self.fp.flush()

    def test_1(self):
        self.assertEqual(count_lines(self.fp.name), 3)

    def tearDown(self):
        self.fp.close()
