from day1 import part1, part2

def test_1():
    assert(part1(['R2', 'L3']) == 5)

def test_2():
    assert(part1(['R2', 'R2', 'R2']) == 2)

def test_3():
    assert(part1(['R5', 'L5', 'R5', 'R3']) == 12)

def test_4():
    assert(part2(['R8', 'R4','R4', 'R8']) == 4)
