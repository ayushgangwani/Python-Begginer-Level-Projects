import random

options = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock, Paper, Scissors!")
print("First to 3 points wins!\n")

while True:
    user_score = 0
    comp_score = 0

    # Loop until someone scores 3
    while user_score < 3 and comp_score < 3:
        user = input("Type Rock/Paper/Scissors: ").strip().lower()
        
        if user not in options:
            print("❌ Invalid choice! Please type Rock/Paper/Scissors.")
            continue

        computer = random.choice(options)

        if (user == "scissors" and computer == "paper") or \
           (user == "paper" and computer == "rock") or \
           (user == "rock" and computer == "scissors"):
            user_score += 1
            print(f"You chose {user.capitalize()} | Computer chose {computer.capitalize()}")
            print("✅ You Won This Round!")

        elif user == computer:
            print(f"You chose {user.capitalize()} | Computer chose {computer.capitalize()}")
            print("😅 It's a Tie!")

        else:
            comp_score += 1
            print(f"You chose {user.capitalize()} | Computer chose {computer.capitalize()}")
            print("💻 Computer Won This Round!")

        print(f"🏆 Score -> You: {user_score} | Computer: {comp_score}\n")

    # Final Result
    if user_score == 3:
        print("🎉 Congrats! You won the game!")
    else:
        print("💻 Computer won the game. Better luck next time!")

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
