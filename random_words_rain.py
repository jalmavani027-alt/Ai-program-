import random
import shutil
import time
import os

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()<>?/[]{}"

width = shutil.get_terminal_size().columns
height = shutil.get_terminal_size().lines

columns = [random.randint(-height, 0) for _ in range(width)]

try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        screen = [[" " for _ in range(width)] for _ in range(height)]

        for i in range(width):
            columns[i] += 1

            if columns[i] > height + random.randint(5, 25):
                columns[i] = random.randint(-20, 0)

            for trail in range(15):
                y = columns[i] - trail

                if 0 <= y < height:
                    screen[y][i] = random.choice(chars)

        print("\033[92m", end="")

        for row in screen:
            print("".join(row))

        print("\033[0m", end="")

        time.sleep(0.05)

except KeyboardInterrupt:
    os.system("cls" if os.name == "nt" else "clear")
    print("Matrix stopped.")