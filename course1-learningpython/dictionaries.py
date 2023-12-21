'''Dictionaries'''
#in python dictionaries are used to store data by using a key and value pair. they are a great way to store groups of info.
car = {
  "brand": "Tesla",
  "model": "3",
  "year": 2019
}


'''ASSIGNMENT #!1'''
def get_character_record(name, server, level, rank):
    record = {
        "name": name,
        "server": server,
        "rank": rank,
        "level": level,
        "id": f"{name}#{server}"
    }
    return record

'''Duplicate Keys'''
#Because dictionaries rely on unique keys, 
# you can't have two of the same key in the same dictionary. If you try to use the same key twice, the first value will simply be overwritten.
def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "level": 1, #will use level instead
        "rank": rank, 
        "rank": 2, #will use rank instead.
        "id": f"{name}#{server}",
    }
'''ACCESSING Dictionary Values'''
#A value is retrieved from a dictionary by specifying its corresponding key in square brackets.
# The syntax looks similar to indexing into a list.

car = {
    'make': 'tesla',
    'model': '3'
}
print(car['make'])
# Prints: tesla

'''SETTING Dictionary Values'''
#it is common to use empty or blank dictionaries.
#we can add keys and values later using dynamic values.
#the syntax is the same as getting data out of a key
#just use the (=) operator to assign a value to that key
names = ["jack bronson", "jill mcarty", "john denver"]

names_dict = {}
for name in names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    name_lst = name.split()

    # here we update the dictionary
    names_dict[name_lst[0]] = name_lst[1]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty', 'john': 'denver'}

#my practice
#create a new dict 
players_dict = {}

players_dict["Kobe"] = 24
print(players_dict)
#prints: {'Kobe': 24}

'''Deleting dictionary values'''
#you can delete using the del keyword 

names_dict = {
    'jack': 'bronson',
    'jill': 'mcarty',
    'joe': 'denver'
}

del names_dict['joe']

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty'}

#deleting keys that do not exist

names_dict = {
    'jack': 'bronson',
    'jill': 'mcarty',
    'joe': 'denver'
}

del names_dict['unknown']
# ERROR HERE, key doesn't exist

'''checking for existence'''
cars = {
    'ford': 'f150',
    'tesla': '3'
}

print('ford' in cars)
# Prints: True

print('gmc' in cars)
# Prints: False
'''COUNTING PRACTICE
'''
def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name in enemies_dict:
            enemies_dict[enemy_name] += 1
        else:
            enemies_dict[enemy_name] = 1
    return enemies_dict

'''ITERATING OVER A DICTIONARY IN PYTHON'''
fruit_sizes = {
    "apple": "small",
    "banana": "large",
    "grape": "tiny"
}

for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")

# name: apple, size: small
# name: banana, size: large
# name: grape, size: tiny
