class Dog():
    """Simple model of dog """

    # self must come before the parameters
    # every method call will auto pass self, which is reference to
    # the instance itself, gives access to attribute and methods of
    # the class
    def __init__(self, name, age):
        """initializes name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll(self):
        """Simulate rolling over"""
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
# intance.attribute is the my_dog.name, this is how you access
print("My dog name is " + my_dog.name.title()+".")
print("My dog is " + str(my_dog.age)+" years old.")
#This is how you call method from instance
my_dog.sit()
my_dog.roll()

