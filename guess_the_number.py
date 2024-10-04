import random

def guess_the_number():
    #Step 1: Generate a random number between 1 and 100
    number_to_guess = random.randint(1,100)
    attemps = 0
    max_attempts = 10

    print("Welcom to Guess the Number")
    print("I have selected a number between 1 and 100.")
    print("You have {max_attempts} attempts to guess it.")

    #Step 2: Start the guessing loop
    while attemps < max_attempts:
        #Step 3: Get user input
        guess = input("Enter your guess: ")

        #Step 4: Validate input
        if not guess.isdigit():
            print("Please enter a valid number")
            continue
        guess = int(guess)
        attempts += 1

        # Step 5: Check the guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

# Step 6: Run the game
if __name__ == "__main__":
    guess_the_number()