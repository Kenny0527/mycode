#!/usr/bin/env python3

# create a list of your favorite foods by adding 3 lists together
favFood = [ "pizza", "mashed-potatoes" ]
favFood2 = [ "steak", "oranges" ]
favFood3 = [ "mango", "berries", "banana" ]

favFood.extend(favFood2)
favFood.append(favFood3)

# print the list
print( favFood )

# print your favorite food item on the list
print()
print( "My Favorite food is: " + favFood[0] )
print( "My second favorite food is: " + favFood[2] )
print( "My third favorite food is: " + favFood[4][0] )

# create a dictionary, 3 qualities of your favorite superhero
superHeroDict = {"power":"x-ray vision", "hair": "wavering", "outfit": "full-plate", "planet": "earth"}

# print all keys and values seperately
print()
print( superHeroDict.keys() )
print( superHeroDict.values() )
