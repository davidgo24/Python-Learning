'''SETS'''
#sets are like lists, except they are unordered and guarantee uniqueness
#there can be no two of the same value in a set
fruits = {'apple', 'banana', 'grape'}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}
'''ADD VALUE'''
#you can add a value by 
fruits = {'apple', 'banana', 'grape'}
fruits.add('pear')
print(fruits)
# Prints: {'banana', 'grape', 'pear', 'apple'}

#note, if you add a value that already exists, no error will be raised

'''EMPTY SET'''
#because empty brackets {} as such, create an empty dictionary. we must rewrite an empyty set a different way for it to be read as an empty set
fruits = set()

#example
empty_set = {}
print(type(empty_set))
actual_empty_set = set()
print(type(actual_empty_set))
#prints <class 'dict'>
#prints <class 'set'>

'''iterate over values in a set'''
fruits = {'apple', 'banana', 'grape'}
for fruit in fruits:
    print(fruit)
    # Prints:
    # banana
    # grape
    # apple
    
'''assignment'''
def remove_duplicates(spells):
    new_set = set(spells)
    spells_without_duplicates = []
    for x in new_set:
        spells_without_duplicates.append(x)
    return spells_without_duplicates
        
#or can be written using a list comprehension

def remove_duplicates(spells):
    new_set = set(spells)
    removed_dupes = list(new_set) # this is called a list comprehension
    return removed_dupes