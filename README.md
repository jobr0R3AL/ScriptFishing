# ScriptFishing!

ScriptFishing! | Small terminal fishing script. Made in python!

idk but i asked copilot to make this long ass essay or smth:
## 📋 Overview

ScriptFishing is a fun, interactive terminal-based fishing simulator written in Python. Simulate the thrill of fishing with a simple script that randomly determines whether you catch a fish or lose your line!

## 🎣 How It Works

### Game Mechanics

1. **Casting Your Line** - When you run the script, it simulates casting your fishing line with a 1.5 second delay
2. **Chance-Based Catch** - There's a 40% chance (`catch_chance = 0.4`) of successfully catching a fish
3. **Random Fish Selection** - If you catch something, the script randomly selects from 5 different fish species:
   - Trout!
   - Bass!
   - Rainbow Trout!
   - Salmon!
   - Pike!
4. **Fish Details** - Each successful catch includes:
   - **Weight**: Randomly generated between 2-18 kg
   - **Size**: Randomly generated between 12-36 inches
5. **Failure** - If you don't catch anything, the fish snaps your line and gets away

## 🚀 Getting Started

### Requirements
- Python 3.x

### Running the Script

```bash
python3 "ScriptFishing!.py"
```

Or make it executable and run directly:
```bash
chmod +x "ScriptFishing!.py"
./ScriptFishing!.py
```

### Example Output

**Success:**
```
fishing...
you got a...
Salmon!
weight: 14 kg | Size: 28 inches
```

**Failure:**
```
fishing...
Ah! It snapped the line! The fish got away sadly.
```

## 📝 Code Breakdown

| Variable | Purpose |
|----------|---------|
| `catch_chance` | Probability of catching a fish (0.4 = 40%) |
| `fish` | List of possible fish species |
| `weight` | Random weight in kg (2-18 range) |
| `size` | Random size in inches (12-36 range) |

The script uses Python's `random` module for all randomization and `time.sleep()` to create suspense before revealing the catch result.

## 🎯 Future Enhancements

Potential improvements:
- Add difficulty levels
- Track total catches/misses
- Implement a scoring system
- Add more fish species
- Create a persistent high score file

---

**Enjoy fishing! 🎣**
