# when one class inherits from another, it takes all attributes and methods
# of the first class. Original class is the parent class and new is child
# 
# NOTE: you can import classes from a module
# eg.: from car import ElectricCar as EC
# or: from car import Car, ElectricCar
# or: import car # for everything
# You can iport modules into another
# e.g. if you made cars and electric car separate, you would need to import 
# Car into the ElectricCar file then when accessing both in main you'd need
# from car import Car
# from electric_car import ElectricCar

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

    def fill_gas_tank(self):
        print("Filling..... guzzle guzzle")


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+ "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)


class ElectricCar(Car):
    #takes in Car, but makes specific for electric cars
    def __init__(self, make, model, year):
        #initialize attributes of parent class
        super().__init__(make, model, year)
        #creates new instance of battery and stores in self.battery
        self.battery = Battery()

    # def describe_battery(self):
    #     print("This car has a "+str(self.batter_size)+ "-kWh battery.")

    #overriding parent method by calling your own method same name
    def fill_gas_tank(self):
        print("This car doesn't use gas!")



my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()