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

'''Boolean Logic'''
#Boolean logic refers to logic dealing with boolean (True or False) values. For example,

#Dogs must have four legs and weigh less than 100 kilograms. (Both conditions must be true)

#Cars are cool if they go faster than 200 MPH, or if they are electric. (At least one condition must be true)

#As we discussed earlier, the logical operators and and or can be used to perform boolean logic.

#The and operator returns True if both of the conditions on either side evaluates to True:
def is_dog(num_legs, weight):
    return num_legs == 4 and weight < 100

'''#9'''
def does_attack_hit(attack_roll, armor_class):
    if (attack_roll != 1 and attack_roll >= armor_class) or (attack_roll == 20):
        return True
    else:
        return False
         
'''#10'''
def should_serve_customer(customer_age, on_break, time):
    if (time >= 5) and (time <=10) and (not on_break) and (customer_age >= 21):
        return True
    else:
        return False
        
'''#11'''
def check_parking_meter(time_parked, time_purchased):
    if time_parked >= time_purchased:
        return "overtime charged"
    else:
        return "no charges yet"
#OR can be written as
def check_parking_meter(time_parked, time_purchased):
    if time_parked >= time_purchased:
        return "overtime charged"
    return "no charges yet"
'''#12'''
#COMBAT ADVANTAGE
#A new text-based RPG you are building doesn't have any way for players to know if they are strong enough to fight certain enemies.

#If a player's power level is greater than the enemies' defense that player has an advantage
#If the player's power and enemies' defense are equal they are evenly matched
#Otherwise, that player has a disadvantage.
#CHALLENGE
#On line 4 write an if/elif/else block. It should either set advantage, disadvantage, or evenly_matched to True depending on the values of player_power and enemy_defense.

#For example, if the player's power is greater than the enemy's defense, advantage should be set to True. etc.

def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False #these are our starting arguments
    if player_power > enemy_defense: 
        advantage = True #if this test passes, lets flip the switch to true
    elif player_power == enemy_defense:
        evenly_matched = True #elif this test passes, lets flip this switch to true 
    else:
        disadvantage = True #else flip this switch to true
    
    return advantage, disadvantage, evenly_matched
'''#13'''

#GAS MILEAGE
#There isn't a gas station between Tyler's house and his work. He is trying to figure out if his car has enough gas to get him to work and back home.

#CHALLENGE
#Complete the has_enough_gas function.

#Do some Pythonic math to determine how many gallons are needed for Tyler to get to work AND make it back home after he gets off work. Assign the result to a gallons_needed variable.

#Return True if there are at least enough gallons in the tank based on the gallons_needed variable, and False otherwise.
def has_enough_gas(gallons_in_car, miles_to_work, miles_per_gallon):
    total_mileage = miles_to_work * 2 #here i am calculating the total distance (mi)
    gallons_needed = total_mileage / miles_per_gallon #the argument mpg provides the info we need to calc gallons needed
    if gallons_in_car >= gallons_needed: #now that the math is done, we can use boolean logic to determine if we have enough gas pased on our scenario
        return True
    return False

'''Recap'''
#1. comparisons use boolean logic - true of false
#2. we can use operators such as: > < >= >= <= == != 
#3. if statements are a way to set conditions 
#4. if statements say, only if something is true, execute this code. 

