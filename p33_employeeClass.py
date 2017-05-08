# test exercise with unittest

class Employee():
    #initialize employee
    def __init__(self, first, last, salary):
        self.first = first.title()
        self.last = last.title()
        self.salary = salary


    #giving a raise
    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salary += amount


