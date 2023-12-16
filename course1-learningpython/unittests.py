'''Unit Tests'''
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