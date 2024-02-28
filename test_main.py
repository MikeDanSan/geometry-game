import unittest
from main import Point

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.point = Point(2, 8)

    def test_point_creation(self):
        self.assertIsInstance(self.point, Point, "Object should be an instance of Point class.")

    def test_point_x_attribute(self):
        self.assertEqual(self.point.x, 2, "Attribute x should be equal to 2.")

    def test_point_y_attribute(self):
        self.assertEqual(self.point.y, 8, "Attribute y should be equal to 8.")

    def test_falls_in_rectangle_true(self):
        lower_left = (1, 1)
        upper_right = (3, 10)
        self.assertTrue(self.point.falls_in_rectangle(lower_left, upper_right), "Point should fall within rectangle.")

    def test_falls_in_rectangle_false(self):
        lower_left = (3, 9)
        upper_right = (10, 20)
        self.assertFalse(self.point.falls_in_rectangle(lower_left, upper_right), "Point should not fall within rectangle.")

    def test_distance_from_point(self):
        other_point = Point(5, 10)
        expected_distance = ((2 - 5)**2 + (8 - 10)**2) ** 0.5
        self.assertEqual(self.point.distance_from_point(other_point), expected_distance, "Distance calculation is incorrect.")

    def test_distance_from_same_point(self):
        same_point = Point(2, 8)
        self.assertEqual(self.point.distance_from_point(same_point), 0, "Distance from the same point should be 0.")

    def test_distance_from_point_negative_coordinates(self):
        negative_point = Point(-2, -3)
        expected_distance = ((2 - (-2))**2 + (8 - (-3))**2) ** 0.5
        self.assertEqual(self.point.distance_from_point(negative_point), expected_distance, "Distance calculation with negative coordinates is incorrect.")

if __name__ == '__main__':
    unittest.main()