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
    
    class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage

'''Inheritance with Multiple Children Part 1'''

class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.name = name
        self.health = health
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows == 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target_damage = target.take_damage(10)
        
'''Inheritance with multiple children Part 2'''
class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.name = name
        self.health = health
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows == 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target_damage = target.take_damage(10)


class Wizard(Hero):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.name = name
        self.health = health
        self.__mana = mana

    def cast(self, target):
        if self.__mana < 25:
            raise Exception("not enough mana")
        self.__mana -= 25
        target.take_damage(25)
        


#You'll often find in production software that it's more likely that an inheritance tree is more wide than deep. In other words, instead of a deep tree like:
#Organism -> Animal -> Mammal -> Feline -> Cat
#Dragon -> Drake
       #-> Wyvern
       #-> Hydra
       #-> Druk

'''WHY ARE INHERITANCE TREES OFTEN WIDE INSTEAD OF DEEP?'''

#As we talked about earlier, in good software a child class is a strict subset of its parent class. 
# In a deep tree, that means the children need to be perfect members of all the parent class "types". 
# That simply doesn't happen very often in the real world. 
# It's much more likely that you'll have a base class that simply has many sibling classes that are slightly different variations of the base.

'''DRAGONS ASSIGNMENT'''

class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        hit_by_blast = []
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                hit_by_blast.append(unit)
        return hit_by_blast
    
'''Using the classes'''
#adding a method to begin fight
    
    def main():
    dragons = [
        Dragon("Green Dragon", 0, 0, 1),
        Dragon("Red Dragon", 2, 2, 2),
        Dragon("Blue Dragon", 4, 3, 3),
        Dragon("Black Dragon", 5, -1, 4),
    ]

    # don't touch above this line

    for i in range(0, len(dragons)):
        dragon = dragons[i]
        describe(dragon)

    for i in range(0, len(dragons)):
        dragon = dragons[i]
        other_dragons = dragons.copy()
        del other_dragons[i]
        dragon.breathe_fire(3, 3, other_dragons)




# don't touch below this line


def describe(dragon):
    print(f"{dragon.name} is at {dragon.pos_x}/{dragon.pos_y}")


class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        print(f"{self.name} breathes fire at {x}/{y} with range {self.__fire_range}")
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                print(f"{unit.name} is hit by the fire")


main()