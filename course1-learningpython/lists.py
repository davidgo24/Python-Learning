'''#LISTS'''
#A natural way to organize and store data is in a List. Some languages call them "arrays", but in Python we just call them lists. Think of all the apps you use and how many of the items in the app are organized into lists.

inventory = ["Iron Breastplate", "Healing Potion", "Leather Scraps"]

flower_types = [
    "daffodil",
    "rose",
    "chrysanthemum"
]

player_ages = [
    23,
    18,
    31,
    42
]
#Counting in Progamming
#we start counting at 0 instead of 1

names = ["Bob", "Lane", "Alice", "Breanna"]

#bob = 0 index

#INDEXING INTO LISTS
#We access items in a list directly 
# by using their index. 
# Indexes start at 0 (the first item) and 
# increment by one with each successive item. The syntax is as follows:

best_languages = ["JavaScript", "Go", "Rust", "Python", "C"]
print(best_languages[1])
# prints "Go", because index 1 was provided

'''ASSIGNMENT #1'''
def get_leather_straps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]

    item_index = 1

    return inventory[item_index]
'''LIST LENGTH'''
def get_last_index(lst):
    length_list = len(lst)
    return length_list - 1 

'''LIST UPDATES'''
#we can update lists using the following
def smelt_ore():
    inventory = ["Healing Potion", "Iron Ore", "Bread", "Shortsword"]
    print(f"Inventory: {inventory}")

    # don't touch above this line

    inventory[1] = "Iron Bar"

    # don't touch below this line

    return inventory

'''APPENDING VALUES 
'''
'''ASSIGNMENT #2'''
cards = []
cards.append("nvidia")
cards.append("amd")
# the cards list is now ['nvidia', 'amd']

def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)
        
    return player_ids

'''POP VALUES'''
#.pop() is the opposite of .append(). Pop removes the last element from the list and returns it for use. For example:

vegetables = ["broccoli", "cabbage", "kale", "tomato"];
last_vegetable = vegetables.pop()
# vegetables = ['broccoli', 'cabbage', 'kale']
# last_vegetable = 'tomato'

'''ASSIGNMENT'''
def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    # don't touch above this line

    for i in range(0, len(inventory)):
        item = inventory.pop()
        
        # don't touch below this line
        print(f"Selling: {item}")
        print(f"inventory: {inventory}")

'''counting the items in a list'''
def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0
    
    for i in range(0, len(items)):
        if items[i] == "Potion": #this makes sense because i does not represent the item in the list, it reprsents the value.. 1,2,4,5 so we must call the actual item/position of item from the list using items[i]
            potion_count += 1
        elif items[i] == "Bread":
            bread_count += 1
        elif items[i] == "Shortsword":
            shortsword_count += 1
            
# or you can write as this  // since we do not care about the index, we can directly grab the item from the actual list since we no there is a finite number and we only need to stop at the final value.
#aka we do not need to know the index! so we can write like this. 
    for i in items:
        if i == "Potion":
            potion_count += 1
        elif i == "Bread":
            bread_count += 1
        elif i == "Shortsword":
            shortsword_count += 1
'''#No index syntax'''

trees = ['oak', 'pine', 'maple']
for tree in trees:
    print(tree)
# Prints:
# oak
# pine
# maple

'''When an index in a for loop is required vs when it is not '''\
#rememebr we use a for loop to do something a certain amount of times (when we know it needs to be done more than once and we know how many times)

my_list = [5, 3, 7, 1, 8]
for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 2
print(my_list)  # Prints: [25, 9, 49, 1, 64]
#In this case, we can't simply iterate over the values of my_list, because we wouldn't be able to modify them. We need the indices to square every number in place.

#When an index is not required:

animals = ['cat', 'dog', 'bear', 'turtle']
for animal in animals:
    print(f"I like {animal}s.")

#Here, we're just printing each item in the list & there's no need to modify them. This makes the for item in items syntax cleaner and more concise.