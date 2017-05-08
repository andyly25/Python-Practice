#Making an object from a class is called 'instantiation' and we 
#work with instances of a class
# classes represent real world things and objects based on those

class Car():

    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        #print a statement showing the car's mileage
        print("This car has " + str(self.odometer_reading)+ " miles of it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles



car1 = Car('honda', 'fit', 2017)
print(car1.get_descriptive_name())
car1.read_odometer()
#modifying attributes with a method
car1.update_odometer(39)
car1.read_odometer()
car1.update_odometer(21)
car1.increment_odometer(100)
car1.read_odometer()