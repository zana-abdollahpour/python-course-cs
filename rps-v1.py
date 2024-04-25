print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player1, please make your move: ")
print("*** NO CHEATING! ***\n" * 20)
player2 = input("Player2, please make your move: ")

# Verbose
# if player1 == "rock" and player2 == "scissors":
#     print("Player1 wins!")
# elif player1 == "rock" and player2 == "paper":
#     print("Player2 Wins!")
# elif player1 == "paper" and player2 == "rock":
#     print("Player1 Wins!")
# elif player1 == "paper" and player2 == "scissors":
#     print("Player2 Wins!")
# elif player1 == "scissors" and player2 == "rock":
#     print("Player2 Wins!")
# elif player1 == "scissors" and player2 == "paper":
#     print("Player1 Wins!")
# elif player1 == player2:
#     print("It's a tie!")
# else:
#     print("Something went wrong")


p1_wins = "Player 1 Wins!"
p2_wins = "Player 2 Wins!"
tie = "It's a tie!"

if player1 == player2:
    print(tie)
elif player1 == "rock":
    if player2 == "scissors":
        print(p1_wins)
    if player2 == "paper":
        print(p2_wins)
elif player1 == "paper":
    if player2 == "rock":
        print(p1_wins)
    if player2 == "scissors":
        print(p2_wins)
elif player1 == "scissors":
    if player2 == "paper":
        print(p1_wins)
    if player2 == "rock":
        print(p2_wins)
