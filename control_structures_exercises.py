# 1)Conditional Basics

#prompt the user for a day of the week, print out whether the day is Monday or not
def is_monday():
    x = input("enter a day: ")
    if x == 'monday':
        return True
    if x == 'Monday':
        return True
    else:
        return False
        
is_monday()

#prompt the user for a day of the week, print out whether the day is a weekday or a weekend
weekday = 'Monday', 'Tuesday', 'Wednesday', 'Thurday', 'Friday'
weekend = 'Saturday', 'Sunday'

def weekend_or_weekday():
    x = input("please enter a day in lower case: ")
    if x == 'monday':
        print('weekday')
    if x == 'tuesday':
        print('weekday')
    if x == 'wednesday':
        print('weekday')
    if x == 'thurday':
        print('weekday')
    if x == 'friday':
        print('weekday')
    if x == 'saturday':
        print('weekend')
    if x == 'sunday':
        print('weekend')
        
weekend_or_weekday()

#create variables and make up values for

#the number of hours worked in one week
hours_worked_in_a_week = 40
#the hourly rate
hourly_rate = 17.50
#how much the week's paycheck will be
weeks_pay_check = (hours_worked_in_a_week * hourly_rate)
weeks_pay_check
#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

def weekly_pay_check():
    x=int(input("enter number of hours worked this week: "))
    if  x <= 40:
        return (x * 17.50)
    if x > 40:
        return (x * 40) + ((x - 40) * (23.25))
weekly_pay_check()

#2) Create an integer variable i with a value of 5.
i = 5
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i = i + 1
i

#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

l = 2
while l <= 100:
    print(l)
    l = l * 2
l 

#Alter your loop to count backwards by 5's from 100 to -10.
l = 100
for l in range(100,-15,-5):
    print(l)
l

#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
k = 2
while k <= 1000000:
    print(k)
    k = k ** k
k

# Write a loop that uses print to create the output shown below.

l = 100
for l in range(100,0,-5):
    print(l)
l

#Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.

n = 7
i = 1
for i in range(1,11):
    print(n,"x",i, "=", (n * i ))
    i <= 10 ++ i
n

#Create a for loop that uses print to create the output shown below.


for i in range(2,10):
    for n in range(1, i + 1):
        print(i, end="")

#better code

for i in range(1, 10):
    o = str(i) * int(i)
    print(o)

#break and continue

#Prompt the user for an odd number between 1 and 50.
#  Use a loop and a break statement to continue prompting
#  the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this).
#  Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.


# while true will run indefinetly
# is digit will return false for floats
while True:
    yike = input('enter an odd number from 1 - 50: ')
    if yike.isdigit():
        yike =int(yike)
        if yike % 2 == 0:
            print('sir this is not an odd number')
        else:
            print("checks out")
            break
    else:
        print("numbers please")

print("number to skip is: ", yike)

for h in range(50):
    if yike == h:
        print("Yikes! skipping number:", yike)
    elif h % 2 == 1:
        print("here is and off number:", h)




#elif means 

#The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, 
# so you'll need to convert this to a numeric type.)
#Write a program that prompts the user for a positive integer.
#  Next write a loop that prints out the numbers from the number the user entered down to 1.

def print_count_to_number(start_at, end_at, increment):
    count_out = [print(num) for num in range(start_at, end_at, increment)]


def count_to_user_number():
    user_input = input('Gimmie an positive integer: ')
    
    while True:
        if user_input.isdigit() == False:
            print(f'{user_input} ain\'t no integer')
            break

        user_int = int(user_input)
        
        if user_int > 0:
            print_count_to_number(0, user_int+1, 1)
            
        user_input = input('Give me another positive integer: ')

count_to_user_number()

#Fizzbuzz

#One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

#Write a program that prints the numbers from 1 to 100.
#For multiples of three print "Fizz" instead of the number
#For the multiples of five print "Buzz".


for num in range(1, 101):
    fb = ''
    if num % 3 == 0:
        fb += 'Fizz'
    if num % 5 == 0:
        fb += 'Buzz'
    if not fb:
        fb = num
    print(fb)

#Display a table of powers.

#Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
#Ask if the user wants to continue.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.


top_output_format = "{col_num:>8s} | {col_square:>8s} | {col_cube:>8s}"
lbl_num = '{:<8s}'.format('number')
lbl_square = '{:<8s}'.format('squared')
lbl_cube = '{:<8s}'.format('cubed')
lbl_fill = '{:-<8s}'.format('')

def output_table_of_powers(upto_number):
    print('\nTable for {}\n'.format(upto_number))
    print(top_output_format.format(col_num=lbl_num, col_square=lbl_square, col_cube=lbl_cube))
    print(top_output_format.format(col_num=lbl_fill, col_square=lbl_fill, col_cube=lbl_fill))
    for num in range(1, upto_number + 1):
        print(top_output_format.format(col_num=str(num), col_square=str(num **2), col_cube=str(num ** 3)))

        def get_user_number_for_table():
    go_on = 'Y'
    
    while go_on == 'Y':
        user_input = input('Gimmie a positive integer to power up: ')
        
        if user_input.isdigit() == False:
            print(f'{user_input} ain\'t no positive integer. How\'s about 5?')
            user_input = 5

        user_int = int(user_input)

        if user_int > 20:
            print('Sorry, I ain\'t countin\' that high. How\'s about 20?')
            user_int = 20

        if user_int < 3:
            print('Don\'t wanna go that low. How\'s about 3?')
            user_int = 3

        output_table_of_powers(user_int)
        
        go_on = input('Wanna try again? (Y/N) ').upper()
        

get_user_number_for_table()

