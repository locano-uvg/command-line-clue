#!/usr/bin/env python3

import os
import shutil
from pathlib import Path
import random

structure = {
  "town hall": {
    "offices": {
      "records": {
        "archives": {}
      },
      "meeting rooms": {
        "council chamber": {}
      }
    }
  },
  "park": {
    "playground": {
      "sandbox": {}
    },
    "pond": {
      "dock": {}
    },
    "gazebo": {}
  },
  "shops": {
    "bakery": {
      "kitchen": {},
      "storage": {}
    },
    "market": {
      "aisles": {},
      "stockroom": {}
    },
    "cafe": {}
  },
  "houses": {
    "mansion": {
      "library": {
        "study": {}
      },
      "garden": {
        "greenhouse": {}
      }
    },
    "cottage": {
      "living room": {},
      "cellar": {}
    }
  },
  "school": {
    "classrooms": {
      "science lab": {},
      "art room": {}
    },
    "gymnasium": {},
    "cafeteria": {
      "kitchen": {}
    }
  }
}

class MysteryGame:
  def __init__(self):
    # All possible people who might be in the town
    self.all_people = [
      "The Librarian", "The Shopkeeper", "The Gardener", "The Teacher", "The Mayor", "The Chef",
      "The Postman", "The Baker", "The Police Officer", "The Doctor", "The Artist", "The Musician",
      "The Carpenter", "The Tailor", "The Banker", "The Journalist", "The Florist", "The Clockmaker",
      "The Blacksmith", "The Innkeeper","The Jocker", "The Engineer"
    ]

    self.students = [
      "Ludwing", "Nadissa"
    ]

    # All possible objects that might be found
    self.all_objects = [
      "Garden Shears", "Kitchen Knife", "Heavy Book", "Bronze Trophy", "Glass Bottle", "Letter Opener",
      "Walking Stick", "Brass Candlestick", "Old Key", "Fountain Pen", "Silver Watch", "Magnifying Glass",
      "Antique Compass", "Paint Brush", "Crystal Vase", "Iron Poker", "Leather Gloves", "Brass Bell",
      "Steel Ruler", "Wooden Box"
    ]

    # We'll populate these during game generation
    self.suspects = []        # The 6 chosen suspects
    self.weapons = []         # The 6 chosen weapons
    self.guilty_suspect = ""  # The answer
    self.murder_weapon = ""   # The answer
    self.murder_location = "" # The answer

    # Will store our clue distribution
    self.room_contents = {}   # Will map room paths to their contents

    # Get all possible room paths
    self.all_rooms = self._get_all_rooms()

  def _get_all_rooms(self):
    """Gets all possible room paths from our directory structure."""
    def get_paths(structure, current_path=""):
      paths = []
      for name, substructure in structure.items():
        new_path = f"{current_path}/{name}" if current_path else name
        paths.append(new_path)
        if substructure:  # If there are subdirectories
          paths.extend(get_paths(substructure, new_path))
      return paths
    return get_paths(structure)

  def generate_mystery(self, num_suspects=6, num_weapons=6):
    """
    Generates all elements of our mystery game.

    Args:
        num_suspects (int): Number of suspects to include in the game. 
                           Must be between 3 and len(all_people).
        num_weapons (int): Number of weapons to include in the game.
                          Must be between 3 and len(all_objects).

    The function ensures the game remains balanced by:
    1. Validating the input numbers are reasonable for a solvable game
    2. Adjusting the distribution of clues based on the number of suspects/weapons
    3. Maintaining the ratio of real clues to red herrings
    """
    # Input validation to ensure the game is solvable
    num_suspects = max(3, min(num_suspects, len(self.all_people)))
    num_weapons = max(3, min(num_weapons, len(self.all_objects)))

    # Select our random suspects and weapons based on the parameters
    self.suspects = random.sample(self.all_people, num_suspects)
    self.weapons = random.sample(self.all_objects, num_weapons)

    # Choose our answers
    self.guilty_suspect = random.choice(self.suspects)
    self.murder_weapon = random.choice(self.weapons)
    self.murder_location = random.choice(self.all_rooms)

    # Remove answers from distribution pools
    available_suspects = [s for s in self.suspects if s != self.guilty_suspect]
    available_weapons = [w for w in self.weapons if w != self.murder_weapon]
    available_rooms = [r for r in self.all_rooms if r != self.murder_location]

    # Scale the number of extra people and objects based on the game difficulty
    # For easier games (fewer suspects), we add fewer red herrings
    extra_people_count = min(
      len(available_rooms) - len(available_suspects),
      round((20 - num_suspects) * 0.5)  # Use fewer red herrings for easier games
    )
    extra_objects_count = min(
      len(available_rooms) - len(available_weapons),
      round((20 - num_weapons) * 0.5)
    )

    # Create pools for distribution with scaled red herrings
    distribution_people = available_suspects + random.sample(
      [p for p in self.all_people if p not in self.suspects],
      extra_people_count
    )

    distribution_objects = available_weapons + random.sample(
      [o for o in self.all_objects if o not in self.weapons],
      extra_objects_count
    )

    # Initialize all rooms as empty
    self.room_contents = {room: {"people": [], "objects": []} for room in self.all_rooms}

    # Distribute items, ensuring a good spread of clues
    for person in distribution_people:
      room = random.choice(available_rooms)
      self.room_contents[room]["people"].append(person)

    for obj in distribution_objects:
      room = random.choice(self.all_rooms)
      self.room_contents[room]["objects"].append(obj)

  def generate_notebook(self):
    """Generates the content for notebook.md"""
    return f"""# Detective's Notebook

## Suspects
{chr(10).join(f'- [ ] {suspect}' for suspect in self.suspects)}

## Weapons
{chr(10).join(f'- [ ] {weapon}' for weapon in self.weapons)}

## Notes
*Use this space to record your findings and deductions...*

Location of the crime is still unknown - the room must have been empty when it happened...
"""

  def create_room_files(self, room_path: Path, content: dict):
    """Creates persons.txt and objects.txt with their contents."""
    with open(room_path / "persons.txt", "w") as f:
      f.write("\n".join(content.get("people", [])))

      with open(room_path / "objects.txt", "w") as f:
        f.write("\n".join(content.get("objects", [])))

  def create_game_directories(self, base_path: str = "game"):
    base_dir = Path(base_path)

    if base_dir.exists():
      shutil.rmtree(base_dir)

    base_dir.mkdir()

    # Create notebook.md

    with open(base_dir / "notebook.md", "w") as f:
      f.write(self.generate_notebook())

    def create_directories(current_path: Path, structure: dict):
      for name, substructure in structure.items():
        new_path = current_path / name

        try:
          new_path.mkdir(exist_ok=True)
        except Exception as e:
          continue

        # Get relative path for content lookup
        rel_path = str(new_path.relative_to(base_dir))

        # Get and create room contents
        contents = self.room_contents.get(rel_path, {"people": [], "objects": []})

        try:
          # Create persons.txt
          with open(new_path / "persons.txt", "w") as f:
            f.write("\n".join(contents["people"]))

          # Create objects.txt
          with open(new_path / "objects.txt", "w") as f:
            f.write("\n".join(contents["objects"]))

        except Exception as e:
          print(f"Error creating files in {new_path}: {e}")

        # Process subdirectories
        if substructure:
          create_directories(new_path, substructure)

    create_directories(base_dir, structure)

  def check_lateral_path(self, current_segments, next_segments):
    if len(current_segments) != len(next_segments):
        return False
        
    parent_segments = current_segments[:-1]
    next_parent_segments = next_segments[:-1]
    
    return (parent_segments == next_parent_segments and 
            current_segments[-1] != next_segments[-1])

  def create_lateral_clue(self, current_room, next_room):
    next_location = next_room.split('/')[-1]
    lateral_path_dialogue_variations = [
        "You hear sound coming from the nearby {next_location}.",
        "A staff member mentions checking the {next_location}.",
        "Through the window, you can see the lights are on in the {next_location}.",
        "The janitor suggests taking a look in the {next_location}.",
        "Recent activity has been reported in the {next_location} area.",
        "You overhear someone mentioning suspicious noises from the {next_location}.",
        "You get the feeling you should check the {next_location}.",
        "Security cameras caught movement near the {next_location} entrance.",
        "A cleaning schedule shows the {next_location} was cleaned after this spot.",
        "Local gossip suggests something unusual in the {next_location}."
    ]
    chosen_dialogue = random.choice(lateral_path_dialogue_variations)
    
    clue_text = f"""Investigation Update:

{chosen_dialogue.format(next_location=next_location)}

Hint: To reach this location, you'll need to move back and down to the next location: 'cd "../{next_location}"'
"""
    
    current_path = Path("game") / Path(current_room)
    with open(current_path / "clue.txt", "w") as f:
        f.write(clue_text)
    
  def create_upward_clue(self, current_room, next_room):
    next_location = next_room.split('/')[0]
    next_location_specific = next_room.split('/')[-1]

    upward_dialogue_variations = [
        "Something tells me we should go back and check somewhere else in the {next_location}.",
        "A police report mentions returning to the {next_location} for another look.",
        "Your intuition suggests backtracking to the {next_location} and looking for something else.",
        "Maybe we should check back in the {next_location}.",
        "An old note suggests reconsidering the {next_location}.",
        "The evidence points back to the {next_location}.",
        "We should double-check something back in the {next_location}.",
        "New information suggests returning to the {next_location}.",
        "Perhaps we missed a detail in the {next_location}.",
        "The investigation leads back to the {next_location}."
    ]
    
    updown_dialogue_variations = [
        "Check the {next_location_specific} in the {next_location}.",
        "Go to the {next_location_specific} in the {next_location}.",
        "Go back and check the {next_location_specific} in the {next_location}.",
    ]

    if next_location != next_location_specific:
      chosen_dialogue = random.choice(updown_dialogue_variations)
    else:
      chosen_dialogue = random.choice(upward_dialogue_variations)
    
    clue_text = f"""New Clue:

{chosen_dialogue.format(next_location=next_location, next_location_specific=next_location_specific)}

Hint: You'll need to go back several directories to reach this location.
Remember that you can use multiple '../' to go up multiple levels:
- 'cd ..'    goes up one level
- 'cd ../..' goes up two levels
- and so on...

"""
    
    current_path = Path("game") / Path(current_room)
    with open(current_path / "clue.txt", "w") as f:
        f.write(clue_text)
    
  def generate_final_location_variations(self):
    """
    Creates dramatic dialogue templates for the final revelation at the murder location.
    These templates should create a sense of discovery and conclusion.
    """
    dialogue_variations = [
        "The evidence is clear - this is where the crime took place! The room's undisturbed state tells the whole story.",
        "At last! This untouched crime scene reveals the truth. No one has been here since the incident.",
        "Your detective instincts were right - this empty room holds the answers. The pristine state of things confirms this is where it happened.",
        "The undisturbed dust patterns confirm it - you've found the crime scene! The emptiness of the room speaks volumes.",
        "Here it is - the untouched crime scene! The stillness of this room suggests no one has entered since the incident.",
        "You can feel it - this is where it happened. The undisturbed state of the room confirms your suspicions.",
        "The perfect preservation of this room tells you everything - this is definitely the crime scene!",
        "Your investigation has led you to the truth - this empty room is where it all happened!",
        "The pristine condition of this room confirms your theory - you've found the crime scene!",
        "Success! This untouched room is exactly what you've been looking for - the scene of the crime!"
    ]
    return dialogue_variations

  def add_murder_location_to_path(self, important_rooms):
    """
    Adds the murder location to our sequence of important rooms and creates
    the final revelation clue at that location.
    
    Args:
        important_rooms: List of current important room paths
    
    Returns:
        Updated list of important rooms including the murder location
    """
    # Add the murder location to our path
    updated_rooms = important_rooms + [self.murder_location]
    
    # Create the final revelation clue
    dialogue_options = self.generate_final_location_variations()
    chosen_dialogue = random.choice(dialogue_options)
    
    final_clue = f"""Investigation Conclusion:

{chosen_dialogue}

Your careful detective work has paid off. The empty state of this room matches 
witness accounts - no one was around when the crime occurred. This must be 
where the murderer carried out their plan!

Make sure to document this discovery in your notebook.md file along with your 
other findings about the weapon and suspect."""

    # Create the clue file in the murder location
    murder_path = Path("game") / Path(self.murder_location)
    with open(murder_path / "clue.txt", "w") as f:
        f.write(final_clue)
    
    return updated_rooms

  def create_breadcrumbs(self):
    important_rooms = []

    # Go through each room in our room_contents
    for room_path, contents in self.room_contents.items():
      # Check if this room has any of our suspects (except the guilty one)
      has_suspect = any(person in self.suspects for person in contents["people"])

      # Check if this room has any of our weapons (except the murder weapon)
      has_weapon = any(object in self.weapons for object in contents["objects"])

      # If the room has either a suspect or a weapon, it's important
      if has_suspect or has_weapon:
        important_rooms.append(room_path)
    important_rooms.sort()

    important_rooms = self.add_murder_location_to_path(important_rooms)

    dialogue_variations = [
      "I overheard {person} mentioning something strange they noticed near the {location}.",
      "{person} came running to the police station, insisting they saw suspicious activity around the {location}.",
      "According to {person}, there were unusual sounds coming from the {location} last night.",
      "During the morning roll call, {person} reported odd footprints leading to the {location}.",
      "The night watchman spoke with {person}, who noticed an unfamiliar figure lurking near the {location}.",
      "{person} left an anonymous tip about unusual activity at the {location}.",
      "Earlier today, {person} reported seeing an unexpected light in the {location}.",
      "A note from {person} mentions witnessing something concerning near the {location}.",
      "While making their rounds, {person} noticed the {location} door was slightly ajar.",
      "Local residents say {person} was the last one to report activity near the {location}."
    ]

    if not important_rooms:
      return  # Safety check in case there are no important rooms

    first_destination = important_rooms[0].split('/')[-1]
    observer = random.choice(self.all_people)
    chosen_dialogue = random.choice(dialogue_variations)

    clue_text = chosen_dialogue.format(
      person=observer,
      location=first_destination
    )

    full_clue = f"""Detective's Initial Report:

{clue_text}

This seems like a good place to start our investigation. Remember to:
- Use 'cd' to move between locations
- Use 'ls' to list the contents of each location
- Use 'cat' to read any text files you find
"""

    base_dir = Path("game")
    with open(base_dir / "clue.txt", "w") as f:
      f.write(full_clue)

    next_location_dialogue_variations = [
      "You notice fresh footprints leading towards the {next_location}.",
      "A trail of scattered papers points deeper into the {next_location}.",
      "Through the window, you spot movement in the direction of the {next_location}.",
      "The floorboards creak, suggesting someone recently walked towards the {next_location}.",
      "A local resident mentions seeing a shadowy figure entering the {next_location}.",
      "You find a dropped keychain with a tag labeled '{next_location}'.",
      "The dust on the floor shows a clear path heading to the {next_location}.",
      "A security guard mentions hearing noises coming from the {next_location}.",
      "Recent scratches on the floor lead towards the {next_location}.",
      "A hastily written note mentions checking the {next_location} next."
    ]

    for i in range(len(important_rooms) - 1):
        current_room = important_rooms[i]
        next_room = important_rooms[i + 1]
        
        current_segments = current_room.split('/')
        next_segments = next_room.split('/')
        
        # Check if next_room is truly a subdirectory of current_room
        is_subdirectory = (
            # Must be longer (deeper) than current path
            len(next_segments) > len(current_segments) and
            # All segments up to current path length must match
            all(current_segments[j] == next_segments[j] 
                for j in range(len(current_segments)))
        )
        
        if is_subdirectory:
            # The next location to point to is the next segment after current path
            next_location = next_segments[len(current_segments)]
            
            chosen_dialogue = random.choice(next_location_dialogue_variations)
            
            clue_text = f"""Investigation Update:

{chosen_dialogue.format(next_location=next_location)}

Remember: Use 'cd "{next_location}"' to follow this lead.
"""
            
            current_path = Path("game") / Path(current_room)
            with open(current_path / "clue.txt", "w") as f:
                f.write(clue_text)
            
        elif self.check_lateral_path(current_segments, next_segments):
            self.create_lateral_clue(current_room, next_room)
        else:
          self.create_upward_clue(current_room, next_room)

    return important_rooms

if __name__ == "__main__":
  game = MysteryGame()
  game.generate_mystery(3, 3)
  game.create_game_directories()
  game.create_breadcrumbs()
  print("Your mystery game has been generated!")
  print("use `cd game` and begin investigating.")
