'''Python Numbers'''
#in Python, numbers without a decimal are integers - integers are whole numbers: 3, -3
#arithmetic can be performed
2 + 1
# 3
2 - 1
# 1
2 * 2
# 4
3 / 2
# 1.5 (a float)
#FLOATS
#my_int = 5 - integer
#my_float = 5.5 - float

#integers and floats are number types in python

#ASSIGNMENT #1 - 
#Complete the missing sections of the calculate_damage function.
#Fix the total_damage variable so that it contains the sum of all the different weapons' damage values.
#Fix the average_damage variable so that it contains the average weapon damage.

def calculate_damage(sword, arrow, spear, dagger, fire):
    total_damage = sword + arrow + spear + dagger + fire
    print("total damage:", total_damage)
    average_damage = (total_damage / 5)
    print("average damage:", average_damage)
    return total_damage, average_damage


#Python has great out-of-the-box support for mathematical operations. 
# This, among other reasons, is why it has had such success in artificial intelligence, 
# machine learning, and data science applications.

#FLOOR Division 
7 // 3
# 2 (an integer)
#Floor division is like normal division except the result is floored afterward, which means the remainder is removed. 

#EXPONENTS

#Python has built-in support for exponents - something most languages require a math library for.
 # reads as "three squared" or
# "three raised to the second power"
3 ** 2
# 9

#REASSIGNMENT USINGPLUS EQUALS AND OTHER OPS
#python makes reassignment easy when doing math. In JavaScript or Go you might be
# familiar with the ++ syntax for incrementing a number variable. In Python, we use the += operator instead.

star_rating = 4
star_rating += 1
# star_rating is now 5
star_rating = 4
star_rating -= 1

# star_rating is now 3

star_rating = 4
star_rating *= 2
# star_rating is now 8

star_rating = 4
star_rating /= 2
# star_rating is now 2

#ASSIGNMENT#2
#Complete the get_hurt function. It should use the -= operator to subtract damage
# from current_health and then return the new current_health.
def get_hurt(current_health, damage):
    current_health -= damage # instead of writing it as new_health = damage + current_health 
    print("current health:", current_health)
    return current_health

#Scientific Notation
#You can add the letter e or E followed
# by a positive or negative integer to specify that you're using scientific notation.
print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071

print(8.2e-3)
#Print 0.0082
#If you're not familiar with scientific notation,
# it's a way of expressing numbers that are too large or too small to conveniently write normally.

#UNDERSCORES FOR READABILITY
#Python also allows you to represent large numbers in the decimal format using underscores 
# instead of commas to make it easier to read.
num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000

#ASSIGNMENT#3
#Due to the constraints of our app's server, there is a maximum number of players we can have on a single "Fantasy Quest" server.

#Complete the max_players_on_server function. It takes no inputs, but simply returns 3 static values:

#The max players on a "small" server: 1,024,000,000,000,000,000 (1.024e18)
#The max players on a "medium" server: 10,240,000,000,000,000,000
#The max players on a "large" server: 102,400,000,000,000,000,000

def max_players_on_server():
    small_server = 1.024e18
    medium_server = 1.024e19
    large_server = 1.024e20
    print(small_server, medium_server, large_server)
    return small_server, medium_server, large_server

#LOGICAL Operators
#Logical operators deal with boolean values, True and False.
#True AND True is True
#True AND False is False
#False AND False is False

#True OR True is True
#True OR False is True
#False OR False is False

#Python Syntax
print(True and True)
# prints True

print(True or False)
# prints True

#Nesting with Parentheses
print((True or False) and False)
#returns false becuase of second logical operator

#Binary Numbers
#you can think of it multiple ways 
#note base 10 (0-9) can be thought of as breaking down cash in your experience
#base 2 / binary 
#can be thought of as running out of places when using 0 and 1. (every double of base 2 is raising squaring the binary )
#practice thinking og whrere there is white space with 0s to fill

#For 0-9
#0000 = 0
#0001 = 1
#0010 = 2
#0011 = 3
#0100 = 4

#BINARY IN PYTHON
#You can write an integer in Python using binary syntax using the 0b prefix
print(0b0001)
# Prints 1
print(0b0100)
#Print 4
print(0b1000)
#Print 8
print(0b0101)
# Prints 5

#The following is simply showing you how to operate with binary 
0101 = 5
&
0111 = 7
=
0101 = 5

#read: FALSE AND TRUE = FALSE 

#BINARY NOTATION
#When writing a number in binary, the prefix 0b is used to indicate that what follows is a binary number.(BINARY OP IS TOP TO BOTTOM)

0b0101 is 5
0b0111 is 7

#remember 1 = TRUE and 0 = FALSE


#IMPORTANT**

#THE BINARY AND OPERATION WILL ALWAYS REDUCE THE TOTAL # OF 1'S IN THE RESULT
#THIS IS CALLED MASKING OR FILTERING.
#FOR EXAMPLE 

#lets say we have a number 
01011110001111

#say we only wat to keep the first 5 values
#we can mask it by doing the following
01011110001111
&
01011000000000
=
01011000000000

#ASSIGNMENT: GUILD "AKA TEAM" PERMISSIONS
#At sometimes is the case that applications store user permissions as binary values. Think about it, if I have 4 different permissions a user can have, then I can store that as a 4-digit binary number, and if a certain bit is present, I know the permission is enabled. This can be a lot more efficient than storing entire strings.
#Let's pretend we have 4 permissions related to "guilds" in Fantasy Quest ("guild" is just a fancy videogame word for "team"):

#can_create_guild - Leftmost bit (0b1000)
#can_review_guild - Second to leftmost bit (0b0100)
#can_delete_guild - Second to rightmost bit (0b0010)
#can_edit_guild - Rightmost bit (0b0001)
#If a user has no permissions, their binary permissions would be 0b0000.

#If a user only has the can_create_guild permission, their binary permissions would be 0b1000, but a user with can_review_guild and can_edit_guild permissions would be 0b0101.

#To check for, say, the can_review_guild permission, we can perform a bitwise AND operation on the user's permissions and the enabled can_review_guild bit (0b0100). If the result is 0b0100 again, we know they have that specific permission!

_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def can_create_bits(user_permissions):
    return user_permissions & can_create_guild 


def can_review_bits(user_permissions):
    return user_permissions & can_review_guild 

def can_delete_bits(user_permissions):
    return user_permissions & can_delete_guild 


def can_edit_bits(user_permissions):
    return user_permissions & can_edit_guild
