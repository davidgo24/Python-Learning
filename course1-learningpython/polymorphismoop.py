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
        
        
'''example #2: building on ex.1 - getting the edges of the rectangle'''     
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_left_x(self):
        if self.x1 < self.x2:
            return self.x1
        return self.x2
        
    def get_right_x(self):
        if self.x2 > self.x1:
            return self.x2
        return self.x1

    def get_top_y(self):
        if self.y1 > self.y2:
            return self.y1
        return self.y2

    def get_bottom_y(self):
        if self.y2 < self.y1:
            return self.y2
        return self.y1 
        
'''example #3: coninuation problem: overlapping '''
class Rectangle:
    def overlaps(self, rect):
        return (self.get_left_x() <= rect.get_right_x() and 
                self.get_right_x() >= rect.get_left_x() and
                self.get_top_y() >= rect.get_bottom_y() and
                self.get_bottom_y() <= rect.get_top_y())
        

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_left_x(self):
        if self.x1 < self.x2:
            return self.x1
        return self.x2

    def get_right_x(self):
        if self.x1 > self.x2:
            return self.x1
        return self.x2

    def get_top_y(self):
        if self.y1 > self.y2:
            return self.y1
        return self.y2

    def get_bottom_y(self):
        if self.y1 < self.y2:
            return self.y1
        return self.y2
    
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

'''example 4: continuation - hitbox'''
class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        half_height = height / 2
        half_width = width / 2
        self.__hit_box = Rectangle(
            pos_x - half_width,
            pos_y - half_height,
            pos_x + half_width,
            pos_y + half_height,
        )

    def in_area(self, x_1, y_1, x_2, y_2):
        r1 = Rectangle(x_1, y_1, x_2, y_2)
        return r1.overlaps(self.__hit_box)

