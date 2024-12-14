def find_pairs(number):
    pairs = []
    for i in range(1, 20):
        for j in range(i+1, 20):
            pair_sum = i + j
            if number % pair_sum == 0:
                pairs.append((i, j))
    return pairs

def generate_password(number, pairs):
    password = ""
    for pair in pairs:
        password += str(pair[0]) + str(pair[1])
    return password
number = 3
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 4
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 5
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 6
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 7
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 8
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 9
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 10
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 11
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 12
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 13
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 14
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 15
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 16
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 17
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 18
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 19
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")
number = 20
pairs = find_pairs(number)
password = generate_password(number, pairs)
print(f"{number}: {password}")

