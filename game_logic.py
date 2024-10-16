import random

def generate_number(difficulty):
    """Generates a number based on the difficulty level."""
    if difficulty == "Easy":
        return random.randint(1, 10)
    elif difficulty == "Medium":
        return random.randint(1, 100)
    elif difficulty == "Hard":
        return random.randint(1, 200)

def check_guess(guess, number_to_guess):
    """Check the player's guess against the number to guess."""
    if guess < number_to_guess:
        return "Too low!"
    elif guess > number_to_guess:
        return "Too high!"
    else:
        return "Correct!"
