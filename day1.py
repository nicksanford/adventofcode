from collections import namedtuple

movements = 'R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5'.split(', ')

State = namedtuple('State', ['facing', 'x', 'y'])
Move = namedtuple('Move', ['direction', 'blocks'])

def is_right(direction):
    return direction == 'R'

def parse_move(movement_str):
    return Move(direction=movement_str[0], blocks=int(movement_str[1:]))

def new_vector(state, move):
    if state.facing == 'N':
        return State('E',1,0) if is_right(move.direction) else State('W',-1,0)
    elif state.facing == 'S':
        return State('W',-1,0) if is_right(move.direction) else State('E',1,0)
    elif state.facing == 'E':
        return State('S',0,-1) if is_right(move.direction) else State('N',0,1)
    elif state.facing == 'W':
        return State('N',0,1) if is_right(move.direction) else State('S',0,-1)

def move_along_vector(state, vector, scalar):
    return vector._replace(x=state.x + vector.x * scalar,
                           y=state.y + vector.y * scalar)

def skip_to_last_state(state, move):
    return move_along_vector(state, new_vector(state, move), move.blocks)

def taxicab_geometry(start, end):
    return abs(start.y - end.y) + abs(start.x - end.x)

def traverse(state, move):
    return skip_to_last_state(state, move)

def part1(movements):
    moves = map(parse_move, movements)
    start = State(facing='N', x=0, y=0)
    end = reduce(traverse, moves, start)
    return taxicab_geometry(start, end)

def get_all_states_on_move(state, move):
    vector = new_vector(state, move)
    blocks = range(1, move.blocks+1)
    return [move_along_vector(state, vector, block)
            for block in blocks]

def state_to_position(state):
    return (state.x, state.y)

def first_dup_visit((founds, states), move):
    new_states = get_all_states_on_move(states[-1], move)
    positions = map(state_to_position, states)
    states_already_visited = [new_state for new_state in new_states
                                if state_to_position(new_state) in positions]


    return (founds + states_already_visited, states + new_states)

def part2(movements):
    start = State(facing='N', x=0, y=0)
    moves = [parse_move(movement) for movement in movements]
    init_founds = []
    init_states = [State(facing='N', x=0, y=0)]
    founds, _new_states = reduce(first_dup_visit,
                                           moves,
                                           (init_founds, init_states))
    end = founds[0]
    return taxicab_geometry(start, end)

def main():
    print('part1: {}'.format(part1(movements)))
    print('part2: {}'.format(part2(movements)))

if __name__ == '__main__':
    main()
