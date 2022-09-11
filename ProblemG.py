eq = input().split(' ')[2:]

b = int(f'{eq[0]}{eq[1][:-1]}')
c = int(f'{eq[2]}{eq[3]}')

d = ((b ** 2) - 4 * c) ** 0.5

x = sorted([int((-b + d) // 2), int((-b - d) // 2)], key=abs, reverse=True)

print(
    f'(x {"-" if x[0] > 0 else "+"} {abs(x[0])})(x {"-" if x[1] > 0 else "+"} {abs(x[1])})')
