import re

test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open("day_3_input.txt", 'r') as ifile:
    real = ifile.read()

valid = re.findall(r'mul\((\d+),(\d+)\)', real)
print(sum([int(a)*int(b) for a, b in valid]))

do_dont = re.split(r'(do\(\)|don\'t\(\))', real)
total = 0
do = True
for group in do_dont:
    if group == "don't()":
        do = False
        continue
    if group == "do()":
        do = True
        continue
    if do:
        valid = re.findall(r'mul\((\d+),(\d+)\)', group)
        total += sum([int(a)*int(b) for a, b in valid])

print(total)