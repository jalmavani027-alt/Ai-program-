"""
Cursor Dinosaur — a little pixel-art T-rex (Chrome-dino style) that
follows your mouse cursor around the screen.

INSTALL (one time):
    pip install pyautogui

RUN:
    python cursor_dino.py

HOW IT WORKS:
    - A small borderless, always-on-top, transparent window is created.
    - Every 20ms it reads the real mouse position (pyautogui.position())
      and moves the window to sit just beside the cursor.
    - The dinosaur is drawn as pixel blocks on a tkinter Canvas (no
      external image files needed), and it alternates between two leg
      poses to look like it's running whenever the mouse is moving.
    - It also flips to face the direction you're moving in.

Tested on Windows / macOS / Linux (X11). On some Linux window managers
true transparency may not work — the window will still function, just
with a solid background color instead of a transparent one.
"""

import tkinter as tk
import pyautogui

# ---------- Config ----------
PIXEL = 4                 # size of each "pixel" block (bigger = bigger dino)
UPDATE_MS = 20             # how often we poll the cursor (ms)
OFFSET_X = 28               # how far beside the cursor the dino sits
OFFSET_Y = 10
BG_TRANSPARENT_COLOR = "magenta"  # color that gets treated as transparent
DINO_COLOR = "#535353"            # classic dino grey

# Pixel-art grid for the dino (1 = draw a pixel, 0 = empty)
# Two frames for a simple running animation.
FRAME_A = [
    "0000111110000",
    "0000111111000",
    "0000111111100",
    "0001111111100",
    "0011111111100",
    "0011111111000",
    "1111111111000",
    "1111111110000",
    "1111111111000",
    "0011111111100",
    "0011100111100",
    "0011000011000",
]

FRAME_B = [
    "0000111110000",
    "0000111111000",
    "0000111111100",
    "0001111111100",
    "0011111111100",
    "0011111111000",
    "1111111111000",
    "1111111110000",
    "1111111111000",
    "0011111111100",
    "0011110001100",
    "0001100001100",
]

# eye pixel (row, col) so we can punch a little white/black dot in the head
EYE = (2, 10)


class CursorDino:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)      # no title bar/border
        self.root.attributes("-topmost", True) # always on top
        try:
            self.root.attributes("-transparentcolor", BG_TRANSPARENT_COLOR)
        except tk.TclError:
            pass  # not supported on this platform (e.g. some Linux WMs)

        rows = len(FRAME_A)
        cols = len(FRAME_A[0])
        w, h = cols * PIXEL, rows * PIXEL

        self.canvas = tk.Canvas(
            self.root, width=w, height=h,
            highlightthickness=0, bg=BG_TRANSPARENT_COLOR
        )
        self.canvas.pack()

        self.frame_toggle = False
        self.last_x, self.last_y = pyautogui.position()
        self.facing_right = True

        self.draw_dino(FRAME_A, facing_right=True)
        self.update_loop()
        self.root.mainloop()

    def draw_dino(self, frame, facing_right=True):
        self.canvas.delete("all")
        rows = len(frame)
        cols = len(frame[0])
        for r, row in enumerate(frame):
            for c, val in enumerate(row):
                if val == "1":
                    col = c if facing_right else (cols - 1 - c)
                    x0 = col * PIXEL
                    y0 = r * PIXEL
                    color = DINO_COLOR
                    if (r, c) == EYE:
                        color = "white"
                    self.canvas.create_rectangle(
                        x0, y0, x0 + PIXEL, y0 + PIXEL,
                        fill=color, outline=""
                    )

    def update_loop(self):
        x, y = pyautogui.position()

        # figure out movement direction to decide which way dino faces
        dx = x - self.last_x
        if dx > 1:
            self.facing_right = True
        elif dx < -1:
            self.facing_right = False
        moving = abs(dx) > 1 or abs(y - self.last_y) > 1

        # animate legs only while moving
        if moving:
            self.frame_toggle = not self.frame_toggle
        frame = FRAME_A if self.frame_toggle else FRAME_B
        self.draw_dino(frame, facing_right=self.facing_right)

        # position window beside the cursor
        offset_x = OFFSET_X if self.facing_right else -OFFSET_X - 52
        new_x = x + offset_x
        new_y = y + OFFSET_Y
        self.root.geometry(f"+{new_x}+{new_y}")

        self.last_x, self.last_y = x, y
        self.root.after(UPDATE_MS, self.update_loop)


if __name__ == "__main__":
    print("Cursor Dino is running. Move your mouse! Press Ctrl+C in this")
    print("terminal (or close the console) to stop it.")
    CursorDino()
