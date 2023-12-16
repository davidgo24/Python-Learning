'''Unit Tests- Testing and Debugging'''
# a unit test is an automated program that tests a small "unit" of a code. Usually it is a function or two

#ASSIGNMENT (code produced by me)
def total_xp(level, xp_to_add):
    level_up_increment = level * 100
    xp_for_level = level_up_increment + xp_to_add
    return xp_for_level

#UNIT TESTS ran 
from main import *

run_cases = [
    (1, 200, 300),
    (2, 50, 250),
]

submit_cases = run_cases + [
    (0, 0, 0),
    (0, 200, 200),
    (176, 350, 17950),
    (250, 100, 25100),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = total_xp(input1, input2)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

#2 LESSON TYPES
#As we talked about, there are 2 types of coding lessons on Boot.dev:

#Console output lessons
#Unit-test lessons
#CONSOLE OUTPUT LESSONS
#Only 1 file of code, usually with a comment explaining where to write your code
#When you "submit" your code, its console output must match the expected output exactly to pass
#Debug print statements will cause your code to fail submission, so remove them before submitting
#UNIT-TEST LESSONS
#2 files of code: main and main_test. You can read the tests but you can't edit them
#When you "submit" your code, the return values of your functions must match the expected values exactly to pass
#Console output is ignored, you can leave debug print statements in your code
#WHICH IS MORE COMMON?
#Going forward you'll encounter far more unit-test lessons than console output lessons, but you'll still see both from time to time. Different concepts are better suited to different types of lessons.

##--

'''PROCESS FOR SOLVING HARD CODING PROBLEMS'''
#Read the lesson first! Figure out the examples before writing your own code.
#Read the assignment. Understand the goal of the assignment before you start writing code.
#Start writing code.
#Add print() statements. Don't wait until you've written a lot of code to start testing. Add print() statements and use the Run button to see if your code is doing what you expect at each step. It's easier to find issues in small bits of code than in large blocks of code.
#Keep running, printing, and fixing until you're confident your code is working.
#Submit your code. If the assignment you're working on has unit tests, no need to remove your debugging print() statements. If the assignment you're working on is testing console output, be sure to remove your print() statements before submitting.
#Compare your code to the instructor's. You will not be penalized for looking at the solution after you have successfully completed the assignment.

'''Debugging Practice'''
#TIP
#Write a few lines of code, use testing tools such as print() to make sure you are on the right track, then keep writing code

def unlock_achievement(before_xp, ach_xp, ach_name):
    players_xp = before_xp + ach_xp
    alert_message = f"Achievement Unlocked: {ach_name}"
    '''using the print statement below to test'''
    print("Achievement unlocked:", ach_name)
    return players_xp, alert_message
    
'''Testing and Debugging Recap:'''
#1. use the print() statement consistently to test code 
#2. It is easier to find issues in small bits of code, so do not wait until the end. 

