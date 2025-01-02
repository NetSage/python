import random

print('''
================================
Rock Paper Scissors Lizard Spock
================================
1) ✊ (Rock)
2) ✋ (Paper)
3) ✌️ (Sicissors)
4) 🦎 (Lizard)
5) 🖖 (Spock)
''')

emoji = ['✊', '✋', '✌️', '🦎', '🖖']

computer = random.randint(1, 5)

player = 0

while True:
  try:
    player = int(input("Enter a number: "))       
  except ValueError:
    print("Not a number")
  if player == 1 or player == 2 or player == 3 or player == 4 or player == 5:
    break
  else:
    print('Not 1, 2, 3, 4, or 5')


print('You chose: ' + emoji[player - 1])
print('Computer chose: ' + emoji[computer - 1])

win = 'The Player Won!'

if player == computer:
  print("It's a tie!")
elif player == 1 and (computer == 4 or computer == 3):
  print(win)
elif player == 2 and (computer == 1 or computer == 5):
  print(win)
elif player == 3 and (computer == 2 or computer == 4):
  print(win)
elif player == 4 and (computer == 2 or computer == 5):
  print(win)
elif player == 5 and (computer == 3 or computer == 1):
  print(win)
else:
  print('The Computer Wins')