list1 = []
list2 = []
result = 0

with open('input.txt', 'r') as input:
    for line in input:
        list1.append(int(line.split('   ')[0]))
        list2.append(int(line.split('   ')[1]))

set1 = set(list1)

# convert list2 to frequency map
map2 = {}
for item in list2:
    if item in map2:
        map2[item] += 1
    else:
        map2[item] = 1

for i in set1:
    if i in map2:
        result += abs(i * map2[i])
 
print(result)