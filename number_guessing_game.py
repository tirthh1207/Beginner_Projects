import random

win_no  = random.randint(1,101)

total_gusses = 1
while True:
    user_guess = int(input("Enter the number of guesses you want: "))
    # Validate the input
    if user_guess <1 or user_guess >100:
        user_guess = int(input("Enter the number of guesses you want: "))
        print("Please enter a number between 1 and 100")
        continue

    # Check how close the guess is
    in_close = abs(user_guess - win_no)     
    if in_close != 0 and in_close <= 10:
        print(f"You are very close! but {'Low'if user_guess < win_no else 'High'}")
        total_gusses += 1  
        continue
    # Give hints to the user
    if user_guess < win_no:
        print('It\'s low! Try again.')
    elif user_guess > win_no:
        print('It\'s high! Try again.')
    else:
        print('Congratulations! You guessed it right.')
        print(f'You guessed it in {total_gusses} tries.')
        break
    total_gusses += 1



