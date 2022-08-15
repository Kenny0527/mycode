#!/usr/bin/env python3

"""Alta3 Research | controlling pytest behaviors with conftest.py"""

# this function is to select hurricane category
def hurricaneCategory(hurricanews):
    print()
    # conditional statmenet to check if its wind speed is not a hurricane
    if hurricanews < 74:
        print("The current wind speed is not considered a hurricane. Please enter a new wind speed over 74 mph. ")
    
    # conditional statement to check if its wind speed is a category 1 hurricane
    elif hurricanews < 96:
        print("You are in a Category 1 Hurricane! Grab the kids and get out of town")

    # conditional statement to check if its wind speed is a category 2 hurricane
    elif hurricanews < 111:
        print("You are in a Category 2 Hurricane! It's not too late, board up the windows and doors.")

    # conditional statement to check if its wind speed is a category 3 hurricane
    elif hurricanews < 130:
        print("You are in a Category 3 Hurricane! Its too late to leave, get away from the windows and doors")

    # conditional statement to check if its wind speed is a category 4 hurricane
    elif hurricanews < 157:
        print("You are in a Category 4 Hurricane! The coast guard is gone, get elevated in case of flooding. Turn on the radio and stay updated.")

    # conditional statement to check if its wind speed is a category 5 hurricane
    else:
        print("You are in a Gategory 5 Hurricane! It's too late for you, bend over and kiss your butt goodbye.")

#------------------------------ MAIN ----------------------------

def main():
    """Alta3 Research | RZFeeser
        if, elif, else - a simple program using conditioanls to make a decision"""

    message = 'A program that returns severity of a hurricane based upon wind speeds. Hurricane category 1 base wind speed is 74 mph. There are 5 categories of hurricanes, with windspeeds exceeding 150 mph'

    # wrap hurricanews in a float() to accept decimals as numbers
    print(message)
    print()
    hurricanews = float(input("What is the hurricanes windspeed in mph? "))
    hurricaneCategory(hurricanews)

#----------------------- RUN MAIN FUNCTION ----------------------

if __name__ == "__main__":
    main()
