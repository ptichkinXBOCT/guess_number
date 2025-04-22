with open('input.txt', 'r') as file:
    data = file.read()
    J, S = str.split(data, '\n')

count_drag = 0
for jewel in J:
    for stone in S:
        if stone == jewel:
            count_drag += 1

with open('output.txt', 'w') as file:
    file.write(str(count_drag))
