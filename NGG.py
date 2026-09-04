import random

number = random.randint(1, 100)
attempts = 0

print("================================")
print("      NUMBER GUESSING GAME")
print("================================")

print("I have selected a number between 1 and 100.")
print("Try to guess it!")

while True:

    guess = int(input("\nEnter your guess: "))

    attempts = attempts + 1

    if guess < number:
        print("Too low! Try again.")

    elif guess > number:
        print("Too high! Try again.")

    else:
        print("\n🎉 Congratulations!")
        print("You guessed the correct number.")
        print("Number of attempts:", attempts)
        break