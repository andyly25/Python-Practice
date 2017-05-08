#first we import unittest
import unittest
from p25_testName import get_formatted_name

#Now we create a class containing a series of test for get_formatted_name
#must inherit from unittest.Testcase so Python knows how to run the tests
class NamesTestCase(unittest.TestCase):
    #tests for p26_names.py
    #we're verifying if the first and last name are formatted correctly
    #Any method that starts with test_ will run automatically

    def test_first_last_name(self):
        # Do names like 'Charles Dickens' work?
        formatted_name = get_formatted_name('charles', 'dickens')
        # we use the assert method to verify that a result matches what we want
        self.assertEqual(formatted_name, 'Charles Dickens')

    #now lets write a second test for middle name
    def test_first_last_middle_name(self):
        # DO names like 'Abra Kadabra Alakazam' work?
        formatted_name = get_formatted_name(
            'abra', 'alakazam', 'kadabra')
        self.assertEqual(formatted_name, 'Abra Kadabra Alakazam')

#After running and receiving the results
#the single dot means a single test passed
#0K means all unit tests in the test case passed
unittest.main()
