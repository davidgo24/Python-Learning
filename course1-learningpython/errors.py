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
# Don't edit below this line
#code area 

def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")


main()

#TRY/EXCEPT REVIEW
#The try block is executed until an exception is raised or it completes, 
# whichever happens first. In this case, a "divide by zero" error is raised because division by zero is impossible. 
# The except block is only executed if an exception is raised in the try block. 
# It then exposes the exception as data (e in our case) so that the program can handle the exception gracefully without crashing.

#therefore
#if no exceptions are raised in the try block, the except block will not execute

def main():
        print(get_player_record(1))
        print(get_player_record(2))
        print(get_player_record(3))
        try: #this is the try block
            print(get_player_record(4))
        except Exception as e: #this is the except block 
            print(e)

'''ERROR VS BUGS'''
#a bug 
#crashing
#unexpectedly 
#solution: we must fix this code

#error
#internet lost
#expected/handle
#when an error happens, we must have code in place to handle the error. else it does become a bug in the sense that we are not handling it properly.

'''syntax for raising exceptions'''
raise Exception("something bad happened")
#asssignment 
def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")
#. When you are able to detect that something is amiss, you should be raising the errors yourself, in addition to the "default" exceptions that the Python interpreter will raise.

'''ASSSIGNMENT '''
 def handle_get_player_record(player_id):
    try:
        return get_player_record(player_id)
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e
    
    
# Don't edit below this line


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]
