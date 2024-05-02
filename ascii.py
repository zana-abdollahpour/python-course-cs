from pyfiglet import figlet_format
from termcolor import colored

allowed_colors = ("red", "green", "blue", "yellow", "magenta", "cyan", "white")

msg = input("What would you like to print? ")
color = input("what color? ")
if color not in allowed_colors:
    color = "magenta"

ascii_msg = figlet_format(msg)
colored_ascii = colored(ascii_msg, color=color)
print(colored_ascii)
