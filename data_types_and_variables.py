# You have rented some movies for your kids: The little mermaid (for 3 days),
#  Brother Bear (for 5 days, they love it),
#  and Hercules (1 day, you don't know yet if they're going to like it).
#  If price for a movie per day is 3 dollars, how much will you have to pay?



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


