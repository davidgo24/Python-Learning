'''LOOPS'''

#loops are a programmers bestfriend
#they allow us to the same operation multiple times without having to write
#it explicitly each time

#for ex:
print(0)
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
#can be looped as
for i in range(0, 10):
    print(i)
#Start with i equals 0. (i in range(0)
#If i is not less than 10 (range(0, 10)), exit the loop.
#Print i to the console. (print(i))
#Add 1 to i. (range defaults to incrementing by 1)
#Go back to step 2

#*important note* for loops default to increments of 1

'''ASSIGNMENT#1'''
def print_numbers():
    '''the obj is to print the nums 0-99 to the console'''
    for i in range(0,100):
        print(i)
def print_numbers():
    '''now print the nums 0-199'''
    for i in range(0,200):
        print(i)
    