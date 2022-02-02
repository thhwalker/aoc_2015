start = (0,0)
s_x = r_x = s_y = r_y = 0

santa_d = robo_d = {
    start:1
}

def do_work(step:str, x:int, y:int) -> tuple:
    if step == '^':
        x += 1
    if step == 'v':
        x -= 1
    if step == '>':
        y += 1
    if step == '<':
        y -= 1
    return (x,y)


with open("day3.input", 'r') as f:
    puzzle_input = f.read()

#puzzle_input = "^>v<"
for i, step in enumerate(puzzle_input):
    if (i % 2) == 0:
        r_x, r_y = do_work(step, r_x, r_y)
        robo_d[(r_x,r_y)] = robo_d.get((r_x,r_y), 0) + 1
    else:
        s_x, s_y = do_work(step, s_x, s_y)
        santa_d[(s_x,s_y)] = santa_d.get((s_x,s_y), 0) + 1

full_d = {**santa_d, **robo_d}
print(full_d)
print(len([v for v in full_d.values()]))