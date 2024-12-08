def parse_input(input_data):
    parts = input_data.strip().split('\n\n')
    rules = [tuple(map(int, line.split('|'))) for line in parts[0].splitlines()]
    updates = [list(map(int, line.split(','))) for line in parts[1].splitlines()]
    return rules, updates

def is_correct_order(update, rules):
    applicable_rules = {(x, y) for x, y in rules if x in update and y in update}
    for x, y in applicable_rules:
        if update.index(x) > update.index(y):
            return False
    return True

def reorder_update(update, rules):
    # Create a directed graph of dependencies
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    indegree = defaultdict(int)
    
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            indegree[y] += 1
    
    # Topological sort using Kahn's algorithm
    queue = deque([u for u in update if indegree[u] == 0])
    sorted_update = []
    
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_update

def find_middle_page(update):
    mid_index = len(update) // 2
    return update[mid_index]

def solve_part_two(input_data):
    rules, updates = parse_input(input_data)
    
    sum_of_middle_pages = 0
    for update in updates:
        if not is_correct_order(update, rules):
            correct_order_update = reorder_update(update, rules)
            sum_of_middle_pages += find_middle_page(correct_order_update)
    
    return sum_of_middle_pages

# Example input data
with open ('input.txt', 'r') as file:
    input_data = file.read()

# Calculate the answer using example input data
answer_part_two = solve_part_two(input_data)
print(answer_part_two)  # Output should be 123 for this example input data.
