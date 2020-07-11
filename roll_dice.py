import random
import time
import os

c=0
val=[]
while True:
    n=int(input('Choose one option:\n1.Roll the dice\n2.Quit\n'))
    if n==2:
        break
    else:
        print('Rolling...')
        time.sleep(1)
        print('You got',random.randint(1,6))
        time.sleep(2)
        os.system('cls')