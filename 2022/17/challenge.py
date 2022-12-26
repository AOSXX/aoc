

with open("data.txt") as f:
    inp = f.read().strip()
# inp = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

ROCKS = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # -
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],  # +
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],  # L reverse
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # |
    [(0, 0), (0, 1), (1, 0), (1, 1)]  # o
]


def gen_rock(dx, dy, r):
    # Returns a rock and min and max y of the rock.
    rock_shape = ROCKS[r]
    rock = set((x + dx, y + dy) for x, y in rock_shape)
    return rock, rock_shape[0][1] + dy, rock_shape[-1][1] + dy


r = 0
SOURCE_OFFSET = 3
source_row = SOURCE_OFFSET
SOURCE_COL = 2

rock_cnt = 1
rock, y1, y2 = gen_rock(source_row, SOURCE_COL, 0)
rx = source_row
j = 0
J = len(inp)
h_filled = [-1 for _ in range(7)]
filled = {(-1, i) for i in range(7)}

cache = {}
sdiff = 0
CAP1, CAP2 = 2022, 1000000000000
res1 = 0
cache_used = False
while rock_cnt <= CAP2:
    jet = inp[j]
    j = (j + 1) % J

    dy = 1 if jet == ">" else -1
    if 0 <= y1 + dy and y2 + dy < 7:
        rock_ = set((cell[0], cell[1] + dy) for cell in rock)
        if not (rock_ & filled):
            rock = rock_
            y1 += dy
            y2 += dy
    rock_ = set((cell[0] - 1, cell[1]) for cell in rock)
    if not (rock_ & filled):
        rock = rock_
        continue

    for cell in rock:
        # add 1 since the rock itself is occupying that cell and it has to be _ABOVE_
        source_row = max(cell[0] + 1 + SOURCE_OFFSET, source_row)
        h_filled[cell[1]] = max(h_filled[cell[1]], cell[0])
    # Strip out stuff of filled if it's too far below what we've seen.
    #  keep 3 extra rows because rocks can be as tall as 4 cells
    min_row = min(h_filled) - 4
    filled = {cell for cell in filled if cell[0] > min_row} | rock
    rock, y1, y2 = gen_rock(source_row, SOURCE_COL, rock_cnt % 5)

    if rock_cnt == CAP1:
        res1 = source_row - SOURCE_OFFSET
    rock_cnt += 1
    rx = source_row

    if not cache_used and rock_cnt > CAP1:
        ck = [source_row - mx for mx in h_filled]
        cache_key = (rock_cnt % 5, j, tuple(ck))
        if cache_key not in cache:
            cache[cache_key] = (source_row, rock_cnt)
        else:
            old_cap, old_rock_cnt = cache[cache_key]
            diff = source_row - old_cap
            rocks_apart = (rock_cnt - old_rock_cnt)

            mult = (CAP2 - rock_cnt) // rocks_apart
            rock_cnt += (rocks_apart * mult)
            sdiff = (diff * mult)
            cache_used = True

print(f"Part 1: {res1}\nPart 2: {source_row + sdiff - SOURCE_OFFSET}")