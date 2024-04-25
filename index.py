# times = int(input("How many times do I have to tell you? "))

# for t in range(times):
#     print(f"{t+1} Clean up your room!".upper())

for num in range(1, 21):
    if num == 4 or num == 13:
        print(f"{num} is Legendary...")
    elif num == 19:
        print(f"{num} is for delusionals and traitors")
    elif num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
