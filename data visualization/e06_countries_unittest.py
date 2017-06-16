import unittest

from e06_countries import get_country_code

class CountryCodesTestCase(unittest.TestCase):
    # Testing e06_countries.py
    # recall that you use test at the beginning of the def
    def test_get_country_code(self):
        country_code = get_country_code('Andorra')
        self.assertEqual(country_code, 'ad')

        country_code = get_country_code('United Arab Emirates')
        self.assertEqual(country_code, 'ae')

        # haha I spelled Antarctica wrong the first time
        # spelled as Antartica
        country_code = get_country_code('Antarctica')
        self.assertEqual(country_code, 'aq')

unittest.main()
        