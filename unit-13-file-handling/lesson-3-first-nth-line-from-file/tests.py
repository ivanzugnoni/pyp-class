import unittest
import tempfile


class AssignmentTestCase(unittest.TestCase):
    def setUp(self):
        self.fp = tempfile.NamedTemporaryFile(mode="w")
        self.fp.write('this is line 1\n')
        self.fp.write('this is line 2\n')
        self.fp.write('this is line 3\n')
        self.fp.flush()

    def test_read_second_line(self):
        self.assertEqual(read_line_number(self.fp.name, 2),
                        'this is line 2\n')

    def test_read_last_line(self):
        self.assertEqual(read_line_number(self.fp.name, 3),
                        'this is line 3\n')

    def tearDown(self):
        self.fp.close()
