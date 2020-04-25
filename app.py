import random
import time
r = 'rock'
p = 'paper'
s = 'scissors'
user_input = ''
game_active = True

while True:
    while True:
        while True:
            user_input = input('Please Enter Rock, Paper or Scissors: ').lower()
            if user_input == r:
                break
            elif user_input == p:
                break
            elif user_input == s:
                break
            else:
                print('InputError')
                pass

        outcome_list = [r, p, s]
        comp_choice = random.choice(outcome_list)
        time.sleep(1)
        print(f'Computer chooses {comp_choice.capitalize()} ')

        if comp_choice == r and user_input == p:
            print('You Win')
            break
        elif comp_choice == r and user_input == s:
            print('Computer Wins')
            break
        else:
            pass #restart

        if comp_choice == p and user_input == s:
            print('You Win')
            break
        elif comp_choice == p and user_input == r:
            print('Computer Wins')
            break
        else:
            pass #restart

        if comp_choice == s and user_input == r:
            print('You Win')
            break
        elif comp_choice == s and user_input == p:
            print('Computer Wins')
            break
        else:
            pass #restart

    play_again = input('Would you like to play again? ').lower()

    if play_again == 'yes':
        pass
    else:
        break





