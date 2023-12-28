'''Inheritance'''

#Inheritance is the defining trait of object-oriented languages.
# Non-OOP languages like Go and Rust provide encapsulation and abstraction features as almost every language does. 
# Inheritance on the other hand tends to be unique to class-based languages like Python, Java, and Ruby.

'''What is inheritance?'''
#Inheritance allows one class (aka "the child class") to inherit the properties and methods of another class (aka "the parent class").
#This powerful language feature helps us avoid writing a lot of the same code twice. It allows us to DRY (don't repeat yourself) up our code.

'''Syntax'''
#In Python, one class can inherit from another using the following syntax.
class Animal:
    # parent "Animal" class

class Cow(Animal):
    # child class "Cow" inherits "Animal"

#to use the constructor of the parent class we can use python's built-in function super()
class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

class Cow(Animal):
    def __init__(self):
        # call the parent constructor to
        # give the cow some legs
        super().__init__(4)

'''Assignment #1'''
class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows): 
        super().__init__(name) #we use the super function to reference the constructor for the parent class human. then we insert name as the argument.
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

'''When should inheritance be used?'''
#Inheritance is a powerful tool, but it is a really bad idea to try to overuse it.
# Inheritance should only be used when every instance of the child class can also be considered the same type as the parent class.
#When a child class inherits from a parent, it inherits everything. If you only want to share some functionality, 
# inheritance probably is not the best answer. In that case, you would probably just want to share some functions, 
# or maybe make a new parent class that both classes inherit from.

'''Inheritance Hierarchy'''
#There is no limit to how deeply we can nest an inheritance tree.
# For example, a Cat can inherit from an Animal that inherits from LivingThing.
# That said, we should always be careful that each time we inherit from a base class the child is a strict subset of the parent.
# You should never think to yourself "my child's class needs a couple of the parent's methods, but not these other ones" and still decide to inherit from that parent.

#example
class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if self.__num_arrows - num < 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= num


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        self.use_arrows(3)
        target_name = target.get_name()
        return f"{target_name} was shot by 3 crossbow bolts"