def nextPalindrome(x):
    x = int(x)
    for i in range(len(str(x)) // 2):
        while str(x)[i] != str(x)[-(i + 1)]:
            x -= 10 ** i
    return x


target = int(input())
out = []

while sum(out) < target:
    out.append(nextPalindrome(target - sum(out)))

print(len(out))

for x in out:
    print(x)
