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


'''Assignment #1'''
#return the getters 
class Wizard:
    def __init__(self, name):
        self.name = name
        self.__mana = 45
        self.__health = 65

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health
'''operating on an instance of a class'''

class Wizard:
    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health

    def get_fireballed(self):
        self.__health -= 30 

    def drink_mana_potion(self):
        self.__mana += 40 

'''completing a method'''
class Wizard:
    def cast_fireball(self, target):
        fireball_cost = 20
        if self.__mana < fireball_cost:
            raise Exception(f"{self.name} cannot cast fireball")
        print(f"{self.name} casts fireball at {target.name}")
        self.__mana -= fireball_cost
        target.get_fireballed()


'''encapsulation does not make systems more secure'''
#it is intended to be used for cleaner code. 
#so developers working with the code do not have to worry about it. 

'''encapsulation enforcing in python'''
#Python is a very dynamic language, and that makes it difficult for the interpreter to enforce some of the safeguards that languages like Go do.
# That's why encapsulation in Python is achieved mostly by convention rather than by force.

#Prefixing methods and properties with a double underscore is a strong suggestion to the users of your class that they shouldn't be touching that stuff.
# If a developer wanted to break convention, there are ways to get around the double underscore rule.

class Wall:
    def __init__(self, height):
        # this warns developers to not
        # access the `__height` property directly
        self.__height = height

    def get_height(self):
        return self.__height


'''personal practice with bank account challenge'''
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance 

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Cannot deposit zero or negative funds")
        return amount + self.balance

    def withdraw(self, amount):
        pass

bankaccount_david = BankAccount(1234, 50)
bankaccount_davidtwentyfive=bankaccount_david.deposit(25)
print(bankaccount_davidtwentyfive)


'''Bank Account Example solution by David'''

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number 
        self.__balance = initial_balance 

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance 

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Cannot deposit zero or negative funds")
        self.__balance += amount #use the increment tool to add to the initial balance - initially i was returning the calculation only so it was not reflecting on the initial balance

    def withdraw(self, amount): 
        if amount <= 0:
            raise ValueError("Cannot withdraw zero or negative funds")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount #use the decrement tool to subtract from the initial balance count
            
'''Student Records assignment by david'''
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.__courses = {}
        

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        elif (score >= 80 and score <=89):
            return "B"
        elif (score >=70 and score <=79):
            return "C"
        elif (score >=60 and score <69):
            return "D"
        return "F"

    def add_course(self, course_name, score): 
        #It should calculate_letter_grade based on the score. 
        #It should set the course_name as a key in the courses dictionary and the calculated letter grade as the corresponding value.
        letter_grade = self.calculate_letter_grade(score) #make sure to include self
        self.__courses[course_name] = letter_grade
        

    def get_courses(self):
        #It should return the private __courses dictionary.
        return self.__courses
    
    
'''a few words on why we use self'''

# #Method Invocation: When you call a method on an instance of a class,
# you don't explicitly pass the instance as an argument. Python automatically does this for you.
self.calculate_letter_grade(score)
Student.calculate_letter_grade(self, score)
