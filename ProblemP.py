def verify(index, available, preserve):
    if index > 0 and available[index - 1] > 0:
        available[index - 1] -= 1
        t = verify(index - 1, available, preserve)
        if t:
            return True
        available[index - 1] += 1
    if index < (len(available) - 1) and available[index + 1] > 0:
        available[index + 1] -= 1
        t = verify(index + 1, available, preserve)
        if t:
            return True
        available[index + 1] += 1
    if index == preserve and sum(available) == 0:
        return True
    else:
        return False


mx = int(input())

freqs = list(map(lambda x: int(x), input().split(" ")))

final = 0

for i in range(mx):
    for j in range(mx):
        if i != j:
            a = freqs.copy()
            a[i] -= 1
            k = verify(i, a, j)
            final += k

print(final)
