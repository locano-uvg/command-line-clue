# Contenido {#contenido .TOC-Heading}

[Mi primera idea fue listar todos los archivos del directorio para ver
que tenía de frente -- Ver Caminos.txt -
[1](#mi-primera-idea-fue-listar-todos-los-archivos-del-directorio-para-ver-que-tenía-de-frente-ver-caminos.txt--)](#mi-primera-idea-fue-listar-todos-los-archivos-del-directorio-para-ver-que-tenía-de-frente-ver-caminos.txt--)

# 

# Mi primera idea fue listar todos los archivos del directorio para ver que tenía de frente -- Ver Caminos.txt - 

rowl@L4PT0P-R7A:\~/STW/EXE1-CLUE/STW1-command-line-clue/game\$ tree

.

├── Residential Area

│   ├── cottage

│   │   ├── cellar

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── living room

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── mansion

│   │   ├── garden

│   │   │   ├── clue.txt

│   │   │   ├── greenhouse

│   │   │   │   ├── objects.txt

│   │   │   │   └── persons.txt

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── library

│   │   │   ├── clue.txt

│   │   │   ├── objects.txt

│   │   │   ├── persons.txt

│   │   │   └── study

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── objects.txt

│   └── persons.txt

├── accuse.py

├── clue.txt

├── notebook.md

├── park

│   ├── gazebo

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── objects.txt

│   ├── persons.txt

│   ├── playground

│   │   ├── objects.txt

│   │   ├── persons.txt

│   │   └── sandbox

│   │   ├── clue.txt

│   │   ├── objects.txt

│   │   └── persons.txt

│   └── pond

│   ├── dock

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── objects.txt

│   └── persons.txt

├── school

│   ├── cafeteria

│   │   ├── kitchen

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── classrooms

│   │   ├── art room

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── objects.txt

│   │   ├── persons.txt

│   │   └── science lab

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── gymnasium

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── objects.txt

│   └── persons.txt

├── shops

│   ├── bakery

│   │   ├── kitchen

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── objects.txt

│   │   ├── persons.txt

│   │   └── storage

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── cafe

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── market

│   │   ├── aisles

│   │   │   ├── clue.txt

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── objects.txt

│   │   ├── persons.txt

│   │   └── stockroom

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── objects.txt

│   └── persons.txt

└── town hall

├── objects.txt

├── offices

│   ├── meeting rooms

│   │   ├── council chamber

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── objects.txt

│   ├── persons.txt

│   └── records

│   ├── archives

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── objects.txt

│   └── persons.txt

└── persons.txt

37 directories, 79 files

# Cómo son 79 archivos, mejor decidí usar un script (cortesía de chatgpt) que me diera los archivos no vacíos -- Ver script1.txt -- ahora eran 24

rowl@L4PT0P-R7A:\~/STW/EXE1-CLUE/STW1-command-line-clue/game\$ find .
-type f -size +0c \| while read -r file; do

if file \"\$file\" \| grep -q text; then

if grep -q \'\[\^\[:space:\]\]\' \"\$file\"; then

echo \"\$file\"

fi

fi

done

./clue.txt

./school/gymnasium/persons.txt

./school/classrooms/art room/persons.txt

./school/classrooms/science lab/objects.txt

./Caminos.txt

./town hall/persons.txt

./ArchivosNoVacios.txt

./park/gazebo/persons.txt

./park/gazebo/objects.txt

./park/playground/sandbox/persons.txt

./park/playground/sandbox/clue.txt

./accuse.py

./shops/cafe/objects.txt

./shops/bakery/persons.txt

./shops/bakery/storage/objects.txt

./shops/bakery/objects.txt

./shops/market/aisles/clue.txt

./shops/market/aisles/objects.txt

./shops/market/objects.txt

./Residential Area/mansion/garden/persons.txt

./Residential Area/mansion/garden/clue.txt

./Residential Area/mansion/library/clue.txt

./Residential Area/mansion/library/objects.txt

./Residential Area/mansion/objects.txt

./notebook.md

# Y por pereza a leer esos 24 archivos manualmente XD le puse al script que me imprimiera su contenido. Y leí todo junto. -Ver ContenidoGame.txt -

rowl@L4PT0P-R7A:\~/STW/EXE1-CLUE/STW1-command-line-clue/game\$ find .
-type f -size +0c \| while read -r file; do

if file \"\$file\" \| grep -q text; then

if grep -q \'\[\^\[:space:\]\]\' \"\$file\"; then

echo \"========== \$file ==========\"

cat \"\$file\"

echo

fi

fi

done

========== ./clue.txt ==========

Detective\'s Initial Report:

The night watchman spoke with The Teacher, who noticed an unfamiliar
figure lurking near the garden.

This seems like a good place to start our investigation. Remember to:

\- Use \'cd\' to move between locations

\- Use \'ls\' to list the contents of each location

\- Use \'cat\' to read any text files you find

========== ./school/gymnasium/persons.txt ==========

The Librarian

========== ./school/classrooms/art room/persons.txt ==========

The Tailor

========== ./school/classrooms/science lab/objects.txt ==========

Silver Watch

========== ./Caminos.txt ==========

.

├── Caminos.txt

├── Residential Area

│   ├── cottage

│   │   ├── cellar

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── living room

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── mansion

│   │   ├── garden

│   │   │   ├── clue.txt

│   │   │   ├── greenhouse

│   │   │   │   ├── objects.txt

│   │   │   │   └── persons.txt

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── library

│   │   │   ├── clue.txt

│   │   │   ├── objects.txt

│   │   │   ├── persons.txt

│   │   │   └── study

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── objects.txt

│   └── persons.txt

├── accuse.py

├── clue.txt

├── notebook.md

├── park

│   ├── gazebo

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── objects.txt

│   ├── persons.txt

│   ├── playground

│   │   ├── objects.txt

│   │   ├── persons.txt

│   │   └── sandbox

│   │   ├── clue.txt

│   │   ├── objects.txt

│   │   └── persons.txt

│   └── pond

│   ├── dock

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── objects.txt

│   └── persons.txt

├── school

│   ├── cafeteria

│   │   ├── kitchen

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── classrooms

│   │   ├── art room

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── objects.txt

│   │   ├── persons.txt

│   │   └── science lab

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── gymnasium

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── objects.txt

│   └── persons.txt

├── shops

│   ├── bakery

│   │   ├── kitchen

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── objects.txt

│   │   ├── persons.txt

│   │   └── storage

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── cafe

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── market

│   │   ├── aisles

│   │   │   ├── clue.txt

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── objects.txt

│   │   ├── persons.txt

│   │   └── stockroom

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── objects.txt

│   └── persons.txt

└── town hall

├── objects.txt

├── offices

│   ├── meeting rooms

│   │   ├── council chamber

│   │   │   ├── objects.txt

│   │   │   └── persons.txt

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── objects.txt

│   ├── persons.txt

│   └── records

│   ├── archives

│   │   ├── objects.txt

│   │   └── persons.txt

│   ├── objects.txt

│   └── persons.txt

└── persons.txt

37 directories, 80 files

========== ./town hall/persons.txt ==========

The Shopkeeper

The Clockmaker

========== ./ArchivosNoVacios.txt ==========

./clue.txt

./school/gymnasium/persons.txt

./school/classrooms/art room/persons.txt

./school/classrooms/science lab/objects.txt

./Caminos.txt

./town hall/persons.txt

./park/gazebo/persons.txt

./park/gazebo/objects.txt

./park/playground/sandbox/persons.txt

./park/playground/sandbox/clue.txt

./accuse.py

./shops/cafe/objects.txt

./shops/bakery/persons.txt

./shops/bakery/storage/objects.txt

./shops/bakery/objects.txt

./shops/market/aisles/clue.txt

./shops/market/aisles/objects.txt

./shops/market/objects.txt

./Residential Area/mansion/garden/persons.txt

./Residential Area/mansion/garden/clue.txt

./Residential Area/mansion/library/clue.txt

./Residential Area/mansion/library/objects.txt

./Residential Area/mansion/objects.txt

./notebook.md

========== ./park/gazebo/persons.txt ==========

The Banker

========== ./park/gazebo/objects.txt ==========

Glass Bottle

========== ./park/playground/sandbox/persons.txt ==========

The Florist

The Engineer

========== ./park/playground/sandbox/clue.txt ==========

New Clue:

Go back and check the aisles in the shops.

Hint: You\'ll need to go back several directories to reach this
location.

Remember that you can use multiple \'../\' to go up multiple levels:

\- \'cd ..\' goes up one level

\- \'cd ../..\' goes up two levels

\- and so on\...

========== ./accuse.py ==========

#!/usr/bin/env python3

import sys

import hashlib

def get_hash(s):

return hashlib.md5(s.lower().strip().encode()).hexdigest()

EXPECTED_SUSPECT = \"af98fd762836823db7d8c2f86904f7e4\"

EXPECTED_WEAPON = \"f530318169a256f2e165942674d53795\"

\# We accept either the full path or just the room name

EXPECTED_LOCATION_HASHES = \[\"369603e020e4328eaf933837db134889\",
\"bde94582c0df875f118f2b8989e8648f\"\]

def print_usage():

print(\"Usage: python3 accuse.py \\\"\<Suspect Name\>\\\" \\\"\<Weapon
Name\>\\\" \\\"\<Room Name\>\\\"\")

print(\"Example: python3 accuse.py \\\"The Gardener\\\" \\\"Garden
Shears\\\" \\\"Garden\\\"\")

print(\"Don\'t forget the quotes if the name has spaces!\")

if len(sys.argv) != 4:

print(\"❌ Error: You need to provide exactly 3 arguments.\")

print_usage()

sys.exit(1)

suspect = sys.argv\[1\]

weapon = sys.argv\[2\]

location = sys.argv\[3\]

suspect_match = get_hash(suspect) == EXPECTED_SUSPECT

weapon_match = get_hash(weapon) == EXPECTED_WEAPON

location_match = get_hash(location) in EXPECTED_LOCATION_HASHES

if suspect_match and weapon_match and location_match:

print(\"\\n🎉 CONGRATULATIONS DETECTIVE! 🎉\")

print(\"You have correctly identified the killer, the weapon, and the
location!\")

print(f\"It was {suspect} with the {weapon} in the {location}.\")

print(\"The town is safe once again thanks to your command line
skills.\")

sys.exit(0)

else:

print(\"\\nYour accusation is incorrect:\")

print(f\"Suspect: {\'✅ Correct\' if suspect_match else \'❌
Incorrect\'}\")

print(f\"Weapon: {\'✅ Correct\' if weapon_match else \'❌
Incorrect\'}\")

print(f\"Location: {\'✅ Correct\' if location_match else \'❌
Incorrect\'}\")

print(\"\\nKeep investigating!\")

sys.exit(1)

========== ./shops/cafe/objects.txt ==========

Fountain Pen

========== ./shops/bakery/persons.txt ==========

The Artist

========== ./shops/bakery/storage/objects.txt ==========

Letter Opener

========== ./shops/bakery/objects.txt ==========

Heavy Book

Bronze Trophy

========== ./shops/market/aisles/clue.txt ==========

New Clue:

Go back and check the aisles in the shops.

Hint: You\'ll need to go back several directories to reach this
location.

Remember that you can use multiple \'../\' to go up multiple levels:

\- \'cd ..\' goes up one level

\- \'cd ../..\' goes up two levels

\- and so on\...

========== ./shops/market/aisles/objects.txt ==========

Leather Gloves

========== ./shops/market/objects.txt ==========

Garden Shears

========== ./Residential Area/mansion/garden/persons.txt ==========

The Gardener

The Doctor

========== ./Residential Area/mansion/garden/clue.txt ==========

Investigation Update:

Through the window, you can see the lights are on in the library.

Hint: To reach this location, you\'ll need to move back and down to the
next location: \'cd \"../library\"\'

========== ./Residential Area/mansion/library/clue.txt ==========

New Clue:

Go back and check the sandbox in the park.

Hint: You\'ll need to go back several directories to reach this
location.

Remember that you can use multiple \'../\' to go up multiple levels:

\- \'cd ..\' goes up one level

\- \'cd ../..\' goes up two levels

\- and so on\...

========== ./Residential Area/mansion/library/objects.txt ==========

Walking Stick

========== ./Residential Area/mansion/objects.txt ==========

Steel Ruler

========== ./notebook.md ==========

\# Detective\'s Notebook

\## Suspects

\- \[ \] The Gardener

\- \[ \] The Florist

\- \[ \] The Carpenter

\## Weapons

\- \[ \] Leather Gloves

\- \[ \] Walking Stick

\- \[ \] Old Key

\## Notes

\*Use this space to record your findings and deductions\...\*

Location of the crime is still unknown - the room must have been empty
when it happened\...

# Filtrar texto importante

========== ./clue.txt ==========

Detective\'s Initial Report:

The night watchman spoke with The Teacher, who noticed an unfamiliar
figure lurking near the garden.

========== ./school/gymnasium/persons.txt ==========

The Librarian

========== ./school/classrooms/art room/persons.txt ==========

The Tailor

========== ./school/classrooms/science lab/objects.txt ==========

Silver Watch

========== ./town hall/persons.txt ==========

The Shopkeeper

The Clockmaker

========== ./park/gazebo/persons.txt ==========

The Banker

========== ./park/gazebo/objects.txt ==========

Glass Bottle

========== ./park/playground/sandbox/persons.txt ==========

The Florist

The Engineer

========== ./park/playground/sandbox/clue.txt ==========

New Clue:

Go back and check the aisles in the shops.

========== ./shops/cafe/objects.txt ==========

Fountain Pen

========== ./shops/bakery/persons.txt ==========

The Artist

========== ./shops/bakery/storage/objects.txt ==========

Letter Opener

========== ./shops/bakery/objects.txt ==========

Heavy Book

Bronze Trophy

========== ./shops/market/aisles/clue.txt ==========

New Clue:

Go back and check the aisles in the shops.

========== ./shops/market/aisles/objects.txt ==========

Leather Gloves

========== ./shops/market/objects.txt ==========

Garden Shears

========== ./Residential Area/mansion/garden/persons.txt ==========

The Gardener

The Doctor

========== ./Residential Area/mansion/garden/clue.txt ==========

Investigation Update:

Through the window, you can see the lights are on in the library.

========== ./Residential Area/mansion/library/clue.txt ==========

New Clue:

Go back and check the sandbox in the park.

========== ./Residential Area/mansion/library/objects.txt ==========

Walking Stick

========== ./Residential Area/mansion/objects.txt ==========

Steel Ruler

# Etapa de análisis

## Primer razonamiento

La pista inicial nos dice que el maestro vio a alguien en el jardín.

En el jardín:

La investigación se actualiza. Se miran las luces encendidas en la
biblioteca.

Se encuentran el doctor y el jardinero.

En la biblioteca:

Encontramos una pista que dice que busquemos la caja de arena en el
parque.

En la caja de arena se nos indica que revisemos los pasillos de la
tienda.

En los pasillos de la tienda nos redirige hacia los mismos pasillos de
la tienda - \"Go back and check the aisles in the shops.\"-así que la
locación es aisles.

En aísles se encuentran guantes de cuero, así que el objeto es Leather
Gloves. Guantes de ese tipo es más probable que haya usado el jardinero
que el doctor, persona: The Gardener

"

rowl@L4PT0P-R7A:\~/STW/EXE1-CLUE/STW1-command-line-clue/game\$ python3
accuse.py \"The Gardener\" \"Leather Gloves\" \"aisles\"

Your accusation is incorrect:

Suspect: ❌ Incorrect

Weapon: ❌ Incorrect

Location: ✅ Correct

Keep investigating!

"

## Segundo razonamiento

Al ver que sí es la locación pero no el objeto ni la persona, voy a
suponer que lo que he encontrado es lo que tiene coartada; es decir, lo
que no encontré comparado con mi lista de notas es lo que fue.

\## Suspects

\- \[ \] The Gardener

\- \[ \] The Florist

\- \[ \] The Carpenter

\## Weapons

\- \[ \] Leather Gloves

\- \[ \] Walking Stick

\- \[ \] Old Key

Comparando las personas y objetos los que no aparecieron son el
carpintero y la vieja llave. Objeto: Old Key, Killer: The Carpenter.

"

rowl@L4PT0P-R7A:\~/STW/EXE1-CLUE/STW1-command-line-clue/game\$ python3
accuse.py \"The Carpenter\" \"old key\" \"aisles\"

🎉 CONGRATULATIONS DETECTIVE! 🎉

You have correctly identified the killer, the weapon, and the location!

It was The Carpenter with the old key in the aisles.

The town is safe once again thanks to your command line skills.

"
