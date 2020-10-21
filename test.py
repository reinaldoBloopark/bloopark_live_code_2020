import unittest
from main import overlap
from main import find_overlaps

class TestLineOverlap(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.l1 = (1, 8)
        cls.l2 = (2, 6)

        cls.l3 = (10, 20)
        cls.l4 = (1, 9)

        cls.l5 = (15, 20)
        cls.l6 = (1, 15)

        cls.to_test = {
            'A': (3, 6),
            'B': (1, 8),
            'C': (15, 11),
            'D': (6, 9)}
        cls.response = [('A', 'B'), ('A', 'D'), ('B', 'D')]

        cls.to_test_2 = {
            'A': (1, 10),
            'B': (15, 11)}
        cls.response_2 = []

    def test_overlap_ok(self):

        self.assertTrue(overlap(self.l1, self.l2))
        self.assertTrue(overlap(self.l5, self.l6))

    def test_overlap_not_ok(self):
        self.assertFalse(overlap(self.l3, self.l4))

    def test_find_overlaps_ok(self):

        self.assertEqual(find_overlaps(self.to_test), self.response)

    def test_find_overlaps_not_ok(self):

        self.assertEqual(find_overlaps(self.to_test_2), self.response_2)

if __name__ == '__main__':
    unittest.main()
