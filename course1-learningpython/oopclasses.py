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
    
