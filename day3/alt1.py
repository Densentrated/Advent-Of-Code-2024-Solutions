import re

with open('input.txt', 'r') as file:
    data = file.read()

print(data)
filtered_data = re.sub(r'[^0-9,()muldonot]', '', data)
print(filtered_data)