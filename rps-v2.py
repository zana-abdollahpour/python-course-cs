from random import choice


print("Rock...")
print("Paper...")
print("Scissors...")

p_choice = input("Please make your move: ").lower()
ai_choice = choice(["rock", "paper", "scissors"])
print(f"You choose {p_choice}, AI choose {ai_choice}...")

p_wins = "Player 1 Wins!"
ai_wins = "AI Wins!"
tie = "It's a tie!"

if p_choice == ai_choice:
    print(tie)
elif p_choice == "rock":
    if ai_choice == "scissors":
        print(p_wins)
    if ai_choice == "paper":
        print(ai_wins)
elif p_choice == "paper":
    if ai_choice == "rock":
        print(p_wins)
    if ai_choice == "scissors":
        print(ai_wins)
elif p_choice == "scissors":
    if ai_choice == "paper":
        print(p_wins)
    if ai_choice == "rock":
        print(ai_wins)
