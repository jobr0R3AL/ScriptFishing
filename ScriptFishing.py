#!/usr/bin/env python3
inv = []
import time
import random

catch_chance = 0.4
fish_types = [
    "Trout!", 
    "Bass!", 
    "Rainbow Trout!", 
    "Salmon!", 
    "Pike!",
    "Catfish!",     # Heavy bottom feeder
    "Walleye!",     # Clean classic
    "Goldfish?!",   # Super rare meme catch
    "Sturgeon!",    # Absolute prehistoric unit
    "Carp!"         # Big chonker
]


print("fishing...")
time.sleep(1.5)
if random.random() < catch_chance:
    random_fish = random.choice(fish_types)
    weight = random.randint(1, 18)
    size = random.randint(2, 36)
    print("you got a...")
    print(f"{random_fish}")
    print(f"weight: {weight} kg | Size: {size} inches")

    inv.append(random_fish)
# this sits right in the background making a log for the like fishing stuff
    with open("fishing_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{random_fish} ({weight} kg | {size} inches)\n")

else:
    print("Ah! It snapped the line! The fish got away sadly.")


input("\nPress Enter to close...")
