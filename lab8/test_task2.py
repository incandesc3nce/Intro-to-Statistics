import unittest
from task2 import Angle, Angle2D

class TestAngle(unittest.TestCase):
    def test_angle_constructor(self):
        angle = Angle(45, 30, 15)
        self.assertEqual(angle._Angle__degree, 45)
        self.assertEqual(angle._Angle__minutes, 30)
        self.assertEqual(angle._Angle__seconds, 15)

    def test_angle_read(self):
        angle = Angle(0, 0, 0)
        angle.read()
        # Assuming user inputs 60 for degrees, 45 for minutes, and 30 for seconds
        self.assertEqual(angle._Angle__degree, 60)
        self.assertEqual(angle._Angle__minutes, 45)
        self.assertEqual(angle._Angle__seconds, 30)

    def test_angle_display(self):
        angle = Angle(90, 15, 30)
        expected_output = "90° 15' 30\""
        self.assertEqual(angle.display(), expected_output)

    def test_angle_round(self):
        angle = Angle(120, 45, 30)
        angle.round()
        # Assuming the rounded angle is 121 degrees
        expected_output = "Округленный угол:\n121° 0' 0\""
        self.assertEqual(angle.display(), expected_output)

    def test_angle_add(self):
        angle1 = Angle(45, 30, 15)
        angle2 = Angle(60, 15, 30)
        angle1.add(angle2)
        # Assuming the sum of angles is 105 degrees
        expected_output = "Сумма углов:\n105° 45' 45\""
        self.assertEqual(angle1.display(), expected_output)


class TestAngle2D(unittest.TestCase):
    def test_angle2d_constructor(self):
        angle2d = Angle2D(45, 30, 15, 10)
        self.assertEqual(angle2d._Angle__degree, 45)
        self.assertEqual(angle2d._Angle__minutes, 30)
        self.assertEqual(angle2d._Angle__seconds, 15)
        self.assertEqual(angle2d._Angle2D__z, 10)

    def test_angle2d_read(self):
        angle2d = Angle2D(0, 0, 0, 0)
        angle2d.read()
        # Assuming user inputs 60 for degrees, 45 for minutes, 30 for seconds, and 5 for z
        self.assertEqual(angle2d._Angle__degree, 60)
        self.assertEqual(angle2d._Angle__minutes, 45)
        self.assertEqual(angle2d._Angle__seconds, 30)
        self.assertEqual(angle2d._Angle2D__z, 5)

    def test_angle2d_display(self):
        angle2d = Angle2D(90, 15, 30, 20)
        expected_output = "90° 15' 30\"\nz: 20"
        self.assertEqual(angle2d.display(), expected_output)

    def test_angle2d_round(self):
        angle2d = Angle2D(120, 45, 30, 15)
        angle2d.round()
        # Assuming the rounded angle is 121 degrees and rounded z is 15
        expected_output = "Округленный угол:\n121° 0' 0\"\nОкругленный z: 15"
        self.assertEqual(angle2d.display(), expected_output)

    def test_angle2d_add(self):
        angle2d_1 = Angle2D(45, 30, 15, 10)
        angle2d_2 = Angle2D(60, 15, 30, 5)
        angle2d_1.add(angle2d_2)
        # Assuming the sum of angles is 105 degrees and sum of z is 15
        expected_output = "Сумма углов:\n105° 45' 45\"\nСумма z: 15"
        self.assertEqual(angle2d_1.display(), expected_output)


if __name__ == '__main__':
    unittest.main()