# Mystery in the Small Town: A Command Line Investigation Game

Welcome, Detective! A crime has occurred in our small town, and we need your command line investigation skills to solve it. You'll explore different locations, gather clues, and use your powers of deduction to find the culprit.

## The Crime

A crime has been committed in our quiet town. The police have narrowed down the list of suspects and potential weapons, but they need your help to identify the perpetrator and the murder weapon. The crime must have taken place in an empty room, as no one in town witnessed the act.

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

For example, let's say you're investigating the library:
```bash
cd library
ls              # Shows: objects.txt  persons.txt
cat persons.txt # Might show: "The Teacher"
```
If you find The Teacher here, you can cross them off your suspect list!

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
