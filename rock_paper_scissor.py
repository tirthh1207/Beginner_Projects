
import random


def play_game():
    win_conditions = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    total_play = 0
    user_points = 0
    com_points = 0

    while True:
      
        user_choice = input("Enter rock, paper, or scissors (E for exit): ").lower()
        com_choice = random.choice(['rock', 'paper', 'scissors'])
        if user_choice == 'e':
            print("Exiting the game. Goodbye!")
            print(f"-->Total plays: {total_play}, Your points: {user_points}, Computer points: {com_points}")
            break
        elif user_choice.lower() == 'score':
            print(f"-->Total plays: {total_play}, Your points: {user_points}, Computer points: {com_points}")
            continue
        elif user_choice not in win_conditions:
            print("-->Invalid choice. Please choose rock, paper, or scissors.")
            continue

        if user_choice == com_choice:
            print(f"-->You chose {user_choice}, computer chose {com_choice}. IT'S A TIE!")

        
        elif com_choice == win_conditions[user_choice]:
            user_points += 1
            print(f"-->You chose {user_choice}, computer chose {com_choice}. YOU WIN!")
        else:
            com_points += 1
            print(f"-->You chose {user_choice}, computer chose {com_choice}. YOU LOSE!")

        total_play += 1

    if user_points == com_points:
        print("-->It's a tie overall!")
    elif user_points > com_points:
        print("-->You are leading!")
    else:
        print("-->Computer is leading!")
if __name__ == "__main__":
    play_game()