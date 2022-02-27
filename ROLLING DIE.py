# rolling dice

import random

def roll_dice(min,max):
    while True:
        print("rolling dice.......")
        number=random.randint(min,max)
        print(f"your number:{number}")
        break

roll_dice(1,6)
