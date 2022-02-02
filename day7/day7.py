TEST_INPUT = '''
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
'''
TEST = False
wires = {}

with open("day7.input", 'r') as f:
    puzzle_input = TEST_INPUT.strip().splitlines() if TEST is True else f.read().splitlines()

for command in puzzle_input:
    c = command.split()
    print(c)
    if len(c) == 3:
        wires[c[-1]] = int(c[0])
    if "AND" in c:
        wires[c[-1]] = wires.get(c[0],0) & wires.get(c[2],0)
    if "OR" in c:
        wires[c[-1]] = wires.get(c[0],0) | wires.get(c[2],0)
    if "LSHIFT" in c:
        wires[c[-1]] = wires.get(c[0],0) << int(c[2])
    if "RSHIFT" in c:
        wires[c[-1]] = wires.get(c[0],0) >> int(c[2])
    if "NOT" in c:
        wires[c[-1]] = ~ wires.get(c[1],0) % 65536
    else:
        print("SOMETHING WENT WRONG YOU DUMB DUMB")

print(wires['a'])