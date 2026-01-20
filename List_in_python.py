# lists in python

# find the length of each list below declared
#fruits = ['Banana', 'Orange', 'Apple', 'Mango']
#colors = ['Red', 'Yellow', 'Green', 'Blue', 'White', 'Black']
#animal_products = ['milk', 'meat', 'butter', 'yoghurt']
#web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']
#countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

#print(" Length of Fruits:", len(fruits))
#print(" Fruits Lists:",fruits)
#print(" Length of Colors:", len(colors))
#print(" Colors List:",colors)
#print(" Length of Animals Products:", len(animal_products))
#print(" Animals Products:",animal_products)
#print(" Length of Web Techs:", len(web_techs))
#print(" Web Techs List:",web_techs)
#print(" Length of Countries:", len(countries))
#print(" Countries List:",countries)


# Access the list items using for loop
#fruits = ['Banana', 'Orange', 'Mango', 'Apple']
#for fruit in fruits:
#   print(fruit)

# Access the list items using both positive and negative index
#fruits = ["Banana","Orange","Apple","Mango"]
#print("Fruit Name:",fruits[0])
#print(fruits[0])
#print("Fruit Name:",fruits[1])
#print(fruits[1])
#print("Fruit Name:",fruits[-1])
#print(fruits[-1])
#print("Fruit Name:",fruits[-2])
#print(fruits[-2])


# unpacking the list items and access them one by one without using index
#fruits = ["Banana", "Orange", "Apple", "Mango", "lemon", "pineapple"]
#first_fruit, second_fruit, third_fruit, fourth_fruit, *rest = fruits
#print(first_fruit)
#print(second_fruit)
#print(third_fruit)
#print(fourth_fruit)
#print(*rest)

#first, second, third, fourth, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
#print(first)
#print(second)
#print(third)
#print(fourth)
#print(*rest)
#print(tenth)

#countries = ["India", "china", "Russia", "Brazil", "South Africa", "Dubai", "Canada", "Greece"]
#In, Ch, Ru, Bz, *rest, Gr = countries
#print(In)
#print(Ch)
#print(Ru)
#print(Bz)
#print(*rest)
#print(Gr)


# Positive Index slicing for the Lists
#fruits = ['Banana', 'Orange', 'Apple', 'Mango', 'Lemon', 'Pineapple']
#print(fruits[::-1]) # reverse the list
#print(fruits[1:3]) # it won't include the 1st index
#print(fruits[0:6]) # all items in list
#print(fruits[::2]) #here it will take every second item [ banana, apple, lemon]
#print(fruits[2:])
#print(fruits[3:])
# Negative index slicing for the lists
#print(fruits[-6:]) # all items in list
#print(fruits[-4:-1])
#print(fruits[-6:-2]) # it will return after -2 index values like -3,-4,-5 and -6
#print(fruits[-5:]) # it will return upto -5 index items in the list
#print(fruits[::-1]) # reverse the list


# Modifying the list
#fruits = ['Banana', 'Orange', 'Apple', 'Mango', 'Lemon', 'Pineapple']
#fruits[0] = 'Grapes'
#print(fruits)
#fruits[1] = 'Watermelon'
#print(fruits)
#fruits[4] = 'pomegranate'
#print(fruits)
#last_index = len(fruits) - 1
#fruits[last_index] = 'muskmelon'
#print(fruits)


# checking an item is in list or not.
#fruits = ['Banana', 'Orange', 'Apple', 'Mango', 'Lemon', 'Pineapple']
#does_exist = 'Banana' in fruits
#print(does_exist)
#does_exist = 'watermelon' in fruits
#print(does_exist)


# Adding item into list using append().
#fruits = ['Banana', 'Orange', 'Apple', 'Mango', 'Lemon', 'Pineapple']
#fruits.append('Grapes')
#print(fruits)
#fruits.append('Muskmelon')
#print(fruits)

# inserting a single item in a list using insert()
#fruits = ['Banana', 'Orange', 'Apple', 'Mango', 'Lemon']
#fruits.insert(2, 'Pineapple')
#print(fruits)
#fruits.insert(4,'Grapes')
#print(fruits)
#fruits.insert(-2, 'Watermelom') # inserting item using negative index.
#print(fruits)

# Remove the items in list using remove()
#fruits = ['Banana', 'Orange', 'Apple', 'Mango', 'Lemon', 'Pineapple']
#fruits.remove('Pineapple')
#print(fruits)
#fruits.append('Pineapple')
#print(fruits)
#fruits.remove('Orange')
#print(fruits)

# remove the items in list using pop()
#fruits = ['Banana', 'Orange', 'Apple', 'Mango', 'Lemon', 'Pineapple']
#fruits.pop()
#print(fruits)
#fruits.pop(4)
#print(fruits)
#fruits.insert(4, 'Watermelon')
#print(fruits)
#fruits.remove('Watermelon')
#print(fruits)

# remove the items in list using del[] method.
#fruits = ['Banana', 'Orange', 'Apple', 'Mango', 'Lemon', 'Pineapple']
#del fruits[2]
#print(fruits)
#fruits.insert(2,'Apple')
#print(fruits)
#del fruits[1:4] # it delete the 1,2,3 indexs in list it wont delete 4th index.
#print(fruits)
#fruits.insert(1,'Orange')
#print(fruits)
#fruits.insert(2,'Apple')
#print(fruits)
#del fruits
#print(fruits) # it will give error as name fruits is not defined

# Clear the list items using clear()
#fruits = ['Banana', 'Orange', 'Apple', 'Mango', 'Lemon', 'Pineapple']
#fruits.clear()
#print(fruits)

# copying a list and saving into variable.
#fruits = ['Banana', 'Orange', 'Apple', 'Mango', 'Lemon']
#fruits_copy = fruits.copy()
#print(fruits_copy)

# Concatnate or joining the list using + operator
#positive_numbers = [1,2,3,4,5]
#zero = [0]
#negative_numbers = [-1,-2,-3,-4,-5]
#integers = negative_numbers + zero + positive_numbers
#print(integers)
#fruits = ['Banana', 'Orange', 'Mango', 'Pineapple']
#vegetables = ['onions', 'carrot', 'beetroot']
#fruits_vegetables = vegetables + fruits
#print(fruits_vegetables)

# Join the lists using extend() Method
#num2 = [4,5,6]
#num1.extend(num2)
#print(num1)
#positive_numbers = [1,2,3,4,5]
#zero = [0]
#negative_numbers = [-1,-2,-3,-4,-5]
#negative_numbers.extend(zero)
#negative_numbers.extend(positive_numbers)
#print("Integers:", negative_numbers)
#fruits = ['Banana', 'Orange', 'Mango', 'Pineapple']
#vegetables = ['onions', 'carrot', 'beetroot']
#fruits.extend(vegetables)
#print("Fruits and Vegetables:",fruits)

# Count the number of times an item repeat in the list
#fruits = ['Banana', 'Orange', 'Mango', 'Pineapple']
#count = fruits.count('Pineapple')
#print(count)
#numbers = [0,20,15,24,18,0,15,18,34,90,0]
#count = numbers.count(0)
#print(count)

# check the index of an item in list using index()
#fruits = ['banana','apple','mango','lemon','pineapple']
#print(fruits.index('apple'))
#print(fruits.index('mango'))
#print(fruits.index('pineapple'))
#numbers = [1,2,3,4,5]
#print(numbers.index(1))
#print(numbers.index(5))

# Reverse the list order using reverse() method
#fruits = ['banana','apple','mango','lemon','pineapple']
#fruits.reverse()
#print(fruits)
#Reversed_fruits = fruits[::-1]# using index we are reversing the list
#print(Reversed_fruits)

# Sorting list items using sort() method
#fruits = ['banana','apple','mango','lemon','pineapple']
#fruits.sort()
#print(fruits)
#fruits.sort(reverse=True)
#print(fruits)
#numbers = [9,2,7,4,1,0,5,8]
#numbers.sort()
#print(numbers)
#numbers.sort(reverse=True)
#print(numbers)






