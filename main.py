import random
user_input = input("Enter a choice (R, P, S): ")
possible_actions = ["R", "P", "S"]
cpu_option = random.choice(possible_actions)
print(f"\nPlayer {user_input}, CPU {cpu_option}.\n")

if user_input == cpu_option:
    print(f"Both players selected {user_input}. It's a tie!")
elif user_input == "R":
    if cpu_option == "S":
        print("ROCK smashes SCISSORS! You win!")
    else:
        print("PAPER covers ROCK! You lose.")
elif user_input == "PAPER":
    if cpu_option == "R":
        print("P covers ROCK! You win!")
    else:
        print("SCISSORS cuts PAPER! You lose.")
elif user_input == "S":
    if cpu_option == "P":
        print("SCISSORS cuts PAPER! You win!")
    else:
        print("ROCK smashes SCISSORS! You lose.")