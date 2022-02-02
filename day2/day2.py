def get_wrapping_paper(l:int, w:int, h:int) -> int:
    first = l * w
    second = w * h
    third = h * l
    return (2 * first) + (2 * second) + (2 * third) + min([first, second, third])

def get_ribbon_length(l:int, w:int, h:int) -> int:
    ribbon = l * w * h
    sides = sorted([l,w,h])[:-1]
    b = 0
    for x in sides:
        b += 2*x
    return ribbon + b

with open("day2.input", 'r') as f:
    puzzle_input = f.read().splitlines()

answer = ans2 = 0

for line in puzzle_input:
    l, w, h = line.split('x')
    answer += get_wrapping_paper(int(l), int(w), int(h))
    ans2 += get_ribbon_length(int(l), int(w), int(h))


print(f"Part one: {answer}, Part two: {ans2}")