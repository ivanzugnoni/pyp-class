import unittest


class AssignmentTestCase(unittest.TestCase):
    def setUp(self):
        with open('test-file.txt', 'w') as f:
            f.write('this is line 1\n')
            f.write('this is line 2\n')
            f.write('this is line 3\n')

    def test_reads_first_line(self):
        self.assertEqual(read_first_line('test-file.txt'),
                         'this is line 1\n')
