'''LOOPS'''

#loops are a programmers bestfriend
#they allow us to the same operation multiple times without having to write
#it explicitly each time

#for ex:
print(0)
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
#can be looped as
for i in range(0, 10):
    print(i)
#Start with i equals 0. (i in range(0)
#If i is not less than 10 (range(0, 10)), exit the loop.
#Print i to the console. (print(i))
#Add 1 to i. (range defaults to incrementing by 1)
#Go back to step 2

#*important note* for loops default to increments of 1

'''ASSIGNMENT#1'''
def print_numbers():
    '''the obj is to print the nums 0-99 to the console'''
    for i in range(0,100):
        print(i)
def print_numbers():
    '''now print the nums 0-199'''
    for i in range(0,200):
        print(i)
    

'''For Loop Range'''
#The range() function we've been using in our for loops actually has an optional 3rd parameter: the "step".

for i in range(0, 10, 2):
    print(i)
# prints:
# 0
# 2
# 4
# 6
# 8

'''Range Continued'''
def count_down(start, end):
    for i in range(start, end, -1):
        print(i)
        #counts from start to end arguments by -1
'''F-Strings in Python'''
#you can create a string with dynamic values by using f-strings
num_bananas = 10
print(f"You have {num_bananas} bananas")

'''#2'''
def check_for_meals_and_retirement(starting_age, ending_age):
    for age in range(starting_age, ending_age):
        if age < 8:
            print(f"You qualify for free meals. You are {age} years old.")
        elif age > 65:
            print(f"You qualify for retirement. You are {age} years old.")
    
'''increment and decrement'''

number_of_enemies = 10
number_of_enemies += 2
# number_of_enemies is 12
number_of_enemies = 10
number_of_enemies -= 2
# number_of_enemies is 8
'''#3'''
def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total
'''#4'''
def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total
'''Optional Challenges'''
#Rocket Launch
def countdown_to_blastoff():
    for num in range(10, 0, -1):
        if num > 1:
            print(f"{num}. . .")
        elif num == 1:
            print(f"{num}. . . Blastoff!")

#SQUARING Numbers
def calculate_squares(start, end):

    for num in range(start, end):
        num_squared = num ** 2 ## using the ** operator
        print(f"{num} squared = {num_squared}")
#the importance of having a counter and using increment (pretend you are adding to a scoreboard)
def calculate_experience_points(level):
    xp = 0 
    for num in range(level):
        xp += num * 5
    return xp

#DISCOVER PRIME NUMBER TOOL
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

#not the % divides and outputs a remainder