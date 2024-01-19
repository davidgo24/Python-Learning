'First Class Functions'



'Anonymous Functions aka Lambda Functions'

#we do not declare a name when writing a lambda function. this is the reason they are referred to as anonymous functions.
#it is similar to writing a math formula. With the exception that the formila
#can be customized and written to fit the desired outcome
#the key is that it allows you create functions quickly and pass them around as a data.
# lambda fcns are data in the form of a function. Functions as values. 


#Assignment #1 - using lambda functions 

#david's solution
def categorize_file(filename):
    get_category = lambda extension: 'Text' if '.txt' in extension else 'Document' if '.docx' in extension else 'Code' if '.py' in extension else 'Unknown'
    
    return get_category(filename[filename.rfind(".") :]) #returns the result of calling the anon fcn get_cat()
#lamba functions remind me of single variable expressions in math


#can also be written as:

def categorize_file(filename):
    get_category = lambda extension: {
        ".txt": "Text",
        ".docx": "Document",
        ".py": "Code",
    }.get(extension, "Unknown")

    return get_category(filename[filename.rfind(".") :])

'''First Class and Higher Order Functions'''

#a programming language is said to support first-class 
#functions in that language are treated like any other variable 
#the function can be passed as an argument to other functions, 
#can be returned by another function and can be assigned as a value to a variable 

'''first-class function'''
#a function that is treated like any other value 

def square(x):
    return x * x

# assigns function to a variable 


'''higher-order function'''
#a function that accepts another function as an arg or returns a function

def square(x):
    return x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)
# [1, 4, 9, 16, 25]


def change_bullet_style(document):
    return "\n".join(map(convert_line, document.split('\n')))
# Don't edit below this line
'''Map'''

def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
'''filter'''
#the built-in function 'filter' takes a function and an iterable, in this case a list, and returns a new iterable that only contains elements from the original iterable where the result of the function of that item returned true

'''filer assignment'''
def remove_invalid_lines(document):
    return '\n'.join(
        filter(lambda x: not x.startswith('-'), document.split('\n'))
    )

'''reduce'''
#the functtools.reduce() function is a function
#that takes a function and a list of values and applies
#the function to each value in the list, accumulating
#a result as it goes.
# import the functools module
# from the standard library

import functools

def add(sum, y):
    return sum + y

numbers = [1, 2, 3, 4, 5]
sum = functools.reduce(add, numbers)
print(sum)
# 15

'''how do map, filter, and reduce help with functional programming?'''

#example of imperative code to calculate a factorial of num
def factorial(n):
    # a procedure that continuously multiplies
    # the current result by the next number
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


''' example of higher-order function like reduce'''
#a higher-order function like reduce will allow
#us to remove the stateful iteration and mutation
#of the result variable

import functools

def mul(x, y):
    return x * y

def factorial(n):
    return functools.reduce(mul, range(1, n + 1))

#in the functional example
#we are simply composing and combining functions
#to get the result we want 

#we are doing our best to avoid keeping track of state
#and mutating variables


import functools


def accumulate(doc, sentence):
    return doc + '. ' + sentence
#print(accumulate('hi', 'hello'))

def accumulate_first_sentences(sentences, n):
    if not sentences:
        return ''
    if n < 1:
        return ''
    newdoc = functools.reduce(accumulate, sentences[:n])
    return newdoc + '.'

print(accumulate_first_sentences(['kobe', 'is', 'goat'], 2))


