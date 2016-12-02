from collections import namedtuple

movements = "R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5".split(", ")

State = namedtuple('State', ['facing', 'x', 'y'])
Move = namedtuple('Move', ['direction', 'blocks'])

def is_right(direction):
    return direction == 'R'

def traverse_diff(facing, direction):
    if facing == 'N':
        return (1,0,'E') if is_right(direction) else (-1,0,'W')
    elif facing == 'S':
        return (-1,0,'W') if is_right(direction) else (1,0,'E')
    elif facing == 'E':
        return (0,-1,'S') if is_right(direction) else (0,1,'N')
    elif facing == 'W':
        return (0,1,'N') if is_right(direction) else (0,-1,'S')

def parse_move(movement_str):
    return Move(direction=movement_str[0], blocks=int(movement_str[1:]))

def traverse_coords(state, movement_str):
    move = parse_move(movement_str)
    x, y, new_facing = traverse_diff(state.facing, move.direction)
    x_delta, y_delta = x*move.blocks, y*move.blocks
    return State(facing=new_facing, x=state.x + x_delta, y=state.y + y_delta)

def taxicab_geometry(start, end):
    return abs(start.y - end.y) + abs(start.x - end.x)

def main(movements):
    start = State(facing='N', x=0, y=0)
    end = reduce(traverse_coords, movements, start)
    return taxicab_geometry(start, end)

if __name__ == '__main__':
    print main(movements)
