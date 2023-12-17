'''Comparison Operators'''

'''Intro'''
#When coding it's necessary to be able to compare two values. 
# Boolean logic is the name for these kinds of comparison operations that always result in True or False.

#< "less than"
#> "greater than"
#<= "less than or equal to"
#>= "greater than or equal to"
#== "equal to"
#!= "not equal to"#

'''ASSIGNMENT #1'''
def player_1_wins(player_1_score, player_2_score):
    return player_1_score > player_2_score
    
'''Comparison Operator Evaluations'''
#When a comparison happens, the result of the comparison is just a boolean value, it's either True or False.

#Take the following two examples:
is_bigger = 5 > 4
is_bigger = True

'''ASSIGNMENT #2'''
# using is equal to 
def compare_heights(elon_height, sara_height, jill_height, bob_height):
    bob_same_height_as_elon = bob_height == elon_height
    sara_same_height_as_elon = sara_height == elon_height
    jill_same_height_as_sara = jill_height == sara_height
    return bob_same_height_as_elon, sara_same_height_as_elon, jill_same_height_as_sara

'''#3'''
#using greater than or equal to
def can_withstand_blow(hero_armor, enemy_damage):
    return hero_armor >= enemy_damage

'''If statements'''
#It's often useful to only execute code if a certain condition is met:

#if CONDITION:
	# do some stuff here
# code after the if block will run regardless
# For example
if bob_score > bill_score:
	print("Bob Wins!")

print("Game Complete")
'''#4'''
def print_status(player_health):
    if player_health == 0:
        print("dead")
        
    print("status check complete")

'''If practice'''
#Remember, you can use the == operator to check if two values are equal. For example:
is_equal = 5 == 5
# is_equal is True
'''#5'''
def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_swords == number_of_soldiers:
        return "correct amount"
    else:
        return "incorrect amount"
#or can be written as
def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_soldiers == number_of_swords:
        return "correct amount"
    return "incorrect amount" #treat kind of like a print function where it continues if the if statement allows it to 

'''If else'''
#An if statement can be followed by zero or more elif 
# (which stands for "else if") statements, which can be followed by zero or one else statement. For example:
if score > high_score:
    print('High score beat!')
elif score > second_highest_score:
    print('You got second place!')
elif score > third_highest_score:
    print('You got third place!')
else:
    print('Better luck next time')

'''#6'''
#using elif, and else 
def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"
    
'''If else Practice'''
#Here are some basic rules with if/else blocks.

#You can't have an elif or an else without an if
#You can have an else without an elif

'''#7'''
def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    elif current_player_name != high_scoring_player_name: #here we use not equal to since we are working with names. <= could work if it our args were nums
        return "You are not the highest scoring player!"
'''#8'''
def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else:
        return "neither"
