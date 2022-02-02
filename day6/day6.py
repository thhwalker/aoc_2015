lights = {}

with open("day6.input", 'r') as f:
    puzzle_input = f.read().splitlines()

#test input
#puzzle_input = ["turn on 0,0 through 999,999", "toggle 0,0 through 999,0", "turn off 499,499 through 500,500"]

# Part one

for command in puzzle_input:
    c_list = command.split()
    if c_list[0] == "turn":
        a_x, a_y = tuple(int(x) for x in c_list[2].split(','))
        b_x, b_y = tuple(int(x) for x in c_list[4].split(','))
        for i in range(a_x,b_x+1):
            for j in range(a_y, b_y+1):
                lights[(i,j)] = 1 if c_list[1] == "on" else 0
    else:
        a_x, a_y = tuple(int(x) for x in c_list[1].split(','))
        b_x, b_y = tuple(int(x) for x in c_list[3].split(','))
        for i in range(a_x,b_x+1):
            for j in range(a_y, b_y+1):
                lights[(i,j)] = 1 if lights.get((i,j),0) == 0 else 0

print(sum(1 for v in lights.values() if v == 1))

# Part two
lights = {}

for command in puzzle_input:
    c_list = command.split()
    if c_list[0] == "turn":
        a_x, a_y = tuple(int(x) for x in c_list[2].split(','))
        b_x, b_y = tuple(int(x) for x in c_list[4].split(','))
        for i in range(a_x,b_x+1):
            for j in range(a_y, b_y+1):
                if c_list[1] == "on":
                    lights[(i,j)] = lights.get((i,j),0) + 1
                else:
                    lights[(i,j)] = lights.get((i,j),0) - 1 if lights.get((i,j),0) > 0 else 0
    else:
        a_x, a_y = tuple(int(x) for x in c_list[1].split(','))
        b_x, b_y = tuple(int(x) for x in c_list[3].split(','))
        for i in range(a_x,b_x+1):
            for j in range(a_y, b_y+1):
                lights[(i,j)] = lights.get((i,j),0) + 2

print(sum(v for v in lights.values()))