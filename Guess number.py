import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Allow the player 3 chances
chances = 3

print("Welcome to 'Guess the Number'! You have 3 chances to guess a number between 1 and 10.")

# Loop for the 3 chances
for attempt in range(1, chances + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == random_number:
        print("Congratulations! You guessed the number!")
        break
    elif attempt < chances:
        print("Wrong guess. Try again.")
else:
    print("You lost the game. The correct number was:", random_number)
