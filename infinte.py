import random
import time

player = {
    "hp": 100,
    "gold": 0,
    "level": 1,
    "weapon": 10
}

names = [
    "Shadow Beast",
    "Cyber Wolf",
    "Dark Knight",
    "Ancient Robot",
    "Void Monster"
]

locations = [
    "a forgotten laboratory",
    "an abandoned city",
    "a mysterious forest",
    "an underground bunker",
    "a floating island"
]

loot = [
    "Ancient Coin",
    "Energy Core",
    "Crystal",
    "Golden Chip",
    "Unknown Artifact"
]

def slow(text):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.015)
    print()

def fight():
    enemy = random.choice(names)
    enemy_hp = random.randint(30, 70)

    print("\n⚔️ ENEMY:", enemy)
    print("Enemy HP:", enemy_hp)

    while enemy_hp > 0 and player["hp"] > 0:

        print("\n1. Attack")
        print("2. Run")

        choice = input("> ")

        if choice == "1":

            damage = random.randint(
                player["weapon"],
                player["weapon"] + 15
            )

            enemy_hp -= damage

            print("You dealt", damage, "damage!")

            if enemy_hp <= 0:
                reward = random.randint(10, 50)
                player["gold"] += reward
                player["level"] += 1

                print("\n🔥 ENEMY DEFEATED!")
                print("Gold:", reward)
                print("Level:", player["level"])
                return

            enemy_damage = random.randint(5, 20)
            player["hp"] -= enemy_damage

            print("Enemy attacked!")
            print("You lost", enemy_damage, "HP")

        elif choice == "2":
            print("You escaped!")
            return

    if player["hp"] <= 0:
        print("\n💀 GAME OVER")

def explore():

    location = random.choice(locations)

    slow("\nYou enter " + location + "...")

    event = random.randint(1, 4)

    if event == 1:
        fight()

    elif event == 2:
        gold = random.randint(10, 40)
        player["gold"] += gold

        print("💰 You found", gold, "gold!")

    elif event == 3:
        item = random.choice(loot)

        print("🎁 You discovered:", item)

        player["weapon"] += random.randint(2, 8)

        print("Your weapon became stronger!")

    else:
        damage = random.randint(5, 15)
        player["hp"] -= damage

        print("☠️ A trap activated!")
        print("You lost", damage, "HP")

def game():

    slow("Initializing world...")
    time.sleep(1)

    while player["hp"] > 0:

        print("\n" + "=" * 40)
        print("          INFINITE DUNGEON")
        print("=" * 40)

        print("❤️ HP     :", player["hp"])
        print("⭐ Level  :", player["level"])
        print("💰 Gold   :", player["gold"])
        print("⚔️ Weapon :", player["weapon"])

        print("\n1. Explore")
        print("2. Rest")
        print("3. Quit")

        choice = input("\n> ")

        if choice == "1":
            explore()

        elif choice == "2":
            player["hp"] = min(100, player["hp"] + 20)
            print("\n❤️ You rested and recovered HP.")

        elif choice == "3":
            print("\nGame saved. Goodbye.")
            break

        else:
            print("Invalid choice.")

game()
