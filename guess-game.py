from random import randint

random_num = randint(1, 10)

# guess = None
# while guess != random_num:
#     guess = int(input("Pick a number between 0 an 10: "))
#     if guess < random_num:
#         print("Too low!")
#     elif guess > random_num:
#         print("Too high!")
#     else:
#         print("You won")


guess = None
while True:
    guess = int(input("Pick a number between 0 an 10: "))
    if guess < random_num:
        print("Too low!")
    elif guess > random_num:
        print("Too high!")
    else:
        print("You won")
        play_agaian = input("Want to continue playing? (Y/N) ")
        if play_agaian.lower() == "y":
            random_num = randint(1, 10)
            guess = None
        else:
            print("Thank you for playing!")
            break
