def find_pairs(N):
    pairs = []
    for a in range(1, 21):
        for b in range(1, 21):
            if N % (a + b) == 0:
                pairs.append((a, b))
    return pairs
for N in range(3, 21):
    pairs = find_pairs(N)
    if pairs:
        print(f"Для числа {N} найдены следующие пары чисел (a, b), сумма которых делит {N}:")
        for pair in pairs:
            print(pair)

