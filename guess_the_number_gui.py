import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from game_logic import generate_number, check_guess
import style_config as style

# Declare a global variable for the custom font
custom_font = None

# Class definition for the GuessTheNumberApp
class GuessTheNumberApp:
    def __init__(self, master):
        global custom_font
        # Initialize the main window and set its title
        self.master = master
        master.title("Guess the Number")
        master.geometry(style.window_size)
        
        # Apply background color from style_config.py
        master.configure(bg=style.bg_color)

        # Create a style object to style ttk widgets
        self.style = ttk.Style()
        self.style.theme_use('default')

        # Configure button styles using the method from style_config
        style.configure_button_style(self.style)

        # Create a frame and apply padding
        self.frame = tk.Frame(master, bg=style.bg_color)
        self.frame.pack(pady=20)

        # Initialize the game logic variables
        self.number_to_guess = generate_number() #number to guess
        self.attempts = 0 #default attempts number
        self.max_attempts = 10 #max tries

        # Create and display the label for instructions
        self.label = tk.Label(self.frame, text="Guess a number between 1 and 100:", 
                              font=custom_font, fg=style.text_color, bg=style.bg_color)
        self.label.pack(pady=10)

        # Create and display the entry box where the player enters their guess
        self.entry = tk.Entry(self.frame, font=custom_font, bd=2, relief="flat")
        self.entry.pack(pady=10)

        # Modern flat buttons with color styling and rounded corners
        self.guess_button = ttk.Button(self.frame, text="Guess", style="Rounded.TButton", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.reset_button = ttk.Button(self.frame, text="Reset", style="Rounded.TButton", command=self.reset_game)
        self.reset_button.pack(pady=5)

        # Result label
        self.result_label = tk.Label(self.frame, text="", font=custom_font, fg=style.text_color, bg=style.bg_color)
        self.result_label.pack(pady=10)

        self.attempts_label = tk.Label(self.frame, text=f"Attempts: {self.attempts}/{self.max_attempts}", font=custom_font, fg=style.text_color, bg=style.bg_color)
        self.attempts_label.pack(pady=10)

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
    custom_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
    app = GuessTheNumberApp(root)  # Create an instance of the game app
    root.mainloop()  # Start the main event loop to listen for user inputs
