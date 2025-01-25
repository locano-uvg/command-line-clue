# Detective's Notebook

iniciar juego

leer archivo clue.txt, found clue

entrar a carpeta houses

leer archivo personas.txt, nothing

leer archivo objetos.txt, hay glass bottle y steel ruler

entrar a carpeta mansions

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

entrar a carpeta garden

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

entrar a carpeta greenhouse

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta garden

regresar a carpeta mansion

entrar a carpeta library

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

entrar a carpeta study

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta houses y entrar a carpeta cottage

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

entrar a carpeta cellar

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta cottage

entrar a carpeta living room

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta game

entrar a carpeta park

leer archivo personas.txt, posible suspects: The Blacksmith

leer archivo objetos.txt, nothing

entrar a carpeta gazebo

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta park

entrar a carpeta playground

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

entrar a carpeta sandbox

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta park

entrar a carpeta pond

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

entrar a carpeta dock

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta game

entrar a carpeta school

leer archivo clue.txt, found clue

leer archivo personas.txt, found doctor, posible suspects

leer archivo objetos.txt, nothing

entrar a carpeta cafeteria

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

entrar a carpeta kitchen

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta school

entrar a carpeta classroom

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

entrar a carpeta art room

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta classroom

entrar a carpeta science lab

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta school

entrar a carpeta gymnasium

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta game

entrar a carpeta shops

leer archivo personas.txt, nothing

leer archivo objetos.txt, encontar Brass Candelstick

leer archivo personas.txt, nothing

leer archivo clue.txt, found clue and location of the crime

entrar a carpeta bakery

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

leer archivo cluee.txt, found clue

antrar a carpeta kitchen

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta bakery

entrar a carpeta storage

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

leer archivo clue.txt, found clue

regresar a carpeta shops

entrar a carpeta cafe

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta shops

entrar a carpeta market

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

entrar a carpeta aisles

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta market

entrar a carpeta stockroom

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta game

entrar a carpeta town hall

leer archivo personas.txt, found the Jocker

leer archivo objetos.txt, nothing

entrar a carpeta office

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

entrar a carpeta records

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

entrar a carpeta archives

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta offices

entrar a carpeta meeting room

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

entrar a carpeta council chamber

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta game

entrar a carpeta shops

entrar a carpeta bakery

entrar a carpeta storage

regresar a carpeta shops

regresar a carpeta game

entrar a carpeta houses

leer archivo cllue.txt, found clue

leer archivo personas.txt, nothing

leer archivo objetos.txt, nothing

regresar a carpeta game

finalizar juego

## Suspects
- [ ] The Baker
- [X] The Doctor
- [ ] The Shopkeeper

## Weapons
- [ ] Garden Shears
- [x] Glass Bottle
- [ ] Walking Stick

## Notes
*Use this space to record your findings and deductions...*

Location of the crime is still unknown - the room must have been empty when it happened...


Git bash commands


paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025 (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025 (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025 (main)
$ git add .

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025 (main)
$ git commit -m "feat: generate initial game folder from clue"
[main 48fc666] feat: generate initial game folder from clue
 1 file changed, 2 insertions(+)

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025 (main)
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 391 bytes | 391.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/cafetowake/command-line-clue.git
   617af2d..48fc666  main -> main

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025 (main)
$ ls
README.md  clue.py*  game/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025 (main)
$ cd game

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ ls
 clue.txt   houses/   notebook.md   park/   school/   shops/  'town hall'/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ cd houses

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ ls
clue.txt  cottage/  mansion/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ cat objects.txt
Glass Bottle
Steel Ruler
paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ git commit "posible weapon found"
error: pathspec 'posible weapon found' did not match any file(s) known to git

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ git commit -m "posible weapon found"
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ git push
Everything up-to-date

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ ls
clue.txt  cottage/  mansion/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ cd mansion

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion (main)
$ ls
garden/  library/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion (main)
$ ls
garden/  library/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion (main)
$ cd garden

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/garden (main)
$ ls
greenhouse/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/garden (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/garden (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/garden (main)
$ cd greenhouse

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/garden/greenhouse (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/garden/greenhouse (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/garden/greenhouse (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/garden/greenhouse (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/garden (main)
$ ls
greenhouse/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/garden (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion (main)
$ ls
garden/  library/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion (main)
$ cd library

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/library (main)
$ ls
objects.txt  persons.txt  study/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/library (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/library (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/library (main)
$ cd study

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/library/study (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/library/study (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/library/study (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/library/study (main)
$ cd..
bash: cd..: command not found

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/library/study (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/library/study (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion/library (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion (main)
$ ls
garden/  library/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/mansion (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ ls
clue.txt  cottage/  mansion/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ ls
clue.txt  cottage/  mansion/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ cd houses

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ cd cottage

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage (main)
$ ls
 cellar/  'living room'/   objects.txt   persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage (main)
$ cd cellar

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage/cellar (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage/cellar (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage/cellar (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage/cellar (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage (main)
$ ls
 cellar/  'living room'/   objects.txt   persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage (main)
$ cd living room
bash: cd: too many arguments

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage (main)
$ cd 'living room'

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage/living room (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage/living room (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage/living room (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage/living room (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses/cottage (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ ls
 clue.txt   houses/   notebook.md   park/   school/   shops/  'town hall'/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ cd park

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ ls
gazebo/  objects.txt  persons.txt  playground/  pond/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ cat persons.txt
The Blacksmith
paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ git commit -m "possible suspect"
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ git push
Everything up-to-date

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ ls
gazebo/  objects.txt  persons.txt  playground/  pond/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ cd gazebo
l
paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/gazebo (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/gazebo (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/gazebo (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/gazebo (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ ls
gazebo/  objects.txt  persons.txt  playground/  pond/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ cd playground

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/playground (main)
$ ls
objects.txt  persons.txt  sandbox/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/playground (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/playground (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/playground (main)
$ ls
objects.txt  persons.txt  sandbox/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/playground (main)
$ cd sandbox

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/playground/sandbox (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/playground/sandbox (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/playground/sandbox (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/playground/sandbox (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/playground/sandbox (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/playground (main)
$ ls
objects.txt  persons.txt  sandbox/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/playground (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ ls
gazebo/  objects.txt  persons.txt  playground/  pond/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ cd pond

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/pond (main)
$ ls
dock/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/pond (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/pond (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/pond (main)
$ cd dock

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/pond/dock (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/pond/dock (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/pond/dock (main)
$ car persons.txt
bash: car: command not found

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/pond/dock (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/pond/dock (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/pond/dock (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/pond (main)
$ ls
dock/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park/pond (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ ls
gazebo/  objects.txt  persons.txt  playground/  pond/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/park (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ ls
 clue.txt   houses/   notebook.md   park/   school/   shops/  'town hall'/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ cd school

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ ls
cafeteria/  classrooms/  clue.txt  gymnasium/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ cat clue.txt
New Clue:

Go back and check the bakery in the shops.

Hint: You'll need to go back several directories to reach this location.
Remember that you can use multiple '../' to go up multiple levels:
- 'cd ..'    goes up one level
- 'cd ../..' goes up two levels
- and so on...


paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ git commit -m "found new clue"
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ git push
Everything up-to-date

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ ls
cafeteria/  classrooms/  clue.txt  gymnasium/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ cat persons.txt
The Doctor
paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ git commit -m "posible suspects"
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ git push
Everything up-to-date

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ ls
cafeteria/  classrooms/  clue.txt  gymnasium/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ cd cafeteria

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/cafeteria (main)
$ ls
kitchen/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/cafeteria (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/cafeteria (main)
$ persons.txt
bash: persons.txt: command not found

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/cafeteria (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/cafeteria (main)
$ cd kitchen

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/cafeteria/kitchen (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/cafeteria/kitchen (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/cafeteria/kitchen (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/cafeteria/kitchen (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/cafeteria/kitchen (main)
$ cd ../..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ ls
cafeteria/  classrooms/  clue.txt  gymnasium/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ cd classrooms

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms (main)
$ ls
'art room'/   objects.txt   persons.txt  'science lab'/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms (main)
$ car objects.txt
bash: car: command not found

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms (main)
$ ls
'art room'/   objects.txt   persons.txt  'science lab'/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms (main)
$ cd 'art room'

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms/art room (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms/art room (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms/art room (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms/art room (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms (main)
$ ls
'art room'/   objects.txt   persons.txt  'science lab'/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms (main)
$ cd 'science lab'

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms/science lab (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms/science lab (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms/science lab (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/classrooms/science lab (main)
$ cd ../..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ ls
cafeteria/  classrooms/  clue.txt  gymnasium/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ cd gymnasium

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/gymnasium (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/gymnasium (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/gymnasium (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school/gymnasium (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ ls
cafeteria/  classrooms/  clue.txt  gymnasium/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ ls
 clue.txt   houses/   notebook.md   park/   school/   shops/  'town hall'/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ cd shops

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ ls
bakery/  cafe/  clue.txt  market/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cat objects.txt
Brass Candlestick
paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ git commit -m "found clue, location of crime"
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../../README.md

no changes added to commit (use "git add" and/or "git commit -a")

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ git commit -a "found clue"
fatal: paths 'found clue ...' with -a does not make sense

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ git commit -m "found clue"
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../../README.md

no changes added to commit (use "git add" and/or "git commit -a")

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ git push
Everything up-to-date

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ ls
bakery/  cafe/  clue.txt  market/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cd bakery

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery (main)
$ ls
clue.txt  kitchen/  objects.txt  persons.txt  storage/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery (main)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery (main)
$ git commit "found clue"
error: pathspec 'found clue' did not match any file(s) known to git

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery (main)
$ git commit -m "found clue"
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../../../README.md

no changes added to commit (use "git add" and/or "git commit -a")

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery (main)
$ git push
Everything up-to-date

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery (main)
$ ls
clue.txt  kitchen/  objects.txt  persons.txt  storage/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery (main)
$ cd kitchen

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery/kitchen (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery/kitchen (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery/kitchen (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery/kitchen (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery (main)
$ ls
clue.txt  kitchen/  objects.txt  persons.txt  storage/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery (main)
$ cd storage

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery/storage (main)
$ ls
clue.txt  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery/storage (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery/storage (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery/storage (main)
$ cd ../..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ ls
bakery/  cafe/  clue.txt  market/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ git commit -m "found clue"
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../../README.md

no changes added to commit (use "git add" and/or "git commit -a")

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ git push
Everything up-to-date

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ ls
bakery/  cafe/  clue.txt  market/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cd cafe

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/cafe (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/cafe (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/cafe (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/cafe (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ ls
bakery/  cafe/  clue.txt  market/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cd market

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market (main)
$ ls
aisles/  objects.txt  persons.txt  stockroom/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market (main)
$

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market (main)
$ cd aisles

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market/aisles (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market/aisles (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market/aisles (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market/aisles (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market (main)
$ ls
aisles/  objects.txt  persons.txt  stockroom/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market (main)
$ stockroom
bash: stockroom: command not found

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market (main)
$ cd stockroom

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market/stockroom (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market/stockroom (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market/stockroom (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market/stockroom (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market (main)
$ ls
aisles/  objects.txt  persons.txt  stockroom/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ ls
bakery/  cafe/  clue.txt  market/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ ls
 clue.txt   houses/   notebook.md   park/   school/   shops/  'town hall'/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ cd town hall
bash: cd: too many arguments

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ cd 'town hall'

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall (main)
$ ls
objects.txt  offices/  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall (main)
$ cat persons.txt
The Jocker
paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall (main)
$ cd offices

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices (main)
$ ls
'meeting rooms'/   objects.txt   persons.txt   records/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices (main)
$ cd records

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/records (main)
$ ls
archives/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/records (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/records (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/records (main)
$ cd archives

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/records/archives (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/records/archives (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/records/archives (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/records/archives (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/records (main)
$ ls
archives/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/records (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices (main)
$ ls
'meeting rooms'/   objects.txt   persons.txt   records/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices (main)
$ cd 'meeting rooms'

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/meeting rooms (main)
$ ls
'council chamber'/   objects.txt   persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/meeting rooms (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/meeting rooms (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/meeting rooms (main)
$ cd 'council chamber'

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/meeting rooms/council chamber (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/meeting rooms/council chamber (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/meeting rooms/council chamber (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices/meeting rooms/council chamber (main)
$ cd ../..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices (main)
$ ls
'meeting rooms'/   objects.txt   persons.txt   records/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall/offices (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall (main)
$ ls
objects.txt  offices/  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/town hall (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ ls
 clue.txt   houses/   notebook.md   park/   school/   shops/  'town hall'/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ cd shops

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ ls
bakery/  cafe/  clue.txt  market/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cd bakery

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery (main)
$ ls
clue.txt  kitchen/  objects.txt  persons.txt  storage/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery (main)
$ cd storage

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery/storage (main)
$ ls
clue.txt  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery/storage (main)
$ cat clue txt
cat: clue: No such file or directory
cat: txt: No such file or directory

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery/storage (main)
$ cat clue.txt
New Clue:

Maybe we should check back in the shops.

Hint: You'll need to go back several directories to reach this location.
Remember that you can use multiple '../' to go up multiple levels:
- 'cd ..'    goes up one level
- 'cd ../..' goes up two levels
- and so on...


paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery/storage (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery/storage (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/bakery/storage (main)
$ cd ../..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ ls
bakery/  cafe/  clue.txt  market/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cd cafe

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/cafe (main)
$ ls
objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/cafe (main)
$ cat objects.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/cafe (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/cafe (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ ls
bakery/  cafe/  clue.txt  market/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cd market

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market (main)
$ ls
aisles/  objects.txt  persons.txt  stockroom/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops/market (main)
$ cd ../../..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025 (main)
$ cd game

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ ls
 clue.txt   houses/   notebook.md   park/   school/   shops/  'town hall'/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ cd houses

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ ls
clue.txt  cottage/  mansion/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ cat clue.txt
Investigation Update:

You hear sound coming from the nearby school.

Hint: To reach this location, you'll need to move back and down to the next location: 'cd "../school"'

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add
g
paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ git commit -m "found clue"
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../../README.md

no changes added to commit (use "git add" and/or "git commit -a")

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ git push
Everything up-to-date

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ cat persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ cat objects.txt
Glass Bottle
Steel Ruler
paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/houses (main)
$ cd ../school

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ ls
cafeteria/  classrooms/  clue.txt  gymnasium/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ cat clue.txt
New Clue:

Go back and check the bakery in the shops.

Hint: You'll need to go back several directories to reach this location.
Remember that you can use multiple '../' to go up multiple levels:
- 'cd ..'    goes up one level
- 'cd ../..' goes up two levels
- and so on...


paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/school (main)
$ cd ../..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025 (main)
$ ls
README.md  clue.py*  game/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025 (main)
$ cd game

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ ls
 clue.txt   houses/   notebook.md   park/   school/   shops/  'town hall'/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game (main)
$ cd shops

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ ls
bakery/  cafe/  clue.txt  market/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cat clue.tx
cat: clue.tx: No such file or directory

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cat clue.txt
Investigation Conclusion:

Your investigation has led you to the truth - this empty room is where it all happened!

Your careful detective work has paid off. The empty state of this room matches
witness accounts - no one was around when the crime occurred. This must be
where the murderer carried out their plan!

Make sure to document this discovery in your notebook.md file along with your
other findings about the weapon and suspect.
paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cd storage
bash: cd: storage: No such file or directory

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ dir
bakery  cafe  clue.txt  market  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ clue.txt
bash: clue.txt: command not found

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cat clue.txt
Investigation Conclusion:

Your investigation has led you to the truth - this empty room is where it all happened!

Your careful detective work has paid off. The empty state of this room matches
witness accounts - no one was around when the crime occurred. This must be
where the murderer carried out their plan!

Make sure to document this discovery in your notebook.md file along with your
other findings about the weapon and suspect.
paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ dir
bakery  cafe  clue.txt  market  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cd..
bash: cd..: command not found

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/GitHub/command-line-clue-2025/game/shops (main)
$ cd

paula@DESKTOP-EMMTMR9 MINGW64 ~ (main)
$ dir
2023
AppData
Application\ Data
BullseyeCoverageError.txt
Colegio\ Alemán\ de\ Guatemala
Contacts
Cookies
Desktop
Documents
Downloads
Favorites
IntelGraphicsProfiles
Links
Local\ Settings
Music
My\ Documents
NTUSER.DAT
NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TM.blf
NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TMContainer00000000000000000001.regtrans-ms
NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TMContainer00000000000000000002.regtrans-ms
NetHood
OneDrive
OneDrive\ -\ Colegio\ Alemán\ de\ Guatemala
PrintHood
Recent
Saved\ Games
Searches
SendTo
Start\ Menu
Sti_Trace.log
Templates
Videos
edb_mtk.exe
edb_npgsql.exe
edb_pem_agent.exe
edb_pem_agent_8.exe
edb_pem_server.exe
edb_pem_server_8.exe
edb_pgagent_pg17.exe
edb_pgbouncer.exe
edb_pgjdbc.exe
edb_psqlodbc.exe
edb_psqlodbc.exe-20250113210614
edb_sqlprofiler_pg17.exe
edb_xdb_7.exe
get-pip.py
ibisPaint
ntuser.dat.LOG1
ntuser.dat.LOG2
ntuser.ini
pemhttpd.exe
postgis_3_5_pg17.exe
postgresql_17.exe
tracker.prefs
universidad

paula@DESKTOP-EMMTMR9 MINGW64 ~ (main)
$ dir
2023
AppData
Application\ Data
BullseyeCoverageError.txt
Colegio\ Alemán\ de\ Guatemala
Contacts
Cookies
Desktop
Documents
Downloads
Favorites
IntelGraphicsProfiles
Links
Local\ Settings
Music
My\ Documents
NTUSER.DAT
NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TM.blf
NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TMContainer00000000000000000001.regtrans-ms
NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TMContainer00000000000000000002.regtrans-ms
NetHood
OneDrive
OneDrive\ -\ Colegio\ Alemán\ de\ Guatemala
PrintHood
Recent
Saved\ Games
Searches
SendTo
Start\ Menu
Sti_Trace.log
Templates
Videos
edb_mtk.exe
edb_npgsql.exe
edb_pem_agent.exe
edb_pem_agent_8.exe
edb_pem_server.exe
edb_pem_server_8.exe
edb_pgagent_pg17.exe
edb_pgbouncer.exe
edb_pgjdbc.exe
edb_psqlodbc.exe
edb_psqlodbc.exe-20250113210614
edb_sqlprofiler_pg17.exe
edb_xdb_7.exe
get-pip.py
ibisPaint
ntuser.dat.LOG1
ntuser.dat.LOG2
ntuser.ini
pemhttpd.exe
postgis_3_5_pg17.exe
postgresql_17.exe
tracker.prefs
universidad

paula@DESKTOP-EMMTMR9 MINGW64 ~ (main)
$ dir /w
dir: cannot access '/w': No such file or directory

paula@DESKTOP-EMMTMR9 MINGW64 ~ (main)
$ dir w
dir: cannot access 'w': No such file or directory

paula@DESKTOP-EMMTMR9 MINGW64 ~ (main)
$ dir
2023
AppData
Application\ Data
BullseyeCoverageError.txt
Colegio\ Alemán\ de\ Guatemala
Contacts
Cookies
Desktop
Documents
Downloads
Favorites
IntelGraphicsProfiles
Links
Local\ Settings
Music
My\ Documents
NTUSER.DAT
NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TM.blf
NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TMContainer00000000000000000001.regtrans-ms
NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TMContainer00000000000000000002.regtrans-ms
NetHood
OneDrive
OneDrive\ -\ Colegio\ Alemán\ de\ Guatemala
PrintHood
Recent
Saved\ Games
Searches
SendTo
Start\ Menu
Sti_Trace.log
Templates
Videos
edb_mtk.exe
edb_npgsql.exe
edb_pem_agent.exe
edb_pem_agent_8.exe
edb_pem_server.exe
edb_pem_server_8.exe
edb_pgagent_pg17.exe
edb_pgbouncer.exe
edb_pgjdbc.exe
edb_psqlodbc.exe
edb_psqlodbc.exe-20250113210614
edb_sqlprofiler_pg17.exe
edb_xdb_7.exe
get-pip.py
ibisPaint
ntuser.dat.LOG1
ntuser.dat.LOG2
ntuser.ini
pemhttpd.exe
postgis_3_5_pg17.exe
postgresql_17.exe
tracker.prefs
universidad

paula@DESKTOP-EMMTMR9 MINGW64 ~ (main)
$ dir
2023
AppData
Application\ Data
BullseyeCoverageError.txt
Colegio\ Alemán\ de\ Guatemala
Contacts
Cookies
Desktop
Documents
Downloads
Favorites
IntelGraphicsProfiles
Links
Local\ Settings
Music
My\ Documents
NTUSER.DAT
NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TM.blf
NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TMContainer00000000000000000001.regtrans-ms
NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TMContainer00000000000000000002.regtrans-ms
NetHood
OneDrive
OneDrive\ -\ Colegio\ Alemán\ de\ Guatemala
PrintHood
Recent
Saved\ Games
Searches
SendTo
Start\ Menu
Sti_Trace.log
Templates
Videos
edb_mtk.exe
edb_npgsql.exe
edb_pem_agent.exe
edb_pem_agent_8.exe
edb_pem_server.exe
edb_pem_server_8.exe
edb_pgagent_pg17.exe
edb_pgbouncer.exe
edb_pgjdbc.exe
edb_psqlodbc.exe
edb_psqlodbc.exe-20250113210614
edb_sqlprofiler_pg17.exe
edb_xdb_7.exe
get-pip.py
ibisPaint
ntuser.dat.LOG1
ntuser.dat.LOG2
ntuser.ini
pemhttpd.exe
postgis_3_5_pg17.exe
postgresql_17.exe
tracker.prefs
universidad

paula@DESKTOP-EMMTMR9 MINGW64 ~ (main)
$ cd /documents
bash: cd: /documents: No such file or directory

paula@DESKTOP-EMMTMR9 MINGW64 ~ (main)
$ cd /Documents
bash: cd: /Documents: No such file or directory

paula@DESKTOP-EMMTMR9 MINGW64 ~ (main)
$ ls
 2023/
 AppData/
'Application Data'@
 BullseyeCoverageError.txt
'Colegio Alemán de Guatemala'/
 Contacts/
 Cookies@
 Desktop/
 Documents/
 Downloads/
 Favorites/
 IntelGraphicsProfiles/
 Links/
'Local Settings'@
 Music/
'My Documents'@
 NTUSER.DAT
 NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TM.blf
 NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TMContainer00000000000000000001.regtrans-ms
 NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TMContainer00000000000000000002.regtrans-ms
 NetHood@
 OneDrive/
'OneDrive - Colegio Alemán de Guatemala'/
 PrintHood@
 Recent@
'Saved Games'/
 Searches/
 SendTo@
'Start Menu'@
 Sti_Trace.log
 Templates@
 Videos/
 edb_mtk.exe*
 edb_npgsql.exe*
 edb_pem_agent.exe*
 edb_pem_agent_8.exe*
 edb_pem_server.exe*
 edb_pem_server_8.exe*
 edb_pgagent_pg17.exe*
 edb_pgbouncer.exe*
 edb_pgjdbc.exe*
 edb_psqlodbc.exe*
 edb_psqlodbc.exe-20250113210614*
 edb_sqlprofiler_pg17.exe*
 edb_xdb_7.exe*
 get-pip.py*
 ibisPaint/
 ntuser.dat.LOG1
 ntuser.dat.LOG2
 ntuser.ini
 pemhttpd.exe*
 postgis_3_5_pg17.exe*
 postgresql_17.exe*
 tracker.prefs
 universidad/

paula@DESKTOP-EMMTMR9 MINGW64 ~ (main)
$ cd OneDrive

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive (main)
$ ls
 1/                                 UVG/
 2/                                 appsheet/
 Applications/                     'brif 1[832].docx'
 Apps/                             'cinta negra mothefucker.odt'
'DSG onedrive'/                     colegio/
 Desktop/                          'como matar pajaritos  no corregido.docx'
 Document.docx                     'como matar pajaritos .docx'
 Documents/                         cuba.odt
'Ejercicio 2 - Paula De Leon.odt'  'dell latitude 3450'/
 Imágenes/                          desktop.ini
'Meine Erfahrung in Florenz.pptx'   links/
 OneDrive                          'resultados del simulador.xlsx'
'Personal Vault.lnk'*               tablas.html
 Pictures/                         'todo de mi google drive personal'/
'Sprach Paula 2019.docx'            videos/
'Sprach Paula 2019[511].docx'

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive (main)
$ cd Documents

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents (main)
$ ls
 2021.url                             "Paula Daniela's Notebook.url"
 2022.url                              PowerToys/
 Arduino/                              Python/
 Audacity/                            'Python Scripts'/
'Bloc de notas de Paula Daniela.url'  'Sound Recordings'/
 Concepts/                             Tracker/
'Custom Office Templates'/            'UVG 1 semestre.url'
 DSG.url                              'UVG semestre 2.url'
 Dell/                                'UVG semestre 3.url'
 Document.docx                         WindowsPowerShell/
 GitHub/                               Zoom/
 Journals/                             cole.url
'My Data Sources'/                     desktop.ini
'Office Lens'/                        'documentos legales (no mios).docx'
'OneNote Notebooks'/                   try.url
'Outlook Files'/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents (main)
$ cd Github

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github (main)
$ ls
Fase-3/              Proyecto-Grupal-POO/  command-line-clue-2025/
PlataformasUvg2024/  command-line-clue/    uvg-rickmorty/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github (main)
$ cd commond-line-clue-2025
bash: cd: commond-line-clue-2025: No such file or directory

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github (main)
$ cd command-line-clue-2025

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025 (main)
$ ls
README.md  clue.py*  game/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025 (main)
$ cd game

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game (main)
$ ls
 clue.txt   houses/   notebook.md   park/   school/   shops/  'town hall'/

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game (main)
$ cat clue.txt
Detective's Initial Report:

During the morning roll call, The Doctor reported odd footprints leading to the houses.

This seems like a good place to start our investigation. Remember to:
- Use 'cd' to move between locations
- Use 'ls' to list the contents of each location
- Use 'cat' to read any text files you find

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game (main)
$ cd houses

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game/houses (main)
$ ls
clue.txt  cottage/  mansion/  objects.txt  persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game/houses (main)
$ cat clue.txt
Investigation Update:

You hear sound coming from the nearby school.

Hint: To reach this location, you'll need to move back and down to the next location: 'cd "../school"'

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game/houses (main)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add
g
paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game/houses (main)
$ git add
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?
hint: Disable this message with "git config advice.addEmptyPathspec false"

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game/houses (main)
$ git add .
The following paths are ignored by one of your .gitignore files:
game
hint: Use -f if you really want to add them.
hint: Disable this message with "git config advice.addIgnoredFile false"

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game/houses (main)
$ git --help
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--no-lazy-fetch]
           [--no-optional-locks] [--no-advice] [--bare] [--git-dir=<path>]
           [--work-tree=<path>] [--namespace=<name>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game/houses (main)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game/houses (main)
$ git add .
The following paths are ignored by one of your .gitignore files:
game
hint: Use -f if you really want to add them.
hint: Disable this message with "git config advice.addIgnoredFile false"

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game/houses (main)
$ cd ..

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game (main)
$ git add -f
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?
hint: Disable this message with "git config advice.addEmptyPathspec false"

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game (main)
$ git add .
The following paths are ignored by one of your .gitignore files:
game
hint: Use -f if you really want to add them.
hint: Disable this message with "git config advice.addIgnoredFile false"

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game (main)
$ git add
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?
hint: Disable this message with "git config advice.addEmptyPathspec false"

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game (main)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game (main)
$ git add
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?
hint: Disable this message with "git config advice.addEmptyPathspec false"

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game (main)
$ git add .
The following paths are ignored by one of your .gitignore files:
game
hint: Use -f if you really want to add them.
hint: Disable this message with "git config advice.addIgnoredFile false"

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game (main)
$ git add . -f

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game (main)
$ git commit -a -m "finish game"
[main 7a92e3d] finish game
 80 files changed, 364 insertions(+), 7 deletions(-)
 create mode 100644 game/clue.txt
 create mode 100644 game/houses/clue.txt
 create mode 100644 game/houses/cottage/cellar/objects.txt
 create mode 100644 game/houses/cottage/cellar/persons.txt
 create mode 100644 game/houses/cottage/living room/objects.txt
 create mode 100644 game/houses/cottage/living room/persons.txt
 create mode 100644 game/houses/cottage/objects.txt
 create mode 100644 game/houses/cottage/persons.txt
 create mode 100644 game/houses/mansion/garden/greenhouse/objects.txt
 create mode 100644 game/houses/mansion/garden/greenhouse/persons.txt
 create mode 100644 game/houses/mansion/garden/objects.txt
 create mode 100644 game/houses/mansion/garden/persons.txt
 create mode 100644 game/houses/mansion/library/objects.txt
 create mode 100644 game/houses/mansion/library/persons.txt
 create mode 100644 game/houses/mansion/library/study/objects.txt
 create mode 100644 game/houses/mansion/library/study/persons.txt
 create mode 100644 game/houses/mansion/objects.txt
 create mode 100644 game/houses/mansion/persons.txt
 create mode 100644 game/houses/objects.txt
 create mode 100644 game/houses/persons.txt
 create mode 100644 game/notebook.md
 create mode 100644 game/park/gazebo/objects.txt
 create mode 100644 game/park/gazebo/persons.txt
 create mode 100644 game/park/objects.txt
 create mode 100644 game/park/persons.txt
 create mode 100644 game/park/playground/objects.txt
 create mode 100644 game/park/playground/persons.txt
 create mode 100644 game/park/playground/sandbox/objects.txt
 create mode 100644 game/park/playground/sandbox/persons.txt
 create mode 100644 game/park/pond/dock/objects.txt
 create mode 100644 game/park/pond/dock/persons.txt
 create mode 100644 game/park/pond/objects.txt
 create mode 100644 game/park/pond/persons.txt
 create mode 100644 game/school/cafeteria/kitchen/objects.txt
 create mode 100644 game/school/cafeteria/kitchen/persons.txt
 create mode 100644 game/school/cafeteria/objects.txt
 create mode 100644 game/school/cafeteria/persons.txt
 create mode 100644 game/school/classrooms/art room/objects.txt
 create mode 100644 game/school/classrooms/art room/persons.txt
 create mode 100644 game/school/classrooms/objects.txt
 create mode 100644 game/school/classrooms/persons.txt
 create mode 100644 game/school/classrooms/science lab/objects.txt
 create mode 100644 game/school/classrooms/science lab/persons.txt
 create mode 100644 game/school/clue.txt
 create mode 100644 game/school/gymnasium/objects.txt
 create mode 100644 game/school/gymnasium/persons.txt
 create mode 100644 game/school/objects.txt
 create mode 100644 game/school/persons.txt
 create mode 100644 game/shops/bakery/clue.txt
 create mode 100644 game/shops/bakery/kitchen/objects.txt
 create mode 100644 game/shops/bakery/kitchen/persons.txt
 create mode 100644 game/shops/bakery/objects.txt
 create mode 100644 game/shops/bakery/persons.txt
 create mode 100644 game/shops/bakery/storage/clue.txt
 create mode 100644 game/shops/bakery/storage/objects.txt
 create mode 100644 game/shops/bakery/storage/persons.txt
 create mode 100644 game/shops/cafe/objects.txt
 create mode 100644 game/shops/cafe/persons.txt
 create mode 100644 game/shops/clue.txt
 create mode 100644 game/shops/market/aisles/objects.txt
 create mode 100644 game/shops/market/aisles/persons.txt
 create mode 100644 game/shops/market/objects.txt
 create mode 100644 game/shops/market/persons.txt
 create mode 100644 game/shops/market/stockroom/objects.txt
 create mode 100644 game/shops/market/stockroom/persons.txt
 create mode 100644 game/shops/objects.txt
 create mode 100644 game/shops/persons.txt
 create mode 100644 game/town hall/objects.txt
 create mode 100644 game/town hall/offices/meeting rooms/council chamber/objects.txt
 create mode 100644 game/town hall/offices/meeting rooms/council chamber/persons.txt
 create mode 100644 game/town hall/offices/meeting rooms/objects.txt
 create mode 100644 game/town hall/offices/meeting rooms/persons.txt
 create mode 100644 game/town hall/offices/objects.txt
 create mode 100644 game/town hall/offices/persons.txt
 create mode 100644 game/town hall/offices/records/archives/objects.txt
 create mode 100644 game/town hall/offices/records/archives/persons.txt
 create mode 100644 game/town hall/offices/records/objects.txt
 create mode 100644 game/town hall/offices/records/persons.txt
 create mode 100644 game/town hall/persons.txt

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game (main)
$ git push
Enumerating objects: 39, done.
Counting objects: 100% (39/39), done.
Delta compression using up to 8 threads
Compressing objects: 100% (31/31), done.
Writing objects: 100% (37/37), 4.18 KiB | 856.00 KiB/s, done.
Total 37 (delta 13), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (13/13), done.
To https://github.com/cafetowake/command-line-clue.git
   48fc666..7a92e3d  main -> main

paula@DESKTOP-EMMTMR9 MINGW64 ~/OneDrive/Documents/Github/command-line-clue-2025/game (main)
$
