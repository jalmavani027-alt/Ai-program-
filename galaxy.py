import random
import time
import math
import os

STAR_TYPES = [
    "Red Dwarf", "Yellow Star", "Blue Giant",
    "White Dwarf", "Neutron Star"
]

PLANETS = [
    "Rocky", "Ocean", "Desert",
    "Ice", "Gas Giant", "Volcanic", "Forest"
]

EVENTS = [
    "☄️ Meteor Shower",
    "🌌 Wormhole Opened",
    "💥 Supernova Explosion",
    "🛸 Alien Signal Detected",
    "🛰 Ancient Satellite Found",
    "⚫ Black Hole Appeared"
]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def loading():
    print("Generating Universe", end="")
    for _ in range(8):
        print(".", end="", flush=True)
        time.sleep(0.25)
    print("\n")


def generate_star():
    return random.choice(STAR_TYPES)


def generate_planet():
    return random.choice(PLANETS)


def planet_size():
    return round(random.uniform(0.3, 15.0), 2)


def distance():
    return round(random.uniform(0.1, 40), 2)


def life_chance():
    return random.randint(0, 100)


def gravity(size):
    return round(math.sqrt(size) * random.uniform(0.8, 1.4), 2)


def main():

    clear()
    loading()

    galaxy_name = "GX-" + str(random.randint(1000, 9999))
    sectors = random.randint(3, 7)

    print("=" * 60)
    print("           PROCEDURAL GALAXY GENERATOR")
    print("=" * 60)
    print(f"Galaxy Name : {galaxy_name}")
    print(f"Sectors     : {sectors}")
    print()

    total_planets = 0

    for sector in range(1, sectors + 1):

        stars = random.randint(2, 5)

        print(f"========== Sector {sector} ==========")

        for star in range(1, stars + 1):

            star_type = generate_star()

            print(f"\n⭐ Star {star} : {star_type}")

            planets = random.randint(1, 6)

            for p in range(1, planets + 1):

                ptype = generate_planet()
                size = planet_size()
                dist = distance()
                grav = gravity(size)
                life = life_chance()

                print(
                    f"   Planet {p}: {ptype:10} | "
                    f"Size:{size:5} Earth | "
                    f"Gravity:{grav:4}g | "
                    f"Orbit:{dist:5} AU",
                    end=""
                )

                if life > 96:
                    print("  🌎 Intelligent Civilization")
                elif life > 88:
                    print("  🌱 Primitive Life")
                else:
                    print()

                total_planets += 1

        if random.randint(1, 4) == 1:
            print("\nSPECIAL EVENT:", random.choice(EVENTS))

        print()

    print("=" * 60)
    print("UNIVERSE SUMMARY")
    print("=" * 60)
    print("Galaxy :", galaxy_name)
    print("Planets:", total_planets)

    rarity = random.randint(1, 500)

    if rarity == 1:
        print("\n✨ LEGENDARY DISCOVERY!")
        print("You discovered a Dyson Sphere around a forgotten star.")
    elif rarity < 10:
        print("\n👽 Alien empire controls this galaxy.")
    else:
        print("\nEverything appears normal... for now.")

    print("=" * 60)


if __name__ == "__main__":
    main()
