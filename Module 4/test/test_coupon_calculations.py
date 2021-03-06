import unittest
from coupon_calculations import calculate_price


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        #(example) self.assertAlmostEqual(calculate_price(cost, cash off, percent off),"expected result here", places=2)
        self.assertAlmostEqual(calculate_price(4.0, 5.0, 0.1), 4.996, places=2)
        self.assertAlmostEqual(calculate_price(6.0, 5.0, 0.15), 6.851, places=2)
        self.assertAlmostEqual(calculate_price(8.24, 5.0, 0.2), 8.697, places=2)
        self.assertAlmostEqual(calculate_price(6.45, 10.0, 0.1), 2.563, places=2)
        self.assertAlmostEqual(calculate_price(7.85, 10.0, 0.15), 4.013, places=2)
        self.assertAlmostEqual(calculate_price(9.24, 10.0, 0.2), 5.306, places=2)
    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(calculate_price(11.25, 5.0, 0.1), 13.913, places=2)
        self.assertAlmostEqual(calculate_price(22.0, 5.0, 0.15), 23.267, places=2)
        self.assertAlmostEqual(calculate_price(28.33, 5.0, 0.2), 27.734, places=2)
        self.assertAlmostEqual(calculate_price(14.24, 10.0, 0.1), 11.995, places=2)
        self.assertAlmostEqual(calculate_price(21.40, 10.0, 0.15), 18.221, places=2)
        self.assertAlmostEqual(calculate_price(29.21, 10.0, 0.2), 24.240, places=2)
    def test_price_under_between_thirty_fifty(self):
        self.assertAlmostEqual(calculate_price(32.0, 5.0, 0.1), 37.708, places=2)
        self.assertAlmostEqual(calculate_price(38.86, 5.0, 0.15), 42.458, places=2)
        self.assertAlmostEqual(calculate_price(45.64, 5.0, 0.2), 46.413, places=2)
        self.assertAlmostEqual(calculate_price(37.32, 10.0, 0.1), 38.013, places=2)
        self.assertAlmostEqual(calculate_price(41.25, 10.0, 0.15), 40.106, places=2)
        self.assertAlmostEqual(calculate_price(49.39, 10.0, 0.2), 45.353, places=2)
    def test_price_under_over_fifty(self):
        self.assertAlmostEqual(calculate_price(52.24, 5.0, 0.1), 45.067, places=2)
        self.assertAlmostEqual(calculate_price(68.86, 5.0, 0.15), 57.538, places=2)
        self.assertAlmostEqual(calculate_price(70.64, 5.0, 0.2), 55.663, places=2)
        self.assertAlmostEqual(calculate_price(75.32, 10.0, 0.1), 62.315, places=2)
        self.assertAlmostEqual(calculate_price(81.25, 10.0, 0.15), 64.196, places=2)
        self.assertAlmostEqual(calculate_price(105.39, 10.0, 0.2), 80.891, places=2)


if __name__ == '__main__':
    unittest.main()
