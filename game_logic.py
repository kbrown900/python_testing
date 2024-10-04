import random

def generate_number(min_value=1, max_value=100):
    """Generate a random number between 1 and 100."""
    return random.randint(min_value, max_value)

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
