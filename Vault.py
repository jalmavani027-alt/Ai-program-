import json
import os
import random
import time
from datetime import datetime


FILE = "memory_vault.json"


# ==============================
# MEMORY VAULT
# ==============================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def load_memories():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_memories(memories):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(memories, f, indent=4)


def add_memory(memories):
    clear()

    print("""
╔══════════════════════════════════════╗
║           CREATE MEMORY              ║
╚══════════════════════════════════════╝
""")

    title = input("Memory title: ")
    category = input("Category: ")

    print("\nWrite your memory:")
    text = input("> ")

    memory = {
        "id": len(memories) + 1,
        "title": title,
        "category": category,
        "text": text,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M")
    }

    memories.append(memory)
    save_memories(memories)

    print("\n✓ Memory stored successfully.")
    time.sleep(1)


def view_memories(memories):
    clear()

    print("""
╔══════════════════════════════════════╗
║            MEMORY VAULT              ║
╚══════════════════════════════════════╝
""")

    if not memories:
        print("Vault is empty.")
        input("\nPress ENTER...")
        return

    for memory in memories:
        print(f"""
[{memory['id']}] {memory['title']}
Category : {memory['category']}
Date     : {memory['date']}

{memory['text']}
----------------------------------------
""")

    input("Press ENTER...")


def search_memory(memories):
    clear()

    print("""
╔══════════════════════════════════════╗
║           SEARCH MEMORY              ║
╚══════════════════════════════════════╝
""")

    query = input("Search: ").lower()

    results = []

    for memory in memories:
        if (
            query in memory["title"].lower()
            or query in memory["category"].lower()
            or query in memory["text"].lower()
        ):
            results.append(memory)

    if not results:
        print("\nNo matching memories.")
    else:
        print(f"\n{len(results)} result(s) found:\n")

        for memory in results:
            print(f"[{memory['id']}] {memory['title']}")
            print(memory["text"])
            print("-" * 40)

    input("\nPress ENTER...")


def random_memory(memories):
    clear()

    print("""
╔══════════════════════════════════════╗
║         RANDOM MEMORY                ║
╚══════════════════════════════════════╝
""")

    if not memories:
        print("No memories available.")
        input("\nPress ENTER...")
        return

    print("Opening a random memory", end="")

    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")

    memory = random.choice(memories)

    print(f"""

🧠 {memory['title']}

Category : {memory['category']}
Created  : {memory['date']}

"{memory['text']}"
""")

    input("\nPress ENTER...")


def delete_memory(memories):
    clear()

    print("""
╔══════════════════════════════════════╗
║          DELETE MEMORY               ║
╚══════════════════════════════════════╝
""")

    if not memories:
        print("Vault is empty.")
        input("\nPress ENTER...")
        return

    for memory in memories:
        print(f"{memory['id']}. {memory['title']}")

    try:
        memory_id = int(input("\nEnter memory ID: "))
    except ValueError:
        print("Invalid ID.")
        input("\nPress ENTER...")
        return

    found = None

    for memory in memories:
        if memory["id"] == memory_id:
            found = memory
            break

    if found:
        memories.remove(found)
        save_memories(memories)

        print("\n✓ Memory deleted.")
    else:
        print("\nMemory not found.")

    input("\nPress ENTER...")


def statistics(memories):
    clear()

    print("""
╔══════════════════════════════════════╗
║          VAULT STATISTICS            ║
╚══════════════════════════════════════╝
""")

    print("Total memories:", len(memories))

    categories = {}

    for memory in memories:
        category = memory["category"]

        if category not in categories:
            categories[category] = 0

        categories[category] += 1

    print("\nCategories:")

    if categories:
        for category, count in categories.items():
            print(f"  {category}: {count}")
    else:
        print("  None")

    input("\nPress ENTER...")


def main():

    memories = load_memories()

    while True:

        clear()

        print("""
╔══════════════════════════════════════════╗
║                                          ║
║          🧠 DIGITAL MEMORY VAULT         ║
║                                          ║
║        Your memories. Your database.     ║
║                                          ║
╠══════════════════════════════════════════╣
║                                          ║
║  1. ➕ Add Memory                         ║
║  2. 📖 View Memories                     ║
║  3. 🔍 Search Memories                   ║
║  4. 🎲 Random Memory                     ║
║  5. 🗑️ Delete Memory                     ║
║  6. 📊 Statistics                        ║
║  7. 🔒 Exit                              ║
║                                          ║
╚══════════════════════════════════════════╝
""")

        print(f"Stored memories: {len(memories)}")

        choice = input("\nVAULT > ")

        if choice == "1":
            add_memory(memories)

        elif choice == "2":
            view_memories(memories)

        elif choice == "3":
            search_memory(memories)

        elif choice == "4":
            random_memory(memories)

        elif choice == "5":
            delete_memory(memories)

        elif choice == "6":
            statistics(memories)

        elif choice == "7":
            clear()
            print("\n🔒 Memory Vault locked.")
            break

        else:
            print("\nInvalid option.")
            time.sleep(1)


main()
