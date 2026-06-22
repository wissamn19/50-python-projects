"""
Number Guessing Game
Core syntax | Difficulty: Beginner

Concepts: loops, conditionals, random module, stats tracking
"""
import random

def main():
    print("Build Number Guessing Game (0 - 3690)")
    guess = int(input("Give me your guess:"))
    num = 0
    num = random.randint(0 , 3690)
    stats = 0
    while guess != num:
        if guess < num:
            print(f"Nahh, try again. it's upper than {guess}  Come on.")
            guess = int(input("Give me your guess:"))
        elif guess > num:
            print(f"Nahh, try again. it's lower than {guess}  Come on.")
            guess = int(input("Give me your guess:"))
        stats += 1
    if guess == num:
        print(f"YOU GOT IT!!, with {stats} attempts!!")

            
if __name__ == "__main__":
    main()
