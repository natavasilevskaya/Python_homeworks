num = int(input('Input num'))
if 99 < num <= 999:
    summa = num // 100 + num % 100 // 10 + num % 10
    print(summa)
else: 
    print('It is not correct num, input num in range 100-999')
