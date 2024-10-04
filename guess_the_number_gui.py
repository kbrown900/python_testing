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
        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)

        # Difficulty options
        self.difficulty_var = tk.StringVar(value="Medium")  # Default difficulty
        self.difficulty_label = tk.Label(self.frame, text="Select Difficulty:")
        self.difficulty_label.pack(pady=(0, 5))

        self.difficulty_menu = tk.OptionMenu(self.frame, self.difficulty_var, "Easy", "Medium", "Hard", 
                                              command=lambda _: self.reset_game())
        self.difficulty_menu.pack(pady=5)
        
        #Configure Style
        master.configure(bg=style.bg_color)
        self.style = ttk.Style()
        self.style.theme_use('default')
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

        self.entry.bind('<Return>', lambda event: self.check_guess())

        # Define Buttons
        self.guess_button = ttk.Button(self.frame, text="Guess", style="Rounded.TButton", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.reset_button = ttk.Button(self.frame, text="Reset", style="Rounded.TButton", command=self.reset_game)
        self.reset_button.pack(pady=5)

        # Result label
        self.result_label = tk.Label(self.frame, text="", font=custom_font, fg=style.text_color, bg=style.bg_color)
        self.result_label.pack(pady=5)

        # Attempts Label
        self.attempts_label = tk.Label(self.frame, text=f"Attempts: {self.attempts}/{self.max_attempts}", font=custom_font, fg=style.text_color, bg=style.bg_color)
        self.attempts_label.pack(pady=10)

        self.entry.focus_set()

        # Set default values based on difficulty
        self.set_difficulty()

    def set_difficulty(self):
        # Dictionary to hold difficulty settings
        difficulty_settings = {
            "Easy": (1, 50, 10),    # (min, max, attempts)
            "Medium": (1, 100, 7),
            "Hard": (1, 200, 5)
        }

        # Get the current difficulty level
        difficulty = self.difficulty_var.get()
        
        # Unpack the settings for the current difficulty level
        min_num, max_num, max_attempts = difficulty_settings[difficulty]
        
        # Generate the number to guess
        self.number_to_guess = generate_number(min_num, max_num)

        # Update the maximum attempts and the label text
        self.max_attempts = max_attempts
        self.attempts = 0  # Reset attempts
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")

        # Update the guessing instruction label
        self.label.config(text=f"Guess a number between {min_num} and {max_num}:") 


    def check_guess(self):
        guess = self.entry.get()
        
        #input check
        if not guess.isdigit():
            self.result_label.config(text="Please enter a valid number.")
            return
        
        guess = int(guess)
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")

        result = check_guess(guess, self.number_to_guess)
        self.result_label.config(text=result)

        if result == "Correct!":
            self.result_label.config(text=f"Congratulations! You've guessed the number in {self.attempts} attempts!")
            self.entry.config(state='disabled')

        if self.attempts >= self.max_attempts and result != "Correct!":
            self.result_label.config(text=f"Sorry, you've used all attempts. The number was {self.number_to_guess}.")
            self.entry.config(state='disabled')

    #Method to reset game
    def reset_game(self):
        self.set_difficulty()  # Set number and attempts based on difficulty
        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)  # Clear the entry box
        self.result_label.config(text="")
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")

# Main program execution
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    custom_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
    app = GuessTheNumberApp(root)  # Create an instance of the game app
    root.mainloop()  # Start the main event loop to listen for user inputs