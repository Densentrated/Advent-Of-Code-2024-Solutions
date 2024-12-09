from typing import List


# Function that gets the operators\
def validate_expression(numbers, target):
    def backtrack(index, current_value):
        # Base case: if we've used all numbers
        if index == len(numbers):
            return current_value == target
        
        # Recursive case: try both '+' and '*' operators
        return (
            backtrack(index + 1, current_value + numbers[index]) or
            backtrack(index + 1, current_value * numbers[index]) or
            backtrack(index + 1, int(str(current_value) + str(numbers[index])))
        )
    
    # Start recursion with the first number as the initial value
    return backtrack(1, numbers[0])


# Example usage:
numbers = [49, 9, 6, 249, 82, 4, 4, 292]
target = 8299183120
print(validate_expression(numbers, target))  # Output: True or False based on whether a solution exists


with open('input.txt', 'r') as f:
    data = []
    for line in f.read().strip().split('\n'):
        split_string = line.strip().split(': ')
        first_half = int(split_string[0])
        second_half_raw = split_string[1].split(' ')
        second_half_clean = []
        for num in second_half_raw:
            second_half_clean.append(int(num))
        data.append((first_half, second_half_clean))

result = 0
for line in data:
    current_target, current_numbers = line
    print(f"{current_target}: {current_numbers} -> {validate_expression(current_numbers, current_target)}")
    if (validate_expression(current_numbers, current_target)):
        result += current_target

print(result)
