import unittest
from line_overlap import is_line_overlap


class LineOverlapTest(unittest.TestCase):
    def test_can_see_no_overlap(self):
        self.assertFalse(is_line_overlap((1, 5), (6, 7)))
        self.assertFalse(is_line_overlap((6, 7), (1, 5)))

    def test_can_see_overlap(self):
        self.assertTrue(is_line_overlap((1, 5), (4, 8)))
        self.assertTrue(is_line_overlap((1, 5), (2, 3)))
        self.assertTrue(is_line_overlap((2, 3), (1, 5)))
        self.assertTrue(is_line_overlap((1, 5), (-4, 2)))

    def test_can_check_connected_and_same_line(self):
        self.assertTrue(is_line_overlap((1, 5), (5, 8)))
        self.assertTrue(is_line_overlap((1, 5), (0, 1)))
        self.assertTrue(is_line_overlap((-5, -1), (-5, -1)))
