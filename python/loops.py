# region while and for has else
numbers = [1, 2, 3]
value = 10
index = 0

while index < len(numbers):
    if numbers[index] == value:
        break
    index += 1
else:
    # when the executed fully (not out with break nor continue) it
    # enters here
    numbers.append(value)

print(numbers)

for i in range(1, 4):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    # when the executed fully (not out with break nor continue) it
    # enters here
    print('multiple of 7 not found')
# endregion
