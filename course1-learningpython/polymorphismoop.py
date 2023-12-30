'''Polymorphism'''
#While inheritance is the most unique trait that object-oriented languages claim to have, polymorphism is probably the most powerful.

#Polymorphism is the ability of a variable, function or object to take on multiple forms. 
# For example, in a programming language that supports inheritance, classes in the same hierarchical tree may have methods with the same name but different behaviors.
'''Example of Shapes'''
class Creature():
    def move(self):
        print("the creature moves")

class Dragon(Creature):
    def move(self):
        print("the dragon flies")

class Kraken(Creature):
    def move(self):
        print("the kraken swims")

for creature in [Creature(), Dragon(), Kraken()]:
    creature.move()
# prints:
# the creature moves
# the dragon flies
# the kraken swims


'''example #1'''
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2 
        self.y2 = y2 
        print(f"corner1: ({x1},{y1}) corner2: ({x2},{y2})")
        
        
        
        
        
        
