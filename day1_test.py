from day1 import main

def test_1():
    assert(main(['R2', 'L3']) == 5)

def test_2():
    assert(main(['R2', 'R2', 'R2']) == 2)

def test_3():
    assert(main(['R5', 'L5', 'R5', 'R3']) == 12)

