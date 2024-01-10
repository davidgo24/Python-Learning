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
