import json
import os
import getpass
from datetime import datetime

FILE = "bank_data.json"


def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def create_account(data):
    print("\n--- Create Account ---")
    username = input("Username: ")

    if username in data:
        print("Account already exists.")
        return

    pin = getpass.getpass("Create 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("Invalid PIN.")
        return

    data[username] = {
        "pin": pin,
        "balance": 0,
        "history": []
    }

    save_data(data)
    print("Account created successfully.")


def login(data):
    print("\n--- Login ---")
    username = input("Username: ")

    if username not in data:
        print("Account not found.")
        return

    pin = getpass.getpass("PIN: ")

    if pin != data[username]["pin"]:
        print("Incorrect PIN.")
        return

    print(f"\nWelcome {username}")

    while True:
        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Logout")

        choice = input("Choice: ")

        if choice == "1":
            print(f"Balance: ₹{data[username]['balance']}")

        elif choice == "2":
            amount = float(input("Amount: "))
            data[
