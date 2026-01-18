# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

#str_one = 'Thirty'
#str_two = 'Days'
#str_three = 'Of'
#str_four = 'Python'
#space = ' '

#print("Combine into single string:", str_one + space + str_two + space + str_three + space + str_four)
#print("Combine into single string:", str_one + ' ' + str_two + ' ' + str_three +  ' ' + str_four)

# Declare a variable named company and assign it to an initial value "Coding For All".
#company = "Coding For All"
# Print the variable company using print().
#print(company)
# Print the length of the company string using len() method and print().
#print(len(company))
#Length = len(company)
#print(Length)
# Change all the characters to uppercase letters using upper() method.
#print(company.upper())
# Change all the characters to lowercase letters using lower() method.
#print(company.lower())


# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
#company = 'coding for all'
#print(company.capitalize()) # convert 1st letter of string into Capital letter
#print(company.title()) # convert the 1st letter of every word in string into Capital letter
#print(company.swapcase()) # convert the whole string into upper or lower based on input.

# Cut(slice) out the first word of Coding For All string.
#course = "Coding For All"
#cut_slice = course[0:6]
#print(cut_slice)
#cut_slice1 = course[7:10]
#print(cut_slice1)
#cut_slice2 = course[11:14]
#print(cut_slice2)


# Check if Coding For All string contains a word Coding using the method index, find or other methods.
#course = "Coding For All"
#print(course.find('All'))
#print(course.rfind('ll'))
#sub_str = "For"
#print(course.index(sub_str))
#print(course.rindex(sub_str))


# Replace the word coding in the string 'Coding For All' to Python.
#course = 'Coding For All'
#replaced = course.replace('Coding', 'Python')
#print(replaced)
#print(course.replace('Coding For All', 'Python'))

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
#course = "Python for Everyone"
#print(course)
#new_course = course.replace("Everyone", "ALL")
#print(new_course)
#New_Course = course[-8:]
#print(New_Course)
#courses = course.split()
#print(courses)
#result = " ".join("ALL"if word == "Everyone" else word for word in courses )
#print(result)


# Split the string 'Coding For All' using space as the separator (split())
#course = "Coding For All"
#splitting = course.split()
#print(splitting)
#splitting = course.split(',')
#print(splitting)
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
#companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
#splitted = companies.split(",")
#print(splitted)


# What is the character at index 0 in the string Coding For All.
#course = 'Coding For All'
#print(course[0])
# What character is at index 10 in "Coding For All" string.
#print(course[10])
# What is the last index of the string Coding For All.
#print(course.rindex('l'))
# Use index to determine the position of the first occurrence of C in Coding For All.
#result = course.index('C')
#print(result)
# Use index to determine the position of the first occurrence of F in Coding For All.
#print(course.index('F'))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
#print(course.rfind('l'))


# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#sentence = 'You cannot end a sentence with because because because is a conjunction'
#result = sentence.index('because')
#print(result)
#results = sentence.find('because')
#print(results)
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#print(sentence.rfind('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#print(sentence[31:54])


# Does 'Coding For All' start with a substring Coding?
#str = 'Coding For All'
#sub_str = str.startswith('Coding')
#print(sub_str)
# Does 'Coding For All' end with a substring coding?
#substr = str.endswith('Coding')
#print(substr)
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
#str_name = '   Coding For All     '
#print(str_name)
#print(str_name.strip())


# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
#first_str = '30DaysOfPython'
#print(first_str.isidentifier())
#sec_str = 'thirty_days_of_python'
#print(sec_str.isidentifier())


# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# .Join the list with a hash with space string

#libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
#result = ' # '.join(libraries)
#print(result)


# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
#first_str = 'I am enjoying this challenge'
#sec_str = 'I just wonder what is next'
#print(first_str + sec_str)
#print(first_str + '\n' + sec_str)


# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
#Name = 'Asabeneh'
#Age = 250
#Country = 'Finland'
#City = 'Helsinki'
#print("Name \t     Age \t Country \t     City")
#print(f'{Name} \t {Age} \t {Country} \t     {City}')

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
#radius = 10
#phi = 3.14
#area = phi * radius ** 2
#print(f'The area of a circle with radius {radius} is {area} meters square.')
#print("The Area of a circle with radius %d is %d meters square." % (radius, area))
#print('The Area of a circle with radius {} is {} meters square.'.format(radius, area))











