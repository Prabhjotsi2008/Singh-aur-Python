# MAIN-LOGIC OF THE GAME
def game_logic(user_choice,bot_choice):
    if user_choice == bot_choice:
        print("Its a Draw")
        return 0
    else:
        if user_choice == 1 and bot_choice == 2:
            print("You Lose...")
            return -1
        elif user_choice == 1 and bot_choice == 3:
            print("You Won!!!")
            return 1
        elif user_choice == 2 and bot_choice == 1:
            print("You Won!!!")
            return 1
        elif user_choice == 2 and bot_choice == 3:
            print("You Lose...")
            return -1
        elif user_choice == 3 and bot_choice == 1:
            print("You Lose...")
            return -1
        elif user_choice == 3 and bot_choice == 2:
            print("You Win!!!")
            return 1