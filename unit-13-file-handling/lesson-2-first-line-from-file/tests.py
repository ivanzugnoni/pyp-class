import unittest
import tempfile

class AssignmentTestCase(unittest.TestCase):
    def setUp(self):
        self.fp = tempfile.NamedTemporaryFile(mode="w")
        self.fp.write('this is line 1\n')
        self.fp.write('this is line 2\n')
        self.fp.write('this is line 3\n')
        self.fp.flush()

    def test_reads_first_line(self):
        self.assertEqual(read_first_line(self.fp.name),
                         'this is line 1\n')

    def tearDown(self):
        self.fp.close()
