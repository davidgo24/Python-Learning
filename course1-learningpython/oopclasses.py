'''Classes'''
#Object Oriented programming, or "OOP" for short, is a way of writing code that relies on the concepts of classes and objects. 
#The main benefit of writing your code in an object-oriented way is to structure your program into simple, reusable pieces of code.



def get_soldier_dps(soldier):
    for x in soldier:
        return soldier["damage"] * soldier["attacks_per_second"]


def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"


'''Clean Code'''
#oop and other paradigms like functional programming are about making code easier to work with and understand.
#code that is easy to work with = clean code

#clean code is not 
#A way to make your programs run faster
#A way to make your program use less memory
#Necessary to create certain kinds of programs
#Something unique to OOP

#clean code is 
#Designed to make code easier to work with in many situations
#Something that helps humans model the real world
#A way to make finding and fixing bugs easier
#A way to make new feature development faster
#The best way to stay sane as a software engineer

#martin fowler 
#Any fool can write code that a computer can understand. Good programmers write code that humans can understand.
#-- Martin Fowler


#clean code is ... 
#easier to work with as a developer

#the primary goal of oop is ...
#to write cleaner code

'''DRY code'''
#DONT REPEAT YOURSELF code

#we do not want too much of our code doing the same thing 
#when code is duplicated, it can lead to many problems

'''Dry code in practice example'''

#recall we were working with the following code:
soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
#this code was repetitive. so we decided to refactor it.
def soldiers_dps(soldier):
    return soldier["damage"] * soldier["attack_per_second]
                                       
#bear in mind, DRY code does not make your code run faster

'''Classes'''
# A class is a special type of value in an object-oriented programming language like Python. 
# Just like a string, integer or float, a class is essentially a custom type that has some special properties.

#***An object is an instance of a class type.*** In this example, health is an instance of an integer type.
#health is an instance of the type integer here. it is a custom type. 

#in object-oriented-programming we create special classes. the classes have instances that we call objects


'''how do you create a class?'''
#use the keyword class.
#it is common convention to capitalize the name of your class

'''example of a class'''
class Soldier:
    health = 5
    
#so when we create an object class
#we create instances of the class as well. these instances are objects

'''example #2 of a class'''
class NbaPlayers:
    KOBE = 24
    LEBRON = 6
    CURRY = 30


get_players = NbaPlayers()

print(get_players.KOBE)

#the instances or objects are also referred to as properties in a class
    

'''Why are classes useful?'''

#classes are useful because they allow methods to be applied to them. in comparison to dictionaries which are standalone lists. 

'''Methods'''
# a method is a function that is associated with a class. this function has access to the objects in the class. or said as, "has access to all the properties of the objecrt"

'''the special 'SELF VALUE' '''
#methods are nested within the class declaration
#methods always take a special parameter as their first argument known as 'self'. The self variable is a reference to the object itself. by using it, we can read and update properties of the object.
object.method()

class Soldier:
    health = 5

    def take_damage(self, damage):
        self.health -= damage

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# prints "3"

'''Personal Example of how i used the 'self value''''
class NbaPlayers:
    KOBE = 24
    LEBRON = 6
    CURRY = 30
    #we want to apply a method that updates a player's number
    def change_numbers(self, number):
            self.LEBRON = number

get_players = NbaPlayers()
get_players.change_numbers(23)
print(get_players.LEBRON)
#prints the output: 23 when we call the LEBRON property

class Wall:
    armor = 10
    height = 5

    def fortify(self):
        self.armor = self.armor * 2
    #using self is needed. it helps us tell the computer that we are referencing the class itself and its property

#can also be written as the following:
    def fortify(self):
        self.armor *= 2
        
'''methods can return values'''
    #methods do not often return values, they usually mutate the objects/properties in the class. however, you in fact return values with methods.
class NBAPlayers:
    Player = 'Kobe'
    
    def player_name(self):
        return self.Player

nba_star = NBAPlayers()

NAME = nba_star.player_name(Player)
print(NAME)
    
'''method return example'''
class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        self.cost = self.height * self.armor
        return self.cost

'''words on functions'''
#WHAT IS A FUNCTION?
#A function is a piece of code that is called by a name. It can receive data to operate on through parameters and may, optionally, return data. 
# All data that is passed to a function is explicitly passed through parameters.
'''words on methods'''
#WHAT IS A METHOD?
#A method is a piece of code that is called by a name that is associated with an object. Methods and functions are similar but have two key differences.
#A method is implicitly passed the object on which it was called. In other words, you won't see all the inputs in the parameter list
#A method can operate on data that is contained within the class. In other words, you won't see all the outputs in the return statement.
'''oop debate'''
#THE OOP DEBATE
#Because functions are more explicit, some developers argue that functional programming is better than object-oriented programming. 
# In reality, neither paradigm is "better", and the best developers learn and understand both styles and use them as they see fit.
#For example, while methods are more implicit and often make code more difficult to read
# , they also make it easier to group a program's data and behavior in one place, which can lead to a more organized codebase.

#functions are explicit in terms of the inputs and outputs
#methods are implicit in terms of inputs and outputs since you use the objects from the class and they are not necessarily in explicitly declared in the parameter list

'''Constructors or initializers'''

#It's quite rare in the real world to see a class that defines properties in the way we've been doing it.
class Soldier:
    armor = 2
    num_weapons = 2
#instead we use a constructor or initializer 
class Soldier:
    def __init__(self):
        self.armor = 2
        self.num_weapons = 2


class Soldier:
    def __init__(self):
        self.armor = 2
        self.num_weapons = 2
        #this is how we create a constructor using init
        
'''example of a constructor'''
class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = self.width * self.height * self.depth

#__init__ is the name of the constructor name
#think of it as the place where you can initialize the objects you will be using as a general template for the method 

'''multiple objects'''
#if a class is just a type, then an object is just an value.
#You'll hear often that an object is an "instance" of a class. Let's look at what that word means.

#my example of a constructor

class NBAPlayers:
    def __init__(self, name, number, ranking):
        self.name = name 
        self.number = number
        self.ranking = ranking 
        self.goat = f"{self.name} number {self.number}, ranked number {self.ranking}, is the goat"

kobe_bryant = NBAPlayers(name = "kobe", number = 24, ranking = 1) #notice how we created an instance of the constuctor itself. while still being able to use the goat property. 
print(kobe_bryant.goat)
