# Part One
flr = 0

with open("day1.input", 'r') as f:
    puzzle_input = f.read()

for par in puzzle_input:
    flr = flr + 1 if par == '(' else flr - 1

print(f"Floor: {flr}")

# Part Two
flr = chr = 0

for par in puzzle_input:
    chr += 1
    flr = flr + 1 if par == '(' else flr - 1
    if flr < 0:
        print(f"Entered Basement at character: {chr}")
        break