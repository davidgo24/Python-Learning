'''Errors and Exceptions in python'''

#You've probably encountered some errors in your code from time to time if you've gotten this far in the course. 
# In Python, there are two main kinds of distinguishable errors.

#syntax errors
#exceptions

'''syntax error'''
#this is not valid code, so it will error ^
#SyntaxError: invalid syntax

'''Exceptions'''

#Even if your code has the right syntax, however, it may still cause an error when an attempt is made to execute it.
# Errors detected during execution are called "exceptions" and can be handled gracefully by your code.
# You can even raise your own exceptions when bad things happen in your code.

try:
  10 / 0
except Exception as e:
  print(e)

# prints "division by zero"

'''ASSIGNMENT#1'''
#One of the calls to get_player_record is throwing a player id not found exception. 
# Change the code to safely make the calls within a try-except block. If an exception is raised, print the exception instead.

def main():
        print(get_player_record(1))
        print(get_player_record(2))
        print(get_player_record(3))
        try:
            print(get_player_record(4))
        except Exception as e:
            print(e)




