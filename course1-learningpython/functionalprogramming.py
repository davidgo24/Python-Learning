'''what is functional programming?'''
#Functional programming is a paradigm where programs compose functions rather than mutate state (setting and updating variables).

#Functional programming is more about declaring what you want to happen, rather than how you want it to happen.
#Imperative (or procedural) programming declares what should happen, but also exactly how it should happen.

'''imperative(procedural) vs functional programming'''

#imperative - think of a recipe that gets mutated (add stuff on top of it and it changes)
num = get_a()
num = transform_a(num)
num = transform_b(num)
return num

#functional -The important distinction is that in the functional example, we don't need to mutate (change) the values of any variables. There is no statefulness.
return transform_b(transform_a(get_a()))


