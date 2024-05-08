import requests
from pyfiglet import figlet_format  # type: ignore
from termcolor import colored
from random import choice

header = figlet_format("BAD Joke 3000!")  # type: ignore
header = colored(header, "magenta")  # type: ignore
print(header)

term = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
raw_res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": term})
res = raw_res.json()

num_jokes = res["total_jokes"]
results = res["results"]


if num_jokes >= 1:
    print(choice(results)["joke"])
else:
    print("No joke was found wit keyowrd '{}'".format(term))
