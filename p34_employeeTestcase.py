import unittest
from p33_employeeClass import Employee


class EmployeeClassTest (unittest.TestCase):

    def setUp(self):
        ## This is my first attempt, pretty bad
        # self.first = 'Bob'
        # self.last = 'Marley'
        # self.salary = 60000
        # # self.aRaise = None
        # # self.aRaise = 10000
        self.bob = Employee('bob', 'marley', 65000)



    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.bob.give_raise()
        self.assertEqual(self.bob.salary, 70000)


    def test_give_custom_raise(self):
        self.bob.give_raise(10000)
        self.assertEqual(self.bob.salary, 75000)

unittest.main()