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
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.score = 0

        # Create frame style
        self.frame = tk.Frame(master, bg=style.bg_color)
        self.frame.pack(pady=10)

        self.style.configure("CustomCombobox.TCombobox",
                             fieldbackground=style.dropdown_bg_color,  # Background color for the entry field
                             background=style.dropdown_bg_color,  # Background color for the dropdown list
                             foreground=style.dropdown_text_color)  # Text color

        # Create a label to display the score
        self.score_label = tk.Label(self.frame, text=f"Score: {self.score}",
                                    font=("Helvetica", 14), fg=style.text_color, bg=style.bg_color)
        self.score_label.pack(pady=10)

        # Difficulty options
        self.difficulty_var = tk.StringVar(value="Medium")  # Default difficulty
        self.difficulty_label = tk.Label(self.frame, text="Select Difficulty:", font=style.font_style, fg=style.text_color, bg=style.bg_color)
        self.difficulty_label.pack(pady=(0, 5))
        self.difficulty_menu = ttk.Combobox(self.frame, textvariable=self.difficulty_var, 
                                             values=["Easy", "Medium", "Hard"], 
                                             font=style.dropdown_font,
                                             style = "CustomCombobox.TCombobox")
        self.difficulty_menu.bind("<<ComboboxSelected>>", lambda _: self.set_difficulty())
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

        #Set UI focus
        self.entry.focus_set()

        # Set default values based on difficulty
        self.set_difficulty()

    def set_difficulty(self):
        difficulty = self.difficulty_var.get()
        if difficulty == "Easy":
            self.label.config(text="Guess a number between 1 and 50:")
            self.number_to_guess = generate_number(1, 50)
            max_num = 50
            self.max_attempts = 10
        elif difficulty == "Medium":
            self.label.config(text="Guess a number between 1 and 100:")
            self.number_to_guess = generate_number(1, 100)
            max_num = 100
            self.max_attempts = 7
        elif difficulty == "Hard":
            self.label.config(text="Guess a number between 1 and 200:")
            self.number_to_guess = generate_number(1, 200)
            max_num = 200
            self.max_attempts = 5

        # Reset attempts and update the attempts label
        self.attempts = 0
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        self.entry.focus_set()

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

        # Clear the input box after each guess
        self.entry.delete(0, tk.END)

        if result == "Correct!":
            points = max(100 - (self.attempts * 10),0)
            self.score += points
            self.score_label.config(text=f"Score: {self.score}")
            self.result_label.config(text=f"Congratulations! You've guessed the number in {self.attempts} attempts!")
            self.entry.config(state='disabled')

        if self.attempts >= self.max_attempts and result != "Correct!":
            self.result_label.config(text=f"Sorry, you've used all attempts. The number was {self.number_to_guess}.")
            self.entry.config(state='disabled')

    def reset_game(self):
        # Get the current difficulty from the dropdown
        difficulty = self.difficulty_var.get()
        
        # Set the number range and max attempts based on the current difficulty
        if difficulty == "Easy":
            self.number_to_guess = generate_number(1, 50)
            self.max_attempts = 10
        elif difficulty == "Medium":
            self.number_to_guess = generate_number(1, 100)
            self.max_attempts = 7
        elif difficulty == "Hard":
            self.number_to_guess = generate_number(1, 200)
            self.max_attempts = 5

    # Reset attempts
        self.attempts = 0
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")

    # Clear entry box and reset result label
        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)  # Clear the entry box
        self.result_label.config(text="")  # Clear the result label

    # Optionally, you can set focus back to the entry field
        self.entry.focus_set()

    #Reset Score
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")

# Main program execution
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    custom_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
    app = GuessTheNumberApp(root)  # Create an instance of the game app
    root.mainloop()  # Start the main event loop to listen for user inputs