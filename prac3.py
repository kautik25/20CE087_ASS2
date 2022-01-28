x = int(input())
y = list(map(int, input().split(' ')))

a = 0
for i in y:
    b = y.count(i)
    if b == 1:
        c = i
    elif b == x:
        pass
    else:
        a = 1

if a == 1:
    print('something wrong Data.Please Try again')
else:
    print(c)