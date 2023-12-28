'''abstraction'''
#Abstraction is one of the key concepts of object-oriented programming. 
# The goal of abstraction is to handle complexity by hiding unnecessary details. 

'''abstraction vs encapsulation'''
#While definitions are always changing, 
# I like to think about abstraction and encapsulation in the following way.

#Abstraction is a technique that helps us identify what information and behavior should be encapsulated, and what should be exposed.
#Encapsulation is the technique for organizing the code to encapsulate what should be hidden, and make visible what is intended to be visible.

''' SO ARE WE ENCAPSULATING OR ABSTRACTING OUR CODE WHEN WE MAKE PRIVATE DATA AND METHODS? '''
#Both. Almost always we are doing both. The process of using the double underscore is an encapsulation method. 
#The process of deciding which data deserves to be hidden behind the double underscore is an abstraction. Let's look at a concrete example.
import random

my_random_number = random.randrange(5)

class Human:
    def __init__(self, pos_x, pos_y, speed):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        tuple_position = (self.__pos_x, self.__pos_y)
        return tuple_position


