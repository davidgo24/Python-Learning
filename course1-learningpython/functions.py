'''Functions allow us to reuse and organize code.'''
#example
def area_of_circle(r):
    pi = 3.14
    return pi * r * r
#this function takes one input 
# which can also be called a "parameter" or "argument") 
# and returns one output.
'''The return keyword tells the function to 
return the value of the expression that follows it.'''

'''To use or "call" this function we can now pass in any 
number as the input (in this case, the radius), 
and capture the output into a new variable:'''
radius = 5
area = area_of_circle(radius)
print(area)
# 78.5

'''MULTIPLE PARAMETERS'''
#Functions can have multiple parameters (aka inputs)
def create_introduction(name, age, height, weight):
    first_part = "Your name is", name, "You are", age, "years old."
    second_part = "You are", height, "meters tall and weigh", weight, "kilograms."
    full_intro = first_part + " " + second_part
    return full_intro

'''WHERE TO DECLARE FUNCTIONS'''
#Lines of code execute in order from top to bottom, 
#so a variable needs to be created before it can be used. 
#That means that if you define a function,
#you can not call that function until after the definition.

'''ORDER OF FUNCTIONS'''
#All functions must be defined before they're used.
#Most Python developers solve this problem by 
# defining all the functions in their program first,
# then finally calling the "entry point" function last.
# Conventionally this "entry point" function is usually
# called main to keep things simple and consistent.
def main():
    func2()

def func2():
    func3()

def func3():
    print("I'm function 3")

# call entrypoint last
main()

'''Assigment #1'''
#create a function that converts hours to seconds
def hours_to_seconds(hours):
    conversion = hours * 60 * 60
    return conversion

#test

def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(2.5)
test(100)
test(33)

'''None Return '''
#When no return value is specified in a function, (for example, maybe it's a function that prints some text to the console,
# but doesn't explicitly return a value) it will automatically return None. The following code snippets all return the same same value,
# None:
def my_func():
    print("I do nothing")
    return None
def my_func():
    print("I do nothing")
    return
def my_func():
    print("I do nothing")
    
'''Multiple Return Values'''
##In Python, we can return more than one value from a function. 
# All we need to do is separate each value we are returning by a comma, 
# and when we call the function, we need to capture all the returned values in individual variables.

# returns email, age, and status of the user
def get_user():
    return "name@domain.com", 21, "active"

# (How to SET Variables after function is created) sets email, age, and status to values returned from get_user() function
email, age, status = get_user()
print(email, age, status)
# name@domain.com 21 active

'''PARAMETERS VS ARGUMENTS'''
#Parameters are the names used for inputs when defining a function. Arguments are the names of the inputs supplied when a function is called.
# a and b are parameters (definition)
def add(a, b):
    return a + b

# 5 and 6 are arguments (applicaiton)
sum = add(5, 6)

'''DEFAULT VALUES FOR FUNCTION ARGUMENTS'''
#Python has a way to specify a default value for function arguments.
# This can be convenient if a function has arguments that are essentially 
# "optional", and you as the function creator want to use a specific default value in case the caller doesn't provide one.
def get_greeting(email, name="there"):
    return "Hello", name, "welcome! You've registered your email:", email
msg = get_greeting("lane@example.com", "Lane")
# Hello Lane, welcome! You've registered your email: lane@example.com

#If the second parameter is omitted, the default "there" value will be used in its place. 
msg = get_greeting("lane@example.com")
# Hello there, welcome! You've registered your email: lane@example.com

#ASSIGNMENT: DEFAULT VALUES FOR FUNCTION ARGUMENTS
def get_punched(health, armor=0): 
    new_health = health - 50
    after_heal = new_health + armor
    return after_heal

def get_slashed(health, armor=0):
    new_health = health - 100
    after_heal = new_health + armor
    return after_heal

