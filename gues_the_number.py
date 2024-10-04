from game_logic import generate_number, check_guess, reset_game

def guess_the_number():
    number_to_guess = generate_number()
    attempts = 0
    max_attempts = 10

    print("Welcome to 'Guess the Number'!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        result = check_guess(guess, number_to_guess)
        print(result)

        if result == "Correct!":
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
