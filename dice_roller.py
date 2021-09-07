import random


def main():
  dice_rolls = 2
  dice_sum = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    if roll == 1:
      print(f'you rolled a {roll}! Critical Fail')
    elif roll == 6:
      print (f'you have rolled a {roll}! Congratulations!')
    else:
      print(f'You rolled a {roll}')

  if dice_sum == 2:
      print('snake eyes')
  elif dice_sum == 12:
      print(f'{dice_sum}! WOW!')
  else:
    print(f'you have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()