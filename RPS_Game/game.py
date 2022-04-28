import random

game_art = {
'r':
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'p':
'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
's':
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}

options = ['rock', 'paper', 'scissors']
game_defs = {'r':'rock', 'p':'paper', 's':'scissors'}

def draw():
    uc = input('Rock, Paper, or Scissors? ').lower()[0]
    cc = random.choice(options)[0]
    rg_res = [uc,cc]
    print(f'You chose {game_defs[uc]}')
    print(game_art[uc])
    print(f'The computer chose {game_defs[cc]}')
    print(game_art[cc])

    if uc == cc:
        print("It's a tie!")
        return 0
    else:
        if ('r' in rg_res) and ('p' in rg_res):
            if rg_res.index('p') == 1:
                print('Computer wins!')
                return 1
            else:
                print('You win!')
                return 2
        elif('r' in rg_res) and ('s' in rg_res):
            if rg_res.index('r') == 1:
                print('Computer wins!')
                return 1
            else:
                print('You win!')
                return 2
        elif ('s' in rg_res) and ('p' in rg_res):
            if rg_res.index('s') == 1:
                print('Computer wins!')
                return 1
            else:
                print('You win!')
                return 2


if __name__ == '__main__':
    draw()
    while True:
        answer = input('\nWould you like to play again? ').lower()
        if answer.startswith('y'):
            print('')
            draw()
        elif answer.startswith('n'):
            print('Goodbye!')
            exit()
        else:
            print('Invalid input. \n')
            continue
