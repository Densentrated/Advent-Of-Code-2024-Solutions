import re

def parse_and_calculate(filename):
    # Read input file
    with open(filename, 'r') as file:
        data = file.read()

    # Regular expressions for instructions
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")

    # Initialize state
    mul_enabled = True
    total_sum = 0

    # Position in the string
    pos = 0

    while pos < len(data):
        # Check for do() or don't() first, as they affect state
        do_match = do_pattern.search(data, pos)
        dont_match = dont_pattern.search(data, pos)
        mul_match = mul_pattern.search(data, pos)

        # Determine which match comes first
        matches = [(do_match, 'do'), (dont_match, "don't"), (mul_match, 'mul')]
        matches = [(m.start(), m, t) for m, t in matches if m]

        if not matches:
            break

        matches.sort()
        next_pos, match, type_ = matches[0]

        if type_ == 'do':
            mul_enabled = True
            pos = match.end()
        elif type_ == "don't":
            mul_enabled = False
            pos = match.end()
        elif type_ == 'mul':
            if mul_enabled:
                x, y = int(match.group(1)), int(match.group(2))
                total_sum += x * y
            pos = match.end()

    return total_sum

# Usage
result = parse_and_calculate('input.txt')
print(result)
