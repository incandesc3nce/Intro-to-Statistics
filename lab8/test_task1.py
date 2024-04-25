import unittest
from task1 import Angle

class TestAngle(unittest.TestCase):
  def test_read(self):
    angle = Angle(0, 0, 0)
    angle.read()
    self.assertEqual(angle.__degree, 0)
    self.assertEqual(angle.__minutes, 0)
    self.assertEqual(angle.__seconds, 0)

  def test_display(self):
    angle = Angle(45, 30, 15)
    self.assertEqual(angle.display(), "45° 30' 15''")

  def test_round(self):
    angle = Angle(45, 30, 15)
    angle.round()
    self.assertEqual(angle.__degree, 45)
    self.assertEqual(angle.__minutes, 30)
    self.assertEqual(angle.__seconds, 0)

  def test_add(self):
    angle1 = Angle(45, 30, 15)
    angle2 = Angle(15, 45, 30)
    angle1.add(angle2)
    self.assertEqual(angle1.__degree, 61)
    self.assertEqual(angle1.__minutes, 15)
    self.assertEqual(angle1.__seconds, 45)

if __name__ == '__main__':
  unittest.main()
