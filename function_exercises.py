# calling the max function with 1 argument, a list of numbers
# from re import A
# import string
# from tkinter import _TakeFocusValue


max([4, 2, 3, 1])

#defining maximums
maximum_number = max([4, 2, 3, 1])
print(maximum_number)

print('The max is: ' + str(max([4, 2, 3, 1])))

#incrementing fucntion 
def increment(n):
    return n + 1

increment(2)

#you can stack increments
six = increment(increment(increment(3)))

print(six)


six = increment(increment(increment(3)))
six = increment(increment(4))
six = increment(5)
six = 6

def increment(n):
    return n + 1
    print('You will never see this')
    return n + 1

increment(3)

def add(a, b):
    result = a + b
    return result

x = 3
seven = add(x, 4)
#example
add(4,5)


def shout(message):
    print(message.upper() + '!!!')

return_value = shout('hey there')
print(return_value)

#example
shout('waffles')

print(return_value)


def sayhello():
    print('Hey there!')
#example
sayhello()

sayhello()
#correct way to write function above

def sayhello(name='World', greeting='Hello'):
    return '{}, {}!'.format(greeting, name)    #formats the way you want things !!!!!

sayhello('codeup')

sayhello('codeup','what up')

#sayhello('Codeup', greeting='Salutations') # Okay other examples
#sayhello(greeting = 'Salutations', 'Codeup') # ERROR! it has to be in the right format like originally stated

#calling functions

args = ['Codeup', 'Salutations']

sayhello(*args)

#sample 


Waffles = ['syrup', 'butter']

sayhello(*Waffles)
#returns 'butter, syrup'


kwargs = {'greeting': 'Salutations', 'name': 'Codeup'}

sayhello(**kwargs)


#function scope

a_global_variable = 42

#f = fromatting style
#Newest way
print(f' some string {a_global_variable *2 }')  #use this, it is the easiest

# another way:
print('some string {}'.format(a_global_variable))

#others 
def somefunction():
    print('Inside the function: %s' % a_global_variable)

somefunction()
print('Outside the function: %s' % a_global_variable)

def somefunction():
    a_local_variable = 'pizza'
    print('Inside the function: %s' % a_local_variable)

    somefunction()
    print('outside the function: %s' % a_local_variable)

#%s means 

n = 123

def somefunction():
    n = 10
    n = n - 3
    print('Inside the function, n == %s' % n)

print('Outside the function, n == %s' % n)
somefunction()
print('Outside the function, n == %s' % n)
#returns this 
#Outside the function, n == 123
#Inside the function, n == 7
#Outside the function, n == 123


#Lambda Functions
#For functions that contain a single return statement in the function body,
#  python provides a lamdba function. This is a function that accepts 0 or more inputs,
#  and only executes a single return statement (note the return keyword is implied and not required).

add_one = lambda n: n + 1
add_one(9)
#returns 10

square = lambda n: n ** 2
square(9)







#---------------------------------------------------------------------------------------    ------------------------------------    -------------------------------












#  1)
# Define a function named is_two.
#  It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(x):

    if x == 2 or x == '2':
        return True
    else:
        return False

is_two('2')
is_two(2)

#teachers code

def is_two(n):
    return n == 2 and n == '2'

#2)Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(x):
    vowel = ['A','E','I','O','U','a','e','i','o','u']
    if x in vowel:
        return True
    else:
        return False

is_vowel('A')


#teachers code

def is_vowel(somestring):
    if type(somestring) ==str:
        result = somestring.lower() in ['a','e','i','o','u']
        return result
    else:
        return False

#3)Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(x):
    if not is_vowel(x) and x.isalpha():
        return True
    else:
        return False


#teachers code

def is_consonant(somestring):
    if type(somestring) == str:
        only_letters = somestring.isalpha()
        return only_letters and not is_vowel(somestring)
    return False

#4)Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def cap_consonant(text):
    if is_consonant(text[0]): #[]this cap first letter
        return text.capitalize()
    else:
        return text

#teachers code 

def capitalize_starting_consonant(string):
    if type(string) != str:
        return False
    first_letter = string[0]
    if is_consonant(first_letter):
        string = string.capitalize()
    return string


#5)Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.



def calculate_tip(x,y):

    return int(x) * float(y)/100

calculate_tip(100,16)




#6) Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.


def apply_discount(price, discount_percentage):
    discount = price * discount_percentage
    return price - discount

#7) Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(string1):
    if type(string1) != str:
        return 'input must be a string'
    string1 = string1.replace(',', '')
    if string1.isdigit():
        return float(string1)
    else:
        return ' input must be a string that is a number'   


#8) Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(grade):
    if type(grade) == int or type(grade) == float:
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"
    else:
        return "Input must be a number"


#9) Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowela(string1):
    if type(string1) != str:
        return False
    output = ''
    for letter in string1:
        if is_consonant(letter):
            output += letter
    return output

#10) Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
#  leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed


def normalize_name(string):
    output = ''
    string = string.lower()
    for character in string:
        if character.isidentifier() or character == ' ':
            output += character
    output = output.strip()
    output = output.replace(' ', '_')
    return output




#11) Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(string1):
    output = []
    for i, num in enumerate(string1):
        sum_so_far = sum(string1[:i + 1])
        output.append(sum_so_far)
    return output
    
#enumerate look up