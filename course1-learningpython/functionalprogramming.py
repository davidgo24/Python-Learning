'''what is functional programming?'''
#Functional programming is a paradigm where programs compose functions rather than mutate state (setting and updating variables).

#Functional programming is more about declaring what you want to happen, rather than how you want it to happen.
#Imperative (or procedural) programming declares what should happen, but also exactly how it should happen.

'''imperative(procedural) vs functional programming'''

#imperative - think of a recipe that gets mutated (add stuff on top of it and it changes)
num = get_a()
num = transform_a(num)
num = transform_b(num)
return num

#functional -The important distinction is that in the functional example, we don't need to mutate (change) the values of any variables. There is no statefulness.
return transform_b(transform_a(get_a()))

'''assignment #1'''

def stylize_title(document):
    pass


# Don't touch below this line


def center_title(document):
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)


def add_border(document):
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)


'''Assignment #1'''
def stylize_title(document):
    return add_border(center_title(document))
    
    
# Don't touch below this line


def center_title(document):
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)


def add_border(document):
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)

'''Functional programming vs OOP''' #- my goal will be to write an article on fucntional programming - research one primary source - pref. a book 

#OOP and functional approaches aren't even really enemies! The core pillars of OOP are:

#Encapsulation
#Polymorphism
#Abstraction
#Inheritance

#Of those four, the only 
# one that really conflicts with functional programming is inheritance (and the mutable classes that typically come along with it). 
# The other three are perfectly compatible with functional programming, and functional programmers use them all the time.

'''Immutability'''
#A core tenet of functional programming is that data should be immutable. 
# Once a value is created, it cannot be changed. This is in contrast to mutable data, which can be changed after it is created.

