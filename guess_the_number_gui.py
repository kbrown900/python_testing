import tkinter as tk
from game_logic import generate_number, check_guess

class GuessTheNumberApp:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number")

        self.number_to_guess = generate_number()
        self.attempts = 0
        self.max_attempts = 10

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        guess = self.entry.get()

        if not guess.isdigit():
            self.result_label.config(text="Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1

        result = check_guess(guess, self.number_to_guess)
        self.result_label.config(text=result)

        if result == "Correct!":
            self.result_label.config(text=f"Congratulations! You've guessed the number in {self.attempts} attempts!")
            self.entry.config(state='disabled')

        if self.attempts >= self.max_attempts and result != "Correct!":
            self.result_label.config(text=f"Sorry, you've used all attempts. The number was {self.number_to_guess}.")
            self.entry.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessTheNumberApp(root)
    root.mainloop()
