'''Encapsulation'''
#Encapsulation is one of the strongest tools in your tool belt as a software engineer. 
# As we covered in chapter one, writing code that machines understand is easy, but writing code that humans can understand is very difficult.
#Encapsulation is the practice of hiding information inside a "black box" so that other developers working with the code don't have to worry about it.

'''example of a basic example of encapsulation and how it can help '''
acceleration = calc_acceleration(initial_speed, final_speed, time)
#In the example above, to use the calc_acceleration function, we don't need to understand what goes on inside. 
# That's the goal of encapsulation, it makes our lives easier as developers and helps us write cleaner code.

'''encapsulation in oop'''
#In the context of object-oriented programming, we can practice good encapsulation by using private and public members.

'''encapsulation in python'''
#To enforce encapsulation in Python, developers prefix properties and methods that they intend to be private with a double underscore.

class Wall:
    def __init__(self, height):
        # this stops us from accessing the __height
        # property directly on an instance of a Wall
        self.__height = height

    def get_height(self):
        return self.__height

#In the example above, we don't want users of the Wall class to be able to change its height.
# We make the __height property private and expose a public get_height method so that users can still read the height of a wall without being
# tempted to update it. This will stop developers from being able to do something like:
# front_wall is an instance of a Wall
front_wall.__height = 10 # this results in an error


