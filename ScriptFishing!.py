#!/usr/bin/env python3
import time
import random

catch_chance = 0.4
fish = ["Trout!", "Bass!","Rainbow Trout!","Salmon!","Pike!",]

print("fishing...")
time.sleep(1.5)
if random.random() < catch_chance:
    random_fish = random.choice(fish)
    weight = random.randint(2, 18)
    size = random.randint(12,36)
    print("you got a...")
    print(f"{random_fish}")
    print(f"weight: {weight} kg | Size: {size} inches")
else:
    print("Ah! It snapped the line! The fish got away sadly.")


input("\nPress Enter to close...")
