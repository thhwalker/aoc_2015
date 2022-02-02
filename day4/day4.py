import hashlib

puzzle_input = "ckczppom"
i = 0
first_answer = False
while True:
    r = hashlib.md5((puzzle_input + str(i)).encode())

    if r.hexdigest()[:5] == "00000" and first_answer is False:
        print(f"Answer one is: {i}")
        first_answer = True

    if r.hexdigest()[:6] == "000000":
        print(f"Answer two is: {i}")
        break
    i += 1