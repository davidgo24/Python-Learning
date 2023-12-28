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


#i am starting to get the bigger picture

''''spring abstraction assignment'''
class Human:
    def sprint_right(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_right()
        self.move_right()

    def sprint_left(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_left()
        self.move_left()


    def sprint_up(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_up()
        self.move_up()

    def sprint_down(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_down()
        self.move_down()


    def __raise_if_cannot_sprint(self):
        if self.__stamina == 0:
            raise Exception("not enough stamina to sprint")

    def __use_sprint_stamina(self):
        self.__stamina -= 1

    # don't touch below this line

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina


'''HOW OOP DEVELOPERS THINK'''

#As we saw in the last exercise variables can be private, 
# but methods can be private as well. In other words, we can encapsulate behavior as well as data.

'''GROUPING DATA AND BEHAVIOR'''
#Classes in object-oriented programming are all about grouping data and behavior together in one place: an object.  *
# Object-oriented programmers tend to think about programming as a modeling problem. 
# They think, "how can I write a Human class that simulates the data and behavior of a real human?" **
#think of oop as building a controller with a class. this controller has a ton of buttons (methods) 

'''functional programming vs oop'''
#We aren't focusing on functional programming in this course, but to provide some contrast,
# functional programmers tend to think of their code as inputs and outputs. "When a human acts, what are the inputs to that action, and how do the outputs affect my program state?"

#While OOP isn't the only paradigm in programming, it's a tried and true one that is useful in a variety of circumstances.
# In any event, if you have an understanding of multiple ways of thinking about code, you'll be a much better developer overall.


#oop devs think of programs as a modeling problem






