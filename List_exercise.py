# create an empty list
#fruits = []
#print(fruits)

# Declare a list with more than 5 items
#fruits = ['Apple', 'Banana', 'Orange', 'Lemon', 'Watermelon', 'Pineapple']
#print(fruits)

# Find the length of your list
#fruits = ['Apple', 'Banana', 'Orange', 'Lemon', 'Watermelon', 'Pineapple']
#print(len(fruits))

# Get the first item, the middle item and the last item of the list
fruits = ['Apple', 'Banana', 'Orange', 'Lemon', 'Watermelon']
#fruit_one, fruit_two, fruit_middle, *rest, fruit_last = fruits # using unpacking items
#print(fruit_one)
#print(fruit_middle)
#print(fruit_last)
#print(fruits[0:5:2]) # using slicing

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
#mixed_data_types = ['Chandu', '25', '5.11', 'single', 'Sainagar anantapur']
#print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
#it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Print the list using print()
#print(it_companies)
# Print the number of companies in the list
#print(len(it_companies))
# Print the first, middle and last company
#print(it_companies[0:7:3])
# Print the list after modifying one of the companies
#it_companies[0] = 'AWS'
#print(it_companies)
# Add an IT company to it_companies
#it_companies.append('TCS')
#print(it_companies)
# Insert an IT company in the middle of the companies list
#it_companies.insert(4, 'capgemini')
#print(it_companies)
## Change one of the it_companies names to uppercase (IBM excluded!)
#it_companies[1] = 'GOOGLE'
#print(it_companies)
# Join the it_companies with a string '#;  '
#result = ['#;' + item for item in it_companies]
#print(result)
# join the it_companies with a string start with # and end with ;
#result = [ '#' + item for item in it_companies ]
#result = [ item + ';' for item in it_companies ]
#print(result)

# Check if a certain company exists in the it_companies list.
#it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#does_exist = 'Google' in it_companies
#print(does_exist)
#does_exist = 'Capgemini' in it_companies
#print(does_exist)

# Sort the list using sort() method
#it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#it_companies.sort()
#print(it_companies)
# Reverse the list in descending order using reverse() method
#it_companies.sort(reverse=True)
#print(it_companies)

# Slice out the first 3 companies from the list
#it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#result = it_companies[0:3:1]
#print(result)
# Slice out the last 3 companies from the list
#result = it_companies[-3:]
#print(result)
#result = it_companies[4:]
#print(result)
# Slice out the middle IT company or companies from the list
#result = it_companies[3]
#print(result)

# Remove the first IT company from the list
#it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#it_companies.remove('Facebook') # if we know the first item name in list we can remove using item name
#print(it_companies)
#remove_first_company = it_companies[0]
#it_companies.remove(remove_first_company)# if we don't know the first item name in list we can using index like this
#print(it_companies)

# Remove the middle IT company or companies from the list
#it_companies.remove('Apple')# if we know the first item name in list we can remove using item name
#print(it_companies)
#length_it_companies = len(it_companies) # finding the length of list
#middle_company = length_it_companies / 2 # to check the middle index we are dividing by 2 to get the middle index number
#print(middle_company)
#remove_middle_company = it_companies[3] # once we get middle item index number we are saving in variable
#it_companies.remove(remove_middle_company) # now we remove the item which is in middle of list
#print(it_companies)

# Remove the last IT company from the list
#it_companies.remove('Amazon')# using item name we can remove the last item in list
#print(it_companies)
#it_companies.pop() # using pop() default it will remove last item in list
#print(it_companies)
#remove_last_company = it_companies[-1]
#it_companies.remove(remove_last_company)
#print(it_companies) # using the index we can remove the last item in list.

# Remove all IT companies from the list
#it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#it_companies.clear() # using clear() method we are clearing the list items and make list empty
#print(it_companies)
# destroy the IT Companies list
#del it_companies # using del option we are completely destroy or remove the list.
#print(it_companies)

# Join the following lists:
#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']
#front_back_ends = front_end + back_end  # using + operator we join the 2 lists
#print(front_back_ends)
#front_end.extend(back_end) # using extend() method we join 2 lists
#print(front_end)

# After joining the lists in above. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
#full_stack = front_end.copy()
#print(full_stack)
#full_stack.insert(5,'Python')
#print(full_stack)
#full_stack.insert(6,'SQL')
#print(full_stack)
#full_stack = front_back_ends.copy()
#print(full_stack)
#full_stack.insert(5,'Python')
#print(full_stack)
#full_stack.insert(6,'SQL')
#print(full_stack)


# The following is a list of 10 students ages and Sort the list and find the min and max age
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#ages.sort()
#print(ages)
#min_age = ages[0]
#print(min_age)
#max_age = ages[-1]
#print(max_age)
#print(min(ages))
#print(max(ages))
#ages[0] = 18
#print(ages)
#ages[-1] = 28
#print(ages)
#ages_length = len(ages)
#print(ages_length)
# Find the median age (one middle item or two middle items divided by two)
#median_ages = ages[4] + ages[5] / 2
#print(median_ages)
# Find the average age (sum of all items divided by their number )
#avg_ages = sum(ages) / len(ages)
#print(avg_ages)
# Find the range of the ages (max minus min)
#range_ages = max(ages) - min(ages)
#print(range_ages)
# Compare the value of (min - average) and (max - average), use abs() method
#first_num = abs(min(ages) - avg_ages)
#second_num = abs(max(ages) - avg_ages)
#print(first_num, second_num)


# Find the middle country(ies) in the countries list
"""
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
 """
#length_countries = len(countries)
#print(length_countries)
#middle_countries = length_countries // 2
#print(middle_countries)
#print(countries[97])
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
#first_countries = countries[:middle_countries + 1]
#print(len(first_countries))
#print(first_countries)
#second_countries = countries[middle_countries: - 1]
#print(len(second_countries))
#print(second_countries)


# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
#countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
#first_item, second_item, third_item, *rest = countries
#print(first_item)
#print(second_item)
#print(third_item)
#print(rest)