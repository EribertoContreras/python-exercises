# You have rented some movies for your kids: The little mermaid (for 3 days),
#  Brother Bear (for 5 days, they love it),
#  and Hercules (1 day, you don't know yet if they're going to like it).
#  If price for a movie per day is 3 dollars, how much will you have to pay?



from itertools import count


littleMermaid = 3
brotherBear = 5
hercules = 1
price_Per_Day = 3

total_price = (littleMermaid * price_Per_Day)+(brotherBear*price_Per_Day)+(hercules*price_Per_Day)

total_price


#teachers code



#Suppose you're working as a contractor for 3 companies:
 #Google, Amazon and Facebook, they pay you a different rate per hour.
 #  Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
 # How much will you receive in payment for this week?
 #  You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.


google_hr_pay = 400
amazon_hr_pay = 380
facebook_hr_pay = 350

google_hrs = 6
amazon_hrs = 4
facebook_hrs = 10


week_total_pay = (google_hr_pay*google_hrs)+(amazon_hrs*amazon_hr_pay)+(facebook_hr_pay*facebook_hrs)

week_total_pay


#A student can be enrolled to a class only if the class is not full,
#  and the class schedule does not conflict with her current schedule.

class_full = False
conflict_schedule = False

can_be_enrolled = True
#A product offer can be applied only if people buys more than 2 items, and the offer has not expired.
#  Premium members do not need to buy a specific amount of products.

primium_members = True
offer_expired = False
no_items = 3
product_offer = (not offer_expired and no_items > 3) or primium_members
print (product_offer)

#Continue working in your data_types_and_variables.py file. Use the following code to follow the instructions below:


username = 'codeup'
password = 'notastrongpassword'
#Create a variable that holds a boolean value for each of the following conditions:

#the password must be at least 5 characters
#the username must be no more than 20 characters
#the password must not be the same as the username
#bonus neither the username or password can start or end with whitespace

five_characters_or_more = len(password) >= 5
username_twenty_or_less = len(username) >= 20
user_password_not_same = username!= password
bonus_no_whitespace_user = username != username.strip()
bonus_no_whitespace_pass = password == password.strip()




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
output

# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

uppercase_fruits = [fruit.upper() for fruit in fruits]

uppercase_fruits

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

capatilze_fruits = [fruit.capitalize() for fruit in fruits]

capatilze_fruits

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

def vowels_check(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for vowel in vowels:
        count += word.count(vowel)
    if count > 2: return True
    return False

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if vowels_check(fruit)]

fruits_with_more_than_two_vowels

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

def two_vowels_check(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for vowel in vowels:
        count += word.count(vowel)
    if count == 2: return True
    return False

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_only_two_vowels = [fruit for fruit in fruits if two_vowels_check(fruit)]

fruits_with_only_two_vowels


# Exercise 5 - make a list that contains each fruit with more than 5 characters

fruit_five_characters_or_more = [fruit for fruit in fruits if len(fruit) >= 5]

fruit_five_characters_or_more

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

fruit_with_only_five_characters = [fruit for fruit in fruits if len(fruit) == 5]

fruit_with_only_five_characters

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

fruits_less_then_five_characters = [fruit for fruit in fruits if len(fruit) < 5]

fruits_less_then_five_characters

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

count = 0 

character_count_in_fruits = [len(fruit) for fruit in fruits]

character_count_in_fruits

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

fruits_with_letter_a = [fruit for fruit in fruits if ('a') in fruit]

fruits_with_letter_a

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

even_numbers = [number for number in numbers if number % 2 == 0]

even_numbers

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

odd_numbers = [number for number in numbers if number % 2 == 1]

odd_numbers

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

postive_numbers = [number for number in numbers if number > 0]

postive_numbers

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

negative_numbers = [number for number in numbers if number < 0]

negative_numbers

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

two_or_more_numerals = [number for number in numbers if number > 9 if number > -9]

two_or_more_numerals


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

numbers_squared = [number ** 2 for number in numbers if number]

numbers_squared

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

odd_negative_numbers  = [number for number in numbers if number % 2 ==  1 and number < 0]

odd_negative_numbers

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

number_plus_5 = [number + 5 for number in numbers]

number_plus_5

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. 
# *Hint* you may want to make or find a helper function that determines if a given number is prime or not.

primes = [number for number in numbers if (number % number) == 0]

primes
