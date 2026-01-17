
Python Operators Example Programs:
 
1.Use and operator to check if 'on' is found in both 'python' and 'dragon'

first_str = input("Enter first string: ")
sec_str = input("Enter sec string: ")
third_str = input("Enter Third string: ")
result = third_str in sec_str and third_str in first_str
print("Third string is found on both First and Second strings:",result)
Output:
Enter first string: python
Enter sec string: dragon
Enter Third string: on
Third string is found on both First and Second strings: True


2.I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

sentance = input("Enter Sentence: ")
sec_str = input("Enter sec string: ")
result = sec_str in sentence
print("Jargon is Found in Sentance:",result)
output:
Enter Sentence: i hope this course is not full of jargon
Enter sec string: jargon
Jargon is Found in Sentance: True


3.Find the length of the text python and convert the value to float and convert it to string

text = input("Enter the txt: ")
Length_text = len(text)
print("Length of str:",Length_text)
float_text = float(Length_text)
print("Convert Length of text to float:",float_text)
str_text = str(float_text)
print("Convert Float Text to String:",str_text)
output: 
Enter the txt: python
Length of str: 6
Convert Length of text to float: 6.0
Convert Float Text to String: 6.0


4.Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

first_num = int(input("Enter the First Number:"))
sec_num = 2 
remainder = first_num % sec_num
if remainder == 0: 
    print("first_num is Even Number")
else: 
    print("first_num is not an Even Number")
Output: 
Enter the First Number:100
first_num is an Even Number 
and 
Enter the First Number:99
first_num is not an Even Number


5.Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

X = 7
Y = 3
result = X // Y
print(result)
Z = int(2.7)
print(Z)
if result == Z:
    print("Both result and Z values are same.")
Output: 
2
2
Both result and Z values are same.


6.Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

daily_work_hours = int(input("Enter the Daily Working Hours:"))
rate_per_hour = int(input("Enter the Cost per hour:"))
pay_per_day = daily_work_hours * rate_per_hour

print("Payment per day:",pay_per_day)
pay_per_month = pay_per_day * 30

print("Payment per Month:",pay_per_month)
pay_per_anum = pay_per_month * 12

print("Payment per Anum:",pay_per_anum)

Output:
Enter the Daily Working Hours:9
Enter the Cost per hour:700
Payment per day: 6300
Payment per Month: 189000
Payment per Anum: 2268000


7. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years.

years_lived = int(input("Enter the years lived:"))

seconds = years_lived * 365 * 24 * 60 * 60

print("Seconds of life time lived:", seconds)

Output:
Enter the years lived:75
Seconds of life time lived: 2365200000


8. Write a Python script that displays the following table 
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125


Answer: 
a = 1
b = 2
c = 3
d = 4
e = 5

print(a,1,a * a,a ** 2,a ** 3)
print(b,1,b * a,b ** 2,b ** 3)
print(c,1,c * a,c ** 2,c ** 3)
print(d,1,d * a,d ** 2,d ** 3)
print(e,1,e * a,e ** 2,e ** 3)

or 

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
e = int(input("Enter e: "))

print(a,1,a * a,a ** 2,a ** 3)
print(b,1,b * a,b ** 2,b ** 3)
print(c,1,c * a,c ** 2,c ** 3)
print(d,1,d * a,d ** 2,d ** 3)
print(e,1,e * a,e ** 2,e ** 3)



