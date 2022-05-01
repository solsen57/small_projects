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
    player_score = 0
    computer_score = 0
    uc = input('Rock, Paper, or Scissors? ').lower()[0]
    cc = random.choice(options)[0]
    rg_res = [uc,cc]
    print(f'You chose {game_defs[uc]}')
    print(game_art[uc])
    print(f'The computer chose {game_defs[cc]}')
    print(game_art[cc])

    if uc == cc:
        print("It's a tie!")
        return player_score, computer_score
    else:
        if ('r' in rg_res) and ('p' in rg_res):
            if rg_res.index('p') == 1:
                print('Computer wins!')
                computer_score += 1
                return player_score, computer_score
            else:
                print('You win!')
                player_score += 1
                return player_score, computer_score
        elif('r' in rg_res) and ('s' in rg_res):
            if rg_res.index('r') == 1:
                print('Computer wins!')
                computer_score += 1
                return player_score, computer_score
            else:
                print('You win!')
                player_score += 1
                return player_score, computer_score
        elif ('s' in rg_res) and ('p' in rg_res):
            if rg_res.index('s') == 1:
                print('Computer wins!')
                computer_score += 1
                return player_score, computer_score
            else:
                print('You win!')
                player_score += 1
                return player_score, computer_score


if __name__ == '__main__':
    user = 0
    comp = 0
    while True:
        p, c = draw()
        user += p
        comp += c
        print(f'Your Score: {(user)}\nComputer Score: {(comp)}')
        while True:
            answer = input('\nWould you like to play again? ').lower()
            if answer.startswith('y'):
                print('')
                break
            elif answer.startswith('n'):
                print('Goodbye!')
                exit()
            else:
                print('Invalid input. \n')
                continue
