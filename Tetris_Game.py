import pgzrun
import random

WIDTH = 500
HEIGHT = 750

COLS = 10
ROWS = 15
CELL = 50

# store 0 for empty, or the color string for a locked cell
matrix_list = [[0 for _ in range(COLS)] for _ in range(ROWS)]

colors = ["red", "blue", "green", "yellow", "gray", "brown", "orange", "purple", "pink"]

shape_rotation = [
    [[[1], [1], [1], [1]], [[1, 1, 1, 1]]],

    [[[1, 1, 1], [0, 1, 0]], [[1, 0], [1, 1], [1, 0]],
     [[0, 1, 0], [1, 1, 1]], [[0, 1], [1, 1], [0, 1]]],

    [[[1, 0], [1, 0], [1, 1]], [[0, 0, 1], [1, 1, 1]],
     [[1, 1], [0, 1], [0, 1]], [[1, 1, 1], [1, 0, 0]]],

    [[[0, 1], [0, 1], [1, 1]], [[1, 1, 1], [0, 0, 1]],
     [[1, 1], [1, 0], [1, 0]], [[1, 0, 0], [1, 1, 1]]],

    [[[1, 0], [1, 1], [0, 1]], [[0, 1, 1], [1, 1, 0]]],

    [[[0, 1], [1, 1], [1, 0]], [[1, 1, 0], [0, 1, 1]]],
]

random_shape = []
x_shape = 0
y_shape = 0
index = 0
rotate_counter = 0
color = "red"

FALL_DELAY = 0.5       # seconds between normal steps down
SOFT_DROP_DELAY = 0.05  # seconds between steps while holding S
fall_timer = 0.0

game_over = False


def valid_position(shape, x, y):
    """Check that `shape` placed at pixel (x, y) fits on the board
    and doesn't overlap any locked cell."""
    col0 = int(x // CELL)
    row0 = int(y // CELL)
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell == 1:
                r = row0 + i
                c = col0 + j
                if c < 0 or c >= COLS or r >= ROWS:
                    return False
                if r >= 0 and matrix_list[r][c] != 0:
                    return False
    return True


def pickshape():
    global random_shape, x_shape, y_shape, index, rotate_counter, color, game_over

    color = random.choice(colors)
    index = random.randint(0, len(shape_rotation) - 1)
    rotate_counter = 0
    random_shape = shape_rotation[index][rotate_counter]

    width = len(random_shape[0])
    x_shape = ((COLS // 2) - width // 2) * CELL
    y_shape = 0.0

    if not valid_position(random_shape, x_shape, y_shape):
        game_over = True


def rotate():
    global rotate_counter, random_shape

    new_counter = (rotate_counter + 1) % len(shape_rotation[index])
    new_shape = shape_rotation[index][new_counter]

    # try the rotation as-is, then a couple of simple wall-kicks
    for dx in (0, -CELL, CELL, -2 * CELL, 2 * CELL):
        if valid_position(new_shape, x_shape + dx, y_shape):
            rotate_counter = new_counter
            random_shape = new_shape
            move_x(dx)
            return


def move_x(dx):
    global x_shape
    x_shape += dx


def lock_shape():
    col0 = int(x_shape // CELL)
    row0 = int(y_shape // CELL)
    for i, row in enumerate(random_shape):
        for j, cell in enumerate(row):
            if cell == 1:
                r, c = row0 + i, col0 + j
                if 0 <= r < ROWS and 0 <= c < COLS:
                    matrix_list[r][c] = color


def clear_full_rows():
    global matrix_list
    # keep only rows that are NOT full (i.e. still have an empty cell)
    remaining = [row for row in matrix_list if any(cell == 0 for cell in row)]
    cleared = ROWS - len(remaining)
    for _ in range(cleared):
        remaining.insert(0, [0] * COLS)
    matrix_list = remaining


def on_key_down(key):
    global x_shape, y_shape

    if game_over:
        return

    if key == keys.A:
        if valid_position(random_shape, x_shape - CELL, y_shape):
            x_shape -= CELL
    if key == keys.D:
        if valid_position(random_shape, x_shape + CELL, y_shape):
            x_shape += CELL
    if key == keys.SPACE:
        rotate()


def update(dt):
    global y_shape, fall_timer

    if game_over:
        return

    fall_timer += dt
    delay = SOFT_DROP_DELAY if keyboard.s else FALL_DELAY

    if fall_timer >= delay:
        fall_timer = 0.0
        new_y = y_shape + CELL
        if valid_position(random_shape, x_shape, new_y):
            y_shape = new_y
        else:
            # can't move down any further -> lock in place immediately
            lock_shape()
            clear_full_rows()
            pickshape()


def matrix_draw():
    for i in range(ROWS):
        for j in range(COLS):
            cell = matrix_list[i][j]
            if cell != 0:
                screen.draw.filled_rect(Rect(j * CELL, i * CELL, CELL, CELL), cell)


def draw():
    screen.clear()
    matrix_draw()

    if not game_over:
        for i in range(len(random_shape)):
            for j in range(len(random_shape[i])):
                if random_shape[i][j] == 1:
                    screen.draw.filled_rect(
                        Rect(j * CELL + x_shape, i * CELL + int(y_shape), CELL, CELL), color
                    )
    else:
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="red")


pickshape()
pgzrun.go()