import random
import time
import os
import math

# ==============================
# 🚀 SPACE MISSION SIMULATOR
# ==============================

SHIP = {
    "fuel": 100,
    "oxygen": 100,
    "hull": 100,
    "credits": 500
}

planets = [
    "Kepler-452b",
    "Mars",
    "Europa",
    "Titan",
    "Proxima-b",
    "TRAPPIST-1e"
]

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def loading(text):
    print(text, end="", flush=True)

    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)

    print()


def status():
    print("\n╔══════════════════════════════╗")
    print("║        🚀 SHIP STATUS        ║")
    print("╠══════════════════════════════╣")
    print(f"║ Fuel     : {SHIP['fuel']:>3}%              ║")
    print(f"║ Oxygen   : {SHIP['oxygen']:>3}%              ║")
    print(f"║ Hull     : {SHIP['hull']:>3}%              ║")
    print(f"║ Credits  : ${SHIP['credits']:<4}            ║")
    print("╚══════════════════════════════╝")


def scan_planet():
    planet = random.choice(planets)

    print(f"\n🔭 Scanning {planet}...")
    time.sleep(1)

    temperature = random.randint(-180, 500)
    gravity = round(random.uniform(0.2, 2.5), 2)
    life = random.choice([
        "No life detected",
        "Microbial life detected",
        "Possible life detected",
        "Unknown biological signal"
    ])

    print("\nPLANET ANALYSIS")
    print("-" * 35)
    print("Planet      :", planet)
    print("Temperature :", temperature, "°C")
    print("Gravity     :", gravity, "G")
    print("Life        :", life)

    input("\nPress ENTER...")


def explore():
    if SHIP["fuel"] < 15:
        print("\n❌ Not enough fuel.")
        input("Press ENTER...")
        return

    if SHIP["oxygen"] < 15:
        print("\n❌ Oxygen level too low.")
        input("Press ENTER...")
        return

    planet = random.choice(planets)

    print(f"\n🚀 Travelling to {planet}...")
    loading("Entering orbit")

    SHIP["fuel"] -= random.randint(10, 20)
    SHIP["oxygen"] -= random.randint(5, 12)

    event = random.randint(1, 5)

    if event == 1:
        print("\n⚠️ ASTEROID FIELD!")
        damage = random.randint(5, 25)
        SHIP["hull"] -= damage
        print(f"Hull damaged by {damage}%.")

    elif event == 2:
        reward = random.randint(100, 400)
        SHIP["credits"] += reward
        print("\n💎 Rare mineral discovered!")
        print(f"Reward: ${reward}")

    elif event == 3:
        print("\n👽 UNKNOWN SIGNAL DETECTED")
        print("Signal source cannot be identified.")

    elif event == 4:
        print("\n🌌 Beautiful cosmic phenomenon detected.")
        print("Mission crew records the event.")

    else:
        print("\n🛰️ Mission successful!")
        reward = random.randint(50, 200)
        SHIP["credits"] += reward
        print(f"Mission reward: ${reward}")

    input("\nPress ENTER...")


def repair():
    cost = 100

    if SHIP["credits"] < cost:
        print("\n❌ Not enough credits.")
    elif SHIP["hull"] >= 100:
        print("\nHull is already at maximum.")
    else:
        SHIP["credits"] -= cost
        SHIP["hull"] = min(100, SHIP["hull"] + 30)

        print("\n🔧 Repair completed.")
        print("Hull +30%")

    input("Press ENTER...")


def refuel():
    cost = 75

    if SHIP["credits"] < cost:
        print("\n❌ Not enough
