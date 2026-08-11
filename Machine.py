import random
import time

places = [
    "an abandoned space station",
    "a city floating above the clouds",
    "a library with infinite floors",
    "a silent planet",
    "a train traveling through the ocean",
    "a futuristic underground city"
]

objects = [
    "a glowing blue door",
    "an ancient robot",
    "a mysterious black box",
    "a floating clock",
    "a glass cube",
    "a strange golden key"
]

events = [
    "the sky suddenly turned purple",
    "gravity disappeared",
    "every clock stopped at the same time",
    "the walls began moving",
    "the stars started falling",
    "everything became completely silent"
]

characters = [
    "a stranger wearing a silver mask",
    "a robot with human eyes",
    "an astronaut who knew your name",
    "a shadow that could speak",
    "a child carrying a glowing map"
]

endings = [
    "You opened your eyes.",
    "The world suddenly restarted.",
    "You discovered that you were still dreaming.",
    "The mysterious object disappeared.",
    "A voice whispered: 'Wake up.'"
]


def loading():
    print("\nGenerating dream", end="")

    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")

    print("\n")


def generate_dream(name):
    random.seed()

    place = random.choice(places)
    obj = random.choice(objects)
    event = random.choice(events)
    character = random.choice(characters)
    ending = random.choice(endings)

    print("=" * 60)
    print("                 DREAM MACHINE")
    print("=" * 60)

    print(f"\nDreamer: {name}")

    loading()

    print(f"You wake up in {place}.")

    time.sleep(1)

    print(f"\nIn front of you, there is {obj}.")

    time.sleep(1)

    print(f"\nSuddenly, {event}.")

    time.sleep(1)

    print(f"\nThen you see {character}.")

    time.sleep(1)

    print("\nThe stranger looks at you and says:")
    print('"You were never supposed to find this place."')

    time.sleep(1)

    print(f"\nYou follow them toward the object...")

    time.sleep(1)

    print(f"\n{ending}")

    print("\n" + "=" * 60)
    print("              DREAM COMPLETE")
    print("=" * 60)


name = input("Enter your name: ")

generate_dream(name)
