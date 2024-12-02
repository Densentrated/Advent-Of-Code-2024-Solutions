reports = []
result = 0

with open('input.txt', 'r') as input:
    for line in input:
        levels = line.strip().split(' ')
        for i in range(len(levels)):
            levels[i] = int(levels[i])
        reports.append(levels)
    
# function to see if a level is safe or not
def is_safe_report_with_dampener(levels):
    n = len(levels)
    
    def is_safe(levels):
        # Check if the levels are all increasing or all decreasing
        is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
        is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

        # If neither increasing nor decreasing, it's not safe
        if not (is_increasing or is_decreasing):
            return False

        # Check if adjacent levels differ by at least 1 and at most 3
        for i in range(len(levels) - 1):
            if not (1 <= abs(levels[i] - levels[i + 1]) <= 3):
                return False

        return True

    # Check if the report is initially safe
    if is_safe(levels):
        return True

    # Check if removing one level makes the report safe
    for i in range(n):
        modified_levels = levels[:i] + levels[i+1:]  # Remove level at index i
        if is_safe(modified_levels):
            return True

    return False

for report in reports:
    if is_safe_report_with_dampener(report):
        print(report)
        result += 1

print(result)