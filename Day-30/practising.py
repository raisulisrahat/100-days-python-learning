# Here is am showing Practising Day 25 in python

# Random Built-In Modules
import random

def coin_flip():
    return random.choice(["Heads", "Tails"])

def game():
    print("Welcome to the Coin Flip Game!")

    while True:
        user_guess = input("Guess heads or tails: ").capitalize()

        if user_guess not in ["Heads", "Tails"]:
            print("Invalid guess. Please enter 'Heads' or 'Tails'.")
            continue

        result = coin_flip()

        print(f"The coin landed on: {result}")

        if user_guess == result:
            print("Congratulations! Your guess was correct.")
        else:
            print("Sorry! Your guess was incorrect.")

        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != 'yes':
            print("Thanks for playing!")
            break
game()
