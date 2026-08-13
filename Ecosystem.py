import random
import time
import os

WIDTH = 50
HEIGHT = 15

animals = []
plants = []

# -----------------------------
# CREATE WORLD
# -----------------------------

for _ in range(8):
    animals.append({
        "x": random.randrange(WIDTH),
        "y": random.randrange(HEIGHT),
        "energy": random.randint(5, 10)
    })

for _ in range(30):
    plants.append({
        "x": random.randrange(WIDTH),
        "y": random.randrange(HEIGHT)
    })


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def draw_world():
    world = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # Plants
    for plant in plants:
        x = plant["x"]
        y = plant["y"]
        world[y][x] = "🌱"

    # Animals
    for animal in animals:
        x = animal["x"]
        y = animal["y"]
        world[y][x] = "🐾"

    print("+" + "-" * WIDTH + "+")

    for row in world:
        print("|" + "".join(row) + "|")

    print("+" + "-" * WIDTH + "+")


def move_animals():

    for animal in animals:

        direction = random.choice([
            "up",
            "down",
            "left",
            "right",
            "stay"
        ])

        if direction == "up":
            animal["y"] -= 1

        elif direction == "down":
            animal["y"] += 1

        elif direction == "left":
            animal["x"] -= 1

        elif direction == "right":
            animal["x"] += 1

        animal["x"] = max(0, min(WIDTH - 1, animal["x"]))
        animal["y"] = max(0, min(HEIGHT - 1, animal["y"]))

        animal["energy"] -= 1


def eat_plants():

    eaten = []

    for animal in animals:

        for plant in plants:

            if (
                animal["x"] == plant["x"]
                and animal["y"] == plant["y"]
                and plant not in eaten
            ):

                animal["energy"] += 5
                eaten.append(plant)

                break

    for plant in eaten:
        plants.remove(plant)


def reproduce():

    new_animals = []

    for animal in animals:

        if animal["energy"] >= 12:

            if random.random() < 0.25:

                baby = {
                    "x": animal["x"],
                    "y": animal["y"],
                    "energy": 6
                }

                new_animals.append(baby)
                animal["energy"] -= 5

    animals.extend(new_animals)


def remove_dead():

    global animals

    animals = [
        animal for animal in animals
        if animal["energy"] > 0
    ]


def grow_plants():

    for _ in range(random.randint(1, 5)):

        if len(plants) < 80:

            plants.append({
                "x": random.randrange(WIDTH),
                "y": random.randrange(HEIGHT)
            })


# -----------------------------
# START SIMULATION
# -----------------------------

generation = 0

print("VIRTUAL ECOSYSTEM")
print("Press CTRL+C to stop.")

time.sleep(2)

try:

    while True:

        generation += 1

        move_animals()
        eat_plants()
        reproduce()
        remove_dead()
        grow_plants()

        clear()

        print("╔══════════════════════════════════════════════════╗")
        print("║              🌍 VIRTUAL ECOSYSTEM               ║")
        print("╚══════════════════════════════════════════════════╝")

        print(f"\nGeneration : {generation}")
        print(f"Animals    : {len(animals)}")
        print(f"Plants     : {len(plants)}")

        draw_world()

        if len(animals) == 0:
            print("\n☠️ All animals have died.")
            print("The ecosystem collapsed.")
            break

        if len(animals) > 100:
            print("\n⚠️ Population explosion!")

        time.sleep(0.4)

except KeyboardInterrupt:

    clear()

    print("""
╔══════════════════════════════════════╗
║       SIMULATION STOPPED             ║
╚══════════════════════════════════════╝
""")

    print("Final generation:", generation)
    print("Animals:", len(animals))
    print("Plants:", len(plants))
