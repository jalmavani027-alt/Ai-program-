import os
import time
import random
import platform
from datetime import datetime

# -------------------------------
# FAKE OPERATING SYSTEM
# -------------------------------

OS_NAME = "NEXUS OS"
VERSION = "1.0"
USERNAME = "admin"

files = {
    "readme.txt": "Welcome to NEXUS OS!",
    "secret.txt": "There is nothing here... or is there?",
}

notes = []


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def loading(text="Loading"):
    print(text, end="", flush=True)

    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)

    print()


def boot():
    clear()

    print("""
╔══════════════════════════════════════════════╗
║                                              ║
║                 N E X U S                    ║
║                    OS                        ║
║                                              ║
║              Initializing...                 ║
║                                              ║
╚══════════════════════════════════════════════╝
""")

    loading("Starting kernel")
    loading("Loading system services")
    loading("Mounting virtual disk")
    loading("Starting desktop")

    time.sleep(1)


def login():
    while True:
        clear()

        print("╔══════════════════════════════╗")
        print("║         NEXUS OS LOGIN      ║")
        print("╚══════════════════════════════╝")

        user = input("\nUsername: ")
        password = input("Password: ")

        if user == "admin" and password == "1234":
            print("\nLogin successful!")
            time.sleep(1)
            return

        print("\nInvalid credentials.")
        input("Press ENTER to try again...")


def desktop():
    while True:
        clear()

        print("╔══════════════════════════════════════════════╗")
        print("║                 NEXUS OS                    ║")
        print("╠══════════════════════════════════════════════╣")
        print("║                                              ║")
        print("║   1. 📁 File Manager                        ║")
        print("║   2. 📝 Notes                               ║")
        print("║   3. 🧮 Calculator                          ║")
        print("║   4. 💻 System Information                  ║")
        print("║   5. 🕐 Clock                               ║")
        print("║   6. 🎲 Random Number Generator             ║")
        print("║   7. ⚡ Terminal                            ║")
        print("║   8. 🔒 Lock System                         ║")
        print("║   9. ⏻ Shutdown                             ║")
        print("║                                              ║")
        print("╚══════════════════════════════════════════════╝")

        choice = input("\nNEXUS > ")

        if choice == "1":
            file_manager()

        elif choice == "2":
            notes_app()

        elif choice == "3":
            calculator()

        elif choice == "4":
            system_info()

        elif choice == "5":
            clock()

        elif choice == "6":
            random_number()

        elif choice == "7":
            terminal()

        elif choice == "8":
            login()

        elif choice == "9":
            shutdown()
            break

        else:
            print("Unknown application.")
            time.sleep(1)


# -------------------------------
# FILE MANAGER
# -------------------------------

def file_manager():
    while True:
        clear()

        print("╔══════════════════════════════╗")
        print("║        FILE MANAGER          ║")
        print("╚══════════════════════════════╝")

        for i, filename in enumerate(files, 1):
            print(f"{i}. {filename}")

        print("\nC - Create file")
        print("R - Read file")
        print("D - Delete file")
        print("B - Back")

        choice = input("\nFILE > ").lower()

        if choice == "c":
            name = input("File name: ")
            content = input("Content: ")

            files[name] = content

            print("File created.")
            time.sleep(1)

        elif choice == "r":
            name = input("File name: ")

            if name in files:
                print("\n" + files[name])
            else:
                print("File not found.")

            input("\nPress ENTER...")

        elif choice == "d":
            name = input("File name: ")

            if name in files:
                del files[name]
                print("File deleted.")
            else:
                print("File not found.")

            time.sleep(1)

        elif choice == "b":
            break


# -------------------------------
# NOTES
# -------------------------------

def notes_app():
    clear()

    print("╔══════════════════════════════╗")
    print("║          NOTES APP           ║")
    print("╚══════════════════════════════╝")

    if notes:
        print("\nYour notes:\n")

        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")
    else:
        print("\nNo notes available.")

    print("\n1. Add note")
    print("2. Back")

    choice = input("\nNOTES > ")

    if choice == "1":
        note = input("Write note: ")
        notes.append(note)
        print("Saved.")
        time.sleep(1)


# -------------------------------
# CALCULATOR
# -------------------------------

def calculator():
    clear()

    print("╔══════════════════════════════╗")
    print("║         CALCULATOR           ║")
    print("╚══════════════════════════════╝")

    try:
        a = float(input("\nFirst number: "))
        op = input("Operator (+ - * /): ")
        b = float(input("Second number: "))

        if op == "+":
            result = a + b

        elif op == "-":
            result = a - b

        elif op == "*":
            result = a * b

        elif op == "/":
            result = a / b

        else:
            print("Invalid operator.")
            input("Press ENTER...")
            return

        print("\nResult:", result)

    except ZeroDivisionError:
        print("\nCannot divide by zero.")

    except ValueError:
        print("\nInvalid number.")

    input("\nPress ENTER...")


# -------------------------------
# SYSTEM INFORMATION
# -------------------------------

def system_info():
    clear()

    print("╔══════════════════════════════╗")
    print("║       SYSTEM INFORMATION     ║")
    print("╚══════════════════════════════╝")

    print("\nOS Name      :", OS_NAME)
    print("Version      :", VERSION)
    print("User         :", USERNAME)
    print("Python       :", platform.python_version())
    print("Host OS      :", platform.system())
    print("Architecture :", platform.machine())
    print("CPU          :", platform.processor())
    print("Files        :", len(files))
    print("Notes        :", len(notes))

    input("\nPress ENTER...")


# -------------------------------
# CLOCK
# -------------------------------

def clock():
    clear()

    print("╔══════════════════════════════╗")
    print("║             CLOCK            ║")
    print("╚══════════════════════════════╝")

    print("\nCurrent time:")

    print(datetime.now().strftime(
        "%A, %d %B %Y\n%H:%M:%S"
    ))

    input("\nPress ENTER...")


# -------------------------------
# RANDOM NUMBER
# -------------------------------

def random_number():
    clear()

    print("╔══════════════════════════════╗")
    print("║      RANDOM GENERATOR        ║")
    print("╚══════════════════════════════╝")

    number = random.randint(100000, 999999)

    print("\nGenerated number:")
    print("\n", number)

    input("\nPress ENTER...")


# -------------------------------
# TERMINAL
# -------------------------------

def terminal():
    while True:
        clear()

        print("NEXUS TERMINAL")
        print("Type 'help' for commands.")
        print("Type 'exit' to return.\n")

        command = input("root@nexus:~$ ")

        if command == "help":
            print("""
Available commands:

help       Show commands
clear      Clear screen
date       Show date
whoami     Show current user
ls         List files
neofetch   System information
echo       Print text
exit       Return to desktop
""")
            input("\nPress ENTER...")

        elif command == "clear":
            pass

        elif command == "date":
            print(datetime.now())

            input("\nPress ENTER...")

        elif command == "whoami":
            print(USERNAME)

            input("\nPress ENTER...")

        elif command == "ls":
            print("\n".join(files.keys()))

            input("\nPress ENTER...")

        elif command == "neofetch":
            print("""
        ███╗   ██╗███████╗██╗  ██╗
        ████╗  ██║██╔════╝╚██╗██╔╝
        ██╔██╗ ██║█████╗   ╚███╔╝
        ██║╚██╗██║██╔══╝   ██╔██╗
        ██║ ╚████║███████╗██╔╝ ██╗
        ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

        NEXUS OS 1.0
        USER: admin
        SYSTEM: Virtual Computer
""")
            input("\nPress ENTER...")

        elif command.startswith("echo "):
            print(command[5:])
            input("\nPress ENTER...")

        elif command == "exit":
            break

        else:
            print("Command not found.")
            time.sleep(1)


# -------------------------------
# SHUTDOWN
# -------------------------------

def shutdown():
    clear()

    print("\n")
    loading("Saving virtual system")

    print("\nClosing applications...")
    time.sleep(0.8)

    print("Unmounting virtual disk...")
    time.sleep(0.8)

    print("Shutting down NEXUS OS...")
    time.sleep(1)

    clear()

    print("""
╔══════════════════════════════════╗
║                                  ║
║        NEXUS OS SHUT DOWN        ║
║                                  ║
║          See you again.           ║
║                                  ║
╚══════════════════════════════════╝
""")


# -------------------------------
# START OS
# -------------------------------

boot()
login()
desktop()
