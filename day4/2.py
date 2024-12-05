result = 0
with open('input.txt', 'r') as file:
    input_matrix = [list(line.strip()) for line in file if line.strip()]

# get a a 3x3 square,
# append the diagnals
# if both are a xmas or samx, add to result

for r in range(len(input_matrix)-2):
    for c in range(len(input_matrix[0])-2):
        window = [
                input_matrix[r][c:c+3],
                input_matrix[r+1][c:c+3],
                input_matrix[r+2][c:c+3]
            ]
        forward_diagnal = [window[0][0], window[1][1], window[2][2]]
        backward_diagnal = [window[0][2], window[1][1], window[2][0]]

        forward_works = forward_diagnal == list('SAM') or forward_diagnal == list('MAS')
        backward_works = backward_diagnal == list('SAM') or backward_diagnal == list('MAS')
        if (backward_works and forward_works):
            print(window)
            result += 1

print(result)
