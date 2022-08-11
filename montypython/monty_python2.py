#!/usr/bin/env python3
def main():
    round = 0
    answer = " "
    while round < 3 and answer.lower() != "brian" and answer.lower() != "shrubbery":
        round += 1
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        answer = input("Your guess --> ")
        if answer.lower() == "brian":
            print('Correct')
        elif answer.lower() == "shrubbery":
            print("You gave the super secret answer!")
        elif round == 3:
            print("Sorry, the answer was Brian.")
        else:
            print("Sorry! Try again!")

if __name__ == "__main__":
    main()
