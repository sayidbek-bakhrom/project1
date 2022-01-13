import random


user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.\n").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 0, scissors: 2
    computer_choice = options[random_number]
   
    print(f"Computer picked {computer_choice}.")

    if user_input == "rock" and computer_choice == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_choice == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_choice == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_choice:
        print("It's draw")
    else:
        print("You lost!")
        computer_wins += 1


print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times")
print("Goodbye!")