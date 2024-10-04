import tkinter as tk
from game_logic import generate_number, check_guess

# Class definition for the GuessTheNumberApp
class GuessTheNumberApp:
    def __init__(self, master):
        # Initialize the main window and set its title
        self.master = master
        master.title("Guess the Number")

        # Create and pack a frame to hold the widgets (UI components)
        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)

        # Initialize the game logic variables
        self.number_to_guess = generate_number()  # Generate the number to be guessed
        self.attempts = 0  # Track the number of attempts made by the player
        self.max_attempts = 10  # Maximum number of attempts allowed

        # Create and display the label for instructions
        self.label = tk.Label(self.frame, text="Guess a number between 1 and 100:")
        self.label.pack()

        # Create and display the entry box where the player enters their guess
        self.entry = tk.Entry(self.frame)
        self.entry.pack(pady=5)

        # Create and display the "Guess" button that checks the player's guess
        self.guess_button = tk.Button(self.frame, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        # Create and display the "Reset" button to start a new game
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=5)

        # Create and display the label to show the result of the guess
        self.result_label = tk.Label(self.frame, text="")
        self.result_label.pack(pady=5)

        # Create and display the label to track the number of attempts
        self.attempts_label = tk.Label(self.frame, text=f"Attempts: {self.attempts}/{self.max_attempts}")
        self.attempts_label.pack(pady=5)

    # Method to check the player's guess
    def check_guess(self):
        guess = self.entry.get()  # Get the guess from the entry box

        # Validate if the input is a digit
        if not guess.isdigit():
            self.result_label.config(text="Please enter a valid number.")
            return

        guess = int(guess)  # Convert the input to an integer
        self.attempts += 1  # Increment the number of attempts
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")  # Update attempts label

        # Check the player's guess against the generated number
        result = check_guess(guess, self.number_to_guess)
        self.result_label.config(text=result)  # Update the result label based on guess accuracy

        # If the guess is correct, congratulate the player and disable further inputs
        if result == "Correct!":
            self.result_label.config(text=f"Congratulations! You've guessed the number in {self.attempts} attempts!")
            self.entry.config(state='disabled')  # Disable entry to stop further guesses

        # If the maximum attempts are reached and the player hasn't guessed correctly
        if self.attempts >= self.max_attempts and result != "Correct!":
            self.result_label.config(text=f"Sorry, you've used all attempts. The number was {self.number_to_guess}.")
            self.entry.config(state='disabled')  # Disable entry after all attempts are used

    # Method to reset the game
    def reset_game(self):
        self.number_to_guess = generate_number()  # Generate a new number to guess
        self.attempts = 0  # Reset the attempt counter
        self.entry.config(state='normal')  # Re-enable the entry box
        self.entry.delete(0, tk.END)  # Clear the entry box for new input
        self.result_label.config(text="")  # Clear the result label
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")  # Reset the attempts label

# Main program execution
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = GuessTheNumberApp(root)  # Create an instance of the game app
    root.mainloop()  # Start the main event loop to listen for user inputs
