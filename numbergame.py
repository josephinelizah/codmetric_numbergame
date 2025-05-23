import random

print("~~NUMBER GUESSING GAME~~".center(550))
print("Try and guess the number I picked between 1 and 100:)".center(550))


number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess: ")

    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input. Enter valid integer.")
        continue

    attempts += 1

    if guess < number:
        print("Too low...")
    elif guess > number:
        print("Too high...")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
