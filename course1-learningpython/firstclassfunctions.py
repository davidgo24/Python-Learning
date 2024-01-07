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
