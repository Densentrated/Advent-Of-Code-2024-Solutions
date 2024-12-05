import re

with open('input.txt', 'r') as file:
    data = file.read()

print(data)

possible_instructions = []
valid_instructions = []
result = 0


pattern = re.compile(r'mul\(\d+,\d+\)')
possible_instructions = pattern.findall(data)

# Validate the instructions and compute the result
for instruction in possible_instructions:
    match = re.match(r'mul\((\d+),(\d+)\)', instruction)
    if match:
        x, y = int(match.group(1)), int(match.group(2))
        valid_instructions.append((x, y))
        result += x * y

print("Valid instructions:", valid_instructions)
print("Result:", result)



