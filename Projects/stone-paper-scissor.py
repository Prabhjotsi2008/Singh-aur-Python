import random, time
from logic import game_logic

user_score = 0
bot_score = 0

while True:
    # bot_choice = random.choice([1,2,3]) # works same as below
    if user_score == 3 or bot_score == 3:
        time.sleep(1)
        print(f"\n{'='*5} FINAL-RESULT {'='*5}")
        if user_score == 3:
            print("You won the entire Game!!!")
        else:
            print("Bot won the entire Game...")
        print("="*24)
        break

    bot_choice = random.randint(1,3)

    print(f"\n{'='*5} GAME-MENU {'='*5}")
    print("Enter 1 for Stone")
    print("Enter 2 for Paper")
    print("Enter 3 for Scissors")
    print("="*21)

    print()
    user_choice = int(input("Enter your choice: "))
    
    time.sleep(0.5)
    
    if user_choice not in [1,2,3]:
        print("\nInvalid choice...")
        continue

    # dictionary to convert integer choice to corresponding string
    converter = {
        1 : "Stone",
        2 : "Paper",
        3 : "Scissors"
    }

    print(f"\nYou chosed: {converter[user_choice]}")
    print(f"Bot chosed: {converter[bot_choice]}")

    time.sleep(1)
    
    print("\nROUND RESULT: ",end="")
    # MAIN-LOGIC OF THE GAME
    round_result = game_logic(user_choice,bot_choice)

    if round_result == 1:
        user_score += 1
    elif round_result == -1:
        bot_score += 1
    
    print()

    print(f"{'='*5} SCOREBOARD {'='*5}")
    print(f"Your Score: {user_score}")
    print(f"Bot Score: {bot_score}")
    print("=" * 22)

    time.sleep(0.5)