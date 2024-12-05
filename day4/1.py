# Initialize result counter
result = 0

# Open and read the input matrix from 'input.txt'
with open('input.txt', 'r') as file:
    input_matrix = [list(line.strip()) for line in file if line.strip()]

# Define the words to search for
words = ['XMAS', 'SAMX']

# Check the horizontal direction
for line in input_matrix:
    for i in range(len(line) - 3):
        if ''.join(line[i:i+4]) in words:
            result += 1

# Check the vertical direction
for c in range(len(input_matrix[0])):
    for r in range(len(input_matrix) - 3):
        window = ''.join(input_matrix[r+i][c] for i in range(4))
        if window in words:
            result += 1

# Check the forward diagonal direction
for r in range(len(input_matrix) - 3):
    for c in range(len(input_matrix[0]) - 3):
        window = ''.join(input_matrix[r+i][c+i] for i in range(4))
        if window in words:
            result += 1

# Check the backward diagonal direction
for r in range(len(input_matrix) - 3):
    for c in range(3, len(input_matrix[0])):
        window = ''.join(input_matrix[r+i][c-i] for i in range(4))
        if window in words:
            result += 1

# Print the result
print(result)
