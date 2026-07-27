import random

def tree(x, y, angle, depth, canvas):
    if depth == 0:
        return
    length = depth * 1.5
    x2 = x + length * -0.5 * angle_sin(angle)
    y2 = y + length * angle_cos(angle)
    draw_line(x, y, x2, y2, canvas, depth)
    
    # Branch into two, with a bit of randomness
    tree(x2, y2, angle - random.uniform(15, 35), depth - 1, canvas)
    tree(x2, y2, angle + random.uniform(15, 35), depth - 1, canvas)

def angle_sin(deg):
    import math
    return math.sin(math.radians(deg))

def angle_cos(deg):
    import math
    return math.cos(math.radians(deg))

def draw_line(x1, y1, x2, y2, canvas, depth):
    chars = " .,:;+*#@"
    char = chars[min(depth, len(chars) - 1)]
    steps = int(max(abs(x2 - x1), abs(y2 - y1))) + 1
    for i in range(steps + 1):
        t = i / steps
        x = round(x1 + (x2 - x1) * t)
        y = round(y1 + (y2 - y1) * t)
        if 0 <= y < len(canvas) and 0 <= x < len(canvas[0]):
            canvas[y][x] = char

W, H = 60, 30
canvas = [[' ' for _ in range(W)] for _ in range(H)]
tree(W // 2, H - 1, 0, 9, canvas)

for row in reversed(canvas):
    print(''.join(row))
