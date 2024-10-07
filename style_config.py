
import tkinter as tk
from tkinter import font as tkfont

# Define color scheme
bg_color = "#787878"  # Background color
text_color = "#000000"  # Text color
button_color = "#4CAF50"  # Button background color
button_text_color = "#FFFFFF"  # Button text color
window_size = "400x500" # Set window dimensions
font_style = ("Helvetica", 14)  # Default font style
dropdown_font = ("Helvetica", 12)  # Font style for the dropdown
dropdown_bg_color = "#d3d3d3"  # Background color for dropdown
dropdown_text_color = "#ffffff" # Dropdown text color

# Button styles
def configure_button_style(style):
    # Configure the button style
    style.configure('Rounded.TButton',
                    background=button_color,
                    foreground=button_text_color,
                    borderwidth=0,
                    padding=10,
                    relief="flat")  # Flat relief for a modern look

    style.map('Rounded.TButton',
              background=[('active', "#45a049")])