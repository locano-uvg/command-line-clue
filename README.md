The criminal was the Artist and the weapon was the Paint Brush

# Mystery in the Small Town: A Command Line Investigation Game

Welcome, Detective! A crime has occurred in our small town, and we need your command line investigation skills to solve it. You'll explore different locations, gather clues, and use your powers of deduction to find the culprit.

## The Crime

A crime has been committed in our quiet town. The police have narrowed down the list of suspects and potential weapons, but they need your help to identify the perpetrator and the murder weapon. The crime must have taken place in an empty room, as no one in town witnessed the act.

## Game Setup

Before you begin your investigation, you need to generate a fresh mystery to solve. Open your terminal in the game folder and run:

```bash
python3 clue.py
```

This will create a `game` directory containing all the clues, suspects, and weapons for this specific case.

## How to Investigate

### Using the Detective's Notebook

When you start the game, you'll find a `notebook.md` file in your game directory. This notebook contains:
- A list of possible suspects
- A list of potential weapons

As you investigate, you'll cross out suspects and weapons that you find in various locations. The logic is simple: if you find a person or object in a room, they couldn't have been involved in the crime at that time! For example, if you find "The Librarian" in the library, you can cross them off your suspect list.

In your notebook, cross out each eliminated suspect and weapon by changing:
```markdown
- [ ] The Librarian
```
to:
```markdown
- [x] The Librarian
```

The last uncrossed suspect and weapon will be your solution!

### Detective Training (Pro Tips)

Before you start, learn these essential detective skills to move faster:

1. **Tab Completion (The Most Important Skill):**
   Instead of typing the whole name of a room, type the first few letters and press the **Tab** key. Your terminal will finish the name for you! 
   *Example:* Type `cd tow` then press **Tab** -> it becomes `cd "town hall"/`.

2. **Handling Spaces:**
   If a folder has a space (like `town hall`), you must put it in quotes: `cd "town hall"`. If you use **Tab Completion**, the terminal will automatically add quotes or backslashes for you.

3. **Where am I? (`pwd`):**
   If you get lost, type `pwd` (Print Working Directory). It will show you exactly where you are in the town.

4. **Quick Back (`cd -`):**
   Type `cd -` to quickly jump back to the last room you were in.

### Navigating the Town

To move around town and gather evidence, you'll use these simple commands:

1. List what's in your current location:
```bash
ls
```

2. Move to a new location:
```bash
cd library
```

3. Read the contents of a file:
```bash
cat persons.txt
cat objects.txt
```

### Closing the Case

Once you think you've solved the mystery, use the `accuse.py` script in the `game` directory. You'll need to provide the suspect, the weapon, and the room where it happened.

**Important:** You must run this from the `game` folder.

```bash
python3 accuse.py "The Librarian" "Heavy Book" "Library"
```

If you are right, you'll win the game! If not, the script will tell you which parts of your accusation are wrong so you can keep investigating.

### Following the Investigation Trail

To make your investigation easier, we've set up a trail of clues! In many locations, you'll find a `clue.txt` file pointing you toward your next destination. Read these clues using:
```bash
cat clue.txt
```

The clues will help you navigate through town. Sometimes you'll need to:
- Go into a building or room: `cd mansion`
- Go back up one level: `cd ..`
- Go back multiple levels: `cd ../..`
- Move to a parallel room: `cd ../kitchen`

For example, if a clue says "You notice movement in the garden", you might need to:
```bash
cd garden      # Enter the garden
ls             # Check what's here
cat clue.txt   # Read the next clue
```

## Tips for Success
- Always check both `persons.txt` and `objects.txt` in each location
- Update your notebook regularly as you find suspects and weapons
- Follow the trail of clues to ensure you don't miss any locations
- Remember that the crime happened in an empty room
- Keep track of which suspects and weapons you've crossed off

Happy investigating, Detective! The town is counting on you to solve this mystery!
