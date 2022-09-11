target = int(input())

count = int(input())

best = []

for _ in range(count):
    person = [input(), int(input())]
    if not best or abs(target - best[1]) > abs(target - person[1]):
        best = person.copy()

print(best[0])
