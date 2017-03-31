import unittest


class SimplePasswordGeneratorTestCase(unittest.TestCase):

    def test_range_generator_basics(self):
        gen1 = iter(rmotr_range(0, 3))
        self.assertEqual(next(gen1), 0)
        self.assertEqual(next(gen1), 1)
        self.assertEqual(next(gen1), 2)
        with self.assertRaises(StopIteration):
            next(gen1)

        gen2 = iter(rmotr_range(3, 6))
        self.assertEqual(next(gen2), 3)
        self.assertEqual(next(gen2), 4)
        self.assertEqual(next(gen2), 5)
        with self.assertRaises(StopIteration):
            next(gen2)

    def test_range_generator_with_step(self):
        gen1 = iter(rmotr_range(2, 10, 2))
        self.assertEqual(next(gen1), 2)
        self.assertEqual(next(gen1), 4)
        self.assertEqual(next(gen1), 6)
        self.assertEqual(next(gen1), 8)
        with self.assertRaises(StopIteration):
            next(gen1)
