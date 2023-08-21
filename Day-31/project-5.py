# Here i am showing the Day 25 practice project

# Dice Rolling Game
import random

class DiceRoller:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

def main():
    print("Welcome to the Dice Rolling Game!")

    sides = int(input("Enter the number of sides for the dice: "))
    if sides <= 0:
        print("Invalid number of sides. Please enter a positive integer.")
        return

    dice = DiceRoller(sides)

    while True:
        user_choice = input("Roll the dice? (y/n): ").lower()

        if user_choice == 'y':
            result = dice.roll()
            print(f"The dice rolled: {result}")
        elif user_choice == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 'y' to roll or 'n' to exit.")

if __name__ == "__main__":
    main()
