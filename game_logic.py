import random

def generate_number():
    """Generate a random number between 1 and 100."""
    return random.randint(1, 100)

def check_guess(guess, number_to_guess):
    """Check the player's guess against the number to guess."""
    if guess < number_to_guess:
        return "Too low!"
    elif guess > number_to_guess:
        return "Too high!"
    else:
        return "Correct!"

def reset_game():
    """Reset the game state for a new game."""
    return generate_number(), 0  # Return a new number and reset attempts
