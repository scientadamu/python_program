import random
while True:https://github.com/scientadamu/python_program
    posible_choices=["R","S","P"]
    player_choice = None
    system_choice = random.choice(posible_choices)
    while player_choice not in posible_choices:
        player_choice = input("please choice R for Rock, or S for sciessors or P for paper : ").upper()
    if player_choice == system_choice:
        print(f"\nplayer ({player_choice}), \nsystem ({system_choice})")
        print(f"\nTies! both player and system choiced ({player_choice})\n")
        player_choice = input("please choice R for Rock, or S for sciessors or P for paper : ").upper()

    elif player_choice == "R":
        if system_choice == "P":
            print(f"\nplayer ({player_choice}), \nsystem ({system_choice})")
            print(f"\nYou lose! paper cover Rock.\n")

        if system_choice == "S":
            print(f"\nplayer ({player_choice}), \nsystem ({system_choice})")
            print(f"\nYou win! Rock smatch sciessors.\n")
            
    elif player_choice == "S":
        if system_choice == "P":
            print(f"\nplayer ({player_choice}), \nsystem ({system_choice})")
            print(f"\nYou WIN! Sciessors smatch paper.\n")

        if system_choice == "R":
            print(f"\nplayer ({player_choice}), \nsystem ({system_choice})")
            print(f"\nYou Lose! Rock smatch sciessors.\n")
            
    elif player_choice == "P":
        if system_choice == "R":
            print(f"\nplayer ({player_choice}), \nsystem ({system_choice})")
            print(f"\nYou WIN! Paper Cover Rock.\n")

        if system_choice == "S":
            print(f"\nplayer ({player_choice}), \nsystem ({system_choice})")
            print(f"\nYou Lose! Sciessors cut paper.\n")
    play_again=input("Do you want to play again (y/n)")
    
    if play_again !="y":
        break
print("thank you for playing, See you next Time")
