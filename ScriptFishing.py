#!/usr/bin/env python3
import time
import random

catch_chance = 0.3
fish_types = [
    "A WHALE?!?!?!",
    "Trout!", 
    "Bass!", 
    "Rainbow Trout!", 
    "Salmon!", 
    "Pike!",
    "Catfish!",     
    "Walleye!",     
    "Goldfish?!",   
    "Sturgeon!",    
    "Carp!",         
    "Pocket Whale", 
    "Common whitefish?", 
    "Boot..."
]

# LEVEL CALCULATOR - Reads lifetime progress from the local log file
try:
    with open("fishing_log.txt", "r", encoding="utf-8") as f:
        total_catches = len(f.readlines())
except FileNotFoundError:
    total_catches = 0

player_level = 1 + (total_catches // 5)
inv = []

print("-=-=-=-= ScriptFishing! v0.3 =-=-=-=-")
print(f"LIFETIME LEVEL: {player_level} | Catches to Level Up: {5 - (total_catches % 5)}")
print("Commands: 'fish' | 'inv' | 'quit'")

# --- THE MAIN MENU ENGINE ---
while True:
    action = input("\n[Action]: ").strip().lower()
    
    if action == "quit":
        print(f"\nHauled home {len(inv)} fish this session. Tight lines!")
        break
        
    elif action == "inv":
        print("\n--- CURRENT POCKETS ---")
        if not inv:
            print("Pockets are empty! Use 'fish' to cast.")
        else:
            for item in inv:
                print(f"-> {item}")
        print("-------------------------")
        
    elif action == "fish":
        print("Casting line...")
        time.sleep(1.5)
        
        # THE CASINO ROLL (Indented 8 spaces)
        if random.random() < catch_chance:
            random_fish = random.choice(fish_types)
            max_weight = player_level * 20
            weight = random.randint(1, max_weight)
            size = random.randint(2, 26)
            
            print("\nyou got a...")
            print(f"{random_fish}")
            print(f"weight: {weight} kg | Size: {size} inches")
            
            catch_details = f"{random_fish} ({weight} kg | {size} inches)"
            inv.append(catch_details)
            
            # Silent backend disk logging (Indented 12 spaces)
            with open("fishing_log.txt", "a", encoding="utf-8") as log_file:
                log_file.write(f"{catch_details}\n")
            
            # Incremental level-up processing
            total_catches += 1
            if (1 + (total_catches // 5)) > player_level:
                player_level = 1 + (total_catches // 5)
                print(f"\nLEVEL UP! You are now level {player_level}!!")
                
        else: # Lined up perfectly with your catch_chance check!
            print("Ah! It snapped the line! The fish got away sadly.")

