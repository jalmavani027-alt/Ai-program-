import random
import time
import os
from datetime import datetime

# ==============================
# 🕵️ DIGITAL DETECTIVE
# ==============================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def loading(text):
    print(text, end="", flush=True)

    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)

    print()


suspects = [
    "Alex",
    "Riya",
    "Daniel",
    "Maya"
]

locations = [
    "Computer Lab",
    "Library",
    "Workshop",
    "Server Room"
]

objects = [
    "USB Drive",
    "Laptop",
    "Access Card",
    "Security Key"
]

culprit = random.choice(suspects)
location = random.choice(locations)
object_used = random.choice(objects)

# Generate clues
clues = [
    f"The {object_used} was found near the {location}.",
    f"Security cameras detected movement near the {location}.",
    f"Only one suspect had access to the {object_used}.",
    "The incident happened between 10:00 PM and 11:00 PM."
]

random.shuffle(clues)


def intro():
    clear()

    print("""
╔══════════════════════════════════════╗
║                                      ║
║          🕵️ DIGITAL DETECTIVE        ║
║                                      ║
║        CLASSIFIED CASE #2049         ║
║                                      ║
╚══════════════════════════════════════╝
""")

    loading("Opening classified case")
    loading("Decrypting evidence")
    loading("Loading suspect database")

    time.sleep(1)


def show_suspects():
    print("\n👤 SUSPECT DATABASE")
    print("-" * 35)

    for i, suspect in enumerate(suspects, 1):
        print(f"{i}. {suspect}")


def investigate():
    clear()

    print("🔎 INVESTIGATION DATABASE")
    print("=" * 40)

    print("\nAvailable evidence:\n")

    for i, clue in enumerate(clues, 1):
        print(f"[{i}] {clue}")

    print("\n[5] Examine crime scene")
    print("[6] Check system time")
    print("[7] Return")

    choice = input("\nINVESTIGATE > ")

    if choice in ["1", "2", "3", "4"]:
        print("\nEvidence discovered:")
        print(clues[int(choice) - 1])
        input("\nPress ENTER...")

    elif choice == "5":
        print("\n📍 Crime Scene")
        print(f"Location: {location}")
        print(f"Important object: {object_used}")

        input("\nPress ENTER...")

    elif choice == "6":
        print("\nSystem timestamp:")
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        input("\nPress ENTER...")


def accuse():
    clear()

    print("⚠️ FINAL ACCUSATION")
    print("=" * 40)

    show_suspects()

    try:
        choice = int(input("\nWho is the culprit? "))

        if choice < 1 or choice > len(suspects):
            print("\nInvalid suspect.")
            input("Press ENTER...")
            return

        selected = suspects[choice - 1]

        print("\nProcessing accusation...")
        loading("Cross-checking evidence")
        loading("Comparing fingerprints")
        loading("Analyzing access records")

        if selected == culprit:

            clear()

            print("""
╔══════════════════════════════════════╗
║                                      ║
║       ✅ CASE SOLVED                 ║
║                                      ║
╚══════════════════════════════════════╝
""")

            print(f"🎯 Culprit: {culprit}")
            print(f"📍 Location: {location}")
            print(f"🔑 Evidence: {object_used}")

            print("\nAll evidence matches.")

        else:

            clear()

            print("""
╔══════════════════════════════════════╗
║                                      ║
║       ❌ WRONG ACCUSATION            ║
║                                      ║
╚══════════════════════════════════════╝
""")

            print("The real culprit was:", culprit)

        input("\nPress ENTER...")


def game():

    intro()

    while True:

        clear()

        print("""
╔══════════════════════════════════════╗
║          🕵️ DETECTIVE HQ             ║
╠══════════════════════════════════════╣
║                                      ║
║  1. 👤 View Suspects                 ║
║  
