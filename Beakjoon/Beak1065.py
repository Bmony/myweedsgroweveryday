N = int(input())

hansu = 0
if N < 100:
    print(N)
elif N <= 1000 and N > 110:
    for i in range(111, N + 1):
        num = list(map(int, str(i)))
        if (num[2] - num[1]) == (num[1] - num[0]):
            hansu += 1
if N >= 100:
    print(99 + hansu)