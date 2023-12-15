'''#Module 4: Scope'''
#Scope refers to where a variable or 
#function name is available to be used

#Example
def subtract(x, y):
    return x - y
result = subtract(5, 3)
print(x)
# ERROR! "name 'x' is not defined"

#Assignment Solution
def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

max_health = get_max_health(my_modifier, my_level)


 
''' Global Scope '''
#when we define a variable or a function, 
# that name is accessible in every other place in our program, even within other functions.

#Example 
pi = 3.14

def get_area_of_circle(radius):
    return pi * radius * radius
#pi was declared in the parent "global" scope
#therefore it is usable in the function

#ASSIGNMENT
#we needed to declare the var player_level globally
player_level = 4

def calculate_health(modifier):
    return player_level * modifier


def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level

'''Scope Recap'''
#1. We discuessed scope related to where variables or function names
#are available to be used.
#2. variables inside functions operate within the local function scope.
#3. parent "global" scope variables can be used inside functions. 