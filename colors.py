from termcolor import colored

print(colored("HI THERE", color="cyan"))
print(colored("NOT HI THERE", color="red",
      on_color="on_green", attrs=["blink"]))
