import sys
import math


face_right = ">"
face_left = "<"
face_down = "v"
face_up = "^"
block = "#"

debug = False
width, height = [int(i) for i in input().split()]


maze = []
original_position = None
pikaptcha = None
for i in range(height):
    line = input()
    maze.insert(i, [])
    for j in range(width):

        if line[j] in [face_right, face_left, face_down, face_up]:
            original_position = (i, j)
            pikaptcha = line[j]
        
        if line[j] == block:
            maze[i].insert(j, line[j])
        else:
            maze[i].insert(j, 0)

if debug:
    print(maze)
    
side = input()

if side == "L":
    other_side = "R"
elif side == "R":
    other_side = "L"

def get_maze_tile(pos):
    x = pos[0]
    y = pos[1]
    
    if x < 0 or y < 0:
        return block
    elif x >= width:
        return block
    elif y >= height:
        return block
    
    return maze[y][x]
    
def count_entry_on_maze(pos):
    maze[pos[1]][pos[0]] += 1
    
if debug:
    count_entry_on_maze((0, 0))
    print(maze)

def is_empty_tile(position):
    tile = get_maze_tile(position)
    if tile == "#":
        return False
    
    return True
    

def test_up_tile(pos):
    return (pos[0], pos[1] - 1)

def test_down_tile(pos):
    return (pos[0], pos[1] + 1)

def test_left_tile(pos):
    return (pos[0] - 1, pos[1])

def test_right_tile(pos):
    return (pos[0] + 1, pos[1])


adjacent_tiles = {
    face_right: {
        "L": (test_up_tile, face_up),
        "R": (test_down_tile, face_down)
    },
    face_left: {
        "L": (test_down_tile, face_down),
        "R": (test_up_tile, face_up)
    },
    face_up: {
        "L": (test_left_tile, face_left),
        "R": (test_right_tile, face_right)
    },
    face_down: {
        "L": (test_right_tile, face_right),
        "R": (test_left_tile, face_left)
    }
}


def move_pikaptcha(direction, pos):
    count_entry_on_maze(pos)
    
    next_direction = direction
    next_side = side
    for i in range(4):
        next_tile = adjacent_tiles[next_direction][next_side]
        next_pos = next_tile[0](pos)
        if is_empty_tile(next_pos):
            break
        
        next_direction = next_tile[1]
        next_side = other_side

    if next_pos != original_position:
        move_pikaptcha(next_tile[1], next_pos)
    
move_pikaptcha(pikaptcha, original_position)
    
for line in maze:
    print("".join(str(tile) for tile in line))
