def parse_input(grid):
    """Parse the input grid to extract the map, guard's position, and direction."""
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    guard_pos = None
    guard_dir = None
    obstacles = set()
    
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in directions:
                guard_pos = (r, c)
                guard_dir = directions[cell]
            elif cell == '#':
                obstacles.add((r, c))
    
    return obstacles, guard_pos, guard_dir


def turn_right(direction):
    """Turn the guard's direction 90 degrees to the right."""
    return {
        (-1, 0): (0, 1),   # Up -> Right
        (0, 1): (1, 0),    # Right -> Down
        (1, 0): (0, -1),   # Down -> Left
        (0, -1): (-1, 0)   # Left -> Up
    }[direction]


def simulate_patrol(obstacles, start_pos, start_dir, new_obstacle=None):
    """Simulate the patrol and detect if it enters a loop."""
    visited = set()
    pos = start_pos
    direction = start_dir
    
    if new_obstacle:
        obstacles.add(new_obstacle)
    
    while True:
        state = (pos, direction)
        
        if state in visited:
            # Loop detected
            if new_obstacle:
                obstacles.remove(new_obstacle)
            return True
        
        visited.add(state)
        
        # Determine next position
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        
        if next_pos in obstacles:
            # Turn right if there's an obstacle
            direction = turn_right(direction)
        else:
            # Move forward
            pos = next_pos
        
        # Check if the guard has left the grid
        if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(grid) or pos[1] >= len(grid[0]):
            break
    
    if new_obstacle:
        obstacles.remove(new_obstacle)
    
    return False


def find_loop_positions(grid):
    """Find all positions where placing an obstruction causes a loop."""
    obstacles, guard_pos, guard_dir = parse_input(grid)
    loop_positions = set()
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in obstacles and (r, c) != guard_pos:
                if simulate_patrol(obstacles.copy(), guard_pos, guard_dir, new_obstacle=(r, c)):
                    loop_positions.add((r, c))
    
    return len(loop_positions)


# Example usage with the provided grid input
grid = [
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

with open('/home/dense/Projects/Advent-Of-Code-2024-Solutions/day5/input.txt') as f:
    grid = [line.strip() for line in f]

print(find_loop_positions(grid))
