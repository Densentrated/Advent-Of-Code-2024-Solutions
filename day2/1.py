reports = []
result = 0

with open('input.txt', 'r') as input:
    for line in input:
        levels = line.strip().split(' ')
        for i in range(len(levels)):
            levels[i] = int(levels[i])
        reports.append(levels)
    
print(reports)

# function to see if a level is safe or not
def is_safe(report):
    if report[0] < report[1]:
        # increasing case
        for i in range(1, len(report)):
            if report[i] < report[i-1]:
                return False
            if (abs(report[i-1] - report[i]) > 3 or report[i] - report[i-1] == 0):
                return False
    else:
        # decreasing case
        for i in range(1, len(report)):
            if report[i] > report[i-1]:
                return False
            if (abs(report[i-1] - report[i]) > 3 or report[i] - report[i-1] == 0):
                return False
    return True

for report in reports:
    if is_safe(report):
        print(report)
        result += 1

print(result)