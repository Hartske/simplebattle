import unittest
from node import Cell

class Tests(unittest.TestCase):
    # Center point test
    def test_center_point(self):
        cell = Cell()
        cell._x1, cell._x2, cell._y1, cell._y2 = 10, 52, 10, 52
        center = cell.get_center(cell._x1, cell._x2, cell._y1, cell._y2)
        self.assertEqual(
            center,
            [31, 31]
        )

    def test_center_point2(self):
        cell = Cell()
        cell._x1, cell._x2, cell._y1, cell._y2 = 52, 104, 52, 104
        center = cell.get_center(cell._x1, cell._x2, cell._y1, cell._y2)
        self.assertEqual(
            center,
            [78, 78]
        )

    def test_center_point3(self):
        cell = Cell()
        cell._x1, cell._x2, cell._y1, cell._y2 = 10, 40, 10, 40
        center = cell.get_center(cell._x1, cell._x2, cell._y1, cell._y2)
        self.assertEqual(
            center,
            [25, 25]
        )
    
    def test_center_point4(self):
        cell = Cell()
        cell._x1, cell._x2, cell._y1, cell._y2 = 10, 52, 10, 52
        self.assertEqual(
            cell._center,
            [31, 31]
        )

if __name__ == "__main__":
    unittest.main()