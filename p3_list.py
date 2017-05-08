house = ['door', 'kitchen', 'rooms', 'bathroom']
print(house)
#note that lists, arrays and stuffs starts from 0,1,2,...
#you can access last item in the list with -1
#can't use if empty list, returns an error
print(house[1])
print(house[-1])
print(house[2].title())
#modifying the list
house[0] = 'closet'
print(house)
#adding to end of list
house.append("door")
print(house)
#inserting a new element in
house.insert(2, "garage")
print(house)
#remove element
del house[0]
print(house)
#Popping, you can pop() from anyposition as well .pop(2)
house_pop = house.pop()
print(house)
print(house_pop)
#remove() only for the first instance, need loop if to get rid all
no_room = 'garage'
house.remove(no_room)
print(house)
#sorting
colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)
#len() for length of list
print(len(colors))

#loop to go through list
cars = ['toyota', 'honda', 'chevy', 'ford']
for car in cars:
	print("Do you like to buy a ... " + car.title() + "?")
	print("knowing you, a " + car.title() + " is too expensive. \n")
print("Well... that ends the car show today!")

#range 
for value in range(1,5):
	print(value)

nums = list(range(1,7))
print(nums)

even_nums = list(range(2,11,2))
print(even_nums)

odd_nums = list(range(5,16,2))
print(odd_nums)

square_num = []
for val in range(1,11):
	square = val**2
	square_num.append(square)
	#or just square_num.append(val**2) for concise
print(square_num)

#list comprehensions
squares_lc = [value**2 for value in range(1,11)]
print(squares_lc)

#basic statistics
digits = range(0,11)
print(min(digits))
print(max(digits))
print(sum(digits))

numShift = [value+1 for value in range(1,11)]
print(numShift)

#slicing
fruits = ['apple', 'pear', 'banana', 'orange', 'pineapple']
print(fruits[1:4]) #grab in between pos 1 and 4
print(fruits[2:]) #grab pos2 and up
print(fruits[:4]) # grab pos4 and before
print(fruits[-2:]) # last two fruits in list
print(fruits[:-2]) #before last two elements

favFruit = [fruit.title() for fruit in fruits[2:5]]
print(favFruit)

#copying lists
friends_fruit = fruits[:]
fruits.append("durian")
friends_fruit.append("mango")
print('my fruits are: ')
print(fruits)
print('my friends fruits are ')
print(friends_fruit)

#Tuples
#tuples are unchangeable so the list remains as is, raises error is try
#can still loop through as if a normal list
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#Writing over a tuple
print('original dimensions: ')
for dimension in dimensions:
	print (dimension)

dimensions = (400,100)
print("modified dimensions: ")
for dimension in dimensions:
	print (dimension)

	



