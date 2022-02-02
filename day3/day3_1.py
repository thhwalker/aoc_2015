starting_point = (0,0)
x = y = 0

d = {
    starting_point:1
}

with open("day3.input", 'r') as f:
    puzzle_input = f.read()

for step in puzzle_input:
    if step == '^':
        x += 1
    if step == 'v':
        x -= 1
    if step == '>':
        y += 1
    if step == '<':
        y -= 1
    d[(x,y)] = d.get((x,y), 0) + 1
print(d)
print(len([v for v in d.values()]))