m = int(input('Input m: '))
n = int(input('Input n: '))
k = int(input('Input k: '))

pl = m * n
if k % m == 0 and k < pl or k % n == 0 and k < pl:
    print('Yes')
else:
    print('No')