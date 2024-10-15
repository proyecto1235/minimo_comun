import unittest
from src.lcm.Calculo import src

class TestLCM(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(src.lcm(4, 5), 20)
        self.assertEqual(src.lcm(3, 7), 21)
        self.assertEqual(src.lcm(12, 15), 60)
        self.assertEqual(src.lcm(0, 5), 0)  # El MCM con 0 es 0
        self.assertEqual(src.lcm(5, 0), 0)

if __name__ == '__main__':
    unittest.main()
