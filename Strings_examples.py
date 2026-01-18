# creating string
#letter = 'P'                # A string could be a single character or a bunch of texts
#print(letter)               # P
#print(len(letter))          # 1
#greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
#print(greeting)             # Hello, World!
#print(len(greeting))        # 13
#sentence = "I hope you are enjoying 30 days of Python Challenge"
#print(sentence)


#  Multiline string is created by using triple single (''') or triple double quotes ("""). See the example below.

#multiline_string = '''I am a teacher and enjoy teaching.
#I didn't find anything as rewarding as empowering people.
#That is why I created 30 days of python.'''
#print(multiline_string)

# Another way of doing the same thing
#multiline_string = """I am a teacher and enjoy teaching.
#I didn't find anything as rewarding as empowering people.
#That is why I created 30 days of python."""
#print(multiline_string)


# String Concatenation

#first_name = "Chandu"
#last_name = "Dude"
#full_name = first_name + " " + last_name
#print(full_name)
#print(len(full_name))

# escape sequences

#print('30 days of python programming \n started today')
#print('Days\ttopics\texercises')
#print('Day 1 \t5    \t5')
#print('Day 2 \t6    \t10')
#print('Day 3 \t10    \t15')
#print('Day 4 \t8     \t9')
#print('This is backslash symbol (\\) in python')
#print('In every programming language it starts with \"Hello, World!\"')
#print('In every programming language it starts with \'Hello, World!\'')
#print("In every programming language it starts with \"Hello, World!\" ")



# string Formatting old manner (% Operator)

# string only
#first_name = 'Chandu'
#last_name = 'Dudekula'
#course = 'Python'
#formated_string = ' I am %s %s learning %s in 30 days' %(first_name, last_name, course)
#print(formated_string)

# numeric values
#radius = 10
#pi = 3.14
#area = pi * radius ** 2
#formatted_string = 'Area of a Circle with a radius %d, is %.2f.'%(radius, area)
#print(formatted_string)
#print("Area of circle with radius %d, is %.3f." %(radius, area))

# List Values
#python_libraries = ['numpy', 'matplotlib', 'seaborn', 'django', 'flask']
#formatted_strings = 'The following are the Python Libraries:%s' %(python_libraries)
#for_string = 'These python Libraries %s having more demand.' % (python_libraries)
#print(formatted_strings)
#print(for_string)


# New String formatting (str.format)

# string only
#first_name = 'Chandu'
#last_name = 'Dudekula'
#course = 'Python'
#formatted_string = 'I am {} {} learning {} in 30 days' .format(first_name, last_name, course)
#print(formatted_string)
#print("This is {} {} learning {} in 30 days" .format(first_name, last_name, course))

# numeric values
#radius = 10
#phi = 3.14
#area = phi * radius ** 2
#formatted_string = 'The Area of circle with radius {} is {:.2f}:' .format(radius, area)
#print(formatted_string)
#print('Area of circle with radius {}, phi {} and area is {:.2f}:' .format(radius, phi, area))
#print('Area of circle with radius {}, phi {} and area is {:.3f}:' .format(radius, phi, area))


# New String interpolation/ f-string

# string only
#first_name = 'Chandu'
#last_name = 'Dudekula'
#course = 'Python'
#format_string= f'This is {first_name} {last_name} learning {course} in 30 days.'
#print(format_string)
#print(f'This is {first_name} {last_name} learning {course} in 30 days.')
#print(f'I am {first_name} {last_name} learning {course} in 30 days.')

# Numeric only
#radius = 10
#phi = 3.14
#area = phi * radius ** 2
#format_string = f'Area of Circle is {area}'
#print(format_string)
#print(f'The Area of circle is {area}')
#print(f'The Area of circle is {area:.2f}')
#print(f'The Area of circle is {area:.3f}')


# Indexing of a string Characters
#language = 'PYTHON'
#first_char = language[0]
#sec_char = language[1]
#third_char = language[2]
#print(first_char, sec_char, third_char)
#last_char = language[-1]
#print(last_char)
#seclast_char = language[-2]
#print(seclast_char)

# slicing of a string characters
#full_name = "ChanduDudekula"
#first_name = full_name[0:6] # start from zero index and upto 6 but not include 6 i.e [0-5]
#print(first_name)
#last_name = full_name[6:14]
#print(last_name)
#middle_name = full_name[3:9]
#print(middle_name)
#Last_Name = full_name[-8:]
#print(Last_Name)

# Reverse a string in python.
#Full_Name = "Chandu Dudekula"
#Reversed_Name = Full_Name[::-1]
#print(Reversed_Name)


# Skipping the characters while slicing
#full_name = "ChanduDudekula"
#first_name = full_name[0:6] # start from zero index and upto 6 but not include 6 i.e [0-5]
#print(first_name)
#last_name = full_name[6:14:2] # skip every 2nd character while slicing
#print(last_name)
#middle_name = full_name[3:9:2]
#print(middle_name)
#Last_Name = full_name[-8:]
#print(Last_Name)


# palindrome test
#palindrome = Name[::-1]
#print(palindrome == Name)
# OR Using if statement
#if palindrome == Name:
 #   print("Malayalam is a Palindrome")
#else:
 #   print("Malayalam is not a Palindrome")









