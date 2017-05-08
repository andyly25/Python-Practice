import unittest
from p28_cityCountryFunction import getName

class CityCountryTest(unittest.TestCase):
    def test_getName(self):
        fname = getName('seattle', 'washington')
        self.assertEqual(fname, 'Seattle, Washington')


unittest.main()