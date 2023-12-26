'''Challenge #1: Number sum '''

#NUMBER SUM
#Write a function called number_sum(n) that adds up all the numbers from 1 to n. For example:

#number_sum(5) -> 1+2+3+4+5 -> 15

#number_sum(3) -> 1+2+3 -> 6

#my solution
def number_sum(n):
    sum_list = []
    for i in range(0, n + 1):
        sum_list.append(i)
    return sum(sum_list)
        
#alternative method
 
def number_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


'''Challenge #2: Minimum Numbers in Python'''
def find_min(nums):
    SMALLEST_NUM = float("inf")
    for i in nums:
        if i < SMALLEST_NUM:
            SMALLEST_NUM = i 
    return SMALLEST_NUM


'''Challenge #3: removing numbers'''
def remove_nonints(nums):
    new_list = []
    for num in nums:
        if type(num) == int:
            new_list.append(num)
    return new_list

'''Challenge #4: factorial scoreboard'''
#my solution 
def factorial(num):
    factorial_score = 1
    for num in range(1, num+1):
        factorial_score = num * factorial_score
    return factorial_score

#or *= multiplier can be used 

def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

        
