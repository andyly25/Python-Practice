def getName(city, country):
    cityCountryName = city + ", " + country
    return cityCountryName.title()

def cityCountryFunction():
    while True:
        city = input("Please enter a city: ")
        if city == 'q':
            break
        country = input("Please enter a country: ")
        if country == 'q':
            break
        name = getName(city, country)
        print("I want to go to " + name)
    

# cityCountryFunction()
