from random import choice

player_score = 0
ai_score = 0
winning_score = 2

while player_score < winning_score and ai_score < winning_score:
    print(f"palyer score: {player_score}, computer score: {ai_score}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    p_choice = input("Please make your move: ").lower()

    if p_choice == "quit" or p_choice == "q":
        break

    ai_choice = choice(["rock", "paper", "scissors"])
    print(f"You choose {p_choice}, AI choose {ai_choice}...")

    p_wins = "You Win!"
    ai_wins = "AI Wins!"
    tie = "It's a tie!"

    if p_choice == ai_choice:
        print(tie)
    elif p_choice == "rock":
        if ai_choice == "scissors":
            print(p_wins)
            player_score += 1
        if ai_choice == "paper":
            print(ai_wins)
            ai_score += 1
    elif p_choice == "paper":
        if ai_choice == "rock":
            print(p_wins)
            player_score += 1
        if ai_choice == "scissors":
            print(ai_wins)
            ai_score += 1
    elif p_choice == "scissors":
        if ai_choice == "paper":
            print(p_wins)
            player_score += 1
        if ai_choice == "rock":
            print(ai_wins)
            ai_score += 1
    else:
        print("please enter a valid choice")


print(f"FINAL SCORES: palyer: {player_score}, computer: {ai_score}")
if player_score == winning_score:
    print("Congrats! You Won!")
elif player_score == ai_score:
    print("It's a tie")
else:
    print("NO! AI Won!")
