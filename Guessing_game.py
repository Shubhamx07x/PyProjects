import random
import time

ran=input('Enter a Range of Number (ex: 1-10): ')
low,high=map(int,ran.split('-'))

n=random.randint(low,high)

guess=int(input('Guess a no: '))

if n==guess:
    print('your guess is right !!!')
else:
    while True:
      if guess<n:
         print('your Guess is too low')
         guess=int(input('Guess a no: '))
      elif guess>n:
          print('your guess is too high')
          guess=int(input('Guess a no: '))
      elif guess==n:
          print('your guess is right yus !!!')
          print('''
                ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
                ───█▒▒░░░░░░░░░▒▒█───
                ────█░░█░░░░░█░░█────
                ─▄▄──█░░░▀█▀░░░█──▄▄─
                █░░█─▀▄░░░░░░░▄▀─█░░█
                '''
)
          time.sleep(3)
          break
    