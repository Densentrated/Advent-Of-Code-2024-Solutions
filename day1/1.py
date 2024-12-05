list1 = []
list2 = []
result = 0

with open('input.txt', 'r') as input:
    for line in input:
        list1.append(int(line.split('   ')[0]))
        list2.append(int(line.split('   ')[1]))
list1.sort()
list2.sort()

for i in range(len(list1)):
    print(f"{list1[i]} - {list2[i]} = {abs(list1[i] - list2[i])}")
    result += abs(list1[i] - list2[i])

print(result)