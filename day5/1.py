def parse_input(input_data):
    # Split input into rules and updates
    parts = input_data.strip().split('\n\n')
    rules = [tuple(map(int, line.split('|'))) for line in parts[0].splitlines()]
    updates = [list(map(int, line.split(','))) for line in parts[1].splitlines()]
    return rules, updates

def is_correct_order(update, rules):
    # Create a set of applicable rules
    applicable_rules = {(x, y) for x, y in rules if x in update and y in update}
    
    # Check if update respects these applicable rules
    for x, y in applicable_rules:
        if update.index(x) > update.index(y):
            return False
    return True

def find_middle_page(update):
    mid_index = len(update) // 2
    return update[mid_index]

def solve(input_data):
    rules, updates = parse_input(input_data)
    
    sum_of_middle_pages = 0
    for update in updates:
        if is_correct_order(update, rules):
            sum_of_middle_pages += find_middle_page(update)
    
    return sum_of_middle_pages

# Load input data
with open('input.txt', 'r') as file:
    input_data = file.read()

# Calculate the answer using example input data
answer = solve(input_data)
print(answer)  # Output should be 143 for this example input data.
