from collections import namedtuple

movements = "R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5".split(", ")

State = namedtuple('State', ['facing', 'x', 'y'])
Move = namedtuple('Move', ['direction', 'blocks'])

def is_right(direction):
    return direction == 'R'

def parse_move(movement_str):
    return Move(direction=movement_str[0], blocks=int(movement_str[1:]))

def update_state(state, move):
    if facing == 'N':
        state = State('E',1,0) if is_right(move.direction) else State('W',-1,0)
    elif facing == 'S':
        state = State('W',-1,0) if is_right(move.direction) else State('E',1,0)
    elif facing == 'E':
        state = State('S',0,-1) if is_right(move.direction) else State('N',0,1)
    elif facing == 'W':
        state = State('N',0,1) if is_right(move.direction) else State('S',0,-1)

    return state._replace(x=state.x * move.blocks, y=state.y * move.blocks)

def taxicab_geometry(start, end):
    return abs(start.y - end.y) + abs(start.x - end.x)

def traverse(state, movement_str):
    move = parse_move(movement_str)
    return update_state(state.facing, move.direction)

def main(movements):
    start = State(facing='N', x=0, y=0)
    end = reduce(traverse, movements, start)
    return taxicab_geometry(start, end)

if __name__ == '__main__':
    print main(movements)
