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

'''Find an item in a list using the no-index for loop syntax'''
def contains_leather_scraps(items):
    found = False

    # don't touch above this line
    for item in items:
        #if item is called leather scraps then switch found from false to true
        if item == "Leather Scraps":
            found = True
            return found
'''Finding differences in lists'''
def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 43]

    # don't touch above this line

    for i in range(0, len(old_character_levels)):
        if old_character_levels[i] != new_character_levels[i]:
            print(i)

'''Finding max'''
def find_max(nums):
    max_so_far = float("-inf")
    for num in range(0, len(nums)):
        if nums[num] > max_so_far:
            max_so_far = nums[num]
    return max_so_far #it is key for this return statement to be outside of the loop
    #so it can continue checking the entire list.
        
'''Modulo Operator in Python'''
def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        if i % 2 > 0:
            odd_numbers.append(i)
'''SLICING Lists'''
my_list[ start : stop : step ]
#Example
scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:5:2])
# Prints [70, 20]
#The above reads as "give me a slice of the scores list from index 1, up to but not including 5, skipping every 2nd value. All of the sections are optional.

'''ommitting sections of lists'''
#You can also omit various sections ("start", "stop", or "step"). 
# For example, numbers[:3] means "get all items from the start up to (but not including) index 3".
# numbers[3:] means "get all items from index 3 to the end".
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[:3] # Gives [0, 1, 2]
numbers[3:] # Gives [3, 4, 5, 6, 7, 8, 9]

'''USING ONLY THE "STEP" SECTION'''
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2] # Gives [0, 2, 4, 6, 8]

'''NEGATIVE INDICES'''
#Negative indices count from the end of the list. For example, numbers[-1] gives the last item in the list, numbers[-2] gives the second last item, and so on.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[-3:] # Gives [7, 8, 9]

'''SLICING LISTS'''
#when slicing lists, think of counting by the index and not the count. 0,1,2...

def get_champion_slices(champions):
    return champions[2:], champions[:-2:], champions[::2]

'''LIST OPERATIONS / CONCATENATE'''
total = [1, 2, 3] + [4, 5, 6]
print(total)
# Prints: [1, 2, 3, 4, 5, 6]
def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    favorite_weapons
    favorite_armor
    favorite_items
    fav_armory = favorite_weapons + favorite_armor + favorite_items
    return fav_armory
'''LIST OPERATIONS / CONTAINS "X IN ..." '''
fruits = ["apple", "orange", "banana"]
print("banana" in fruits)
# Prints: True

def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]
    return weapon in top_weapons

'''list deletion'''
#Python has a built-in keyword del that deletes items from objects. 
# In the case of a list, you can delete specific indexes or entire slices.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete the fourth item
del nums[3]
print(nums)
# Output: [1, 2, 3, 5, 6, 7, 8, 9]

# delete the second item up to the fourth item
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[1:3]
print(nums)
# Output: [1, 4, 5, 6, 7, 8, 9]

# delete all elements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[:]
print(nums)
# Output: []

