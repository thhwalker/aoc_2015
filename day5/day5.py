from os import nice


with open("day5.input", 'r') as f:
    puzzle_input = f.read().splitlines()

# Part one
vowels = ['a','e','i','o','u']
bad_strings = ["ab","cd","pq","xy"]
nice_count = 0

for string in puzzle_input:
    dbl_char = False
    tri_vowels = 0
    if any(bad in string for bad in bad_strings):
        continue
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            dbl_char = True
            break
    if not dbl_char:
        continue
    for char in string:
        if char in vowels:
            tri_vowels += 1
            if tri_vowels >= 3:
                nice_count += 1
                break
print("Part one", nice_count)

# Part two
nice_count = 0
for string in puzzle_input:
    is_paired = False
    is_repeat = False
    for i in range(1,len(string)):
        if string.count(string[i-1] + string[i]) > 1:
            is_paired = True
            break
    if not is_paired:
        continue
    for i in range(2,len(string)):
        if string[i-2] == string[i]:
            is_repeat = True
            nice_count += 1
            break
print("Part two", nice_count)