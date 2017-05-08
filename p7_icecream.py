#accepting arbitrary number of args
#the * makes an empty tuple called toppings
#if you want multiple args, keep the arbitrary at end by default
def make_icecream(size, *toppings):
    print("\nMaking a "+ str(size)+ " scoop ice cream with the "  
        "following toppings")
    for topping in toppings:
        print("- "+topping)