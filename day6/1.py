def simulate_guard_path(lab_map):
    # Define directions and their respective deltas for movement
    directions = ['^', '>', 'v', '<']  # Up, Right, Down, Left
    direction_deltas = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

    # Find the initial position and direction of the guard
    guard_pos = None
    guard_dir = None
    for r, row in enumerate(lab_map):
        for c, cell in enumerate(row):
            if cell in directions:
                guard_pos = (r, c)
                guard_dir = cell
                break
        if guard_pos:
            break

    visited_positions = set()
    visited_positions.add(guard_pos)

    rows, cols = len(lab_map), len(lab_map[0])

    while True:
        # Calculate the next position based on the current direction
        delta = direction_deltas[guard_dir]
        next_pos = (guard_pos[0] + delta[0], guard_pos[1] + delta[1])

        # Check if the next position is out of bounds
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        # Check if the next position is an obstacle
        if lab_map[next_pos[0]][next_pos[1]] == '#':
            # Turn right 90 degrees
            guard_dir = directions[(directions.index(guard_dir) + 1) % 4]
        else:
            # Move forward
            guard_pos = next_pos
            visited_positions.add(guard_pos)

    return visited_positions


# Example input map
lab_map = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]

# reassign lab map to the the text in the file input.txt as a matrix of characters
with open('/home/dense/Projects/Advent-Of-Code-2024-Solutions/day5/input.txt', 'r') as file:
    lab_map = file.read().splitlines()

# Convert the map to a list of lists for easier manipulation
lab_map = [list(row) for row in lab_map]

# Simulate the guard's path and count distinct positions visited
visited_positions = simulate_guard_path(lab_map)
distinct_positions_count = len(visited_positions)

print("Number of distinct positions visited:", distinct_positions_count)
