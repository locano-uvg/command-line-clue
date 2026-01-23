#!/usr/bin/env python3
import sys
import hashlib

def get_hash(s):
    return hashlib.md5(s.lower().strip().encode()).hexdigest()

EXPECTED_SUSPECT = "af98fd762836823db7d8c2f86904f7e4"
EXPECTED_WEAPON = "f530318169a256f2e165942674d53795"
# We accept either the full path or just the room name
EXPECTED_LOCATION_HASHES = ["369603e020e4328eaf933837db134889", "bde94582c0df875f118f2b8989e8648f"]

def print_usage():
    print("Usage: python3 accuse.py \"<Suspect Name>\" \"<Weapon Name>\" \"<Room Name>\"")
    print("Example: python3 accuse.py \"The Gardener\" \"Garden Shears\" \"Garden\"")
    print("Don't forget the quotes if the name has spaces!")

if len(sys.argv) != 4:
    print("❌ Error: You need to provide exactly 3 arguments.")
    print_usage()
    sys.exit(1)

suspect = sys.argv[1]
weapon = sys.argv[2]
location = sys.argv[3]

suspect_match = get_hash(suspect) == EXPECTED_SUSPECT
weapon_match = get_hash(weapon) == EXPECTED_WEAPON
location_match = get_hash(location) in EXPECTED_LOCATION_HASHES

if suspect_match and weapon_match and location_match:
    print("\n🎉 CONGRATULATIONS DETECTIVE! 🎉")
    print("You have correctly identified the killer, the weapon, and the location!")
    print(f"It was {suspect} with the {weapon} in the {location}.")
    print("The town is safe once again thanks to your command line skills.")
    sys.exit(0)
else:
    print("\nYour accusation is incorrect:")
    print(f"Suspect:  {'✅ Correct' if suspect_match else '❌ Incorrect'}")
    print(f"Weapon:   {'✅ Correct' if weapon_match else '❌ Incorrect'}")
    print(f"Location: {'✅ Correct' if location_match else '❌ Incorrect'}")
    print("\nKeep investigating!")
    sys.exit(1)
