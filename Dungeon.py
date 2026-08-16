import random
import os
import time

WIDTH = 11
HEIGHT = 11

player = [1, 1]
exit_pos = [9, 9]

gold = 0
health = 100
has_key = False

rooms = set()

# -----------------------------
# SCREEN
# -----------------------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")


# -----------------------------
# GENERATE DUNGEON
# -----------------------------

def generate_dungeon():
    global rooms

    rooms = {(1, 1), (9, 9)}

    # Randomly create walkable areas
    for _ in range(65):
        x = random.randint(1, WIDTH - 2)
        y = random.randint(1, HEIGHT - 2)

        rooms.add((x, y))

        # Sometimes connect nearby cells
        if random.random() < 0.5:
            rooms.add((x + 1, y))

        if random.random() < 0.5:
            rooms.add((x, y + 1))


# -----------------------------
# OBJECTS
# -----------------------------

treasures = set()
monsters = set()
key = None


def generate_objects():

    global key

    available = list(
        rooms
        - {
            (1, 1),
            (9, 9)
        }
    )

    random.shuffle(available)

    treasures.update(available[:5])

    monsters.update(available[5:10])

    key = available[10]


# -----------------------------
# DRAW MAP
# -----------------------------

def draw():

    print("╔" + "══" * WIDTH + "╗")

    for y in range(HEIGHT):

        line = "║"

        for x in range(WIDTH):

            pos = (x, y)

            if pos == tuple(player):
                symbol = "🧙"

            elif pos == tuple(exit_pos):
                symbol = "🚪"

            elif pos not in rooms:
                symbol = "██"

            elif pos in monsters:
                symbol = "👾"

            elif pos in treasures:
                symbol = "💰"

            elif pos == key:
                symbol = "🔑"

            else:
                symbol = "  "

            line += symbol

        line += "║"

        print(line)

    print("╚" + "══" * WIDTH + "╝")


# -----------------------------
# MOVE
# -----------------------------

def move(dx, dy):

    global gold
    global health
    global has_key
    global key

    new_x = player[0] + dx
    new_y = player[1] + dy

    new_pos = (new_x, new_y)

    if new_pos not in rooms:
        print("\n🧱 You hit a wall.")
        time.sleep(0.5)
        return

    player[0] = new_x
    player[1] = new_y

    # Treasure
    if new_pos in treasures:

        reward = random.randint(20, 100)

        gold += reward
        treasures.remove(new_pos)

        print(f"\n💰 You found {reward} gold!")

        time.sleep(0.7)

    # Key
    if key == new_pos:

        has_key = True
        key = None

        print("\n🔑 You found the dungeon key!")

        time.sleep(0.7)

    # Monster
    if new_pos in monsters:

        monsters.remove(new_pos)

        damage = random.randint(10, 35)

        health -= damage

        print(f"\n👾 MONSTER ATTACK!")
        print(f"You lost {damage} HP.")

        time.sleep(0.8)


# -----------------------------
# GAME
# -----------------------------

def game():

    global gold
    global health

    generate_dungeon()
    generate_objects()

    while True:

        clear()

        print("""
╔══════════════════════════════════════╗
║          🏰 PROCEDURAL DUNGEON       ║
╚══════════════════════════════════════╝
""")

        print(f"❤️ Health : {health}")
        print(f"💰 Gold   : {gold}")
        print(f"🔑 Key    : {'YES' if has_key else 'NO'}")

        print()

        draw()

        print("""
W = Up
S = Down
A = Left
D = Right
Q = Quit
""")

        command = input("MOVE > ").lower()

        if command == "w":
            move(0, -1)

        elif command == "s":
            move(0, 1)

        elif command == "a":
            move(-1, 0)

        elif command == "d":
            move(1, 0)

        elif command == "q":
            break

        else:
            continue

        # Death
        if health <= 0:

            clear()

            print("""
╔══════════════════════════════════════╗
║                                      ║
║          💀 YOU DIED                 ║
║                                      ║
╚══════════════════════════════════════╝
""")

            print("Gold collected:", gold)

            break

        # Exit
        if player == exit_pos:

            if has_key:

                clear()

                print("""
╔══════════════════════════════════════╗
║                                      ║
║       🏆 DUNGEON ESCAPED!            ║
║                                      ║
╚══════════════════════════════════════╝
""")

                print("💰 Gold collected:", gold)
                print("❤️ Health remaining:", health)

                break

            else:

                print("\n🚪 The exit is locked!")
                print("Find the 🔑 key.")

                time.sleep(1)


# -----------------------------
# START
# -----------------------------

clear()

print("""
╔══════════════════════════════════════╗
║                                      ║
║       🏰 PROCEDURAL DUNGEON         ║
║                                      ║
║      Every game is different.        ║
║                                      ║
╚══════════════════════════════════════╝
""")

time.sleep(1)

game()
