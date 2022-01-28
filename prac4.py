x = int(input())
y = list(map(int, input().split(' ')))
if len(y) == x:
    set1 = set(y)
    lis1 = list(set1)
    lis1.sort()
    lis1.reverse()
    print(lis1[1])
else:
    print(f'Your input digit is {x} and you take {len(y)} input.')